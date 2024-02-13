#큐 1번 문제
## 함수 선언 부분 ##
def is_queue_full():
    global SIZE, queue, front, rear
    if (rear + 1) % SIZE == front: #for문 제거
        return True
    else:
        return False

def is_queue_empty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False

def en_queue(data):
    global SIZE, queue, front, rear
    if is_queue_full():
        print("대기 줄이 꽉 찼습니다..")
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data

def de_queue():
    global SIZE, queue, front, rear
    if is_queue_empty():
        print("바로 입장하시면 됩니다..")
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if (is_queue_empty()):
        print("큐가 비었습니다.")
        return None
    return queue[(front + 1) % SIZE]

## 전역 변수 선언 부분 ##
SIZE = 5
queue = ['정국', '뷔', '지민', '진', '슈가']
front = rear = SIZE

## 메인 코드 부분 ##
if __name__ == "__main__":

    while True:
        print("대기 줄 상태 :", queue)
        entrance = de_queue()
        print(entrance, "이(가) 입장합니다.")

        if front == rear:
            print("식당 영업 종료!")
            break
