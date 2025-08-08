# Gemini Inference

A Python script for interacting with Google's Gemini AI model using streaming inference.

## Setup

### Prerequisites
- Python 3.7 or higher
- A Google AI API key

### Installation

1. Clone this repository:
```bash
git clone https://github.com/Amruth22/gemini-inference.git
cd gemini-inference
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your API key as an environment variable:
```bash
export GEMINI_API_KEY="your_api_key_here"
```

## Usage

### Running the Demo

```bash
python demo.py
```

**Note**: Before running, make sure to replace `INSERT_INPUT_HERE` in the demo.py file with your actual input text.

### Running Tests

Run the unit tests to verify everything is working correctly:

```bash
python -m pytest test_demo.py -v
```

Or using unittest:

```bash
python test_demo.py
```

## Files

- `demo.py` - Main inference script using Gemini 2.0 Flash model
- `test_demo.py` - Comprehensive unit tests for the demo script
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Features

- Streaming response from Gemini AI
- Environment variable configuration for API key
- Comprehensive unit tests with mocking
- Error handling and edge case testing

## API Key Security

**Important**: Never commit your actual API key to version control. Always use environment variables or secure configuration management.

## Testing

The test suite includes:
- Unit tests with mocked API calls
- Tests for different response scenarios
- Environment variable handling tests
- Content structure validation
- Integration test framework (optional)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run the tests
5. Submit a pull request

## License

This project is open source and available under the MIT License.