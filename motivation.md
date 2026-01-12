## Motivation
30+后端程序员在AI浪潮下被转岗，经历了焦虑，对坚持多年技术方向的怀疑，对未来方向的迷茫，感觉自己就像上世纪编译器出现时被取代的汇编程序员。
最终下定决心学AI，重新享受学习的乐趣，不做悲观被淘汰的程序员。
optimistic chat是第一个练手项目，也能在和它聊天时获得积极乐观的情绪。

## Plan
### Add converstion summary to the chat history
1. First step: use langchain middleware to add a summary of the conversation to the chat history with temeporal memory. Done.
2. Second step: use langchain middleware to add a summary of the conversation to the chat history with long-term memory.
3. Third step: customize my own summary middleware with the following functions:
* Summarize the chat history based on a main topic and key points, filter out irrelevant tangents or off-topic discussions, and preserve the original intent and meaning of both user and assistant.
* Create a sub topic for those not directly about the main topic, save it to database and add it to the chat history when the user asks for it.
### Add search tool for agent
1. First step: Add a search tool for agent to search the web with existing api like tavily.
2. Second step: Add rag in search tool to improve the accuracy of search results.
3. Third step: Change search tool to an agent that can search the web, open web pages, summarize web pages based on query (or generate snippet based on web page and query), manage tool call loops, and provide a summary of the search results.
### Add orchestrator for agent
1. First step: Add an orchestrator for agent to manage the conversation and tool calls.
2. Second step: Use local llm model, launch with vllm, for orchestrator.
3. Third step: Finetune the local llm model to get better performance as orchestrator. 
## Evaluation
TODO: add evaluation plan
