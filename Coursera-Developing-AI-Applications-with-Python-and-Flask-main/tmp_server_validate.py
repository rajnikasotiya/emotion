import json
import types
from server import app

class FakeResp:
    def __init__(self):
        self._payload = json.dumps({'anger': 0.9, 'disgust': 0.05, 'fear': 0.02, 'joy': 0.02, 'sadness': 0.01})

    def raise_for_status(self):
        pass

    def json(self):
        return {'text': self._payload}

    @property
    def text(self):
        return self._payload

import EmotionDetection.emotion_detection as ed
ed.requests = types.SimpleNamespace(post=lambda url, headers, json, timeout: FakeResp())

with app.test_client() as client:
    response = client.get('/emotionDetector?textToAnalyze=I think I am having fun')
    print(response.status_code)
    print(response.data.decode())
