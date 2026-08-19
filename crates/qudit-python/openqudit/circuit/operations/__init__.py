import abc

from openqudit import _openqudit
from openqudit.circuit import QuditCircuit  # TODO: Barrier
from openqudit.expressions import (
    BraSystemExpression,
    KetExpression,
    KrausOperatorsExpression,
    UnitaryExpression,
    UnitarySystemExpression,
)

DirectiveOperation = _openqudit.circuit.DirectiveOperation


class Operation(abc.ABC): ...


class ExpressionOperation(Operation): ...


class CircuitOperation(Operation): ...


for cls in (
    UnitaryExpression,
    KrausOperatorsExpression,
    BraSystemExpression,
    UnitarySystemExpression,
    KetExpression,
):
    ExpressionOperation.register(cls)

Operation.register(_openqudit.circuit.DirectiveOperation)

CircuitOperation.register(QuditCircuit)
