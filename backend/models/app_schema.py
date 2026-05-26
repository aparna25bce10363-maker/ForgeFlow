from pydantic import BaseModel
from typing import List

class Field(BaseModel):
    name: str
    type: str
    required: bool

class Table(BaseModel):
    name: str
    fields: List[Field]

class APIEndpoint(BaseModel):
    path: str
    method: str
    request_fields: List[str]
    response_fields: List[str]

class Page(BaseModel):
    name: str
    components: List[str]

class AuthRule(BaseModel):
    role: str
    permissions: List[str]

class AppSchema(BaseModel):
    app_name: str
    database: List[Table]
    apis: List[APIEndpoint]
    pages: List[Page]
    auth_rules: List[AuthRule]