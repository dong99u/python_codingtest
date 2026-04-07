class Node:
    def __init__(self, x, y, val, left=None, right=None):
        self.x = x
        self.y = y
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root: Node = None

    def insert(self, node: Node):
        if not self.root:
            self.root = node
        else:
            curr_node = self.root
            while True:
                if node.x < curr_node.x:
                    if curr_node.left is not None:
                        curr_node = curr_node.left
                    else:
                        curr_node.left = node
                        break
                else:
                    if curr_node.right is not None:
                        curr_node = curr_node.right
                    else:
                        curr_node.right = node
                        break


def solution(node_info):
    nodes = []
    for i, (x, y) in enumerate(node_info):
        nodes.append((i + 1, (x, y)))

    nodes.sort(key=lambda x: (-x[1][1], x[1][0]))

    bst = BST()

    for i in range(len(nodes)):
        val, (x, y) = nodes[i]

        bst.insert(Node(x, y, val))

    def preorder(v: Node):
        if v is None:
            return []

        result = [v.val]
        result += preorder(v.left)
        result += preorder(v.right)

        return result

    def postorder(v: Node):
        if v is None:
            return []

        result = postorder(v.left)
        result += postorder(v.right)
        result += [v.val]

        return result

    answer = []
    answer.append(preorder(bst.root))
    answer.append(postorder(bst.root))

    return answer

if __name__ == '__main__':
    print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))