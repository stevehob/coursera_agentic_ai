# Important!!!
#
# <---- Set your 'OPENAI_API_KEY' as a secret over there with the "key" icon
#
#  !!pip install litellm
import os
import litellm
from litellm import completion
from typing import List, Dict

def generate_response(messages: List[Dict]) -> str:
    """Call LLM to get response"""
    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        api_key=API_KEY,
        max_tokens=1024
    )
    return response.choices[0].message.content

API_KEY = os.environ['OPEN_AI_KEY']

messages = [
    {"role": "system", "content": "You are an expert software engineer that prefers functional programming."},
    {"role": "user", "content": "Write a function to swap the keys and values in a dictionary."}
]

response = generate_response(messages)
print(response)