import unittest
import sys
from io import StringIO
import demo


class TestGeminiInference(unittest.TestCase):
    """Simple inference test with real API call."""

    def test_inference(self):
        """Test actual inference with Gemini API."""
        # Capture output
        captured_output = StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output
        
        try:
            # Run the inference
            demo.generate()
            
            # Get the output
            output = captured_output.getvalue()
            
            # Basic assertions
            self.assertIsInstance(output, str)
            self.assertGreater(len(output), 0, "Should generate some output")
            
            print(f"\nGenerated output: {output}")
            
        finally:
            sys.stdout = original_stdout


if __name__ == '__main__':
    unittest.main()