def factorial(number) -> int:
	pass


def nCr(n, r) -> int:
	'''
	조합 함수
	:param n: 전체 갯수
	:param r: 뽑는 갯수
	:return:
	'''
	numerator = factorial(n)
	denominator = factorial(n-r) * factorial(r)
	return numerator / denominator


if __name__ == "__main__": #메인 파일의 안쪽 코드를 사용하는 모듈
	n = int(input("Input n : "))
	r = int(input("Input r : "))
	print(f"{n}C{r} = {nCr(n, r)}")