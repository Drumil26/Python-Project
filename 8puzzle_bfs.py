from queue import Queue
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def is_goal(state):
    return state == goal_state

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_children(state):
    children = []
    blank_i, blank_j = find_blank(state)
    for move_i, move_j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_i, new_j = blank_i + move_i, blank_j + move_j
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in state]
            new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
            children.append(new_state)
    return children

def bfs(start_state):
    queue = Queue()
    queue.put((start_state, []))
    visited = set()
    while not queue.empty():
        state, path = queue.get()
        if is_goal(state):
            return path
        visited.add(str(state))
        for child in generate_children(state):
            if str(child) not in visited:
                queue.put((child, path + [child]))

start_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
solution = bfs(start_state)
if solution:
    print("Solution found in", len(solution), "moves:")
    for state in solution:
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
