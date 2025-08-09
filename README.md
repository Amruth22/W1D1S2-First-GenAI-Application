# 🤖 Gemini AI Inference Toolkit

> **A beginner-friendly Python project for learning AI integration and API usage**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Google Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange.svg)](https://ai.google.dev/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

This educational project demonstrates how to integrate Google's powerful Gemini AI model into Python applications using streaming inference. Perfect for students learning about AI APIs, Python programming, and modern development practices!

## 📚 What You'll Learn

- **🔌 API Integration**: Connect Python applications to external AI services
- **📡 Streaming Data**: Handle real-time data streams from AI models
- **🧪 Testing Strategies**: Write robust tests for API-dependent code
- **🔒 Security Practices**: Manage API keys and sensitive data safely
- **⚡ CLI Development**: Build command-line interfaces with `argparse`
- **🏗️ Code Architecture**: Structure reusable, maintainable Python modules

---

## 🚀 Quick Start

### 📋 Prerequisites

Before you begin, ensure you have:
- **Python 3.8+** installed ([Download here](https://www.python.org/downloads/))
- A **Google AI API key** ([Get yours here](https://ai.google.dev/))
- Basic understanding of Python and command-line usage

### 🛠️ Installation

#### Step 1: Clone & Navigate
```bash
git clone https://github.com/Amruth22/gemini-inference.git
cd gemini-inference
```

#### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```
**What this installs:**
- `google-genai` - Official Google Generative AI Python client
- `python-dotenv` - Loads environment variables from .env files

#### Step 3: Configure Your API Key

**Option A: Using .env file (Recommended for learning)**
```bash
# Create a .env file in the project root
echo "GEMINI_API_KEY=your_actual_api_key_here" > .env
```

**Option B: Environment Variables**
```bash
# macOS/Linux
export GEMINI_API_KEY="your_actual_api_key_here"

# Windows (Command Prompt)
set GEMINI_API_KEY=your_actual_api_key_here

# Windows (PowerShell)
$env:GEMINI_API_KEY="your_actual_api_key_here"
```

---

## 💻 Usage Examples

### 🎯 Simple CLI Usage

**Just run with default prompt:**
```bash
python demo.py
```
*This will ask "What is AI?" and stream the response live!*

**Custom prompts:**
```bash
# Ask any question
python demo.py --prompt "Explain machine learning in simple terms"

# Generate code
python demo.py --prompt "Write a Python function to sort a list"

# Creative tasks
python demo.py --prompt "Write a haiku about programming"
```

### ⚙️ Advanced CLI Options

```bash
# Use different AI model
python demo.py --prompt "Hello AI!" --model "gemini-2.0-flash"

# Silent mode (no streaming output)
python demo.py --prompt "Calculate 2+2" --no-stream-print

# Short form arguments
python demo.py -p "What is Python?" -m "gemini-2.0-flash"
```

### 🐍 Python Integration

```python
from demo import generate

# Basic usage
response = generate("What are the benefits of Python?")
print(response)

# Without streaming (silent)
response = generate("Write hello world in Java", print_stream=False)
print(response)

# Different model
response = generate("Explain recursion", model="gemini-2.0-flash")
print(response)
```

---

## 🧪 Testing & Quality Assurance

### Running Tests

Our test suite demonstrates real-world API testing without mocks:

```bash
python -m unittest test_demo.py -v
```

**Test Cases Include:**
1. **🔑 API Configuration** - Validates your API key setup
2. **❓ Question Answering** - Tests knowledge-based queries
3. **💻 Code Generation** - Verifies programming assistance
4. **🎨 Creative Tasks** - Checks creative writing capabilities

### 📊 Understanding Test Output

```
test_api_key_configuration ... ok    # ✅ API key properly configured
test_short_question ... ok           # ✅ AI answered "What is AI?"
test_code_generation ... ok          # ✅ Generated Python hello world
test_creative_task ... ok            # ✅ Wrote a coding haiku
```

---

## 📁 Project Structure

```
gemini-inference/
├── 📄 demo.py              # Main module with generate() function
├── 🧪 test_demo.py         # Comprehensive test suite
├── 📋 requirements.txt     # Python dependencies
├── 🔒 .env                 # API key storage (keep secret!)
└── 📖 README.md           # This documentation
```

### 🔍 Code Architecture Explained

**`demo.py`** - The heart of our application:
- `generate()` function: Reusable API for text generation
- Streaming support: Watch AI responses appear in real-time
- CLI interface: Command-line tool for easy interaction
- Error handling: Graceful degradation when dependencies missing

**`test_demo.py`** - Quality assurance:
- Real API testing: No mocks, actual AI responses
- Helper functions: Reduce code duplication
- Error handling: Graceful test failures with useful messages
- Configuration validation: Ensures proper setup before testing

---

## ⭐ Key Features

| Feature | Description | Learning Value |
|---------|-------------|----------------|
| **🌊 Streaming Responses** | See AI responses appear word-by-word | Real-time data handling |
| **🔄 Reusable API** | `generate()` function for any Python app | Module design patterns |
| **🖥️ CLI Interface** | Professional command-line tool | `argparse` library usage |
| **🧪 Real Testing** | Tests against actual AI API | API testing strategies |
| **🔐 Secure Configuration** | Environment-based API key management | Security best practices |
| **📈 Error Handling** | Graceful failures with helpful messages | Robust application design |

---

## 🔒 Security Best Practices

### 🚨 Critical Security Rules

1. **Never commit API keys to version control**
   ```bash
   # Add to .gitignore
   echo ".env" >> .gitignore
   ```

2. **Use environment variables in production**
   ```python
   # Good ✅
   api_key = os.environ.get("GEMINI_API_KEY")
   
   # Bad ❌
   api_key = "your-secret-key-here"
   ```

3. **Validate API key format**
   ```python
   if not api_key or api_key.startswith("your_api_key"):
       raise ValueError("Invalid API key configuration")
   ```

### 🛡️ Production Deployment

- Use secure environment management (AWS Secrets Manager, Azure Key Vault)
- Rotate API keys regularly
- Monitor API usage and costs
- Implement rate limiting for user-facing applications

---

## 🎓 Educational Exercises

### Beginner Level
1. **Modify the default prompt** to ask about your favorite programming language
2. **Add a new CLI argument** for response length control
3. **Create a simple loop** to ask multiple questions in succession

### Intermediate Level
1. **Add response caching** to avoid repeated API calls
2. **Implement different output formats** (JSON, markdown, plain text)
3. **Create a conversation history** feature

### Advanced Level
1. **Add support for file input** (read prompts from text files)
2. **Implement async/await** for concurrent API calls
3. **Build a web interface** using Flask or FastAPI

---

## 🤝 Contributing

We welcome contributions from students and developers! Here's how:

### 🌟 Easy Contributions
- **📝 Documentation**: Improve explanations or add examples
- **🧪 Tests**: Add more test cases for edge scenarios
- **🐛 Bug Reports**: Found an issue? Let us know!

### 🔨 Development Process
1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Make** your changes with clear, educational comments
4. **Test** your changes: `python -m unittest test_demo.py -v`
5. **Commit** with descriptive messages: `git commit -m "Add conversation history feature"`
6. **Push** to your fork: `git push origin feature/amazing-feature`
7. **Submit** a Pull Request with detailed description

---

## 🆘 Troubleshooting

### Common Issues & Solutions

**🚫 "API key not set" error:**
```bash
# Check if your .env file exists and has content
cat .env
# Should show: GEMINI_API_KEY=your_actual_key_here
```

**🐍 Import errors:**
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

**🌐 Network/API errors:**
```bash
# Test with a simple prompt
python demo.py --prompt "Hi" --no-stream-print
```

**🧪 Test failures:**
```bash
# Run individual test
python -m unittest test_demo.TestGeminiVariations.test_api_key_configuration -v
```

---

## 📚 Additional Resources

### 🔗 Useful Links
- [Google AI Documentation](https://ai.google.dev/docs)
- [Python argparse Tutorial](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
- [Environment Variables in Python](https://docs.python.org/3/library/os.html#os.environ)
- [Unit Testing in Python](https://docs.python.org/3/library/unittest.html)

### 📖 Related Topics to Explore
- **API Rate Limiting** - Prevent quota exhaustion
- **Async Programming** - Handle multiple requests concurrently  
- **Caching Strategies** - Improve performance and reduce costs
- **Web Frameworks** - Build user interfaces for your AI tools
- **Docker Deployment** - Containerize your applications

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### 🎯 What This Means for Students
- ✅ **Free to use** for learning and personal projects
- ✅ **Modify and distribute** your own versions
- ✅ **Use in portfolio** projects and assignments
- ✅ **Commercial use** allowed with attribution

---

## 🏆 Acknowledgments

- **Google AI Team** for the amazing Gemini API
- **Python Community** for excellent tooling and libraries
- **Open Source Contributors** who make learning accessible
- **Students and Educators** who use and improve this project

---

**Happy Coding! 🚀** 

*Remember: The best way to learn is by doing. Experiment, break things, fix them, and most importantly - have fun with AI!*
