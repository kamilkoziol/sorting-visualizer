from tkinter import Tk
from graphics.uis import RowUi, HeaderUi
from tkinter.ttk import Button, Frame
from typing import List


class App(Tk):
    header: HeaderUi
    rows: List[RowUi]
    new_row_button: Button

    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Sorting visualizer")
        self.rows = [RowUi(self),
                     RowUi(self)]
        self.header_ui = HeaderUi(self)
        self.buttons_frame = Frame(self)
        self.new_row_button = Button(self.buttons_frame, text="New row", command=self.new_row_button_command)
        self.remove_row_button = Button(self.buttons_frame, text="Remove row", command=self.remove_row_button_command)



    def run(self):
        self.build_grid()
        self.mainloop()

    def build_grid(self):
        self.header_ui.grid(row=0, column=0, pady=15)
        for count, row in enumerate(self.rows):
            row.grid(row=count + 1, column=0)

        self.new_row_button.grid(row=0, column=0)
        self.remove_row_button.grid(row=0, column=1)
        self.buttons_frame.grid(row=len(self.rows) + 1)

    def new_row_button_command(self):
        self.rows.append(RowUi(self))
        self.build_grid()
        self.header_ui.set_canvases_data(self.header_ui.data_provider.get_data())

    def remove_row_button_command(self):
        for row in self.rows:
            row.grid_forget()
        self.rows.pop()
        self.build_grid()


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()

