def issafe(arr, x, y, n):
    # Checking for column attack
    for row in range(x):
        if arr[row][y] == 1:
            return False
    
    # Checking for diagonal attack
    row, col = x, y
    while row >= 0 and col >= 0:
        if arr[row][col] == 1:
            return False
        row -= 1
        col -= 1
    
    # Checking for anti-diagonal attack
    row, col = x, y
    while row >= 0 and col < n:
        if arr[row][col] == 1:
            return False
        row -= 1
        col += 1

    return True

def print_solution(arr, n):
    # This function prints the current board arrangement
    for i in range(n):
        for j in range(n):
            print("Q" if arr[i][j] == 1 else ".", end=" ")
        print()

def nQueen(arr, x, n, count):
    # If all queens are placed, return 1 (a solution is found)
    if x >= n:
        count[0] += 1
        print_solution(arr, n)  # Print the solution
        print()  # Empty line for better readability
        return True

    # Try placing queens in all columns one by one
    for col in range(n):
        if issafe(arr, x, col, n):
            arr[x][col] = 1  # Place queen
            nQueen(arr, x + 1, n, count)
            arr[x][col] = 0  # Backtrack

    return False

def main():
    n = int(input("Enter number of Queens: "))
    arr = [[0] * n for _ in range(n)]
    count = [0]  # This will store the number of solutions
    
    nQueen(arr, 0, n, count)
    
    print(f"Total number of solutions for {n} queens: {count[0]}")

if __name__ == '__main__':
    main()
