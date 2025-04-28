def print_board(elements):
    for i in range(9):
        if i % 3 == 0:
            print()
        if elements[i] == -1:
            print("_", end=" ")
        else:
            print(elements[i], end=" ")
    print()

def solvable(start):
    inv = 0
    for i in range(9):
        if start[i] <= 0:
            continue
        for j in range(i + 1, 9):
            if start[j] <= 0:
                continue
            if start[i] > start[j]:
                inv += 1
    return inv % 2 == 0

def heuristic(state, goal):
    h = 0
    for num in range(1, 9):  # tiles 1 to 8
        idx_state = state.index(num)
        idx_goal = goal.index(num)
        row_state, col_state = divmod(idx_state, 3)
        row_goal, col_goal = divmod(idx_goal, 3)
        h += abs(row_state - row_goal) + abs(col_state - col_goal)
    return h

def move(state, direction):
    new_state = state[:]
    idx = new_state.index(-1)
    row, col = divmod(idx, 3)

    if direction == 'left' and col > 0:
        new_state[idx], new_state[idx - 1] = new_state[idx - 1], new_state[idx]
    elif direction == 'right' and col < 2:
        new_state[idx], new_state[idx + 1] = new_state[idx + 1], new_state[idx]
    elif direction == 'up' and row > 0:
        new_state[idx], new_state[idx - 3] = new_state[idx - 3], new_state[idx]
    elif direction == 'down' and row < 2:
        new_state[idx], new_state[idx + 3] = new_state[idx + 3], new_state[idx]
    else:
        return None  # invalid move

    return new_state

def get_possible_moves(state):
    idx = state.index(-1)
    row, col = divmod(idx, 3)
    moves = []
    if col > 0:
        moves.append('left')
    if col < 2:
        moves.append('right')
    if row > 0:
        moves.append('up')
    if row < 2:
        moves.append('down')
    return moves

def solve_eight_puzzle(start, goal):
    g = 0  # move counter
    current = start[:]
    print("Initial board:")
    print_board(current)

    while True:
        if current == goal:
            print("\nSolved in {} moves.".format(g))
            break

        moves = get_possible_moves(current)
        best_move = None
        min_cost = float('inf')

        for move_dir in moves:
            next_state = move(current, move_dir)
            if next_state:
                cost = heuristic(next_state, goal) + g + 1  # g + 1 because we consider the next move
                if cost < min_cost:
                    min_cost = cost
                    best_move = next_state

        if best_move is None:
            print("No solution found.")
            break

        current = best_move
        g += 1
        print_board(current)

def main():
    start = []
    goal = []
    print("Enter the start state (use -1 for the empty space):")
    for _ in range(9):
        start.append(int(input()))

    print("Enter the goal state (use -1 for the empty space):")
    for _ in range(9):
        goal.append(int(input()))

    if solvable(start):
        solve_eight_puzzle(start, goal)
    else:
        print("This puzzle is not solvable.")

if __name__ == "__main__":
    main()
