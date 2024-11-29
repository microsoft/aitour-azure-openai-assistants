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

## Demos 2 and 3

1. An Azure subscription
1. Access to the Azure OpenAI GPT-4o model deployment
1. The demos require the Azure OpenAI key, endpoint, and deployment to be added to the **./demos-2-3/.env** file.
1. Demo 2 and 3 are run in a Python environment. You will need to install the required libraries and run the Jupyter Notebooks. You can run the demos in a Codespace or locally in a dev container or a Python virtual environment.

### Demo 2

The objective is to learn about Azure OpenAI Function Calling using the Azure OpenAI API. There are copious notes in the Jupyter Notebook to help you understand the code.

1. Set up the .env file with the Azure OpenAI key, endpoint, and deployment.
1. Run the **[Introduction to Azure OpenAI Function Calling](demo-2-function-calling.ipynb)** Jupyter Notebook. Note, you'll be prompted to select a kernel source. Select the Python Environments, then select the **Recommended** Python environment.

### Demo 3

The objective is to learn about Azure OpenAI Assistants using the Azure OpenAI API. There are copious notes in the Jupyter Notebook to help you understand the code.

1. Run the Jupyter Notebook **demo-3-contoso-sales-analysis.ipynb**.
1. Set up the .env file with the Azure OpenAI key, endpoint, and deployment.
1. Run the **[Contoso Sales Analysis Assistant](demo-3-contoso-sales-analysis.ipynb)** Jupyter Notebook. Note, you'll be prompted to select a kernel source. Select the Python Environments, then select the **Recommended** Python environment.

### Demo 3 with Azure AI Agents Service

In this folder, you can also find a [version of the demo 3](demo-3-contoso-sales-analysis-agents-service.ipynb) that uses the new Azure AI Agents Service, which builds upon Azure OpenAI Assistants API and provides additional enterprise-grade capabilities and more flexibility.
The Azure AI Agent Service is currently in preview, so to use it you need to request access to the [preview program](https://nam.dcv.ms/nzy5CEG6Br).

In addition to the pre-requisites listed above, to run [demo-3-contoso-sales-analysis-agents-service.ipynb](demo-3-contoso-sales-analysis-agents-service.ipynb), you need the following:

1. An Azure AI Hub and an Azure AI Project in Azure AI Foundry;
1. An Azure OpenAI resource or an Azure AI resource connected to your project;
1. A gpt-4o model deployment within your project.

Learn how to create an Azure AI Foundry Project and connect it to an Azure OpenAI resource [here](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects?tabs=ai-studio).
Then go through this [quickstart](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-playground#deploy-a-chat-model) to create a gpt-4o model deployment.

Next, set up the .env file with the Azure AI Project connection string. You can find the connection string in the Azure AI Foundry portal, under the project details in the overview page.

Finally, login to your Azure AI Foundry account using the Azure CLI:

```bash
    az login --tenant <your-tenant-id>
```

and select the subscription that has been allowlisted for the service private preview.

## Running the Demos

You can run the demos in a Codespace or locally in a dev container or a Python virtual environment. It's recommended to run the demos in a Codespace, but choose the option that works best for you.

### Codespaces

Open the repo [Introduction to Azure Open AI Assistants](https://github.com/microsoft/aitour-azure-openai-assistants) in a Codespace and run the demos in the Jupyter Notebooks in your browser.

### Local installation

#### Install with Dev Containers

The demos can be run in a Dev Container in Visual Studio Code.

1. Install Visual Studio Code
1. Install the Remote - Containers extension
1. Install Docker
1. Open the repo in Visual Studio Code and click the "Reopen in Container" button

#### Install on the Local Machine

Create a Python Virtual Environment

##### Windows

1. Create a new Python virtual environment by running the following command in your terminal:

    ```bash
    python -m venv .venv
    ```

2. Activate the virtual environment:

    ```bash
    .venv\Scripts\activate
    ```

##### macOS and Linux

1. Create a new Python virtual environment by running the following command in your terminal:

    ```bash
    python3 -m venv .venv
    ```

2. Activate the virtual environment:

    ```bash
    source .venv/bin/activate
    ```

##### Update pip

```bash
pip install --upgrade pip
```

##### Pip install required libraries

```bash
pip install -r requirements.txt
```
