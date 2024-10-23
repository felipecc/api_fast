from abc import ABC, abstractmethod
from typing import List
from app.models.atendimento import Atendimento


class ServiceAtendimentoInterface(ABC):
    @abstractmethod
    def get_atendimentos(self) -> List[Atendimento] | None:
        pass
