class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list) -> list:
        reachable_nodes = set()
        for _, to_node in edges:
            reachable_nodes.add(to_node)

        ret = []
        for num in range(n):
            if num not in reachable_nodes:
                ret.append(num)
        return ret


sol = Solution()
ans = sol.findSmallestSetOfVertices(
    5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]])
print(ans)
