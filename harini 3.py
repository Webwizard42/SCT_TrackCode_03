def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def is_valid(grid, row, col, num):
    # Row
    if num in grid[row]:
        return False
    # Column
    if num in (grid[i][col] for i in range(9)):
        return False
    # 3x3 block
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0  # Backtrack
                return False
    return True

# Take user input for the unsolved Sudoku puzzle
print("Enter the Sudoku puzzle row-by-row (use 0 for empty cells):")
puzzle = []
for i in range(9):
    while True:
        try:
            row = list(map(int, input(f"Row {i+1}: ").strip().split()))
            if len(row) == 9 and all(0 <= n <= 9 for n in row):
                puzzle.append(row)
                break
            else:
                print("❗ Enter exactly 9 numbers (0–9).")
        except ValueError:
            print("❗ Invalid input. Only numbers allowed.")

# Show original puzzle
print("\n🔢 Original Sudoku Puzzle:")
print_grid(puzzle)

# Solve and show result
if solve_sudoku(puzzle):
    print("\n✅ Solved Sudoku Puzzle:")
    print_grid(puzzle)
else:
    print("\n❌ This Sudoku puzzle has no solution.")
