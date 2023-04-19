import random
import math

class EightPuzzle:
    GOAL_STATE = [[1,2,3],[4,5,6],[7,8,0]]

    def __init__(self, state=None):
        if state is None:
            self.state = [[0,0,0],[0,0,0],[0,0,0]]
            self.shuffle()
        else:
            self.state = state

    def shuffle(self):
        for i in range(1000):
            self.move(random.choice(self.get_valid_moves()))

    def move(self, direction):
        x,y = self.find(0)
        if direction == 'left':
            self.state[x][y], self.state[x][y-1] = self.state[x][y-1], self.state[x][y]
        elif direction == 'right':
            self.state[x][y], self.state[x][y+1] = self.state[x][y+1], self.state[x][y]
        elif direction == 'up':
            self.state[x][y], self.state[x-1][y] = self.state[x-1][y], self.state[x][y]
        elif direction == 'down':
            self.state[x][y], self.state[x+1][y] = self.state[x+1][y], self.state[x][y]

    def get_valid_moves(self):
        x,y = self.find(0)
        moves = []
        if y > 0:
            moves.append('left')
        if y < 2:
            moves.append('right')
        if x > 0:
            moves.append('up')
        if x < 2:
            moves.append('down')
        return moves

    def find(self, value):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == value:
                    return i,j

    def is_goal(self):
        return self.state == EightPuzzle.GOAL_STATE

    def manhattan_distance(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    x,y = self.find(self.state[i][j])
                    distance += abs(x-i) + abs(y-j)
        return distance

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.state])

def simulated_annealing(initial_state, temperature, cooling_rate):
    current = EightPuzzle(initial_state)
    T = temperature
    while T > 1:
        neighbor = EightPuzzle(current.state)
        neighbor.move(random.choice(neighbor.get_valid_moves()))
        delta_E = neighbor.manhattan_distance() - current.manhattan_distance()
        if delta_E < 0 or random.uniform(0, 1) < math.exp(-delta_E / T):
            current = neighbor
        T *= cooling_rate
    return current.state

# Example usage:
initial_state = [[8,7,6],[5,4,3],[2,1,0]]
temperature = 100
cooling_rate = 0.95
solution = simulated_annealing(initial_state, temperature, cooling_rate)
print(solution)
