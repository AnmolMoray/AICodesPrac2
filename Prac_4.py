from collections import deque

# Define the goal state
#goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
goal_state=[[1,4,7],[2,5,8],[3,6,0]]

# Define possible moves
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # down right up left

def get_neighbors(state):
    neighbors = []
    zero_i, zero_j = None, None

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zero_i, zero_j = i, j

    for move in moves:
        new_i, new_j = zero_i + move[0], zero_j + move[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row.copy() for row in state]
            new_state[zero_i][zero_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[zero_i][zero_j]
            neighbors.append(new_state)

    return neighbors

def bfs(start_state):
    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            return path

        visited.add(tuple(map(tuple, state)))

        for neighbor in get_neighbors(state):
            if tuple(map(tuple, neighbor)) not in visited:
                queue.append((neighbor, path + [neighbor]))

# Example usage
start_state = [[3, 7, 5], [0, 6, 4], [2, 8, 1]]

solution_path = bfs(start_state)


if solution_path:
    print("Solution found!")
    for step, state in enumerate(solution_path):
        print(f"Step {step + 1}:")
        for row in state:
            print("|", end="")
            for col in row:
                print(col if col != 0 else " ", end="|")
            print("")
        print("\n")
else:
    print("No solution found.")
