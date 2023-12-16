from my_python_app import MathIsCool
from typing import Callable, List, Tuple

runnable_test : List[Tuple[str,Callable]]
runnable_test = []

def test(func: Callable) -> Callable :
	def safe_test_wrap(*args, **kargs) -> None | Exception:
		try:
			func(*args,**kargs)
			return None
		except Exception as error:
			return error
	runnable_test.append((func.__name__,safe_test_wrap))
	return safe_test_wrap			

@test
def test_sum():
	math = MathIsCool()
	r = math.sum(5,3)
	assert r == 8

@test
def test_sub():
	math = MathIsCool()
	r = math.sub(5,3)
	assert r == 2

@test
def test_mul():
	math = MathIsCool()
	r = math.mul(5,3)
	assert r == 15

@test
def test_div():
	math = MathIsCool()
	r = math.div(9,3)
	assert r == 3

@test
def test_mod():
	math = MathIsCool()
	r = math.mod(5,3)
	assert r == 2

@test
def test_sqr():
	math = MathIsCool()
	r = math.sqr(16)
	assert r == 4

@test
def test_pow():
	math = MathIsCool()
	r = math.pow(5,3)
	assert r == 125

@test
def test_fail():
	assert False

if __name__ == '__main__':
	successes = 0
	for instance in runnable_test:
		name = instance[0]
		print(f"| Running test {name}")
		result = name = instance[1]()
		if result is None:
			successes += 1
		else:
			print(f"|\tError={repr(result)}")
	print(f"| Test run {len(runnable_test)} | Test passed {successes} | Success percentage {100.0*(successes/len(runnable_test)):.2f}% |")
	