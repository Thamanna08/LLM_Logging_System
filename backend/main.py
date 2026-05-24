from fastapi import FastAPI
from backend.database import engine,Base,SessionLocal
from backend.models import ChatLog
from backend.sdk import sdk_chat

app=FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/chat")
def chat(data:dict):

    db=SessionLocal()

    prompt=data["prompt"]

    provider=data.get(
        "provider",
        "ollama"
    )

    session_id=data.get(
        "session_id",
        "default"
    )

    history=db.query(
        ChatLog
    ).filter(
        ChatLog.session_id==session_id
    ).all()

    context=""

    for h in history[-3:]:

        context+=f"User:{h.prompt}\n"

        context+=f"Assistant:{h.response}\n"

    full_prompt=context+"\nUser:"+prompt

    result=sdk_chat(
        full_prompt,
        provider
    )

    log=ChatLog(

        session_id=session_id,

        prompt=prompt,

        response=result["response"],

        provider=provider,

        model="llama3",

        latency=result["latency"],

        token_usage=result["tokens"],

        status=result["status"],

        error=result["error"]
    )

    db.add(log)

    db.commit()

    return result

@app.get("/history")
def history():

    db=SessionLocal()

    return db.query(
        ChatLog
    ).all()

@app.get("/resume/{session_id}")
def resume(session_id:str):

    db=SessionLocal()

    return db.query(
        ChatLog
    ).filter(
        ChatLog.session_id==session_id
    ).all()

@app.delete("/cancel/{session_id}")
def cancel(session_id:str):

    db=SessionLocal()

    db.query(
        ChatLog
    ).filter(
        ChatLog.session_id==session_id
    ).delete()

    db.commit()

    return {
        "message":"Conversation deleted"
    }

@app.post("/ingest")
def ingest(log:dict):

    return {
        "received":log
    }