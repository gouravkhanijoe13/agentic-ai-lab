# Lesson 1: LLM Fundamentals
**Date:** 2026-04-29  
**Time to complete:** ~45–60 minutes

---

## What You'll Learn
1. What an LLM actually is (conceptually)
2. How an LLM processes your input
3. How to call the Anthropic API with Python
4. What "tokens" are and why they matter
5. How to interpret and control the response

---

## Part 1: The Mental Model — What IS an LLM?

Think of an LLM (Large Language Model) as a **very sophisticated next-word predictor**, trained on a massive chunk of human-written text.

When you send it the text: _"The capital of France is..."_  
It predicts: _"Paris"_

But after training on hundreds of billions of words, this "prediction" gets incredibly powerful. The model learns grammar, facts, reasoning patterns, code syntax, and even social norms — all as statistical relationships between tokens (chunks of text).

**Key insight for you as a Java engineer:**  
An LLM is not a function with a fixed algorithm. It's a **statistical model** with ~70–500 billion parameters (think of parameters as learned weights, like millions of tiny dials tuned during training). When you call the API, you're running inference through those weights.

```
Your text → Tokenized → Run through neural network layers → Output token probabilities → Sample next token → repeat
```

The output isn't deterministic by default (unlike your Java methods). The same input can yield different outputs on different calls. You'll learn how to control this with `temperature`.

---

## Part 2: The Anatomy of an API Call

Every LLM API call has these core components:

| Component | What it is | Java analogy |
|-----------|-----------|--------------|
| **Model** | Which LLM to use (e.g., `claude-sonnet-4-6`) | Which version of a library/JAR |
| **System prompt** | Background instructions that shape behavior | Constructor / configuration |
| **User message** | Your actual input/question | Method argument |
| **Max tokens** | Maximum response length (in tokens) | Buffer size limit |
| **Temperature** | How "random" the output is (0=deterministic, 1=creative) | Random seed control |

---

## Part 3: What is a Token?

Tokens are the unit of currency in LLM land. They're not exactly words — they're chunks of text that the model processes.

- `"Hello"` → 1 token  
- `"Hello, world!"` → 4 tokens  
- `"unbelievable"` → 3 tokens (`un`, `believ`, `able`)  
- 1 token ≈ 0.75 words on average  
- **You pay per token (input + output)**

This matters because:
- API cost = input tokens × price + output tokens × price
- Every model has a **context window** (max tokens it can hold in "memory" at once)
- Claude's context window is 200,000 tokens (huge — ~150,000 words!)

---

## Part 4: Let's Write Code!

### Setup
```bash
pip install anthropic
export ANTHROPIC_API_KEY="your-key-here"
```

Get your key at: https://console.anthropic.com

### Exercise 1: Your First API Call
Run `01_first_call.py`

### Exercise 2: Exploring Tokens  
Run `02_tokens.py`

### Exercise 3: Temperature and Randomness
Run `03_temperature.py`

### Exercise 4: Streaming Responses
Run `04_streaming.py`

### Exercise 5: Multi-turn Conversation
Run `05_conversation.py`

---

## Homework / Experiments

After running all exercises, try these modifications:

1. **Change the model** — swap `claude-sonnet-4-6` for `claude-haiku-4-5-20251001` (cheaper, faster). Notice the difference in quality and speed.
2. **Crank temperature to 1.0** on exercise 3 and run the same question 5 times. See the variety!
3. **Hit the context limit** — in exercise 5, keep chatting until you've sent 10+ messages. Notice how the conversation history grows.
4. **Count your tokens** — look at the `usage` field in the response. Try to minimize your prompt while keeping the answer quality.

---

## Key Takeaways

- LLMs are **stateless** — they don't remember between API calls. You pass the full history every time.
- The **system prompt** is your most powerful tool for shaping behavior.
- **Tokens = money + memory**. Always think about token efficiency.
- Temperature controls creativity vs. consistency — most production apps use 0–0.3.
- Next lesson: We'll master prompt engineering to get dramatically better outputs.

---

## What's Next → Lesson 2: Prompt Engineering
You'll learn how to write prompts that consistently produce the outputs you need — including few-shot examples, chain-of-thought reasoning, and XML structuring.
