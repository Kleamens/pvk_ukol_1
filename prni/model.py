from enum import Enum
class FileFlags(Enum):
    EMPTY = 1
    EXCEEDED = 2

class FileViolation():
    def __init__(self,abspath:str, filename:str, flag:FileFlags):
      self.abspath = abspath
      self.filename =filename 
      self.flag =flag 
