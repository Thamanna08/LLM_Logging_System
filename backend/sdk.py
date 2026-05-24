import time
from backend.providers import local_chat

def sdk_chat(prompt,provider):

    start=time.time()

    try:

        response=local_chat(prompt)

        latency=time.time()-start

        return {

            "response":response,

            "latency":latency,

            "status":"success",

            "error":None,

            "tokens":len(prompt.split())+len(response.split())
        }

    except Exception as e:

        latency=time.time()-start

        return {

            "response":"",

            "latency":latency,

            "status":"failed",

            "error":str(e),

            "tokens":0
        }