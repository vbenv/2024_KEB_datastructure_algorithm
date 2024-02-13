## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def print_nodes(start):
	current = start
	if current is None:
		return
	print(current.data, end =' ')
	while current.link is not None:
		current = current.link #노드를 다음 노드로 연결해주는 것
		print(current.data, end =' ')
	print()


def insert_Node(find_data, insert_data) :
	global head, current, pre

	if head.data is find_data:
		node = Node()
		node.data = insert_data
		node.link = head
		head = node
		return

	current = head
	while current.link is not None:  # 중간 노드 삽입
		pre = current
		current = current.link
		if current.data is find_data:
			node = Node()
			node.data = insert_data
			node.link = current
			pre.link = node
			return

	node = Node()  # 마지막 노드 삽입
	node.data = insert_data
	current.link = node

head, current, pre = None, None, None
dataArray = ["태간", "근태", "태우", "성찬"]


if __name__ == "__main__" :
	node = Node()		# 첫 번째 노드
	node.data = dataArray[0]
	head = node

	for data in dataArray[1:]:	# 두 번째 이후 노드
		pre = node
		node = Node()
		node.data = data
		pre.link = node

	print_nodes(head)

insert_Node("다현", "현우")
print_nodes(head)
def delete_Node(delete_data):
	global head, current, pre

	if head.data is delete_data:
		current = head
		head = head.link
		print(f'{delete_data}이(가) 솔로앨범 냄')
		del current
		return

delete_Node("태간")

print_nodes(head)
