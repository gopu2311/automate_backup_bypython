import shutil 
import datetime
import os
def backup_file(source,destination):
    today = datetime.date.today()
    backup_file_name =os.path.join(destination,f"backup_{today}")
    shutil.make_archive(backup_file_name,'gztar',source)
source=" "
destination = " "
backup_file(source,destination)



