from tkinter import Canvas, StringVar, Tk
from tkinter.ttk import Combobox, Frame, Label, Button
from typing import List
from data_providers import DataProvider
from algorithms.algorithm_provider import AlgorithmProvider
import threading
from multipledispatch import dispatch
import loader


class CanvasUi(Frame):


    def __init__(self, master=None, **kw):
        self.master = master
        self.canvas: Canvas
        self.data: List[int]
        self.first: bool = True
        self.rects = []

        super().__init__(master, **kw)
        self.canvas = Canvas(self, width=800, height=220, bd=5, bg="white")

    def grid(self, *args, **kwargs):
        self.canvas.pack()
        super().grid(*args, **kwargs)

    @dispatch()
    def draw(self):
        self.draw(0, 0)

    @dispatch(int, int, list)
    def draw(self, i, j, data):
        self.data = data
        self.draw(i, j)

    @dispatch(int, int)
    def draw(self, i, j):
        if not self.first:
            self.swap_rectangles(i, j)
            return
        self.rects = []
        self.first = False
        self.canvas.delete("all")
        canvas_width = 800
        canvas_height = 220

        x_width = canvas_width/(len(self.data) + 1)
        offset = 4
        spacing = 2
        for i, value in enumerate(self.data):
            x0 = i * x_width + offset + spacing
            y0 = canvas_height - value
            x1 = (i + 1) * x_width + offset
            y1 = canvas_height
            self.rects.append(self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue", tags=str(i)))

    def set_data(self, data):
        self.data = data
        self.draw()

    def start_sorting(self):
        algorithm_provider = AlgorithmProvider(self.master.settings_ui.algorithm_value.get())
        algorithm = algorithm_provider.get_algorithm()
        sorter = algorithm(self.data, self)
        sorter.sort()

    def swap_rectangles(self, i, j):
        if j==i:
            return
        self.canvas.delete(self.rects[i])
        self.canvas.delete(self.rects[j])
        canvas_width = 800
        canvas_height = 220
        self.update_idletasks()
        x_width = canvas_width / (len(self.data) + 1)
        offset = 4
        spacing = 2
        value = self.data[i]
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - value
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        self.rects[i] = self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue")

        value = self.data[j]
        x0 = j * x_width + offset + spacing
        y0 = canvas_height - value
        x1 = (j + 1) * x_width + offset
        y1 = canvas_height
        self.rects[j] = self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue")


class SettingsUi(Frame):


    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

        AlgorithmProvider.load_plugins()

        self.algorithm_label: Label
        self.algorithm_combobox: Combobox
        self.algorithm_values: List[str] = AlgorithmProvider.get_algotihms_list()
        self.algorithm_value: StringVar

        self.algorithm_value = StringVar()
        self.algorithm_label = Label(self, text="Algorithm")
        self.algorithm_combobox = Combobox(self, textvariable=self.algorithm_value, values=self.algorithm_values)

    def grid(self, *args, **kwargs):
        self.build_grid()
        super().grid(*args, **kwargs)

    def set_default_values(self):
        self.algorithm_value.set(self.algorithm_values[0])

    def build_grid(self):
        self.set_default_values()
        self.algorithm_label.grid(row=0, column=0, sticky="W", padx=10, pady=5)
        self.algorithm_combobox.grid(row=0, column=1, padx=10, pady=5)


class RowUi(Frame):


    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.settings_ui: SettingsUi = SettingsUi(self)
        self.canvas_ui: CanvasUi = CanvasUi(self)

    def grid(self, *args, **kwargs):
        self.build_grid()
        super().grid(*args, **kwargs)

    def pack(self, *args, **kwargs):
        self.build_grid()
        super().pack(*args, **kwargs)

    def build_grid(self):
        self.settings_ui.grid(row=0, column=1)
        self.canvas_ui.grid(row=0, column=0)

    def start_sorting(self):
        self.canvas_ui.start_sorting()


class HeaderUi(Frame):

    speed_label: Label
    speed_combobox: Combobox
    speed_values: List[str] = ["Slow", "Medium", "Speed"]
    speed_value: StringVar

    data_label: Label
    data_combobox: Combobox
    data_values: List[str] = ["Random", "Sinus", "Sorted", "Reverse sorted"]
    data_value: StringVar

    generate_array_button: Button
    sort_button: Button

    master: Tk

    data_provider: DataProvider
    data: List[int]

    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

        self.master = master

        self.speed_value = StringVar()
        self.speed_label = Label(self, text="Sorting speed")
        self.speed_combobox = Combobox(self, textvariable=self.speed_value, values=self.speed_values)

        self.data_value = StringVar()
        self.data_value.trace("w", self.data_combobox_command)
        self.data_label = Label(self, text="Data type")
        self.data_combobox = Combobox(self, textvariable=self.data_value, values=self.data_values)

        self.sort_button = Button(self, text="Sort", command=self.start_sorting)
        self.generate_array_button = Button(self, text="Generate array", command=self.generate_array_button_command)

        self.set_default_values()

    def set_default_values(self):
        self.speed_value.set(self.speed_values[0])
        self.data_value.set(self.data_values[0])

    def build_grid(self):

        self.speed_label.grid(row=1, column=0, sticky="W", padx=10, pady=5)
        self.speed_combobox.grid(row=1, column=1, padx=10, pady=5)

        self.data_label.grid(row=2, column=0, sticky="W", padx=10, pady=5)
        self.data_combobox.grid(row=2, column=1, padx=10, pady=5)

        self.sort_button.grid(row=3, column=0, pady=5)
        self.generate_array_button.grid(row=3, column=1, pady=5)

    def pack(self, *args, **kwargs):
        self.build_grid()
        super().pack(*args, **kwargs)

    def grid(self, *args, **kwargs):
        self.build_grid()
        super().grid(*args, **kwargs)

    def data_combobox_command(self, *args):
        if not self.data_value.get() == "Random":
            self.generate_array_button["state"] = "disabled"
        else:
            self.generate_array_button["state"] = "active"
        self.data_provider = DataProvider.get_data_provider(self.data_value.get())
        self.set_canvases_data(self.data_provider.get_data())

    def start_sorting(self):
        threads = []
        for row in self.master.rows:
            x = threading.Thread(target=row.start_sorting)
            threads.append(x)
            x.start()

    def set_canvases_data(self, data):
        for row in self.master.rows:
            row.canvas_ui.first = True
            row.canvas_ui.set_data(data)

    def generate_array_button_command(self):
        self.data_provider.regenerate_data()
        self.set_canvases_data(self.data_provider.get_data())

