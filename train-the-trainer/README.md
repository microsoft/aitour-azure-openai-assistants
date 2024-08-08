# Contoso Sales Analysis Assistant

## Chat Completions API vs Assistants API

The primitives of the Chat Completions API are Messages, on which you perform a Completion with a Model (gpt-3.5-turbo, gpt-4, etc). It is lightweight and powerful, but inherently stateless, which means you have to manage conversation state, tool definitions, retrieval documents, and code execution manually.

### The primitives of the Assistants API are

- Assistants, which encapsulate a base model, instructions, tools, and (context) documents,
- Threads, which represent the state of a conversation, and
- Runs, which power the execution of an Assistant on a Thread, including textual responses and multi-step tool use.

## Why use the OpenAI Assistants API

The OpenAI Assistants API allows you to build conversational agents that can understand and respond to user inputs. You can use the API to automate tasks, provide information, or guide users through a process.

The Assistants API is not the only way to build conversational agents, but it offers several advantages:

1. Simplicity: The API abstracts away the complexity of building a conversational agent, allowing you to focus on the content and logic of the conversation.
2. Scalability: The API is designed to handle a large number of concurrent users, making it suitable for production use.
3. Customization: The API allows you to customize the behavior of the assistant by providing training data and defining conversational flows.
4. Integration: The API can be integrated with other services and systems, allowing you to build assistants that interact with external data sources.

## Objective

This notebook demonstrates the following:

1. Generative AI
1. Function calling
1. Code Generation

Reference:
- Learn more about how to use Assistants with our [How-to guide on Assistants](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/assistant)
- [Assistants OpenAI Overview](https://platform.openai.com/docs/assistants/overview) 

## Programming Languages
 - Python

## Deploy Azure OpenAI Resources

Create OpenAI resources in Azure portal and get the key and endpoint to use in the code. You can follow the instructions [here](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource).

Ideally use the OpenAI GPT-4o model for best results.

1. Rename the .env.sample file to .env
2. Add the OpenAI key and endpoint in the .env file

    ```text
    OPENAI_URI=
    OPENAI_KEY=
    OPENAI_VERSION=2024-05-01-preview
    OPENAI_GPT_DEPLOYMENT=
    ```
    
  ## Installation

Create a Python Virtual Environment

### Windows

1. Create a new Python virtual environment by running the following command in your terminal:

    ```bash
    python -m venv .venv
    ```

2. Activate the virtual environment:

    ```bash
    .venv\Scripts\activate
    ```

### macOS and Linux

1. Create a new Python virtual environment by running the following command in your terminal:

    ```bash
    python3 -m venv .venv
    ```

2. Activate the virtual environment:

    ```bash
    source .venv/bin/activate
    ```

### Update pip

```bash
pip install --upgrade pip
```

### Pip install required libraries

pip install -r requirements.txt



