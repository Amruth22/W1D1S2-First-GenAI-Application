import unittest
from unittest.mock import patch, MagicMock
import os
import sys
from io import StringIO

# Import the module we're testing
import demo


class TestGeminiInference(unittest.TestCase):
    """Simple unit tests for Gemini inference."""

    @patch('demo.genai.Client')
    def test_generate_basic_inference(self, mock_client_class):
        """Test basic inference functionality."""
        # Setup mock client
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client
        
        # Mock response chunks
        mock_chunk = MagicMock()
        mock_chunk.text = "Hello from Gemini!"
        mock_client.models.generate_content_stream.return_value = [mock_chunk]
        
        # Capture output
        captured_output = StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output
        
        try:
            # Set API key and run
            with patch.dict(os.environ, {'GEMINI_API_KEY': 'test_key'}):
                demo.generate()
            
            # Check output
            output = captured_output.getvalue()
            self.assertEqual(output, "Hello from Gemini!")
            
        finally:
            sys.stdout = original_stdout

    @patch('demo.genai.Client')
    def test_api_key_usage(self, mock_client_class):
        """Test that API key is properly used."""
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client
        mock_client.models.generate_content_stream.return_value = []
        
        with patch.dict(os.environ, {'GEMINI_API_KEY': 'my_test_key'}):
            demo.generate()
        
        # Verify client was created with correct API key
        mock_client_class.assert_called_once_with(api_key='my_test_key')

    @patch('demo.genai.Client')
    def test_model_selection(self, mock_client_class):
        """Test that correct model is used."""
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client
        mock_client.models.generate_content_stream.return_value = []
        
        with patch.dict(os.environ, {'GEMINI_API_KEY': 'test_key'}):
            demo.generate()
        
        # Check that gemini-2.0-flash model was used
        call_args = mock_client.models.generate_content_stream.call_args
        self.assertEqual(call_args.kwargs['model'], 'gemini-2.0-flash')

    @patch('demo.genai.Client')
    def test_streaming_response(self, mock_client_class):
        """Test streaming response handling."""
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client
        
        # Mock multiple chunks
        chunks = []
        for i in range(3):
            chunk = MagicMock()
            chunk.text = f"Part {i+1} "
            chunks.append(chunk)
        
        mock_client.models.generate_content_stream.return_value = chunks
        
        # Capture output
        captured_output = StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output
        
        try:
            with patch.dict(os.environ, {'GEMINI_API_KEY': 'test_key'}):
                demo.generate()
            
            # Check that all chunks were printed
            output = captured_output.getvalue()
            self.assertEqual(output, "Part 1 Part 2 Part 3 ")
            
        finally:
            sys.stdout = original_stdout

    @patch('demo.genai.Client')
    def test_no_api_key(self, mock_client_class):
        """Test behavior when no API key is provided."""
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client
        mock_client.models.generate_content_stream.return_value = []
        
        # Clear environment variables
        with patch.dict(os.environ, {}, clear=True):
            demo.generate()
        
        # Verify client was created with None API key
        mock_client_class.assert_called_once_with(api_key=None)


if __name__ == '__main__':
    unittest.main()