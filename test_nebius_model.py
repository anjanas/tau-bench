#!/usr/bin/env python3
"""
Test script to verify a Nebius model ID works.
Usage: python test_nebius_model.py "model-id"
"""

import os
import sys
from openai import OpenAI

def test_model(model_id: str):
    """Test if a model ID works with Nebius."""
    api_key = os.getenv("NEBIUS_API_KEY")
    if not api_key:
        print("Error: NEBIUS_API_KEY environment variable is not set")
        sys.exit(1)
    
    base_url = "https://api.studio.nebius.com/v1"
    
    try:
        client = OpenAI(api_key=api_key, base_url=base_url)
        
        print(f"Testing model: {model_id}")
        print("=" * 60)
        
        # Try a simple completion
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "user", "content": "Say 'Hello' if you can read this."}
            ],
            max_tokens=10
        )
        
        print(f"✅ Success! Model '{model_id}' is available.")
        print(f"Response: {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        error_msg = str(e)
        if "404" in error_msg or "does not exist" in error_msg:
            print(f"❌ Error: Model '{model_id}' does not exist in Nebius.")
            print()
            print("To find available models:")
            print("1. Check https://studio.nebius.com/")
            print("2. Check https://docs.studio.nebius.com/")
            print("3. Try different model IDs (without 'openai/' prefix)")
        else:
            print(f"❌ Error: {error_msg}")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_nebius_model.py 'model-id'")
        print()
        print("Example:")
        print("  python test_nebius_model.py 'deepseek-ai/DeepSeek-R1-0528'")
        print("  python test_nebius_model.py 'gpt-oss-120b'")
        sys.exit(1)
    
    model_id = sys.argv[1]
    test_model(model_id)

