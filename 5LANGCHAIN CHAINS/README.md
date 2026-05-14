# LangChain Chains

This folder contains my hands-on practice with different types of chains in LangChain.  
The main goal was to understand how multiple LLM operations can be connected together to build more powerful GenAI workflows.

---

# 📌 What are Chains in LangChain?

Chains allow us to combine prompts, models, and logic into a sequence of operations.  
Instead of making a single LLM call, chains help in building step-by-step workflows.

LangChain provides different types of chains depending on the use case.

---

# 📂 Files Overview

## 🔹 simple_chain.py

### Definition

A simple chain connects a prompt directly to an LLM and generates output.

### Implementation

- Created a basic prompt
- Passed input to the model
- Generated direct response

### Use Case

- Simple Q&A
- Text generation
- Beginner-level workflows

---

## 🔹 sequential_chain.py

### Definition

Sequential chains pass the output of one chain as input to another chain.

### Implementation

- Connected multiple chains together
- Used output from previous step in next step
- Built multi-step workflow

### Use Case

- Blog generation
- Multi-step reasoning
- Content pipelines

### Workflow Example

```text id="ijcsmt"
Input → Chain 1 → Output → Chain 2 → Final Output
```
