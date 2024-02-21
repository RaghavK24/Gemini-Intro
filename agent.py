import requests
import json
import sys
import os

import gemini_functions

api_key = "AIzaSyCzFzmViU4INtFv6gG6WsLiAt39om0mqH0"

# def parse_function_response(message):
#     function_call = message[0]["functionCall"]
#     function_name = function_call["name"]

#     print("Gemini: Called function " + function_name )

#     try:
#         arguments = function_call["args"]

#         if hasattr(gemini_functions, function_name):
#             function_response = getattr(gemini_functions, function_name)(**arguments)
#         else:
#             function_response = "ERROR: Called unknown function"
#     except TypeError:
#         function_response = "ERROR: Invalid arguments"

#     return (function_name, function_response)


def run_conversation(message, messages = []):
    messages.append(message)

    with open("messages.json", "w") as f:
        f.write(json.dumps(messages, indent=4))

    data = {
        "contents": [messages],
        "tools": [{
            "functionDeclarations": gemini_functions.definitions
        }]
    }

    response = requests.post("https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+api_key, json=data)

    if response.status_code != 200:
        print(response.text)
        print("ERROR: Unable to make request")
        sys.exit(1)

    response = response.json()

    if "content" not in response["candidates"][0]:
        print("ERROR: No content in response")
        print(response)
        sys.exit(1)

    message = response["candidates"][0]["content"]["parts"]
    messages.append({
        "role": "model",
        "parts": message
    })

    if "functionCall" in message[0]:
        print("function called")
        # function_name, function_response = parse_function_response(message)
        function_call = message[0]["functionCall"]
        function_name = function_call["name"]
        # message = {
        #     "role": "function",
        #     "parts": [{
        #         "functionResponse": {
        #             "name": function_name,
        #             "response": {
        #                 "name": function_name,
        #                 "content": f"{function_name} was used"
        #             }
        #         }
        #     }]
        # }
        if function_name == "final_answer":
            final_message = {
                "role": "model",
                "parts": function_call["args"]["message"]
            }

            messages.append(final_message)

            with open("messages.json", "w") as f:
                f.write(json.dumps(messages, indent=4))

            user_message = input("Gemini: " + function_call["args"]["message"] + "\nYou: ")
            message = {
                "role": "user",
                "parts": [{"text": user_message}]
            }
        else:
            message={
                "role": "user",
                "parts": [{"text": "Okay so do more function_calls if you sense it, and if you have found all the functions that could be used for the main message i gave then just trigger final_answer"}]
            }



    else:
        user_message = input("Gemini: " + message[0]["text"] + "\nYou: ")
        message = {
            "role": "user",
            "parts": [{"text": user_message}]
        }

    run_conversation(message, messages)

messages = []

system_message = "You are an AI bot that can do everything using function calls. When you are asked to do something, use the function calls you have available and then respond with a message shortly confirming what you have done. Just note that there can be either a single function or multiple function that user intends to use. And always remember that final_answer function is only to be called when you think you have the final answer"
user_message = input("Gemini: What do you want to do?\nYou: ")
message = {
    "role": "user",
    "parts": [{"text": system_message + "\n\n" + user_message}]
}

run_conversation(message, messages)