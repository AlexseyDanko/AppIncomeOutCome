from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class OperationType(str, Enum):
    INCOME = 'income'
    OUTLAY = 'outlay'


class OperationBase(BaseModel):
    date: date
    type_operation: OperationType
    total_sum: Decimal
    description: Optional[str]
    need_for_action: Optional[str]


class Operation(OperationBase):
    id: int

    class Config:
        orm_mode = True


class OperationCreate(OperationBase):
    pass


class OperationUpdate(OperationBase):
    pass
