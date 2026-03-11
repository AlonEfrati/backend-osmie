from fastapi import FastAPI
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig

app = FastAPI()


@app.get("/transcript/{video_id}")
def get_transcript(video_id: str):
    proxy_config = WebshareProxyConfig(
        proxy_username="ortdpewv-1",
        proxy_password="4wsz5w2utihy",
    )
    ytt_api = YouTubeTranscriptApi(proxy_config=proxy_config)
    result = ytt_api.fetch(video_id)
    return {"transcript": result}
