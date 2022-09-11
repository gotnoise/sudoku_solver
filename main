from tkinter import *
from solution import solve


window = Tk()
window.title("Sudoku Solver")
window.minsize(width=200, height=200)
window.config(bg="#F2D388")

table, sudoku_table = [], []
for x in range(9):
    for y in range(9):
        entry = Entry(width=2, bd=5, justify="center", bg="#A7D2CB", fg="black",
                      font=('Times', 25, 'bold italic'))
        entry.grid(column=y, row=x, ipadx=3, ipady=3)
        table.append(entry)

for num in range(0, 81, 9):
    sudoku_table.append(table[num:num + 9])

button = Button(text="solve", command=lambda: solve(sudoku_table), bg="#C98474", fg="black",
                activebackground="#C98474", width=20, height=2)
button.config(width=10, bd=7)
button["font"] = ("Helvetica", 10, "bold")
button.grid(column=0, row=10, columnspan=9)

window.mainloop()
