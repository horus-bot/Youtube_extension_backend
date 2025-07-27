import json 
from transcription import translation 

def serial():
    object = translation()
    str_format=json.dumps(object)
    return str_format

if __name__=="__main__":
    serial()