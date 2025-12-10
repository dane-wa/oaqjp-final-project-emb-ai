from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result1 = emotion_detector("I’m glad this happened")
        self.assertEqual(result1["dominant_emotion"], "joy")
        result2 = emotion_detector("I’m really angry about this")
        self.assertEqual(result2["dominant_emotion"], "anger")
        result3 = emotion_detector("I feel disgusted just hearing about it")
        self.assertEqual(result3["dominant_emotion"], "disgust")
        result4 = emotion_detector("I’m so sad about this")
        self.assertEqual(result4["dominant_emotion"], "sadness")
        result5 = emotion_detector("I’m really afraid that this will happen")
        self.assertEqual(result5["dominant_emotion"], "fear")
    

if __name__ == "__main__":
    unittest.main()



