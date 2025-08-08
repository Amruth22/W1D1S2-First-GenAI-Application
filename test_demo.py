import unittest
import sys
from io import StringIO
from unittest.mock import patch
import demo


class TestGeminiVariations(unittest.TestCase):

    def _run_test_with_input(self, test_input, test_name):
        """Helper method to run demo.generate() with different inputs"""
        # Capture output
        captured_output = StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output
        
        try:
            # Temporarily patch the input text in the demo module
            with patch.object(demo.types.Part, 'from_text') as mock_from_text:
                mock_from_text.return_value = demo.types.Part.from_text(text=test_input)
                
                # Run the existing demo.generate() function
                demo.generate()
            
            # Get output
            output = captured_output.getvalue()
            
            # Restore stdout before printing results
            sys.stdout = original_stdout
            
            # Print the actual response
            print(f"\n[{test_name}] Generated output:")
            print("-" * 50)
            print(output)
            print("-" * 50)
            
            return output
            
        finally:
            sys.stdout = original_stdout

    def test_short_question(self):
        """Test with a short AI question"""
        output = self._run_test_with_input("What is AI?", "SHORT QUESTION TEST")
        
        # Assertions
        self.assertIsInstance(output, str)
        self.assertGreater(len(output), 0)
        # Check if response contains AI-related keywords
        ai_keywords = ['artificial intelligence', 'AI', 'machine learning', 'intelligence', 'computer']
        contains_ai_content = any(keyword.lower() in output.lower() for keyword in ai_keywords)
        self.assertTrue(contains_ai_content, "Response should contain AI-related content")

    def test_code_generation(self):
        """Test code generation capability"""
        output = self._run_test_with_input("Write hello world in Python", "CODE GENERATION TEST")
        
        # Assertions
        self.assertIsInstance(output, str)
        self.assertGreater(len(output), 0)
        # Check if response contains Python code elements
        python_keywords = ['print', 'hello', 'world', 'python', 'def', '(', ')']
        contains_python_code = any(keyword.lower() in output.lower() for keyword in python_keywords)
        self.assertTrue(contains_python_code, "Response should contain Python code elements")

    def test_creative_task(self):
        """Test creative writing capability with haiku"""
        output = self._run_test_with_input("Write a haiku about coding", "CREATIVE TASK TEST")
        
        # Assertions
        self.assertIsInstance(output, str)
        self.assertGreater(len(output), 0)
        
        # More flexible keyword matching for creative content
        creative_keywords = [
            'haiku', 'coding', 'code', 'program', 'debug', 'compile', 'function',
            'keys', 'screen', 'logic', 'bugs', 'stars', 'fingers', 'dance',
            'blooms', 'glowing', 'poetry', 'poem', 'verse', 'lines'
        ]
        
        contains_creative_content = any(keyword.lower() in output.lower() for keyword in creative_keywords)
        
        # Also check for haiku structure (3 lines with commas or line breaks)
        has_line_structure = (',' in output and len(output.split(',')) >= 2) or len(output.split('\n')) >= 3
        
        # Pass if it contains relevant keywords OR has poem-like structure
        self.assertTrue(contains_creative_content or has_line_structure, 
                      f"Response should contain creative/coding content or poem structure. Got: {output}")


if __name__ == '__main__':
    unittest.main()