class FenwickTree:
    def __init__(self, nums_node: int):
        self.nums_node = nums_node
        self.arr = [0] * nums_node
        self.total = 0

    def get_sum(self, index: int):
        if index < 0:
            return self.total - self.get_sum(~index)
        if index >= self.nums_node:
            return self.total
        result = 0
        while index >= 0:
            result += self.arr[index]
            index = (index & (index + 1)) - 1
        return result

    def update(self, index: int, delta: int):
        self.total += delta
        while index < self.nums_node:
            self.arr[index] += delta
            index = index | (index + 1)


class Solution:
    # O(n^3)
    def numTeams(self, rating: list) -> int:
        count = 0
        rating_len = len(rating)
        for i in range(rating_len - 2):
            for j in range(i + 1, rating_len - 1):
                for k in range(j + 1, rating_len):
                    if (rating[i] < rating[j] and rating[j] < rating[k]) or (rating[i] > rating[j] and rating[j] > rating[k]):
                        count += 1
        return count

    # O(n^2)
    def numTeams(self, rating: list) -> int:
        count = 0
        rating_len = len(rating)
        for i in range(rating_len):
            temp_map = {
                'left_less': 0,
                'right_more': 0,
                'left_more': 0,
                'right_less': 0
            }
            for j in range(rating_len):
                if (rating[j] < rating[i]):
                    if j < i:
                        temp_map['left_less'] += 1
                    else:
                        temp_map['right_less'] += 1
                if (rating[j] > rating[i]):
                    if j < i:
                        temp_map['left_more'] += 1
                    else:
                        temp_map['right_more'] += 1
            count += temp_map['left_less'] * temp_map['right_more'] + \
                temp_map['left_more'] * temp_map['right_less']
        return count

    # O(n*log(n))
    def numTeams(self, rating: list) -> int:
        count = 0
        rating_len = len(rating)

        sort_map = {r: i for i, r in enumerate(sorted(rating))}

        left_tree = FenwickTree(rating_len)
        right_tree = FenwickTree(rating_len)

        for rat in rating:
            right_tree.update(sort_map[rat], 1)

        for rat in rating:
            index = sort_map[rat]
            right_tree.update(index, -1)
            count += (left_tree.get_sum(index) *
                      right_tree.get_sum(~index))
            count += (left_tree.get_sum(~index) * right_tree.get_sum(index))
            left_tree.update(index, 1)

        return count
