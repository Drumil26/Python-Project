initial_state = [[1, 2, 3], [4, 6, 0], [7, 5, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)


def calculate_heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                h += 1
    return h


def hill_climbing(initial_state):
    current_state = initial_state
    while True:
        blank_x, blank_y = find_blank(current_state)
        
        neighbors = []
        if blank_x > 0:
            new_state = [row[:] for row in current_state]
#             print(new_state)
            new_state[blank_x][blank_y], new_state[blank_x-1][blank_y] = new_state[blank_x-1][blank_y], new_state[blank_x][blank_y]
            neighbors.append(new_state)
#             print(new_state)
        if blank_x < 2:
            new_state = [row[:] for row in current_state]
#             print(new_state)
            new_state[blank_x][blank_y], new_state[blank_x+1][blank_y] = new_state[blank_x+1][blank_y], new_state[blank_x][blank_y]
            neighbors.append(new_state)
#             print(new_state)
        if blank_y > 0:
            new_state = [row[:] for row in current_state]
            new_state[blank_x][blank_y], new_state[blank_x][blank_y-1] = new_state[blank_x][blank_y-1], new_state[blank_x][blank_y]
            neighbors.append(new_state)
        if blank_y < 2:
            new_state = [row[:] for row in current_state]
            new_state[blank_x][blank_y], new_state[blank_x][blank_y+1] = new_state[blank_x][blank_y+1], new_state[blank_x][blank_y]
            neighbors.append(new_state)
      
        neighbor_heuristics = [calculate_heuristic(neighbor) for neighbor in neighbors]
        
        if calculate_heuristic(current_state) == 0:
            return current_state
        if min(neighbor_heuristics) >= calculate_heuristic(current_state):
            return current_state
        min_index = neighbor_heuristics.index(min(neighbor_heuristics))
        current_state = neighbors[min_index]


print("Initial state:")
for row in initial_state:
    print(row)
    
result = hill_climbing(initial_state)

print("Result:")
for row in result:
    print(row)
