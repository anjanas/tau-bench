# Using Nebius Model with run.py

## Setup

1. **Set your Nebius API key in `.env` file:**
   ```
   NEBIUS_API_KEY=<>
   ```

2. **Load the environment variable** (if using python-dotenv):
   ```bash
   pip install python-dotenv
   ```
   Or export it manually:
   ```bash
   export NEBIUS_API_KEY="your-key-here"
   ```

## Usage

### Basic Example

Run with Nebius as the model provider:

```bash
python run.py \
  --agent-strategy tool-calling \
  --env retail \
  --model "your-nebius-model-id" \
  --model-provider nebius \
  --user-model gpt-4o \
  --user-model-provider openai \
  --user-strategy llm \
  --max-concurrency 10
```

### Using Nebius for Both Agent and User

```bash
python run.py \
  --agent-strategy tool-calling \
  --env retail \
  --model "your-nebius-model-id" \
  --model-provider nebius \
  --user-model "your-nebius-model-id" \
  --user-model-provider nebius \
  --user-strategy llm \
  --max-concurrency 10
```

### Available Agent Strategies

- `tool-calling` - Native tool calling (recommended)
- `act` - ACT strategy
- `react` - ReAct strategy  
- `few-shot` - Few-shot learning

### Available User Strategies

- `llm` - Basic LLM user simulation
- `react` - ReAct user simulation
- `verify` - Verify user simulation
- `reflection` - Reflection user simulation

## Model ID

**Important:** Replace `"your-nebius-model-id"` with a valid model identifier from Nebius AI Studio.

### Finding Available Models

1. **Check Nebius AI Studio Dashboard:**
   - Visit https://studio.nebius.com/
   - Log in and check the available models in your account

2. **Check Nebius Documentation:**
   - Visit https://docs.studio.nebius.com/
   - Look for the models section

3. **Use the helper script:**
   ```bash
   python list_nebius_models.py
   ```

4. **Common model ID formats:**
   - `deepseek-ai/DeepSeek-R1-0528`
   - `meta-llama/Meta-Llama-3-70B-Instruct`
   - Or check your Nebius dashboard for exact model IDs

### Testing a Model ID

Before running the full script, you can test if a model ID works:

```bash
python test_nebius_model.py "your-model-id"
```

This will quickly verify if the model exists and is accessible.

### Error: Model Not Found

If you get an error like:
```
NotFoundError: The model `gpt-oss-120b` does not exist.
```

This means the model ID you're using doesn't exist in Nebius. 

**Common issues:**
1. **Don't use prefixes**: Nebius doesn't use `openai/` or other prefixes. Use just the model name.
2. **Check exact spelling**: Model IDs are case-sensitive and must match exactly.
3. **Verify availability**: Not all models are available in all accounts/regions.

**To fix:**
1. Check your Nebius dashboard at https://studio.nebius.com/ for exact model IDs
2. Use the test script: `python test_nebius_model.py "model-id"`
3. Try without any prefix (e.g., use `gpt-oss-120b` instead of `openai/gpt-oss-120b`)

## How It Works

The code has been modified to:
1. Accept `nebius` as a valid provider in `run.py`
2. Configure litellm to use Nebius's OpenAI-compatible API endpoint (`https://api.studio.nebius.com/v1`)
3. Automatically use the `NEBIUS_API_KEY` environment variable for authentication

When you specify `--model-provider nebius`, the agents will:
- Use litellm's `openai` provider internally
- Point to Nebius's API base URL
- Authenticate using your `NEBIUS_API_KEY`

## Notes

- The Nebius API is OpenAI-compatible, so it works seamlessly with litellm
- Make sure your `.env` file is in the project root directory
- The API key is automatically loaded from the `NEBIUS_API_KEY` environment variable

