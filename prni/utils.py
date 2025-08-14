from smbclient import listdir,scandir
from typing import List
from model import FileViolation,FileFlags

from static import logger


def bytes_to_megabytes(bytes_value):
    megabytes = bytes_value / (1024 * 1024)
    return megabytes


def smb_scan(path,size_limit):
    file_violations :List[FileViolation]  = list()

    for file_info in scandir(path=path):
        if file_info.is_file():
            file_size = bytes_to_megabytes(file_info.smb_info.allocation_size)
            if file_size > size_limit:
                file_violations.append(FileViolation(
                abspath=file_info.path,
                filename=file_info.name,
                flag=FileFlags.EXCEEDED))
                logger.info("File too big: " + file_info.path)    

        elif file_info.is_dir():
            if(len(listdir(file_info.path))==0):
                file_violations.append(FileViolation(
                abspath=file_info.path,
                filename=file_info.name,
                flag=FileFlags.EMPTY))
                logger.info("Directory Empty: " + file_info.path)
            else:
                file_violations.extend(smb_scan(path=file_info.path,size_limit=size_limit))
            
    return file_violations
    