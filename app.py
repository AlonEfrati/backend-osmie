from fastapi import FastAPI
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig

app = FastAPI()


@app.get("/transcript/{video_id}")
def get_transcript(video_id: str):
    proxy_config = WebshareProxyConfig(
        proxy_username="ortdpewv-rotate",
        proxy_password="4wsz5w2utihy",
        domain_name="proxy.webshare.io",
        port=80,
    )
    ytt_api = YouTubeTranscriptApi(proxy_config=proxy_config)
    result = ytt_api.fetch(video_id)
    return {"transcript": result}
