# coding=utf-8

from sqlalchemy import Column, String

from marshmallow import Schema, fields
from modules.entities import Base, Entity


class Alarms(Entity, Base):
    __tablename__ = 'alarms'

    title = Column(String)
    description = Column(String)

    def __init__(self, importance, description, created_by):
        Entity.__init__(self, created_by)
        self.importance = importance
        self.description = description


class AlarmSchema(Schema):
    id = fields.Number()
    importance = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
