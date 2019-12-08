"""Contains window application"""
import json
import time
import tkinter as tk
from datetime import datetime
from tkinter import messagebox

from generator.BlumMicaliGenerator import BlumMicaliGenerator
from generator.PrimeGenerator import PrimeGenerator


class BlumMicaliGeneratorApplication(tk.Frame):
    """Application for Blum-Micali generator"""
    generator: BlumMicaliGenerator

    random_number: str

    def __init__(self, master=None):
        self.generator = BlumMicaliGenerator(
            base=PrimeGenerator.get_prime(digits=2),
            modulus=PrimeGenerator.get_prime(digits=20),
            root=PrimeGenerator.get_prime(digits=5)
        )
        super().__init__(master)
        self.master = master
        self.pack()
        self._create_widgets()

    def _create_widgets(self):
        self.parameters_frame = tk.LabelFrame(text="Parameters")
        self.parameters_frame.pack(fill='x', expand=True)

        self.modulus_frame = tk.LabelFrame(self.parameters_frame, text="Modulus")
        self.modulus_frame.pack(fill='x', expand=True)
        self.modulus_input = tk.Entry(self.modulus_frame, bd=5)
        self.modulus_input.insert(tk.END, self.generator.p)
        self.modulus_input.pack(fill='x', expand=True)

        self.base_frame = tk.LabelFrame(self.parameters_frame, text="Base")
        self.base_frame.pack(fill='x', expand=True)
        self.base_input = tk.Entry(self.base_frame, bd=5)
        self.base_input.insert(tk.END, self.generator.a)
        self.base_input.pack(fill='x', expand=True)

        self.root_frame = tk.LabelFrame(self.parameters_frame, text="Root")
        self.root_frame.pack(fill='x', expand=True)
        self.root_input = tk.Entry(self.root_frame, bd=5)
        self.root_input.insert(tk.END, self.generator.x_prev)
        self.root_input.pack(fill='x', expand=True)

        self.bit_length_frame = tk.LabelFrame(self.parameters_frame, text="Bit length")
        self.bit_length_frame.pack(fill='x', expand=True)
        self.bit_length_input = tk.Entry(self.bit_length_frame, bd=5)
        self.bit_length_input.insert(tk.END, 256)
        self.bit_length_input.pack(fill='x', expand=True)

        self.key_generation = tk.Button(self)
        self.key_generation["text"] = "Random number"
        self.key_generation["command"] = self._generate_key
        self.key_generation.pack()

        self.statistics_frame = tk.LabelFrame(text="Generation statistics")
        self.statistics_frame.pack(fill='x', expand=True)
        self.generation_time_text_area = tk.Text(self.statistics_frame, state='disabled', height=1)
        self.generation_time_text_area.pack(fill='x', expand=True)
        self.ratio_text_area = tk.Text(self.statistics_frame, state='disabled', height=1)
        self.ratio_text_area.pack(fill='x', expand=True)

        self.number_frame = tk.LabelFrame(text="Generated number")
        self.number_frame.pack(fill='x', expand=True)
        self.number_text_area = tk.Text(self.number_frame, height=40)
        self.number_text_area.pack(fill='x', expand=True)

    @staticmethod
    def _save_string_to_file(text: str):
        now = datetime.now()
        dt_string: str = now.strftime("%d-%m-%Y-%H-%M-%S")
        print("date and time = ", dt_string)
        file = open('generated-' + dt_string + '.txt', 'w')
        file.write(text)
        file.close()

    def _save_params_to_file(self, generation_time: float, bit_ratio: float):
        base: int = int(self.base_input.get())
        modulus: int = int(self.modulus_input.get())
        root: int = int(self.root_input.get())

        now = datetime.now()
        dt_string: str = now.strftime("%d-%m-%Y-%H-%M-%S")
        params_string: str = json.dumps({'base': base,
                                         'modulus': modulus,
                                         'root': root,
                                         'generation time': "{0}s".format(generation_time),
                                         '1 to 0 ration': bit_ratio})
        print("params = ", params_string)
        file = open('params-' + dt_string + '.json', 'w')
        file.write(params_string)
        file.close()

    def _generate_key(self):
        try:
            base: int = int(self.base_input.get())
            modulus: int = int(self.modulus_input.get())
            root: int = int(self.root_input.get())
            if base != self.generator.a or modulus != self.generator.p or root != self.generator.root:
                self.generator = BlumMicaliGenerator(
                    base=base,
                    modulus=modulus,
                    root=root
                )
        except:
            messagebox.showinfo("Initialization", "Generator initialization failure")
            return
        bit_length: int = int(self.bit_length_input.get())
        start = time.time()
        self.random_number = self.generator.generate_random_number(bit_length)
        time_elapsed = round(time.time() - start, 3)
        bit_ratio: float = round(self.random_number.count("1") / self.random_number.count("0"), 5)
        self.number_text_area.delete('1.0', tk.END)
        if bit_length <= 20000:
            self.number_text_area.insert(tk.END, self.random_number)
        self.generation_time_text_area.configure(state='normal')
        self.generation_time_text_area.delete('1.0', tk.END)
        self.generation_time_text_area.insert(tk.END, "Time: {0}s".format(time_elapsed))
        self.generation_time_text_area.configure(state='disabled')
        self.ratio_text_area.configure(state='normal')
        self.ratio_text_area.delete('1.0', tk.END)
        self.ratio_text_area.insert(tk.END, "1 to 0 ratio: {0}".format(bit_ratio))
        self.ratio_text_area.configure(state='disabled')
        BlumMicaliGeneratorApplication._save_string_to_file(self.random_number)
        self._save_params_to_file(time_elapsed, bit_ratio)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Blum-Micali generator")
    app = BlumMicaliGeneratorApplication(master=root)
    app.mainloop()
