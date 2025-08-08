import unittest
import demo


class TestGeminiVariations(unittest.TestCase):

    def test_short_question(self):
        output = demo.generate("What is AI?", print_stream=False)
        self.assertIsInstance(output, str)
        self.assertGreater(len(output), 0)
        ai_keywords = ['artificial intelligence', 'AI', 'machine learning', 'intelligence', 'computer']
        self.assertTrue(any(k.lower() in output.lower() for k in ai_keywords))

    def test_code_generation(self):
        output = demo.generate("Write hello world in Python", print_stream=False)
        self.assertIsInstance(output, str)
        self.assertGreater(len(output), 0)
        python_keywords = ['print', 'hello', 'world', 'python', 'def', '(', ')']
        self.assertTrue(any(k.lower() in output.lower() for k in python_keywords))

    def test_creative_task(self):
        output = demo.generate("Write a haiku about coding", print_stream=False)
        self.assertIsInstance(output, str)
        self.assertGreater(len(output), 0)
        creative_keywords = ['haiku', 'coding', 'code', 'program', 'debug', 'compile', 'function',
                             'keys', 'screen', 'logic', 'bugs', 'stars', 'fingers', 'dance',
                             'blooms', 'glowing', 'poetry', 'poem', 'verse', 'lines']
        has_keywords = any(k.lower() in output.lower() for k in creative_keywords)
        has_structure = (',' in output and len(output.split(',')) >= 2) or ('\n' in output and len(output.split('\n')) >= 3)
        self.assertTrue(has_keywords or has_structure)


if __name__ == '__main__':
    unittest.main()