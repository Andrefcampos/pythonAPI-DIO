from typing import Annotated
from pydantic import Field, PositiveFloat
from contrib.schema import BaseSchema

class Atletas(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', examples='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', examples='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', examples=30)]
    altura: Annotated[float, Field(description='Altura do atleta', example=1.80)]
    sexo: Annotated[str, Field(description='Sexo do atleta', examples='F', max_length=1)]
    peso: Annotated[float, Field(description='Peso do atleta', examples=85.50)]