import unittest
import os
import demo


class TestGeminiVariations(unittest.TestCase):

    def test_api_key_configuration(self):
        """Test that API key is properly configured"""
        api_key = os.environ.get("GEMINI_API_KEY")
        self.assertIsNotNone(api_key, "GEMINI_API_KEY environment variable is not set")
        self.assertGreater(len(api_key.strip()), 0, "GEMINI_API_KEY is empty")
        self.assertFalse(api_key.startswith("your_api_key"), "GEMINI_API_KEY appears to be placeholder text")

    def setUp(self):
        """Check API key availability before running tests"""
        if not os.environ.get("GEMINI_API_KEY"):
            self.skipTest("GEMINI_API_KEY not set")

    def _basic_response_validation(self, output, min_length=10):
        """Common validation logic for all responses"""
        self.assertIsInstance(output, str)
        self.assertGreater(len(output), min_length)

    def _safe_generate(self, prompt, **kwargs):
        """Wrapper for demo.generate with error handling"""
        try:
            return demo.generate(prompt, print_stream=False, **kwargs)
        except Exception as e:
            self.fail(f"API call failed: {e}")

    def test_short_question(self):
        output = self._safe_generate("What is AI?")
        self._basic_response_validation(output)
        ai_keywords = ['artificial intelligence', 'AI', 'machine learning', 'intelligence', 'computer']
        self.assertTrue(any(k.lower() in output.lower() for k in ai_keywords))

    def test_code_generation(self):
        output = self._safe_generate("Write hello world in Python")
        self._basic_response_validation(output)
        python_keywords = ['print', 'hello', 'world', 'python', 'def', '(', ')']
        self.assertTrue(any(k.lower() in output.lower() for k in python_keywords))

    def test_creative_task(self):
        output = self._safe_generate("Write a haiku about coding")
        self._basic_response_validation(output)
        creative_keywords = ['haiku', 'coding', 'code', 'program', 'debug', 'compile', 'function',
                             'keys', 'screen', 'logic', 'bugs', 'stars', 'fingers', 'dance',
                             'blooms', 'glowing', 'poetry', 'poem', 'verse', 'lines']
        has_keywords = any(k.lower() in output.lower() for k in creative_keywords)
        has_structure = (',' in output and len(output.split(',')) >= 2) or ('\n' in output and len(output.split('\n')) >= 3)
        self.assertTrue(has_keywords or has_structure)


if __name__ == '__main__':
    unittest.main()