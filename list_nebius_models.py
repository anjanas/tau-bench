#!/usr/bin/env python3
"""
Helper script to list available models in Nebius AI Studio.
This script attempts to query the Nebius API to discover available models.
"""

import os
import sys
from openai import OpenAI

def list_nebius_models():
    """List available models from Nebius AI Studio."""
    api_key = os.getenv("NEBIUS_API_KEY")
    if not api_key:
        print("Error: NEBIUS_API_KEY environment variable is not set")
        print("Please set it with: export NEBIUS_API_KEY='your-key-here'")
        sys.exit(1)
    
    base_url = "https://api.studio.nebius.com/v1"
    
    try:
        client = OpenAI(api_key=api_key, base_url=base_url)
        
        # Try to list models (if the API supports it)
        try:
            models = client.models.list()
            print("Available models in Nebius AI Studio:")
            print("=" * 60)
            for model in models.data:
                print(f"  - {model.id}")
            return
        except Exception as e:
            print(f"Note: Direct model listing not available: {e}")
            print()
        
        # Alternative: Try some common model formats
        print("Since direct model listing isn't available, here are some tips:")
        print("=" * 60)
        print("1. Check the Nebius AI Studio dashboard:")
        print("   https://studio.nebius.com/")
        print()
        print("2. Check the Nebius documentation:")
        print("   https://docs.studio.nebius.com/")
        print()
        print("3. Common model ID formats might be:")
        print("   - deepseek-ai/DeepSeek-R1-0528")
        print("   - meta-llama/Meta-Llama-3-70B-Instruct")
        print("   - Or check your Nebius dashboard for exact model IDs")
        print()
        print("4. You can test a model ID by trying to use it:")
        print("   python run.py --model 'model-id' --model-provider nebius ...")
        
    except Exception as e:
        print(f"Error connecting to Nebius API: {e}")
        print()
        print("Make sure:")
        print("1. Your NEBIUS_API_KEY is correct")
        print("2. You have internet connectivity")
        print("3. The Nebius API is accessible")


if __name__ == "__main__":
    list_nebius_models()

