def factorial(number) -> int:
	'''
	factorail by repetition
	:param number: number(int)
	:return: factorial result (int)
	'''
	result = 1
	for i in range(1, number+1):
		result = result * i
	return result


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


if __name__ == "__main__": #메인 파일의 안쪽 코드를 사용하는 모듈
	n = int(input("Input n : "))
	r = int(input("Input r : "))
	print(f"{n}C{r} = {nCr(n, r)}")