import ollama
import json
import os

# This programm requires ollama installed with a model such as Mistral or Llama
userwish = input("What should i do for you, master: ")
response = ollama.chat(
    model="mistral",
    messages=[
        {
            "role": "user",
            #for linux users with bash
            #"content": f'Return the following as json for a bash command on linux. dont change the command at all. leave it the same. only return the json and dont tell me anything else. the jason format should be like this. {{"command": the_command}}{inp}',
            # for windows users with powershell
            #f'Return the following as json for a powershell command on windows. dont change the command at all. leave it the same. only return the json and dont tell me anything else. the jason format should be like this. {{"command": the_command}}{inp}',
            # for mac users with zsh
            #f'Return the following as json for a zsh command on mac os. dont change the command at all. leave it the same. only return the json and dont tell me anything else. the jason format should be like this. {{"command": the_command}}{inp}'           
        },
    ],
)
print(response["message"]["content"])
command = json.loads(response["message"]["content"])["command"]
yn = input(f"{command}: execute y/n: ")
if yn.lower().strip() == "y":
    os.system(command)
