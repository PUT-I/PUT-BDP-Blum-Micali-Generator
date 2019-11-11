"""Contains window application"""

import tkinter as tk

from generator.PrimeGenerator import PrimeGenerator


class PrimeGeneratorApplication(tk.Frame):
    """Application for prime generator"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self._create_widgets()

    def _create_widgets(self):
        self.parameters_frame = tk.LabelFrame(text="Parameters")
        self.digits_frame = tk.LabelFrame(self.parameters_frame, text="Number of digits")
        self.digits_frame.pack()
        self.digits_input = tk.Entry(self.digits_frame, bd=5)
        self.digits_input.pack()
        self.parameters_frame.pack()

        self.prime_frame = tk.LabelFrame(text="Generated Prime")
        self.prime_frame.pack()
        self.prime_text_area = tk.Text(self.prime_frame, height=4)
        self.prime_text_area.pack()

        self.prime_generation = tk.Button(self)
        self.prime_generation["text"] = "Random prime"
        self.prime_generation["command"] = self._generate_prime
        self.prime_generation.pack()

    def _generate_prime(self):
        digits: int = int(self.digits_input.get())
        random_number: int = PrimeGenerator.get_prime(digits=digits)
        self.prime_text_area.delete('1.0', tk.END)
        self.prime_text_area.insert(tk.END, random_number)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Prime generator")
    app = PrimeGeneratorApplication(master=root)
    app.mainloop()
