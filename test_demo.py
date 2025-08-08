import unittest
import sys
from io import StringIO
import demo


class TestGeminiVariations(unittest.TestCase):

    def test_short_question(self):
        """Test with a short AI question"""
        # Temporarily modify the input in demo module
        def modified_generate():
            client = demo.genai.Client(
                api_key=demo.os.environ.get("GEMINI_API_KEY"),
            )
            model = "gemini-2.0-flash"
            contents = [
                demo.types.Content(
                    role="user",
                    parts=[
                        demo.types.Part.from_text(text="What is AI?"),
                    ],
                ),
            ]
            generate_content_config = demo.types.GenerateContentConfig()
            
            for chunk in client.models.generate_content_stream(
                model=model,
                contents=contents,
                config=generate_content_config,
            ):
                print(chunk.text, end="")
        
        # Capture output
        captured_output = StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output
        
        try:
            # Run modified function
            modified_generate()
            
            # Get output
            output = captured_output.getvalue()
            
            # Restore stdout before printing results
            sys.stdout = original_stdout
            
            # Print the actual response
            print(f"\n[SHORT QUESTION TEST] Generated output:")
            print("-" * 50)
            print(output)
            print("-" * 50)
            
            # Assertions
            self.assertIsInstance(output, str)
            self.assertGreater(len(output), 0)
            # Check if response contains AI-related keywords
            ai_keywords = ['artificial intelligence', 'AI', 'machine learning', 'intelligence', 'computer']
            contains_ai_content = any(keyword.lower() in output.lower() for keyword in ai_keywords)
            self.assertTrue(contains_ai_content, "Response should contain AI-related content")
            
        finally:
            sys.stdout = original_stdout

    def test_code_generation(self):
        """Test code generation capability"""
        # Temporarily modify the input in demo module
        def modified_generate():
            client = demo.genai.Client(
                api_key=demo.os.environ.get("GEMINI_API_KEY"),
            )
            model = "gemini-2.0-flash"
            contents = [
                demo.types.Content(
                    role="user",
                    parts=[
                        demo.types.Part.from_text(text="Write hello world in Python"),
                    ],
                ),
            ]
            generate_content_config = demo.types.GenerateContentConfig()
            
            for chunk in client.models.generate_content_stream(
                model=model,
                contents=contents,
                config=generate_content_config,
            ):
                print(chunk.text, end="")
        
        # Capture output
        captured_output = StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output
        
        try:
            # Run modified function
            modified_generate()
            
            # Get output
            output = captured_output.getvalue()
            
            # Restore stdout before printing results
            sys.stdout = original_stdout
            
            # Print the actual response
            print(f"\n[CODE GENERATION TEST] Generated output:")
            print("-" * 50)
            print(output)
            print("-" * 50)
            
            # Assertions
            self.assertIsInstance(output, str)
            self.assertGreater(len(output), 0)
            # Check if response contains Python code elements
            python_keywords = ['print', 'hello', 'world', 'python', 'def', '(', ')']
            contains_python_code = any(keyword.lower() in output.lower() for keyword in python_keywords)
            self.assertTrue(contains_python_code, "Response should contain Python code elements")
            
        finally:
            sys.stdout = original_stdout

    def test_creative_task(self):
        """Test creative writing capability with haiku"""
        # Temporarily modify the input in demo module
        def modified_generate():
            client = demo.genai.Client(
                api_key=demo.os.environ.get("GEMINI_API_KEY"),
            )
            model = "gemini-2.0-flash"
            contents = [
                demo.types.Content(
                    role="user",
                    parts=[
                        demo.types.Part.from_text(text="Write a haiku about coding"),
                    ],
                ),
            ]
            generate_content_config = demo.types.GenerateContentConfig()
            
            for chunk in client.models.generate_content_stream(
                model=model,
                contents=contents,
                config=generate_content_config,
            ):
                print(chunk.text, end="")
        
        # Capture output
        captured_output = StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output
        
        try:
            # Run modified function
            modified_generate()
            
            # Get output
            output = captured_output.getvalue()
            
            # Restore stdout before printing results
            sys.stdout = original_stdout
            
            # Print the actual response
            print(f"\n[CREATIVE TASK TEST] Generated output:")
            print("-" * 50)
            print(output)
            print("-" * 50)
            
            # Assertions
            self.assertIsInstance(output, str)
            self.assertGreater(len(output), 0)
            # Check if response contains haiku/poetry elements
            haiku_keywords = ['haiku', 'coding', 'code', 'lines', 'syllables']
            coding_keywords = ['code', 'coding', 'program', 'debug', 'compile', 'function']
            contains_haiku_content = any(keyword.lower() in output.lower() for keyword in haiku_keywords)
            contains_coding_content = any(keyword.lower() in output.lower() for keyword in coding_keywords)
            
            # Should contain either haiku structure or coding-related content
            self.assertTrue(contains_haiku_content or contains_coding_content, 
                          "Response should contain haiku or coding-related content")
            
        finally:
            sys.stdout = original_stdout


if __name__ == '__main__':
    unittest.main()