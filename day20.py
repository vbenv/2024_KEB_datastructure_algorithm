import random

answer = random.randint(1, 100)
chance = 7
i = 7
while chance != 0:
	chance -= 1
	print(f'chance left {chance+1}')
	guess= int(input("Input guess number : "))
	if guess == answer:
		print(f'You win. Answer is {answer}, {7-chance}번 만에 맞췄습니다.')
		break
	elif guess > answer:
		print("Down")
	else:
		print("Up")
else:
	print("Game Over")
