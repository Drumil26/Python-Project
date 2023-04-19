import heapq
goal_state = [[1,2,3],[4,5,6],[7,8,0]]
def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                count += 1
    return count
def best_first_search(start_state):
    frontier = [(heuristic(start_state), start_state)]
    visited = set()
    num_expanded = 0
    while frontier:
        current = heapq.heappop(frontier)[1]
        if current == goal_state:
            return num_expanded
        visited.add(tuple(map(tuple, current)))
        for i in range(3):
            for j in range(3):
                if current[i][j] == 0:
                    if i > 0:
                        new_state = [row[:] for row in current]
                        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
                        if tuple(map(tuple, new_state)) not in visited:
                            heapq.heappush(frontier, (heuristic(new_state), new_state))
                            num_expanded += 1
                    if i < 2:
                        new_state = [row[:] for row in current]
                        new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
                        if tuple(map(tuple, new_state)) not in visited:
                            heapq.heappush(frontier, (heuristic(new_state), new_state))
                            num_expanded += 1
                    if j > 0:
                        new_state = [row[:] for row in current]
                        new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
                        if tuple(map(tuple, new_state)) not in visited:
                            heapq.heappush(frontier, (heuristic(new_state), new_state))
                            num_expanded += 1
                    if j < 2:
                        new_state = [row[:] for row in current]
                        new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
                        if tuple(map(tuple, new_state)) not in visited:
                            heapq.heappush(frontier, (heuristic(new_state), new_state))
                            num_expanded += 1
    return -1
start_state = [[1,2,3],[4,0,6],[7,5,8]]
num_expanded = best_first_search(start_state)
print("Number of nodes expanded:", num_expanded)
