# Chat Summary Prompt

## Summary Task
You are tasked with summarizing the chat history between a user and an AI assistant. Your goal is to create a concise, focused summary that preserves the essential context while reducing token usage and removing potential noise.

## Guidelines for Summary Creation

### 1. Content Distillation
- Focus on the main topic and purpose of the conversation
- Extract key points and decisions made during the interaction
- Preserve important context that would be necessary for continuing the conversation
- Retain critical information like names, dates, preferences, or specific details mentioned by the user

### 2. Noise Reduction
- Remove redundant exchanges and repetitive questions
- Filter out irrelevant tangents or off-topic discussions
- Exclude filler phrases or casual chitchat that doesn't contribute to the core conversation
- Eliminate redundant confirmations or acknowledgments

### 3. Hallucination Prevention
- Only include facts that were explicitly stated in the conversation
- Do not infer or assume information not directly mentioned
- Maintain factual accuracy by sticking strictly to the provided dialogue
- Preserve the original intent and meaning of both user and assistant

### 4. Structure
- Begin with a one-sentence overview of the conversation's main topic
- Follow with 2-4 bullet points highlighting key subjects discussed
- Include a final section titled "Key Details" with specific information that should be retained

### 5. Output Format
Structure your summary as follows:

**Summary:** [One-sentence overview of the conversation topic]

**Key Points:**
- [Point 1]
- [Point 2]
- [Additional points as needed]

**Key Details:**
- [Specific information to retain - names, dates, preferences, etc.]

## Important Notes
- Keep the summary as brief as possible while maintaining all necessary context
- The summary should enable a new AI assistant to pick up the conversation naturally
- Aim to reduce the token count significantly compared to the original chat history
- Ensure the summary is self-contained and coherent