#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import shutil
import glob
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program for file reorganization")
    parser.add_argument('-S', '--source', type=str, required=True, help="Directory with files")
    parser.add_argument('-d', '--days',   type=int, required=True, help="Interval in days. All files, that older then 'days' will be moved into 'Archive' directory")
    parser.add_argument('-s', '--size',   type=int, required=True, help="File size. All files, that smaller this size will be moved into 'Small' directory")
    
    args = parser.parse_args()
    try:
        if (os.path.exists(args.source)):
            files = glob.glob(args.source+"/*")
            for file in files:
                if os.path.isfile(file):
                    DirectoryToMove = args.source + "/"
                    
                    if os.path.getsize(file) < int(args.size):
                        DirectoryToMove += "Small"
                    elif int((time.time() - os.path.getmtime(file))/86400) > int(args.days):
                        DirectoryToMove += "Archive"
                    else:
                        continue
                    
                    if not os.path.exists(DirectoryToMove):
                        os.makedirs(DirectoryToMove)
                        
                    shutil.move(file, DirectoryToMove+"/"+os.path.basename(file))
                    print("File %s moved to %s" % (file, DirectoryToMove))
                    
                    
        else:
            print("Directory %s not found" % (args.source))
    except Exception as e:
        print(e)
        exit(3)
    