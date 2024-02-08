import mymath
import time




if __name__ == "__main__": #메인 파일의 안쪽 코드를 사용하는 모듈
	n = int(input("Input n : "))
	r = int(input("Input r : "))
	#start = time.time()
	print(f"{n}C{r} = {mymath.nCr(n, r)}")
	#end = time.time()
	#print(f"소요시간 : {end - start}")
	# f = int(input())
	# print(mymath.factorial(f))

