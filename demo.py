# To run this code you need to install the following dependencies:
# pip install google-genai python-dotenv

import os
from google import genai
from google.genai import types

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("python-dotenv not installed. Using system environment variables only.")


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
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt)],
        )
    ]

    config = types.GenerateContentConfig()

    full_text = []
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=config,
    ):
        text = getattr(chunk, "text", None) or ""
        if print_stream and text:
            print(text, end="")
        if text:
            full_text.append(text)

    return "".join(full_text)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Gemini text generation demo")
    parser.add_argument(
        "--prompt",
        "-p",
        type=str,
        required=True,
        help="Prompt to send to the Gemini model",
    )
    parser.add_argument(
        "--model",
        "-m",
        type=str,
        default="gemini-2.0-flash",
        help="Model name to use",
    )
    parser.add_argument(
        "--no-stream-print",
        action="store_true",
        help="Do not print streamed chunks while generating",
    )

    args = parser.parse_args()

    # Run generation with provided args
    _ = generate(prompt=args.prompt, model=args.model, print_stream=not args.no_stream_print)
