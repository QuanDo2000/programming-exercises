class Solution:
    def allPathsSourceTarget(self, graph: list) -> list:
        n_vert = len(graph)
        visited = [False] * n_vert
        paths = []
        self.all_paths(graph, 0, n_vert - 1, visited, [], paths)
        return paths

    def all_paths(self, graph, curr_node, dest_node, visited, temp_path, paths):
        visited[curr_node] = True
        temp_path.append(curr_node)

        if curr_node == dest_node:
            paths.append(temp_path[:])
        else:
            for node in graph[curr_node]:
                if visited[node] == False:
                    self.all_paths(graph, node, dest_node,
                                   visited, temp_path, paths)
        temp_path.pop()
        visited[curr_node] = False


sol = Solution()
graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
res = sol.allPathsSourceTarget(graph)
print(res)
