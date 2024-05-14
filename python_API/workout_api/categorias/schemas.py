from pydantic import Annotated
from pydantic import Field
from workout_api.contrib.schema import BaseSchema

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome da categoria', examples='Scale', max_length=10)]
