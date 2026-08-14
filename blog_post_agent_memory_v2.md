# Your AI Agent Has Amnesia. Every Single Time.

Every API call starts with complete amnesia.

Not degraded memory. Not fuzzy recall.

*Zero.* Like the previous conversation never happened.

Everyone building agents finds this out the hard way. I found it out in Lesson 1, five minutes after making my first Claude API call. Two clean requests, back to back:

```
Call 1: "Hi! My name is Gourav. Please remember this."
Call 2: "What is my name?"
→ "I don't know your name."
```

Mate. It had just been told.

This is the thing no agent tutorial leads with — because it's awkward. The entire "AI assistant" pitch is built on the idea of something that *knows* you, *learns* about you, builds context over time. The reality is a stateless function that forgets everything the moment you hang up.

Your context window is a conversation. Not a brain.

## The illusion everyone falls for

The demo always looks like this:

```python
agent.chat("Who built the Eiffel Tower?")  → "Gustave Eiffel"
agent.chat("When did he die?")              → "He died in 1923"
```

Looks like memory. Feels like memory.

It's a list.

The framework quietly appended both messages to a Python list and shipped the *whole thing* on the second call. The model didn't remember anything — it just read its own previous response, which you silently handed back to it. Frameworks make this invisible, which is why the statelessness hits so hard when you finally see it.

## What "memory" actually is

Here's the full implementation of a "memory-enabled" agent:

```python
messages = []  # This IS the memory

def chat(user_message):
    messages.append({"role": "user", "content": user_message})
    response = client.messages.create(messages=messages)
    messages.append({"role": "assistant", "content": response})
```

That's it.

That's the intelligent assistant. A growing list you manage yourself and shove back into the API on every single call. Lesson 5 in the notebook builds this from scratch in about 20 lines. I watched people's faces when they realise the "memory" is just... their own Python list.

No magic. No session state. No server holding anything for you.

*You* hold the state. The model is just a very smart function.

## Why this bites you in production

Claude has a 200,000 token context window.

Sounds enormous. It isn't.

Fifty turns of real conversation — questions, answers, a bit of back-and-forth — and you're burning through 60–80k tokens without trying. I ran the actual numbers in Lesson 5:

- **Full message buffer** (the naive "just keep everything" approach): ~64,000 tokens across 50 turns
- **Sliding window** (keep the last 10 messages only): ~23,000 tokens
- **Summarisation memory** (LLM compresses old messages into a summary): ~35,000 tokens

The naive approach costs nearly 3x more. And it *crashes* when you finally hit the ceiling.

Every production agent hits this wall. The only question is whether you planned for it.

## The three fixes that actually work

**Sliding window** is the sledgehammer.

Keep the last N messages. Drop everything older. Fast, cheap, brutally predictable. But the agent *genuinely* forgets. Your user's name from turn 2? Gone by turn 11 if your window is 8. Great for short task-based agents. Terrible for anything that's meant to feel like a relationship.

**Summarisation memory** is the move.

When history gets too long, you call the LLM to compress the old messages into a tight summary — a few hundred tokens instead of a few thousand. The summary rides in the system prompt on every future call. Key facts survive: name, goal, preferences, all of it. The full `_build_system_prompt()` implementation is in Lesson 5 — worth reading slowly.

**File-backed long-term memory** is for agents that outlive a single session.

Kill the Python process. Restart. The agent reads from JSON on disk and picks up exactly where it left off. Session count, stored facts, past summaries — all there. This is the difference between a clever demo and something that actually feels like a persistent assistant.

Nope, you don't need a vector database for this. That's Lesson 7. For a first agent, these three cover 80% of real use cases.

## What I'd tell my Java-brain past self

Stop reaching for frameworks before you understand the problem.

LangChain's `ConversationSummaryMemory` is not magic. It's the summarisation pattern above, wrapped in more classes. MemGPT is not magic. It's careful engineering of what goes in `messages[]`. Mem0 is not magic. It's a smarter version of the JSON file.

Build it by hand first.

Once you've hand-rolled a sliding window and watched messages fall off the back, once you've written your own `_summarize()` method and seen the LLM compress 800 tokens into 150, the framework documentation stops looking intimidating. It starts looking like patterns you already know with extra branding on top.

The engineering is the lesson. The abstraction comes after.

---

Next up: multi-agent systems. What happens when you stop trying to make one agent smarter and just give it a team. The memory problem gets nastier. The solutions get genuinely fun.

---

PS — Lesson 5 has all five memory implementations end-to-end. The token cost comparison at the bottom is worth running with your own message lengths.
