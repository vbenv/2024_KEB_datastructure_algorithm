#단순 연결 리스트 01
# 사용자가 이름과 이메일을 입력하면 이메일 순서대로 단순 연결 리스트를 생성하는
# 프로그램을 작성. 이름에서 enter누르면 입력 종료
class Node():
    def __init__(self):
        self.data = None
        self.link = None
def print_nodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link == None:
        current = current.link
        print(current.data, end=' ')
    print()

# 입력받는 노드 처리 함수
def insert_node_list(name_email):
    global head, current, pre

    node = Node()
    node.data = name_email
    if head == None:
        head = node
        return

    if head.data[1] > name_email[1]:
        node.link = head
        head = node
        return

    current = head
    while current.link is not None:
        pre = current
        current = current.link
        if current.data[1] > name_email[1]:
            pre.link = node
            node.link = current
            return

    current.link = node

# 전역 변수 선언
head, current, pre = None, None, None


# 메인 코드 부분
if __name__=="__main__":

    while True:
        name = input("name --> ")
        if name == '':
            print("Terminate program")
            break
        email = input("email --> ")
        insert_node_list([name, email])
        print_nodes(head)




