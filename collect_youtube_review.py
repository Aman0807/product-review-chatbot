from youtube_transcript_api import YouTubeTranscriptApi


video_url = "https://www.youtube.com/watch?v=ac4OCcVyqNE"

video_url= video_url.split('=')[1]
transcript = YouTubeTranscriptApi.get_transcript(video_url)

transcript = '\n'.join(i['text'] for i in transcript )


print(transcript)

with open('youtube_review.txt', 'w') as f:
    f.write(transcript)