#!/usr/bin/python3
"""
Creator:John Fitzpatrick
Email: jjfitzpatrick357@gmail.com
Version: 1.1
"""

import sys
import os
import pathlib #For copying a directory
import shutil #For copying a file
import smtplib
from datetime import datetime #Adds a date and time to logs and backups
from backupcfg import jobs, dstPath, smtp, logPath #Imports the file path from the folder/file

def logging(message, dateTimeStamp):
    try:
        file = open(logPath, "a")
        file.write(f'{message} {dateTimeStamp}.\n')
        file.close()
    except FileNotFoundError:
        print('ERROR: File does not exist.')
    except IOError:
        print('ERROR: File is not accessible.')
            
            
    

def sendEmail(message, dateTimeStamp): 
    """ 
    Send an email message to the specified recipient. 
    Parameters: 
    message (string): message to send. 
    dateTimeStamp (string): Date and time when program was run. 
    """ 
    # create email message 
    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] + '\n' + 'Subject: Backup Error\n\n' + message + '\n' 
        
    # connect to email server and send email
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
        smtp_server.close()
    except Exception as e:
        print("ERROR: Send email failed: " + str(e), file=sys.stderr)

def success(message, dateTimeStamp):
    pass
    

def error(errorMessage, dateTimeStamp):
    print(errorMessage)
    logging(f'FAILURE {errorMessage}', {dateTimeStamp})
    sendEmail(errorMessage, dateTimeStamp)
    
    
def main(): #Defining the function "main" which is the command that executes the backup

    dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")    
    argCount = len(sys.argv)
    #Tests if the job name is specified
    if argCount != 2:
        error("ERROR: job name missing from command line", dateTimeStamp)
    else: 
        jobName = sys.argv[1]#Putting the required job name that needs to be backed up into the command line
        #If the job name is valid
        if jobName not in jobs:#If the name that has been put into the command line is not found it prints an error message
            error(f'ERROR: Jobname {jobName} not defined.',dateTimeStamp)
        else:
            for srcPath in jobs[jobName]: #the path of the jobs in backupcfg.py is defined by srcPath
                if not os.path.exists(srcPath):
                    error("ERROR: file " + srcPath + " does not exist.",dateTimeStamp)
                else:
                    if not os.path.exists(dstPath):
                        error("ERROR: destination path " + srcPath + " does not exist.",dateTimeStamp)
                    else:
                        #the source path is valid
    
                        srcDetails = pathlib.PurePath(srcPath)
                        dstLoc = dstPath + "/" + srcDetails.name + "-" + dateTimeStamp
                        
                        if pathlib.Path(srcPath).is_dir(): #Backup a directory and  files
                            shutil.copytree(srcPath, dstLoc)
                            success('SUCCESS: Files backed up', dateTimeStamp)
                            logging(f"SUCCESS: copied{srcPath} to {dstLoc}",dateTimeStamp)
                        else:
                            shutil.copy2(srcPath, dstLoc)
                            success('SUCCESS: Files backed up', dateTimeStamp)
                            logging(f"SUCCESS: copied{srcPath} to {dstLoc}",dateTimeStamp)
                           
if __name__ == '__main__':
    main()
    


