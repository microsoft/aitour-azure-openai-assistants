# Contoso Sales Analysis Assistant

## Programming Languages

 - Python

## Deploy Azure OpenAI Resources

Create OpenAI resources in Azure portal and get the key and endpoint to use in the code. You can follow the instructions [here](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource).

These demos were tested with Azure OpenAI GPT-4o model. For best results use the same model or newer.

1. Rename or copy the **./demos-2-3/.env.sample** file to **.env**
2. Add the Azure OpenAI key, endpoint, and deployment to the .env file

    ```text
    OPENAI_URI=
    OPENAI_KEY=
    OPENAI_VERSION=2024-05-01-preview
    OPENAI_GPT_DEPLOYMENT=
    ```

## Demo setup

The demos can be run in a Codespace or a local Python environment.

### Codespaces

Open the repo [Introduction to Azure Open AI Assistants](https://github.com/microsoft/aitour-azure-openai-assistants) in a Codespace and run the demos in the Jupyter Notebooks.

## Local installation

## Dev Containers

The demos can be run in a Dev Container in Visual Studio Code.

1. Install Visual Studio Code
1. Install the Remote - Containers extension
1. Install Docker
1. Open the repo in Visual Studio Code and click the "Reopen in Container" button

## Local setup

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



