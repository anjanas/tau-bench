#!/usr/bin/env python3
"""
Example script showing how to use the Nebius model in your code.
"""

import os
from tau_bench.model_utils.model.general_model import model_factory
from tau_bench.model_utils.model.model import Platform

# Set your Nebius API key as an environment variable
# export NEBIUS_API_KEY="your-api-key-here"
# Or set it in code:
# os.environ["NEBIUS_API_KEY"] = "your-api-key-here"

# Method 1: Create a Nebius model directly
def example_direct_usage():
    """Create and use a Nebius model directly."""
    # Create the model
    model = model_factory(
        model_id="openai/gpt-oss-120b",  # Replace with actual Nebius model ID
        platform="nebius",  # or Platform.NEBIUS
        temperature=0.0
    )
    
    # Use the model to generate text
    response = model.generate(
        instruction="You are a helpful assistant.",
        text="What is the capital of France?"
    )
    print(f"Response: {response}")
    
    # Use the model to parse structured data
    from pydantic import BaseModel
    
    class Person(BaseModel):
        name: str
        age: int
    
    parsed = model.parse(
        text="John is 30 years old.",
        typ=Person
    )
    print(f"Parsed: {parsed}")


# Method 2: Use with the API wrapper
def example_api_wrapper():
    """Use Nebius model through the API wrapper."""
    from tau_bench.model_utils.api.api import API
    
    # Create the model
    model = model_factory(
        model_id="your-nebius-model-id",
        platform="nebius",
        temperature=0.0
    )
    
    # Wrap it in an API object
    api = API.from_general_model(model=model)
    
    # Use the API methods
    response = api.generate(
        instruction="You are a helpful assistant.",
        text="What is 2+2?"
    )
    print(f"API Response: {response}")


# Method 3: Use with command-line arguments
def example_with_args():
    """Example of using Nebius with argparse (like in api.py)."""
    import argparse
    from tau_bench.model_utils.api.api import default_api_from_args
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True, help="Nebius model ID")
    parser.add_argument("--platform", type=str, default="nebius")
    parser.add_argument("--base-url", type=str, default=None)
    args = parser.parse_args()
    
    # Create API from args
    api = default_api_from_args(args)
    
    # Use the API
    response = api.generate(
        instruction="You are a helpful assistant.",
        text="Hello!"
    )
    print(f"Response: {response}")


# Method 4: Direct instantiation (if you need more control)
def example_direct_instantiation():
    """Directly instantiate NebiusModel."""
    from tau_bench.model_utils.model.nebius import NebiusModel
    
    model = NebiusModel(
        model="your-nebius-model-id",
        api_key=os.getenv("NEBIUS_API_KEY"),  # or pass directly
        temperature=0.0
    )
    
    # Use the model
    response = model.generate(
        instruction="You are a helpful assistant.",
        text="What is Python?"
    )
    print(f"Response: {response}")


if __name__ == "__main__":
    # Make sure NEBIUS_API_KEY is set
    if not os.getenv("NEBIUS_API_KEY"):
        print("Error: NEBIUS_API_KEY environment variable is not set")
        print("Set it with: export NEBIUS_API_KEY='your-key-here'")
        exit(1)
    
    print("=== Example 1: Direct Usage ===")
    example_direct_usage()
    
    #print("\n=== Example 2: API Wrapper ===")
    # example_api_wrapper()
    
    #print("\n=== Example 3: With Args ===")
    # example_with_args()
    
    #print("\n=== Example 4: Direct Instantiation ===")
    # example_direct_instantiation()

