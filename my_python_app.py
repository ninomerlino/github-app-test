from enum import Enum
from dataclasses import dataclass
from typing import List
from math import sqrt

class Operation(Enum):
	SUM = 0
	SUB = 1
	MUL = 2
	DIV = 3
	MOD = 4
	SQR = 5
	POW = 6

@dataclass
class OperationLog:
	op: Operation
	args: List[float]
	output: float

class MathIsCool:
	log = []

	def sum(self, a: float, b: float) -> float:
		r = a + b
		self.log.append(OperationLog(Operation.SUM,[a,b],r))
		return r

	def sub(self, a: float, b: float) -> float:
		r = a - b
		self.log.append(OperationLog(Operation.SUB,[a,b],r))
		return r

	def mul(self, a: float, b: float) -> float:
		r = a * b
		self.log.append(OperationLog(Operation.MUL,[a,b],r))
		return r
	
	def div(self, a: float, b: float) -> float:
		r = a / b
		self.log.append(OperationLog(Operation.DIV,[a,b],r))
		return r
	
	def mod(self, a: float, b: float) -> float:
		r = a % b
		self.log.append(OperationLog(Operation.MOD,[a,b],r))
		return r

	def sqr(self, a: float) -> float:
		r = sqrt(a)
		self.log.append(OperationLog(Operation.SQR,[a],r))
		return r
	
	def pow(self, a: float, b: float) -> float:
		r = a**b
		self.log.append(OperationLog(Operation.POW,[a,b],r))
		return r