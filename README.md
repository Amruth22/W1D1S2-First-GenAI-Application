# Gemini Inference

A Python script for interacting with Google's Gemini AI model using streaming inference.

## Setup

### Prerequisites
- Python 3.8 or higher
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

3. Set up your API key:
- Using .env (recommended for local dev):
```bash
# .env
GEMINI_API_KEY=your_api_key_here
```
- Or set an environment variable:
```bash
# macOS/Linux
export GEMINI_API_KEY="your_api_key_here"
# Windows (PowerShell)
$env:GEMINI_API_KEY="your_api_key_here"
```

## Usage

### CLI (recommended)

You can now pass the prompt directly on the command line:

```bash
python demo.py --prompt "What is AI?"
```

Optional arguments:
- `--model` / `-m` to choose a model (default: `gemini-2.0-flash`)
- `--no-stream-print` to suppress live streaming output (still returns the full text)

Examples:
```bash
python demo.py --prompt "Write hello world in Python" -m gemini-2.0-flash
python demo.py --prompt "Write a haiku about coding" --no-stream-print
```

### From Python code

```python
from demo import generate

text = generate("Explain quantum computing in simple terms", print_stream=False)
print(text)
```

## Running Tests

The tests make real API calls with different prompts (no mocking).

```bash
python -m unittest test_demo.py -v
```

Tests included:
- Short question: "What is AI?"
- Code generation: "Write hello world in Python"
- Creative task: "Write a haiku about coding"

## Files

- `demo.py` - Reusable generate(prompt) function with CLI support
- `test_demo.py` - Simple tests that call generate() directly
- `.env` - Local environment variables (do not commit secrets)
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Features

- Streaming response from Gemini AI
- Reusable API: `generate(prompt, model="gemini-2.0-flash", print_stream=True) -> str`
- CLI usage with argparse
- Real-call tests without mocks

## API Key Security

- Never commit secrets to version control. This repo currently contains a .env file for convenience; treat this repo as private.
- In production, inject `GEMINI_API_KEY` via secure environment management.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run the tests
5. Submit a pull request

## License

This project is open source and available under the MIT License.
