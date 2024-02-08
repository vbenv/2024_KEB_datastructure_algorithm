# def factorial(number) -> int:
# 	'''
# 	factorail by repetition
# 	:param number: number(int)
# 	:return: factorial result (int)
# 	'''
# 	result = 1
# 	for i in range(1, number+1):
# 		result = result * i
# 	return result

# 재귀함수는 반복문이 사용되는 것이 아닌 자신의 함수를 계속 불러오는 형식으로 사용
# 성능은 무지하게 느림.
def factorial(number) -> int:
	'''
	factorial by recursion
	:param number: number(int)
	:return: factoral result (int)
	'''
	if number == 1:
		return 1
	else:
		return number * factorial(number - 1)

def nCr(n, r) -> int:
	'''
	조합 함수
	:param n: 전체 갯수
	:param r: 뽑는 갯수
	:return:
	'''
	numerator = factorial(n)
	denominator = factorial(n-r) * factorial(r)
	return int(numerator / denominator)