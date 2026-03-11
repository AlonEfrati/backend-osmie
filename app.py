from fastapi import FastAPI
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()


@app.get("/transcript/{video_id}")
def get_transcript(video_id: str):
    ytt_api = YouTubeTranscriptApi()
    result = ytt_api.fetch(video_id)
    return {"transcript": result}
