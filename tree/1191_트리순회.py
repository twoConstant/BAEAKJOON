import sys; sys.stdin = open('1191_트리순회.txt', encoding="UTF-8")
def preorder_traversal(node):
    print(node, end="")
    # 자식 탐색
    if tree[ord(node) - 65][0] and tree[ord(node) - 65][0] != ".":
        preorder_traversal(tree[ord(node) -65][0])
    if tree[ord(node) - 65][1] and tree[ord(node) - 65][1] != ".":
        preorder_traversal(tree[ord(node) - 65][1])

def inorder_traversal(node):
    # 자식 탐색
    if tree[ord(node) - 65][0] and tree[ord(node) - 65][0] != ".":
        inorder_traversal(tree[ord(node) -65][0])
    print(node, end="")
    if tree[ord(node) - 65][1] and tree[ord(node) - 65][1] != ".":
        inorder_traversal(tree[ord(node) - 65][1])

def postorder_traversal(node):

    # 자식 탐색
    if tree[ord(node) - 65][0] and tree[ord(node) - 65][0] != ".":
        postorder_traversal(tree[ord(node) -65][0])
    if tree[ord(node) - 65][1] and tree[ord(node) - 65][1] != ".":
        postorder_traversal(tree[ord(node) - 65][1])
    print(node, end="")


N = int(input())
tree = [[0]*3 for _ in range(26)]       # 0부터 25해서 26개 공간 생성

# 한 행씩 문자로 받아서 아스크코드로 숫자로 변환해서 tree작성
for _ in range(N):
    p, c1, c2 = map(str, input().split())
    # tree 생성하기(단 A가 0으로 설정함을 유의해야됨)
    tree[ord(p) - 65][0] = c1
    tree[ord(p) - 65][1] = c2
    if c1 != ".":
        tree[ord(c1) - 65][2] = p
    if c2 != ".":
        tree[ord(c2) - 65][2] = p
# print(tree)
preorder_traversal("A")       # tree를 전위 순회하면서 출력한다.
print()
inorder_traversal("A")
print()
postorder_traversal("A")
