import tkinter as tk


class CalculatorLogic:
    @staticmethod
    def add_numbers(first_value, second_value):
        try:
            result = float(first_value) + float(second_value)
            return result
        except ValueError:
            return "Not numbers"


class CalculatorApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Sumator")
        self.master.minsize(width=200, height=100)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input_frame = tk.Frame(self)
        self.input_frame.pack(side="top")

        self.first_entry = tk.Entry(self.input_frame)
        self.plus_label = tk.Label(self.input_frame, text="+")
        self.second_entry = tk.Entry(self.input_frame)
        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate)

        self.result_label = tk.Label(self, text="Result...", bg="green", fg="white")

        # place widgets
        self.first_entry.pack(side="left")
        self.plus_label.pack(side="left")
        self.second_entry.pack(side="left")
        self.calculate_button.pack(side="top")
        self.result_label.pack(side="top")

    def calculate(self):
        first_value = self.first_entry.get()
        second_value = self.second_entry.get()
        result = CalculatorLogic.add_numbers(first_value, second_value)
        self.result_label.config(text=str(result), bg="green" if isinstance(result, float) else "red",
                                 fg="white" if isinstance(result, float) else "black")


# create the application
app = CalculatorApp()

# start the program
app.mainloop()
