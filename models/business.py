from tortoise import Model
from pydantic import BaseModel
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from datetime import datetime


class Business(Model):
    id = fields.IntField(pk = True, index = True)
    business_name = fields.CharField(max_length = 20, nullable = False, unique = True)
    city = fields.CharField(max_length = 100, null = False, default = "Unspecified")
    region = fields.CharField(max_length = 100, null = False, default = "Unspecified")
    business_description = fields.TextField(null = True)
    logo = fields.CharField(max_length =200, null = False, default = "default.jpg")
    owner = fields.ForeignKeyField('models.User', related_name='business')    



business_pydantic = pydantic_model_creator(Business, name = "Business")
business_pydanticIn = pydantic_model_creator(Business, name = "Business", exclude_readonly = True)

