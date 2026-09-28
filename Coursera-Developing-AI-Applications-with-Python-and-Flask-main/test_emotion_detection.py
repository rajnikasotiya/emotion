import json
import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


def make_response(scores):
    mock_resp = Mock()
    mock_resp.raise_for_status.return_value = None
    payload = json.dumps(scores)
    mock_resp.json.return_value = {'text': payload}
    mock_resp.text = payload
    return mock_resp


class TestEmotionDetection(unittest.TestCase):
    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_joy(self, mock_post):
        mock_post.return_value = make_response({'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.9, 'sadness': 0.1})
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_anger(self, mock_post):
        mock_post.return_value = make_response({'anger': 0.85, 'disgust': 0.05, 'fear': 0.05, 'joy': 0.03, 'sadness': 0.02})
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'], 'anger')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_disgust(self, mock_post):
        mock_post.return_value = make_response({'anger': 0.1, 'disgust': 0.8, 'fear': 0.05, 'joy': 0.03, 'sadness': 0.02})
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_sadness(self, mock_post):
        mock_post.return_value = make_response({'anger': 0.02, 'disgust': 0.03, 'fear': 0.05, 'joy': 0.1, 'sadness': 0.8})
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_fear(self, mock_post):
        mock_post.return_value = make_response({'anger': 0.05, 'disgust': 0.1, 'fear': 0.8, 'joy': 0.02, 'sadness': 0.03})
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
