import abc

from openqudit.circuit import QuditCircuit  # TODO: Barrier
from openqudit.expressions import (
    BraSystemExpression,
    KetExpression,
    KrausOperatorsExpression,
    UnitaryExpression,
    UnitarySystemExpression,
)


class Operation(abc.ABC): ...


class ExpressionOperation(Operation): ...


class DirectiveOperation(Operation): ...


class CircuitOperation(Operation): ...


for cls in (
    UnitaryExpression,
    KrausOperatorsExpression,
    BraSystemExpression,
    UnitarySystemExpression,
    KetExpression,
):
    ExpressionOperation.register(cls)
CircuitOperation.register(QuditCircuit)
