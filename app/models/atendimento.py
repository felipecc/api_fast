from pydantic import BaseModel


class Atendimento(BaseModel):
    cd_atendimento: int
