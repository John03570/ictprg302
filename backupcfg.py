jobs = {'job1':['/home/ec2-user/environment/ictprg302/dir1'],
        'job2':['/home/ec2-user/environment/ictprg302/dir1/file1.dat'],
        'job3':['/home/ec2-user/environment/ictprg302/dir1/file2.dat'],
        'job4':['/home/ec2-user/environment/ictprg302/file3.dat', '/home/ec2-user/environment/ictprg302/file4.dat']}
        
dstPath = '/home/ec2-user/environment/ictprg302/backups' 

# SMTP settings
smtp = {"sender": "jjfitzpatrick357@gmail.com", # elasticemail.com verified sender
"recipient": "30016678@students.sunitafe.edu.au", # elasticemail.com verified recipient
"server": "smtp.elasticemail.com", # elasticemail.com SMTP server
"port": 2525, # elasticemail.com SMTP port
"user": "jjfitzpatrick357@gmail.com", # elasticemail.com user
"password": ""} # elasticemail.com password


logPath = '/home/ec2-user/environment/ictprg302/backup.log' 