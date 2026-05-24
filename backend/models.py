from sqlalchemy import Column,Integer,String,Text,Float,DateTime
from datetime import datetime
from backend.database import Base

class ChatLog(Base):

    __tablename__="chat_logs"

    id=Column(Integer,primary_key=True)

    session_id=Column(String)

    prompt=Column(Text)

    response=Column(Text)

    provider=Column(String)

    model=Column(String)

    latency=Column(Float)

    token_usage=Column(Integer)

    status=Column(String)

    error=Column(Text)

    created_at=Column(
        DateTime,
        default=datetime.utcnow
    )