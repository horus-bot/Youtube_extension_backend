from url import takeUrl
from youtube_transcript_api import YouTubeTranscriptApi


def subtit():
    ytt_api = YouTubeTranscriptApi()
    content= ytt_api.fetch(takeUrl())
    return content

if __name__=="__main__":
    print(subtit())