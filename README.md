# Introduction to Azure AI Agent Service

[![Azure AI Community Discord](
https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-00001-leestott)

## Session Description

The Azure AI Agent Service allows you to build conversational agents that can understand and respond to user inputs. You can use the API to automate tasks, provide information, or guide users through a process.

The Azure AI Agent Service is not the only way to build conversational agents, but it offers several advantages:

1. **Simplicity**: The API abstracts away the complexity of building a conversational agent, allowing you to focus on the content and logic of the conversation.
2. **Scalability**: The API is designed to handle a large number of concurrent users, making it suitable for production use.
3. **Customization**: The API allows you to customize the behavior of the agent by providing training data and defining conversational flows.
4. **Integration**: The API can be integrated with other services and systems, allowing you to build agents that interact with external data sources.

## Learning Outcomes

1. Understand the Azure AI Agent Service
<!-- 1. Introductions to the Azure AI Agent Service Playground -->
1. Understand Azure OpenAI Chat Completion Function Calling
1. Learn how to build conversational agents

## Technology Used

1. Azure AI Agent Service
<!-- 2. Azure AI Agent Service Playground -->
1. Jupyter Notebooks
1. OpenAI SDK

## Additional Resources and Continued Learning

| Resources          | Links                             | Description        |
|:-------------------|:----------------------------------|:-------------------|
| Future Learning 1  | [Getting started with Azure AI Agent Service](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357) | Learn more about the Azure AI AI Agent Service|
| Future Learning 2  | [Azure AI Agent Service API Documentation](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme) | Learn more about Azure AI Agent Service APIs|

## Content Owners

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->

<table>
<tr>
    <td align="center"><a href="http://learnanalytics.microsoft.com">
        <img src="https://github.com/gloveboxes.png" width="100px;" alt="Dave Glover
"/><br />
        <sub><b>Dave Glover
</b></sub></a><br />
            <a href="https://github.com/gloveboxes" title="talk">📢</a>
    </td>
        <td align="center"><a href="http://learnanalytics.microsoft.com">
        <img src="https://github.com/softchris.png" width="100px;" alt="Chris Noring
"/><br />
        <sub><b>Chris Noring
</b></sub></a><br />
            <a href="https://github.com/softchris" title="talk">📢</a>
    </td>
</tr></table>


<!-- ALL-CONTRIBUTORS-LIST:END -->

## Responsible AI

Microsoft is committed to helping our customers use our AI products responsibly, sharing our learnings, and building trust-based partnerships through tools like Transparency Notes and Impact Assessments.

Many of these resources can be found at:

> [Responsible AI](https://aka.ms/RAI).


### Transparency Note

Microsoft’s approach to responsible AI is grounded in our AI principles of fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability.

Large-scale natural language, image, and speech models - like the ones used in this sample - can potentially behave in ways that are unfair, unreliable, or offensive, in turn causing harms.

Please consult the:

> [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)

to be informed about risks and limitations.

### Safety system

The recommended approach to mitigating these risks is to include a safety system in your architecture that can detect and prevent harmful behavior.

> [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview)

provides an independent layer of protection, able to detect harmful user-generated and AI-generated content in applications and services. Azure AI Content Safety includes text and image APIs that allow you to detect material that is harmful. 

### Content Safety Studio

We also have an interactive Content Safety Studio that allows you to view, explore and try out sample code for detecting harmful content across different modalities. 

The following:

> [Quickstart Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) 

guides you through making requests to the service.

### Evaluation

Another aspect to take into account is the overall application performance. With multi-modal and multi-models applications, we consider performance to mean that the system performs as you and your users expect, including not generating harmful outputs. It's important to assess the performance of your overall application using

> [Generation of quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

You can evaluate your AI application in your development environment using the 

> [Prompt flow SDK](https://microsoft.github.io/promptflow/index.html). 

Given either a test dataset or a target, your generative AI application generations are quantitatively measured with built-in evaluators or custom evaluators of your choice. 

To get started with the prompt flow sdk to evaluate your system, you can follow the:

> [Quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). 

Once you execute an evaluation run, you can: 

> [Visualize the results in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

