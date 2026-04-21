import numpy as np

# Grid size
rows, cols = 3, 4

# Actions: Up, Down, Left, Right
actions = [0, 1, 2, 3]

action_moves = {
    0: (-1, 0),  # Up
    1: (1, 0),   # Down
    2: (0, -1),  # Left
    3: (0, 1)    # Right
}

gamma = 0.9

# Rewards
grid = np.array([
    [0, 0, 0, 1],
    [0, None, 0, -1],
    [0, 0, 0, 0]
], dtype=object)

# Initialize
V = np.zeros((rows, cols))
policy = np.random.choice(actions, size=(rows, cols))

def is_valid(r, c):
    return 0 <= r < rows and 0 <= c < cols and grid[r][c] is not None

def get_next_state(r, c, action):
    dr, dc = action_moves[action]
    nr, nc = r + dr, c + dc

    if not is_valid(nr, nc):
        return r, c
    return nr, nc

def get_reward(r, c):
    if grid[r][c] == 1:
        return 1
    elif grid[r][c] == -1:
        return -1
    return -0.04

def policy_evaluation():
    global V
    while True:
        delta = 0
        new_V = np.copy(V)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] is None:
                    continue

                a = policy[r][c]
                nr, nc = get_next_state(r, c, a)

                reward = get_reward(nr, nc)
                new_V[r][c] = reward + gamma * V[nr][nc]

                delta = max(delta, abs(V[r][c] - new_V[r][c]))

        V = new_V
        if delta < 1e-4:
            break

def policy_improvement():
    global policy
    stable = True

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] is None:
                continue

            old_action = policy[r][c]
            values = []

            for a in actions:
                nr, nc = get_next_state(r, c, a)
                reward = get_reward(nr, nc)
                values.append(reward + gamma * V[nr][nc])

            best_action = np.argmax(values)
            policy[r][c] = best_action

            if best_action != old_action:
                stable = False

    return stable

# Policy Iteration
while True:
    policy_evaluation()
    if policy_improvement():
        break

# Display policy
symbols = ['↑', '↓', '←', '→']

print("\nOptimal Policy:\n")
for r in range(rows):
    for c in range(cols):
        if grid[r][c] is None:
            print(" X ", end="")
        elif grid[r][c] == 1:
            print(" G ", end="")
        elif grid[r][c] == -1:
            print(" P ", end="")
        else:
            print(f" {symbols[policy[r][c]]} ", end="")
    print()

print("\nValue Function:\n", V)