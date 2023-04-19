import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def calculate_heuristic(self):
        # Heuristic function for the 8-puzzle problem
        count = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    x, y = divmod(self.state[i][j]-1, 3)
                    count += abs(x-i) + abs(y-j)
        return count

    def get_children(self):
        # Generate children nodes
        children = []
        i, j = next((i, j) for i in range(3) for j in range(3) if self.state[i][j] == 0)
        for x, y in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
            if 0 <= x < 3 and 0 <= y < 3:
                new_state = [row[:] for row in self.state]
                new_state[i][j], new_state[x][y] = new_state[x][y], new_state[i][j]
                children.append(PuzzleNode(new_state, self, self.cost+1))
        return children

    def __lt__(self, other):
        # Comparison function for priority queue
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def solve_puzzle(start_state):
    # Initialize start node and priority queue
    start_node = PuzzleNode(start_state)
    pq = [start_node]
    heapq.heapify(pq)

    # Initialize closed set and visited set
    closed_set = set()
    visited_set = set()

    while pq:
        # Get node with lowest f value from priority queue
        node = heapq.heappop(pq)

        # Check if goal state has been reached
        if node.heuristic == 0:
            solution = []
            while node.parent:
                solution.append(node.state)
                node = node.parent
            solution.append(node.state)
            return solution[::-1]

        # Add node to closed set and visited set
        closed_set.add(tuple(map(tuple, node.state)))
        visited_set.add(node)

        # Generate children nodes and add them to priority queue
        for child in node.get_children():
            if tuple(map(tuple, child.state)) not in closed_set:
                if child in visited_set:
                    # Update cost of existing node in visited set
                    existing_node = visited_set.pop(visited_set.index(child))
                    if child.cost < existing_node.cost:
                        existing_node.cost = child.cost
                        existing_node.parent = child.parent
                        heapq.heappush(pq, existing_node)
                    else:
                        heapq.heappush(pq, child)
                else:
                    heapq.heappush(pq, child)

    return None  # No solution found
start_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
solution = solve_puzzle(start_state)
if solution is not None:
    print("Solution found:")
    for state in solution:
        print(state)
else:
    print("No solution found.")
