from url import takeUrl
from youtube_transcript_api import YouTubeTranscriptApi


def subtit():
    video_id = takeUrl()
    ytt_api = YouTubeTranscriptApi()
    content = ytt_api.fetch(video_id)
    
    full =""   
    for snippet in content:
         full += (snippet.text)
    return full

if __name__ == "__main__":
   print( subtit())
