
class Tree:
    def garland_length(self, arr):
        length = 0
        for i in range(1, len(arr)):
            length += abs(arr[i] - arr[i - 1])
        return length

tree = Tree()
print(tree.garland_length([1, 2, 3, 4, 5]))
print(tree.garland_length([1, 3, 5, 7, 9]))




