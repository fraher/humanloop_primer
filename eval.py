from humanloop import Humanloop
from dotenv import load_dotenv
import os
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference.models import SystemMessage, UserMessage

load_dotenv()

hl_key = os.getenv('HL_API_KEY')
azure_key = os.getenv('AZURE_API_KEY')
endpoint= os.getenv('LLAMA_ENDPOINT')

print(hl_key)

hl = Humanloop(api_key=hl_key)
model = "Llama-3-3-70B-Instruct-fraher-ai"

template = [
    {"role": "user", "content": "Extract the first name for '{{full_name}}'."},    
]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(azure_key)    
)


def call_azure(**inputs) -> str:
    response = client.complete(
        messages=hl.prompts.populate_template(template=template, inputs=inputs)        
    )

    return response.choices[0].message.content
# Runs the eval and versions the Prompt and Dataset
hl.evaluations.run(
    name="Example Evaluation",
    file={
        "path": "First name extraction",
        "callable": call_azure,
        "type": "prompt",
        "version": {"model": model, "template": template},
    },
    dataset={
        "path": "First names",
        "datapoints": [
            {
                "inputs": {"full_name": "Albert Einstein"},
                "target": {"output": "Albert"},
            },
            {
                "inputs": {"full_name": "Albus Wulfric Percival Brian Dumbledore"},
                "target": {"output": "Albus"},
            },
        ],
    },
    evaluators=[
        {"path": "Example Evaluators/Code/Exact match"},
        {"path": "Example Evaluators/Code/Levenshtein distance"},
        {"path": "Example Evaluators/Code/Latency"},
    ],
)
