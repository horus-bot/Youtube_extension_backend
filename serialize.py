import json 
from transcription import subtit 

def serial(url):
    object = subtit(url)
    str_format=json.dumps(object)
    return str_format

if __name__=="__main__":
    print(serial("https://www.youtube.com/watch?v=ACwnxwu8Tng"))