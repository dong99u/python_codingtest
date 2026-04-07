def solution(nodes):
    def preorder(idx):
        if idx >= len(nodes):
            return ''

        result = str(nodes[idx]) + ' '

        left = idx * 2 + 1
        right = idx * 2 + 2
        result += preorder(left)
        result += preorder(right)

        return result

    def inorder(idx):
        if idx >= len(nodes):
            return ''

        left = idx * 2 + 1
        right = idx * 2 + 2

        result = inorder(left)
        result += str(nodes[idx]) + ' '
        result += inorder(right)

        return result

    def postorder(idx):
        if idx >= len(nodes):
            return ''

        left = idx * 2 + 1
        right = idx * 2 + 2

        result = postorder(left)
        result += postorder(right)
        result += str(nodes[idx]) + ' '

        return result

    return [preorder(0), inorder(0), postorder(0)]




if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5, 6, 7]))