from smbclient import register_session
import csv 
from utils import  smb_scan
from static import logger
from dotenv import load_dotenv
import os

load_dotenv()

# SMB connection servername 
servername = os.getenv("SERVER_NAME")
# SMB connection username 
username = os.getenv("SERVER_USERNAME")
# SMB connection  
password = os.getenv("SERVER_PASSWORD")

#Location where the scan is initiated
start_location = f"//{servername}/shared"

csv_filename = 'output.csv'
# Headers in the CSV file default: "Path", "Name", "Flag"
csv_headers = ["Path", "Name","Flag"]
# File size limit in MB for EXCEEDED flag
SIZE_LIMIT = 500 

register_session = register_session(servername,
                                    username=username,
                                    password=password) 


file_violations = smb_scan(start_location,size_limit=SIZE_LIMIT) 
file_violations = sorted(file_violations,key = lambda file: file.flag.name)

with open(csv_filename,'w') as file: 
   #  Checking if the 
    try:
      assert csv_headers[0]=="Path"
      assert csv_headers[1]=="Name"
      assert csv_headers[2]=="Flag"
    except AssertionError: 
      logger.error("The headers order or values were changed")

    csvwriter = csv.writer(file)
    csvwriter.writerow(csv_headers)

    for file_violation in file_violations:
      csvwriter.writerow([file_violation.abspath,file_violation.filename,file_violation.flag])


