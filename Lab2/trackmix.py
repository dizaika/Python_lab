#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import subprocess
import random
import os
import glob
import time

if __name__ == "__main__":
    random.seed(time.time())
    
    parser = argparse.ArgumentParser(description="Program for make potpourri")
    parser.add_argument('-s', '--source',      type=str,  required=True,     help="Work directory with music" )
    parser.add_argument('-d', '--destination', type=str,  default="mix.mp3", help="Result file name")
    parser.add_argument('-c', '--count',       type=int,  default=-1,        help="File count in potpurri")
    parser.add_argument('-f', '--frame',       type=int,  default=10,        help="second count in frame")
    
    parser.add_argument('-l', '--log',      action="store_true", help="log to stdout")
    parser.add_argument('-e', '--extended', action="store_true", help="fade-in/out")
    
    args = parser.parse_args()
    
    SourceDir       = args.source
    DestinationFile = args.destination
    FileCount       = args.count
    Seconds         = args.frame
    
    log      = args.log
    extended = args.extended
    
    filelist = glob.glob(SourceDir + '/*.mp3')
    
    cwd = os.getcwd()
    
    command = ['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', 'file.txt', DestinationFile]
    MixedTracksCount = 0
    for file in filelist:
        if log:
            print(' --- processing file %d: %s' % (MixedTracksCount, file))
                
        process = subprocess.Popen(["ffmpeg", "-hide_banner", '-i', file], 
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.STDOUT,
                                   universal_newlines=True)
        
        process.wait()
        
        for line in process.stdout:    
            res = line.find('Duration:')
            if res > -1:
                timings = line[12:20].split(':')
                TotalSeconds = int(timings[0])*3600+int(timings[1])*60+int(timings[2])
                
                begin = random.randint(0, TotalSeconds-Seconds)
                
                if extended:
                    process = subprocess.Popen(['ffmpeg', 
                                      '-ss', 
                                      str(begin), 
                                      '-t', 
                                      str(Seconds), 
                                      '-i', 
                                      file, 
                                      '-af', 
                                      'afade=t=in:d=%f,afade=t=out:d=%f:st=%f' % ((Seconds/10), (Seconds/10), (Seconds-Seconds/10)), 
                                      str(MixedTracksCount)+'.mp3'],
                                     stdout=subprocess.PIPE, 
                                     stderr=subprocess.STDOUT,
                                     universal_newlines=True)
                    process.wait()
                else:
                    process = subprocess.Popen(['ffmpeg', 
                                      '-ss', 
                                      str(begin), 
                                      '-t', 
                                      str(Seconds), 
                                      '-i', 
                                      file, 
                                      '-af', 
                                      str(MixedTracksCount)+'.mp3'],
                                     stdout=subprocess.PIPE, 
                                     stderr=subprocess.STDOUT,
                                     universal_newlines=True)
                    process.wait()
                
                with open('file.txt', 'at') as f:
                    f.write("file " + cwd + '/' + str(MixedTracksCount) + '.mp3\n')
                
                break
                
        MixedTracksCount += 1
        if FileCount > -1:
            if MixedTracksCount >= FileCount:
                break;

        
    process = subprocess.Popen(command,
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.STDOUT,
                     universal_newlines=True)
    
    process.wait()
    
    i = 0
    while i < MixedTracksCount:
        print('deleting ' + cwd + '/' + str(i)+'.mp3')
        os.remove(cwd + '/' + str(i)+'.mp3')
        i += 1
        
    os.remove('file.txt')
    
    if log:
        print(' --- done!')