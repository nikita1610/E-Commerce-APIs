from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from models.users import *
from models.products import *
from models.business import *


app =FastAPI()
register_tortoise(
    app,
    db_url='sqlite://database.sqlite3',
    modules={'models': ['models']},
    generate_schemas = True,
    add_exception_handlers = True
)