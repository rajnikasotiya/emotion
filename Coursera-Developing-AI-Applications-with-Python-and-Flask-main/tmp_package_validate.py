import json
import types
from EmotionDetection import emotion_detector
import EmotionDetection

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

EmotionDetection.emotion_detection.requests = types.SimpleNamespace(post=lambda url, headers, json, timeout: FakeResp())
print('import ok')
print(emotion_detector('I hate working long hours.'))
