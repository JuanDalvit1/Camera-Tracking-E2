from sqlalchemy import Column, Integer, String, DateTime
from .config import Base
from datetime import datetime

class ExampleModel(Base):
    __tablename__ = "example"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class CapturedImage(Base):
    __tablename__ = "captured_images"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    file_path = Column(String, index=True)
