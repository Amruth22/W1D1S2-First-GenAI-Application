# Gemini AI Inference System - Coding Challenge

## 🎯 Problem Statement

Build a **Python-based AI Inference System** that integrates with Google's Gemini AI model to provide streaming text generation capabilities. Your task is to create a robust, production-ready system that can handle real-time AI responses, provide both CLI and programmatic interfaces, and include comprehensive testing for API-dependent functionality.

## 📋 Requirements Overview

### Core Functionality
You need to implement a complete AI inference system with:

1. **Streaming Text Generation** using Google Gemini AI API
2. **Command-Line Interface** with argument parsing and user-friendly options
3. **Programmatic API** for integration into other Python applications
4. **Real-time Response Handling** with streaming output capabilities
5. **Comprehensive Testing** including API validation and response verification
6. **Security Best Practices** for API key management and environment configuration

## 🏗️ System Architecture

```
User Input → CLI/API → Gemini Client → Streaming Response → Output Handler
                    ↓
            Environment Config → API Authentication → Error Handling
```

## 📚 Detailed Implementation Requirements

### 1. Core Module (`demo.py`)

**Required Function:**

```python
def generate(prompt: str, model: str = "gemini-2.0-flash", print_stream: bool = True) -> str:
    """
    Generate text from Gemini for a given prompt.

    Args:
        prompt: The user prompt to send to the model.
        model: The Gemini model to use.
        print_stream: If True, prints streamed chunks to stdout as they arrive.

    Returns:
        The full concatenated response text from the stream.
    """
```

**Technical Specifications:**
- **API Integration**: Google Gemini AI client with proper authentication
- **Streaming Support**: Real-time response handling with chunk processing
- **Model Flexibility**: Support for different Gemini model variants
- **Output Control**: Configurable streaming display options
- **Error Handling**: Graceful failure management for API issues

**CLI Interface Requirements:**
- **Argument Parsing**: Use `argparse` for professional command-line interface
- **Default Behavior**: Sensible defaults for quick usage
- **Flexible Options**: Support for custom prompts, models, and output modes
- **Help Documentation**: Clear usage instructions and examples

### 2. Testing Suite (`unit_test.py`)

**Required Test Classes:**

```python
class TestGeminiVariations(unittest.TestCase):
    def test_api_key_configuration(self)
        # Validate API key setup and configuration
    
    def test_short_question(self)
        # Test basic question-answering functionality
    
    def test_code_generation(self)
        # Validate code generation capabilities
    
    def test_creative_task(self)
        # Test creative writing and structured output
```

**Testing Requirements:**
- **Real API Testing**: No mocks - test against actual Gemini API
- **Configuration Validation**: Verify API key setup and environment
- **Response Validation**: Check output quality and expected content
- **Error Handling**: Test graceful failure scenarios
- **Helper Methods**: Reusable validation and testing utilities

### 3. Environment Configuration

**Required Files:**
- **`.env`**: Environment variable storage for API keys
- **`requirements.txt`**: Dependency management
- **`.gitignore`**: Security-focused exclusions

**Configuration Management:**
- **API Key Security**: Environment-based key storage
- **Dependency Management**: Minimal, focused requirements
- **Version Control Safety**: Proper exclusion of sensitive files

## 🧪 Test Cases & Validation

Your implementation will be tested against these scenarios:

### Test Case 1: API Configuration Validation
```python
def test_api_key_configuration(self):
    """Test that API key is properly configured"""
    api_key = os.environ.get("GEMINI_API_KEY")
    self.assertIsNotNone(api_key, "GEMINI_API_KEY environment variable is not set")
    self.assertGreater(len(api_key.strip()), 0, "GEMINI_API_KEY is empty")
    self.assertFalse(api_key.startswith("your_api_key"), "GEMINI_API_KEY appears to be placeholder text")
```

### Test Case 2: Basic AI Interaction
```python
def test_short_question(self):
    output = self._safe_generate("What is AI?")
    self._basic_response_validation(output)
    ai_keywords = ['artificial intelligence', 'AI', 'machine learning', 'intelligence', 'computer']
    self.assertTrue(any(k.lower() in output.lower() for k in ai_keywords))
```

### Test Case 3: Code Generation Capability
```python
def test_code_generation(self):
    output = self._safe_generate("Write hello world in Python")
    self._basic_response_validation(output)
    python_keywords = ['print', 'hello', 'world', 'python', 'def', '(', ')']
    self.assertTrue(any(k.lower() in output.lower() for k in python_keywords))
```

### Test Case 4: Creative Task Handling
```python
def test_creative_task(self):
    output = self._safe_generate("Write a haiku about coding")
    self._basic_response_validation(output)
    # Validate creative content and structure
    creative_keywords = ['haiku', 'coding', 'code', 'program', 'debug', 'compile']
    has_keywords = any(k.lower() in output.lower() for k in creative_keywords)
    has_structure = (',' in output and len(output.split(',')) >= 2) or ('\n' in output and len(output.split('\n')) >= 3)
    self.assertTrue(has_keywords or has_structure)
```

### Test Case 5: CLI Interface Validation
```bash
# Test default behavior
python demo.py

# Test custom prompts
python demo.py --prompt "Explain machine learning"

# Test model selection
python demo.py --model "gemini-2.0-flash" --prompt "Hello AI"

# Test silent mode
python demo.py --no-stream-print --prompt "Calculate 2+2"
```

### Test Case 6: Streaming Functionality
```python
# Test streaming output
response = generate("Tell me about Python programming", print_stream=True)
assert len(response) > 50
assert isinstance(response, str)

# Test silent mode
response = generate("What is 2+2?", print_stream=False)
assert "4" in response or "four" in response.lower()
```

## 📊 Evaluation Criteria

Your solution will be evaluated on:

1. **API Integration** (25%): Proper Gemini AI client usage and authentication
2. **Streaming Implementation** (20%): Real-time response handling and display
3. **CLI Design** (20%): Professional command-line interface with argparse
4. **Testing Quality** (20%): Comprehensive test coverage with real API calls
5. **Code Quality** (15%): Clean architecture, error handling, and documentation

## 🔧 Technical Requirements

### Dependencies
```txt
google-genai>=0.3.0
python-dotenv>=1.0.0
```

### Environment Setup
```env
GEMINI_API_KEY=your_actual_api_key_here
```

### CLI Specifications
```bash
# Required command-line arguments
python demo.py [--prompt PROMPT] [--model MODEL] [--no-stream-print]

# Short form support
python demo.py [-p PROMPT] [-m MODEL]

# Help documentation
python demo.py --help
```

### API Specifications
```python
# Function signature
def generate(prompt: str, model: str = "gemini-2.0-flash", print_stream: bool = True) -> str

# Usage examples
response = generate("What is AI?")
response = generate("Write Python code", model="gemini-2.0-flash", print_stream=False)
```

## 🚀 Advanced Features (Bonus Points)

Implement these for extra credit:

1. **Response Caching**: Cache API responses to avoid repeated calls
2. **Conversation History**: Maintain context across multiple interactions
3. **Output Formatting**: Support for JSON, Markdown, and plain text outputs
4. **Async Support**: Asynchronous API calls for better performance
5. **Rate Limiting**: Implement client-side rate limiting
6. **Configuration Files**: Support for YAML/JSON configuration
7. **Logging System**: Comprehensive logging with different levels
8. **Response Validation**: Content filtering and quality checks

## 📝 Implementation Guidelines

### Core Architecture Patterns

1. **Separation of Concerns**:
   ```python
   # API client logic
   client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
   
   # Streaming handler
   def handle_stream(chunk):
       text = getattr(chunk, "text", None) or ""
       if print_stream and text:
           print(text, end="")
       return text
   
   # Response aggregation
   full_text = []
   for chunk in stream:
       text = handle_stream(chunk)
       if text:
           full_text.append(text)
   ```

2. **Error Handling Strategy**:
   ```python
   try:
       response = client.models.generate_content_stream(...)
   except Exception as e:
       logger.error(f"API call failed: {e}")
       return None
   ```

3. **Configuration Management**:
   ```python
   # Environment variable loading
   try:
       from dotenv import load_dotenv
       load_dotenv()
   except ImportError:
       print("python-dotenv not installed. Using system environment variables only.")
   ```

### Testing Best Practices

1. **Real API Testing**:
   ```python
   def _safe_generate(self, prompt, **kwargs):
       """Wrapper for demo.generate with error handling"""
       try:
           return demo.generate(prompt, print_stream=False, **kwargs)
       except Exception as e:
           self.fail(f"API call failed: {e}")
   ```

2. **Response Validation**:
   ```python
   def _basic_response_validation(self, output, min_length=10):
       """Common validation logic for all responses"""
       self.assertIsInstance(output, str)
       self.assertGreater(len(output), min_length)
   ```

3. **Setup and Teardown**:
   ```python
   def setUp(self):
       """Check API key availability before running API tests"""
       if not os.environ.get("GEMINI_API_KEY"):
           self.skipTest("GEMINI_API_KEY not set")
   ```

## 🎯 Success Criteria

Your implementation is successful when:

- ✅ All unit tests pass with real API calls
- ✅ CLI interface works with all argument combinations
- ✅ Streaming output displays in real-time
- ✅ API key validation prevents unauthorized usage
- ✅ Error handling gracefully manages API failures
- ✅ Code follows Python best practices and PEP 8
- ✅ Documentation is clear and comprehensive
- ✅ Security practices protect sensitive information

## 📋 Submission Requirements

### Required Files
1. **`demo.py`**: Main module with generate() function and CLI interface
2. **`unit_test.py`**: Comprehensive test suite with 4+ test methods
3. **`requirements.txt`**: Minimal dependency list
4. **`.env`**: Environment template (without actual API key)
5. **`.gitignore`**: Security-focused exclusions

### Code Quality Standards
- **Docstrings**: Clear function and class documentation
- **Type Hints**: Use type annotations where appropriate
- **Error Messages**: Helpful error messages for users
- **Comments**: Explain complex logic and API interactions
- **Formatting**: Consistent code style following PEP 8

## 🔍 Sample Usage Examples

### Basic CLI Usage
```bash
# Default prompt
python demo.py
# Output: Streams response to "What is AI?"

# Custom prompt
python demo.py --prompt "Explain quantum computing"
# Output: Streams detailed explanation

# Silent mode
python demo.py --prompt "Write hello world in Java" --no-stream-print
# Output: Returns complete response without streaming
```

### Programmatic Usage
```python
from demo import generate

# Basic usage
response = generate("What are the benefits of Python?")
print(f"Response length: {len(response)} characters")

# Advanced usage
response = generate(
    prompt="Write a function to calculate fibonacci numbers",
    model="gemini-2.0-flash",
    print_stream=False
)
print("Generated code:", response)
```

### Testing Execution
```bash
# Run all tests
python -m unittest unit_test.py -v

# Run specific test
python -m unittest unit_test.TestGeminiVariations.test_code_generation -v

# Expected output:
# test_api_key_configuration ... ok
# test_short_question ... ok  
# test_code_generation ... ok
# test_creative_task ... ok
```

## ⚠️ Important Notes

- **API Key Security**: Never commit real API keys to version control
- **Rate Limits**: Be mindful of API usage quotas and costs
- **Error Handling**: Implement robust error handling for network issues
- **Testing**: Ensure tests can run independently and handle API failures
- **Documentation**: Provide clear usage examples and troubleshooting guides
- **Dependencies**: Keep requirements minimal and well-documented

Build a professional AI inference system that demonstrates modern Python development practices and API integration skills! 🚀