from pydantic import BaseModel
from typing import List, Dict


class Intent(BaseModel):
    app_type: str
    features: List[str]
    roles: List[str]


class Entity(BaseModel):
    name: str
    fields: List[str]


class SystemDesign(BaseModel):
    entities: List[Entity]
    pages: List[str]
    roles: List[str]


class Table(BaseModel):
    name: str
    fields: List[str]


class Endpoint(BaseModel):
    path: str
    method: str


class DatabaseSchema(BaseModel):
    tables: List[Table]


class APISchema(BaseModel):
    endpoints: List[Endpoint]


class UISchema(BaseModel):
    pages: List[Dict]


class AuthSchema(BaseModel):
    roles: Dict[str, List[str]]


class AppConfig(BaseModel):
    database: DatabaseSchema
    api: APISchema
    ui: UISchema
    auth: AuthSchema