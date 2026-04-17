import os
import litellm
import json
from litellm import completion
from typing import List, Dict

API_KEY = os.environ['OPEN_AI_KEY']

def generate_response(messages: List[Dict]) -> str:
    """
    Generates a response from a language model given a list of message dictionaries.

    Args:
        messages (List[Dict]): A list of message dictionaries representing the conversation history.

    Returns:
        str: The generated response content from the language model.
    """
    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        api_key=API_KEY,
        max_tokens=1024
    )
    return response.choices[0].message.content

"""First Prompt:
    Ask the user what function they want to create
    Ask the LLM to write a basic Python function based on the user's description
    Store the response for use in subsequent prompts
    Parse the response to separate the code from the commentary by the LLM"""
what_function_to_create = input("What function do you want to create? ")
#what_function_to_create = "a function that takes a list of integers and returns the sum of all even numbers in the list."

messages = [
    {"role": "system",
     "content": "You are an expert software engineer that writes clean functional python code."},
    {"role": "user", "content": f"Please implement a python function without documentation and no example usage to: ",
      "content": what_function_to_create}
]

response = generate_response(messages)
#print(code_response)
parsed_code_response = response.split("```python")[1].split("```")[0].strip()
print(parsed_code_response)

"""Second Prompt:
    Pass the code generated from the first prompt
    Ask the LLM to add comprehensive documentation including:
    Function description
    Parameter descriptions
    Return value description
    Example usage
    Edge cases"""

messages = [
    {"role": "system",
     "content": "You are an expert software engineer that clearly documents python code."},
    {"role": "user", "content": f"Add documentation to the python code including description of: functions,parameters,return values, example usage, and edge cases"},
    {"role": "assistant", "content": parsed_code_response}
]
response = generate_response(messages)
documented_code_response = response.split("```python")[1].split("```")[0].strip()
print(documented_code_response)

#save to a file
with open("documented_function.py", "w") as f:
    f.write(documented_code_response)
"""Third Prompt:

Pass the documented code generated from the second prompt
Ask the LLM to add test cases using Python's unittest framework
Tests should cover:
Basic functionality
Edge cases
Error cases
Various input scenarios"""