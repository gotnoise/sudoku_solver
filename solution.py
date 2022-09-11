def solution(puzzle):
    time_to_run = 0

    # We replace all the blanks in the puzzle with a list:[1, 2, 3, 4, 5, 6, 7, 8, 9]

    for pos_x in range(0, 9):
        for pos_y in range(0, 9):
            if puzzle[pos_x][pos_y] == 0:
                puzzle[pos_x][pos_y] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # For each item of the puzzle we look for lists to run some checks on.
    # This will repeat forever until all lists are replaced with numbers

    not_solved = True
    while not_solved:
        for pos_x in range(0, 9):
            for pos_y in range(0, 9):
                if type(puzzle[pos_x][pos_y]) == list:

                    # for each list-type item(let's call it candidate list) we create 3 basic lists.
                    # one that includes all items in the same row(named: horizontally),
                    # one that includes all items in the same column(named: vertically),
                    # and one that includes all items in the same box(named: box)

                    horizontally = puzzle[pos_x]
                    vertically = [_[pos_y] for _ in puzzle]
                    box = []
                    box_x = puzzle[(pos_x // 3) * 3:(pos_x // 3) * 3 + 3]
                    for b in box_x:
                        box += b[(pos_y // 3) * 3:(pos_y // 3) * 3 + 3]

                    # 1st CHECK: Checks horizontally and removes from the candidate list integers
                    # it finds in the same row

                    for h in horizontally:
                        if h in puzzle[pos_x][pos_y] and type(h) is int:
                            puzzle[pos_x][pos_y] = [_ for _ in puzzle[pos_x][pos_y] if _ != h]

                    # 2nd CHECK: Checks vertically and removes from the candidate list integers
                    # found in the same column

                    for v in vertically:
                        if v in puzzle[pos_x][pos_y] and type(v) is int:
                            puzzle[pos_x][pos_y] = [_ for _ in puzzle[pos_x][pos_y] if _ != v]

                    # 3rd CHECK: Checks the box and removes from the candidate list integers found in the box

                    for b in box:
                        if b in puzzle[pos_x][pos_y] and type(b) is int:
                            puzzle[pos_x][pos_y] = [z for z in puzzle[pos_x][pos_y] if z != b]

                    # 4th check: it checks all the integers in the candidate list and if any of them
                    # is not found in any additional sub-list of the three main lists we created,
                    # then the list is replaced with this specific integer

                    for nums in puzzle[pos_x][pos_y]:
                        if sum([_ for _ in horizontally if type(_) is list], []).count(nums) == 1 or \
                                sum([_ for _ in vertically if type(_) is list], []).count(nums) == 1 or \
                                sum([_ for _ in box if type(_) is list], []).count(nums) == 1:
                            puzzle[pos_x][pos_y] = nums
                            break

        # we repeat the process 1000 times

        time_to_run += 1
        if time_to_run == 1000:
            not_solved = False
            print(puzzle)
    return puzzle


def solve(sudoku_table):
    table_a, table_b = [], []
    for column in sudoku_table:
        for number in column:
            if number.get() not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                table_a.append(0)
            else:
                table_a.append(int(number.get()))
    for number in range(0, 81, 9):
        table_b.append(table_a[number:number + 9])
    final_solution = solution(table_b)
    for pos_x in range(0, 9):
        for pos_y in range(0, 9):
            if sudoku_table[pos_x][pos_y].get() not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                sudoku_table[pos_x][pos_y].config(fg="#C98474")
                if type(final_solution[pos_x][pos_y]) == list:
                    insert_text = ",".join(str(x_str) for x_str in final_solution[pos_x][pos_y])
                    sudoku_table[pos_x][pos_y].insert(0, insert_text)
                else:
                    sudoku_table[pos_x][pos_y].insert(0, final_solution[pos_x][pos_y])
