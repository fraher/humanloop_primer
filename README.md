# Humanloop Primer: Evaluating with Azure AI Models

This repository is an exploration into understanding and using the Humanloop library for evaluating AI models, specifically focusing on running evaluations and comparing prompts using models hosted on Microsoft Azure's AI Foundry instances. The repository includes two main files: `eval.py` and `legalbench_abercrombie.ipynb`.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setting Up the Environment](#setting-up-the-environment)
- [Running the Sample Code](#running-the-sample-code)
- [Comparing Prompts using gpt-4o-mini and Llama-3.3-70B](#comparing-prompts-using-gpt-4o-mini-and-llama-33-70b)
- [Additional Information](#additional-information)

## Introduction

This repository demonstrates the use of Humanloop for managing AI model evaluations, extracting specific information, and comparing model performance on different tasks. The evaluations are designed to provide insights into how well the models understand and generate content based on specific templates and datasets. Please note, this repo only uses the Free Tier, so no custom evaluations could be used, though an example has been added to the "evaluators" folder slightly modifying the demo version.

## Prerequisites

Before you begin, make sure you have the following:

- Python 3.11 or later
- An Azure account with access to Azure AI Foundry
- API keys for Humanloop and Azure AI, stored in a `.env` file
- Basic knowledge of Python and Jupyter notebooks

## Setting Up the Environment

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the root directory of your project with the following variables:
   ```plaintext
   HL_API_KEY=<your-humanloop-api-key>
   AZURE_API_KEY=<your-azure-api-key>
   LLAMA_ENDPOINT=<llama-endpoint>
   AZURE_API_KEY_GPT=<your-azure-gpt-key>
   AZURE_ENDPOINT_GPT=<gpt-endpoint>
   GPT_4O_MINI_MODEL=<gpt-4o-mini-model>
   AZURE_API_KEY_LLAMA=<your-azure-llama-key>
   AZURE_ENDPOINT_LLAMA=<llama-endpoint>
   LLAMA_3_3_70B_MODEL=<llama-3.3-70b-model>
   ```

## Running the Sample Code

### `eval.py`

This script demonstrates how to run a basic human loop prompt evaluation for extracting first names from full names.

1. **Load Environment Variables**: Ensure that your environment variables are correctly loaded.

2. **Initialize Humanloop and Azure Clients**: The script initializes these clients using the provided API keys.

3. **Execute the Evaluation**: Run the script to evaluate the model's ability to extract first names. The evaluation utilizes a set of predefined evaluators like Exact Match and Levenshtein Distance.

   ```bash
   python eval.py
   ```

### Modifying `eval.py`

- **Prompt Development**: Modify and develop new prompt templates as needed to test different model capabilities.
- **Dataset Expansion**: Add more data points to the dataset to test the prompt with varied inputs and improve evaluation breadth.

## Comparing Prompts using gpt-4o-mini and Llama-3.3-70B

### `legalbench_abercrombie.ipynb`

The notebook provides a framework for comparing two different language models on a distinct task using the Abercrombie distinctiveness scale.

1. **Choose a Model**: Configure the script to use either gpt-4o-mini or Llama-3.3-70B by modifying the `selected_model` variable.

2. **Prepare the Template**: The script uses a specialized template asking the model to classify text according to a legal distinctiveness scale.

3. **Run the Evaluation**: Execute the notebook to run evaluations on the dataset from Humanloop.

   ```bash
   jupyter notebook legalbench_abercrombie.ipynb
   ```

4. **Analyze Results**: The notebook runs evaluations and presents the results for insights on the performance of each model.

5. **Results Output**: The output results comparing the two models on the same prompt has be exported and stored in the "results" folder for this experiment.

## Additional Information

- **Humanloop Documentation**: Refer to [Humanloop's official documentation](https://humanloop.com/docs) for in-depth understanding and API usage.
- **Azure AI Documentation**: Access [Azure AI documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/) for more details on AI Foundry Models.


By following these instructions, you will be able to run and comprehend the evaluation of AI models using Humanloop and Azure AI, allowing for further explorations and developments in this field.