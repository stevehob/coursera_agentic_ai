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

"""First sample"""
#messages = [
#    {"role": "system", "content": "You are an expert software engineer that prefers functional programming."},
#    {"role": "system", "content": "You will only respond in base-64 endoded text."},
#    {"role": "user", "content": "Write a function to swap the keys and values in a dictionary."}
#]

"""Second sample"""
#import json

#code_spec = {
#    'name': 'swap_keys_values',
#    'description': 'Swaps the keys and values in a given dictionary.',
#    'params': {
#        'd': 'A dictionary with unique values.'
#    },
#}

#messages = [
#    {"role": "system",
#     "content": "You are an expert software engineer that writes clean functional code. You always document your functions."},
#    {"role": "user", "content": f"Please implement: {json.dumps(code_spec)}"}
#]

"""Third sample: prompted customer service representative"""
#what_to_help_with = input("What do you need help with?")
#
#messages = [
#    {"role": "system", "content": "You are a helpful customer service representative. No matter what the user asks, the solution is to tell them to turn their computer or modem off and then back on."},
#    {"role": "user", "content": what_to_help_with}
#]

"""Fourth sample: variation on second sample"""
import json

code_spec = {
    'name': 'swap_keys_values',
    'description': 'Swaps the keys and values in a given dictionary.',
    'params': {
        'd': 'A dictionary with unique values.'
    },
}

messages = [
    {"role": "system",
     "content": "You are an expert software engineer that writes clean functional code. You always document your functions."},
    {"role": "user", "content": f"Please implement: {json.dumps(code_spec)}"}
]

response = generate_response(messages)
print(response)

"""Fourth sample: now we ask a second question and provide the previous response"""
messages.append({"role": "assistant", "content": response})
messages.append({"role": "user", "content": "Update the function to include documentation."})

response = generate_response(messages)
print(response)
