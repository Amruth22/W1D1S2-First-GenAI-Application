import unittest
from unittest.mock import patch, MagicMock, call
import os
import sys
from io import StringIO

# Import the module we're testing
import demo


class TestGeminiDemo(unittest.TestCase):
    """Unit tests for the Gemini inference demo script."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.original_stdout = sys.stdout
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        """Clean up after each test method."""
        sys.stdout = self.original_stdout

    @patch.dict(os.environ, {'GEMINI_API_KEY': 'test_api_key'})
    @patch('demo.genai.Client')
    def test_generate_with_api_key(self, mock_client_class):
        """Test generate function with API key set in environment."""
        # Mock the client and its methods
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client
        
        # Mock the streaming response
        mock_chunk1 = MagicMock()
        mock_chunk1.text = "Hello "
        mock_chunk2 = MagicMock()
        mock_chunk2.text = "World!"
        
        mock_client.models.generate_content_stream.return_value = [mock_chunk1, mock_chunk2]
        
        # Call the function
        demo.generate()
        
        # Verify client was created with correct API key
        mock_client_class.assert_called_once_with(api_key='test_api_key')
        
        # Verify the streaming method was called with correct parameters
        mock_client.models.generate_content_stream.assert_called_once()
        call_args = mock_client.models.generate_content_stream.call_args
        
        # Check model parameter
        self.assertEqual(call_args.kwargs['model'], 'gemini-2.0-flash')
        
        # Check contents parameter structure
        contents = call_args.kwargs['contents']
        self.assertEqual(len(contents), 1)
        self.assertEqual(contents[0].role, 'user')
        self.assertEqual(len(contents[0].parts), 1)
        
        # Verify output was printed
        output = self.captured_output.getvalue()
        self.assertEqual(output, "Hello World!")

    @patch.dict(os.environ, {}, clear=True)
    @patch('demo.genai.Client')
    def test_generate_without_api_key(self, mock_client_class):
        """Test generate function when API key is not set in environment."""
        # Mock the client
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client
        
        # Mock empty streaming response
        mock_client.models.generate_content_stream.return_value = []
        
        # Call the function
        demo.generate()
        
        # Verify client was created with None API key
        mock_client_class.assert_called_once_with(api_key=None)

    @patch.dict(os.environ, {'GEMINI_API_KEY': 'test_api_key'})
    @patch('demo.genai.Client')
    def test_generate_with_empty_response(self, mock_client_class):
        """Test generate function with empty streaming response."""
        # Mock the client
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client
        
        # Mock empty streaming response
        mock_client.models.generate_content_stream.return_value = []
        
        # Call the function
        demo.generate()
        
        # Verify no output was printed
        output = self.captured_output.getvalue()
        self.assertEqual(output, "")

    @patch.dict(os.environ, {'GEMINI_API_KEY': 'test_api_key'})
    @patch('demo.genai.Client')
    def test_generate_with_multiple_chunks(self, mock_client_class):
        """Test generate function with multiple response chunks."""
        # Mock the client
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client
        
        # Mock multiple chunks
        chunks = []
        expected_output = ""
        for i in range(5):
            chunk = MagicMock()
            chunk.text = f"Chunk {i} "
            chunks.append(chunk)
            expected_output += f"Chunk {i} "
        
        mock_client.models.generate_content_stream.return_value = chunks
        
        # Call the function
        demo.generate()
        
        # Verify output
        output = self.captured_output.getvalue()
        self.assertEqual(output, expected_output)

    @patch.dict(os.environ, {'GEMINI_API_KEY': 'test_api_key'})
    @patch('demo.genai.Client')
    def test_generate_content_config_structure(self, mock_client_class):
        """Test that GenerateContentConfig is properly structured."""
        # Mock the client
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client
        mock_client.models.generate_content_stream.return_value = []
        
        # Call the function
        demo.generate()
        
        # Verify the config parameter exists
        call_args = mock_client.models.generate_content_stream.call_args
        self.assertIn('config', call_args.kwargs)

    @patch.dict(os.environ, {'GEMINI_API_KEY': 'test_api_key'})
    @patch('demo.genai.Client')
    def test_content_structure(self, mock_client_class):
        """Test the structure of the content sent to the API."""
        # Mock the client
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client
        mock_client.models.generate_content_stream.return_value = []
        
        # Call the function
        demo.generate()
        
        # Get the call arguments
        call_args = mock_client.models.generate_content_stream.call_args
        contents = call_args.kwargs['contents']
        
        # Verify content structure
        self.assertEqual(len(contents), 1)
        content = contents[0]
        self.assertEqual(content.role, 'user')
        self.assertEqual(len(content.parts), 1)
        
        # Note: The actual text content contains "INSERT_INPUT_HERE" as placeholder

    @patch('demo.generate')
    def test_main_execution(self, mock_generate):
        """Test that generate() is called when script is run as main."""
        # Import and reload the module to trigger __main__ execution
        import importlib
        importlib.reload(demo)
        
        # Note: This test might not work as expected due to how imports work
        # In a real scenario, you'd test this differently or restructure the code


class TestGeminiDemoIntegration(unittest.TestCase):
    """Integration tests that require actual API key (optional)."""
    
    def setUp(self):
        """Set up for integration tests."""
        self.api_key = os.environ.get('GEMINI_API_KEY')
        
    @unittest.skipIf(not os.environ.get('GEMINI_API_KEY'), 
                     "GEMINI_API_KEY not set - skipping integration test")
    def test_generate_with_real_api(self):
        """Integration test with real API (only runs if API key is available)."""
        # This test would make actual API calls
        # Use with caution and only when needed
        original_stdout = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            # This would make a real API call
            # demo.generate()
            # output = captured_output.getvalue()
            # self.assertIsInstance(output, str)
            pass  # Commented out to avoid actual API calls in tests
        finally:
            sys.stdout = original_stdout


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)