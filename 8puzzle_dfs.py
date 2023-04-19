goal_state = [[1,2,3], [4,5,6], [7,8,0]]

moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

def dfs(current_state, visited):
    if current_state == goal_state:
        return True
    visited.append(current_state)
    for move, (dx, dy) in moves.items():
        x, y = [(i, j) for i in range(3) for j in range(3) if current_state[i][j] == 0][0]
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in current_state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            if new_state not in visited:
                if dfs(new_state, visited):
                    return True
    visited.pop()
    return False
initial_state = [[1,2,3], [4,0,5], [7,8,6]]
visited = []
dfs(initial_state, visited)

print('Visited States:')
for state in visited:
    for row in state:
        print(row)
    print()
