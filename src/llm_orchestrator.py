import logging
import time
import requests
from typing import Dict, Any
from exceptions import ChapterMakerError

logger = logging.getLogger(__name__)


class LLMOrchestrator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openai.com/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        self.max_retries = 3
        self.retry_delay = 1  # seconds

    def _call_api(self, messages: list) -> Dict[str, Any]:
        retries = 0
        while retries < self.max_retries:
            try:
                response = requests.post(
                    self.base_url,
                    headers=self.headers,
                    json={"model": "gpt-4o", "messages": messages, "temperature": 0.7},
                    timeout=30,
                )
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                retries += 1
                if retries == self.max_retries:
                    raise ChapterMakerError(
                        f"API call failed after {self.max_retries} retries: {str(e)}"
                    )
                logger.warning(
                    f"API call failed, retrying in {self.retry_delay} seconds..."
                )
                time.sleep(self.retry_delay * retries)

    def generate_chapters(self, srt_content: str) -> str:
        prompt = """I will give you a video transcript in SRT format. Create logical chapter markers with timestamp and title. Each chapter should be a distinct section of the video.

    Try to keep chapters to a reasonable length, typically a few minutes each. Usually a ten minute video would have 3-5 chapters.

    VERY IMPORTANT: Only output chapter timestamps and titles in this exact format, with no additional text:
    MM:SS - Chapter Title

    Example:
    00:00 - Introduction
    02:15 - Main Topic
    05:30 - Conclusion

    Each timestamp should be on a new line. Do not include any other text, explanations, or formatting in your response."""
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant that creates YouTube chapters from transcripts.",
            },
            {
                "role": "user",
                "content": f"{prompt}\n\nHere's the transcript:\n\n{srt_content}",
            },
        ]

        response = self._call_api(messages)
        return response["choices"][0]["message"]["content"]

    def generate_titles(self, srt_content: str) -> str:
        prompt = """suggest about 10 short catchy titles for a youtube video with this content. but i don't want them to be cheesy or sound like clickbait.

    VERY IMPORTANT: Only output titles, one per line, with no additional text, numbers, or formatting. DO NOT NUMBER THE LIST OF TITLES.
    
    Example output:

    First Title Here
    Second Title Here
    Third Title Here"""
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant that creates engaging but not clickbait YouTube titles.",
            },
            {
                "role": "user",
                "content": f"{prompt}\n\nHere's the transcript:\n\n{srt_content}",
            },
        ]

        response = self._call_api(messages)
        return response["choices"][0]["message"]["content"]
