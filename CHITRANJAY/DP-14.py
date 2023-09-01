"""
You are part of a team developing a social networking platform called "SocialGraph." As part of this platform,
you have been assigned the task of creating a feature that implements
a depth-first search (DFS) algorithm to traverse the user graph.
This feature will assist users in discovering connections, exploring networks of friends,
and identifying mutual friends within the platform.
To accomplish this, you decide to create a program that takes a user graph as input and implements
the DFS algorithm to traverse the graph. The program will provide users with the traversal result,
along with additional functionality to enhance their social networking experience.
"""


class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        traversal_result = []

        def dfs_recursive(node):
            visited.add(node)
            traversal_result.append(node)

            if node in self.graph:
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        dfs_recursive(neighbor)

        dfs_recursive(start)
        return traversal_result


def main():

    print("Welcome to SocialGraph - Explore Connections!")

    # Example user graph
    social_graph = Graph()
    social_graph.add_edge(12345, 56789)
    social_graph.add_edge(56789, 98765)
    social_graph.add_edge(98765, 43210)
    social_graph.add_edge(43210, 11111)

    # Add more edges as needed

    # Example starting user ID
    start_user = 12345

    traversal_result = social_graph.dfs(start_user)
    print("DFS traversal result:")
    print(" -> ".join(map(str, traversal_result)))


if __name__ == "__main__":
    main()

