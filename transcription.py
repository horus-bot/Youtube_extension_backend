from url import takeUrl
from youtube_transcript_api import YouTubeTranscriptApi


def subtit(url):
    video_id = takeUrl(url)
    ytt_api = YouTubeTranscriptApi()
    content = ytt_api.fetch(video_id)
    
    full =""   
    for snippet in content:
         full += (snippet.text)
    return full

def translation():
    video_id = takeUrl()
    ytt_api = YouTubeTranscriptApi()
    content = ytt_api.fetch(video_id)
    last_snippet = content.to_raw_data()
    return last_snippet

if __name__ == "__main__":
   a=input("please eneter the url ")
   print(subtit(a))
   print(type(a))
