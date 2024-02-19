import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.result_label = tk.Label(self.master, textvariable=self.result_var, font=("Arial", 20), anchor="e", bg="white", bd=5)
        self.result_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('del', 5, 1)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(self.master, text=text, font=("Arial", 15), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, sticky="nsew")
            
            if text == 'C':
                button.config(bg='orange')
            elif text == 'del':
                button.config(bg='red')

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)
        self.master.grid_columnconfigure(3, weight=1)
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_rowconfigure(3, weight=1)
        self.master.grid_rowconfigure(4, weight=1)
        self.master.grid_rowconfigure(5, weight=1)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        elif char == 'C':
            self.result_var.set("0")
        elif char == 'del':
            current = self.result_var.get()
            self.result_var.set(current[:-1] if current != "Error" else "0")
        else:
            current = self.result_var.get()
            if current == "0" or current == "Error":
                self.result_var.set(char)
            else:
                self.result_var.set(current + char)

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
