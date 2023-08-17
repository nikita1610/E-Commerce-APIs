from tortoise import Model
from pydantic import BaseModel
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from datetime import datetime


class Product(Model):
    id = fields.IntField(pk = True, index = True)
    name = fields.CharField(max_length = 100, null = False, index = True)
    category = fields.CharField(max_length = 20, index = True)
    original_price = fields.DecimalField(max_digits = 12, decimal_places = 2)
    new_price = fields.DecimalField(max_digits = 12, decimal_places = 2)
    percentage_discount = fields.IntField()
    offer_expiration_date = fields.DateField(default = datetime.utcnow)
    product_image = fields.CharField(max_length =200, null = False, default = "productDefault.jpg")
    date_published = fields.DatetimeField(default = datetime.utcnow)
    business = fields.ForeignKeyField('models.Business', related_name='products')


product_pydantic  = pydantic_model_creator(Product, name = "Product")
product_pydanticIn = pydantic_model_creator(Product, name = "ProductIn", 
                                            exclude = ("percentage_discount", "id"))