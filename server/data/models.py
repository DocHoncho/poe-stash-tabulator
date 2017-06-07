import datetime

from sqlalchemy import Column, DateTime, Integer, Float, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Account(Base):
	__tablename__ = 'Accounts'

	Id = Column(Integer, primary_key=True)
	Name = Column(String)
	SessionId = Column(String)
	AccountName = Column(String)
	UserEmail = Column(String)
	UserPassword = Column(String)

	CreatedTime = Column(DateTime, default=datetime.datetime.now)
	UpdatedTime = Column(DateTime, onupdate=datetime.datetime.now)
	Active = Column(Boolean, default=True)


class League(Base):
	__tablename__ = "Leagues"

	Id = Column(Integer, primary_key=True)
	Tag = Column(String)
	Name = Column(String)
	StartDate = Column(DateTime)
	EndDate = Column(DateTime)

	CreatedTime = Column(DateTime, default=datetime.datetime.now)
	UpdatedTime = Column(DateTime, onupdate=datetime.datetime.now)
	Active = Column(Boolean, default=True)


class CurrencyType(Base):
	__tablename__ = "CurrencyTypes"

	Id = Column(Integer, primary_key=True)
	Name = Column(String)
	PoeTradeId = Column(Integer)
	ShortHand = Column(String)
	Icon = Column(String)

	CreatedTime = Column(DateTime, default=datetime.datetime.now)
	UpdatedTime = Column(DateTime, onupdate=datetime.datetime.now)
	Active = Column(Boolean, default=True)


class CurrencyTypePrice(Base):
	__tablename__ = "CurrencyTypePrices"

	Id = Column(Integer, primary_key=True)
	Label = Column(String)

	# Source of price point data, e.g., manual, Poe.Ninja, etc.
	Source = Column(String)

	LeagueId = Column(Integer, ForeignKey(League.Id))
	CurrencyId = Column(Integer, ForeignKey(CurrencyType.Id))
	Value = Column(Float)
	SampleTime = Column(DateTime)

	CreatedTime = Column(DateTime, default=datetime.datetime.now)
	UpdatedTime = Column(DateTime, onupdate=datetime.datetime.now)

