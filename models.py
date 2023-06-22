from sqlalchemy import DateTime,Boolean, Column, ForeignKey, Integer, String
from datetime import datetime
from sqlalchemy.orm import relationship

import database


class Address(database.Base):
    __tablename__ = "address"
    address_id = Column(Integer, primary_key=True, index=True)
    house_number = Column(String(50), unique=True)
    area = Column(String(100))
    district = Column(String(30), default='not specified')
    state = Column(String(30), default='not specified')
    country = Column(String(30), default='not specified')
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    modified_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)