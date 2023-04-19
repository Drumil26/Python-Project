from queue import PriorityQueue

class Puzzle:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
    
    def get_manhattan_distance(self, node):
        distance = 0
        for i in range(3):
            for j in range(3):
                if node[i][j] != goal[i][j]:
                    distance=distance+1
        return distance
    
    def get_children(self, node):
        children = []
        row, col = self.find_blank(node)
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for move in moves:
            new_row, new_col = row + move[0], col + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                child = self.copy(node)
                child[row][col], child[new_row][new_col] = child[new_row][new_col], child[row][col]
                children.append(child)
        return children
    
    def find_blank(self, node):
        for i in range(3):
            for j in range(3):
                if node[i][j] == 0:
                    return i, j
    
    def copy(self, node):
        new_node = []
        for row in node:
            new_node.append(row.copy())
        return new_node
    
    def solve(self):
        queue = PriorityQueue()
        queue.put((0, self.start))
        visited = set()
        while not queue.empty():
            node = queue.get()[1]
            if self.is_goal(node):
                return node
            visited.add(str(node))
            for child in self.get_children(node):
                if str(child) not in visited:
                    queue.put((self.get_manhattan_distance(child), child))
        return None
    
    def is_goal(self, node):
        return node == self.goal

# Example usage
start = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
puzzle = Puzzle(start, goal)
solution = puzzle.solve()
if solution is None:
    print("No solution found")
else:
    print("Solution found:")
    for row in solution:
        print(row)
