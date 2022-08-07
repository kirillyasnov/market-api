from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class ShopUnit(Base):
    
    __tablename__ = 'shop_unit'
    
    id = Column(UUID, primary_key=True)
    name = Column(String)
    parent_id = Column(UUID, nullable=True)
    prices = relationship('Price', back_populates='price')
    

class Price(Base):
    
    __tablename__ = 'price'
    
    unit_id = Column(UUID, ForeignKey('shop_unit.id', ondelete='CASCADE'), primary_key=True)
    price = Column(Integer, nullable=True)
    datetime = Column(DateTime, primary_key=True)
    shop_unit = relationship('ShopUnit', back_populates='shop_unit')
    
    
