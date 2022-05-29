from turtle import color
from node import Node, Queue, Stack
import tkinter as tk
from tkinter import filedialog
import os
import PIL


class Maze:
    def __init__(self):
        # self.file_path 
        self.sol_msg=''
        # self.load_file()

        self.root = tk.Tk()
        self.root.wm_attributes('-alpha')
        self.root.geometry('400x400')
        self.bg_image = tk.PhotoImage(file='media/bg1.png')

        # print(bg_image)
        bg_label = tk.Label(self.root, image=self.bg_image)
        bg_label.place(x=0, y=0)

        self.input_button = tk.Button(self.root, text='Choose your maze configuration', command=self.load_file, borderwidth=0).pack(pady=50)

        self.solve_button = tk.Button(self.root, text='Solve maze', command=self.solve, borderwidth=0)
        self.solve_button.pack()
        self.solution_message = tk.Label(self.root, text='', borderwidth=0)
        self.solution_message.pack()

        self.save_button = tk.Button(self.root, text='Save maze', command=self.save, borderwidth=0).pack(pady=40)

        # filename = 



    def load_file(self):
        self.file_path = filedialog.askopenfilename(initialdir = os.getcwd(),
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        ".txt"),
                                                       ("all files",
                                                        "*.*")))

        with open(self.file_path, 'r') as file:
            contents = file.read().splitlines()

        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        self.maze = [[0 for i in range(self.width)] for j in range(self.height)]

        a, b = 0, 0

        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == 'A':
                        a = 1
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == 'B':
                        b = 1
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == ' ':
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)    
            self.walls.append(row)
        
        if not (a or b):
            self.solution_message['text'] = 'Your maze configuration is not correct'
            raise Exception('Ашыбка')

        self.solution = None
    
    def save(self):
        solution  = self.solution[1] if self.solution is not None else None
        # print()
        # self.
        file = open('solution.txt', 'w')

        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    file.write('█')
                elif (i, j) == self.start:
                    file.write('A')
                elif (i, j) == self.goal:
                    file.write('B')
                elif solution is not None and (i, j) in solution:
                    file.write('*')
                else:
                    file.write(" ")
            file.write('\n')
        file.close()
    def find_nei(self, state):
        row, col = state

        candidates = [
            ('up', (row - 1, col)),
            ('right', (row, col + 1)),
            ('down', (row + 1, col)),
            ('left', (row, col - 1)),
        ]

        result = []
        for action, (r, c) in candidates:
            try:
                if not self.walls[r][c]:
                    result.append((action, (r, c)))
            except IndexError:
                continue
        
        return result
            

    def solve(self):
        self.num_explored = 0
        start = Node(self.start, None, None)

        frontier = Queue()
        frontier.add(start)

        self.explored = set()

        while True:
            if frontier.empty():
                self.solution_message['text'] = 'There is not solution'
                # raise Exception('There is not solution!')

            node = frontier.remove()
            if node.state == self.goal:
                actions = []
                cells = []

                while node.parent != None:
                    actions.append(node.action)
                    cells.append(node.state)

                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                self.solution_message['text'] = 'Solution was found!'
                print('раб')
                return 
            
            self.explored.add(node.state)
            for action, state in self.find_nei(node.state):
                if not frontier.containsState(state) and state not in self.explored:
                    child = Node(state, node, action)
                    frontier.add(child)
            
        
m = Maze()

# m.print()

# m.solve()

print()

# m.print()
# 
m.root.mainloop()