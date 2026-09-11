# Local AI Agent

A Python-based local AI agent that uses locally hosted Large Language Models (LLMs) to interact with users, maintain conversation context, and use tools to perform tasks.

This project is being built to understand how AI agents work internally, including model integration, memory, tool usage, and agent orchestration — while keeping inference local through LM Studio.

> 🚧 **Project Status: In Progress**
>
> This project is currently under development. Features and architecture will be added incrementally as the project progresses.

---

## Introduction

The goal of this project is to build a simple AI agent that can run locally without depending entirely on cloud-based AI APIs.

The agent communicates with a locally running LLM through **LM Studio's OpenAI-compatible API**. On top of the model, the project will gradually introduce agent capabilities such as conversation memory and tool usage.

The project is being developed from the fundamentals rather than using a high-level agent framework, with the goal of understanding how the individual components of an AI agent work together.

---

## Planned Architecture

```text
User
 │
 ▼
AI Agent
 │
 ├── Conversation / Memory
 │
 ├── Tool Selection
 │
 ▼
Model Interface
 │
 ▼
LM Studio API
 │
 ▼
Local LLM
```
