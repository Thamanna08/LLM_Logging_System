import requests

def local_chat(prompt):

    response = requests.post(
        "http://host.docker.internal:11434/api/chat",
        json={
            "model":"llama3",
            "stream": False,
            "messages":[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        }
    )

    data = response.json()

    return data["message"]["content"]