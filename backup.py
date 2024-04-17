#!/usr/bin/python3
"""
Creator:John Fitzpatrick
Email: jjfitzpatrick357@gmail.com
Version: 1.1
"""

import sys
import os
import pathlib
import shutil
from datetime import datetime #Adds a date and time to logs and backups
from backupcfg import jobs,dstPath #Imports the file path from the folder/file

def main(): #Defining the function "main" which is the command that executes the backup
    dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S") #Adds the time and date
    argCount = len(sys.argv)
    #Tests if the job name is specified
    if argCount != 2:
        print(f"ERROR: job name missing from command line") #Prints this message when the job name is mising fro the command line
    else: 
        jobName = sys.argv[1]#Putting the required job name that needs to be backed up into the command line
        #If the job name is valid
        if jobName not in jobs:#If the name that has been put into the command line is not found it prints and error message
            print(f'ERROR: Jobname {jobName} not defined.')
        else:
            srcPath = jobs[jobName]#the path of the jobs in backupcfg.py is defined by srcPath
            if not os.path.exists(srcPath):
                print("ERROR: file " + srcPath + " does not exist.")
            else:
                if not os.path.exists(dstPath):
                    print("ERROR: destination path " + srcPath + " does not exist.")
                else:
                    #the source path is valid

                    srcDetails = pathlib.PurePath(srcPath)
                    dstLoc = dstPath + "/" + srcDetails.name + "-" + dateTimeStamp
                    
                    if pathlib.Path(srcPath).is_dir():
                        shutil.copytree(srcPath, dstLoc)
                    else:
                        shutil.copy2(srcPath, dstLoc)
                
               

if __name__ == '__main__':
    main()
    


