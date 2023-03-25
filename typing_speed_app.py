import tkinter as tk
import time


class TypingSpeedApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed App")

        self.sample_text = "The cat in the hat wore a red and white striped hat and played with a ball of string."
        self.words_per_minute = 0
        self.start_time = None

        # create sample text label
        self.sample_text_label = tk.Label(master, text=self.sample_text, font=("Arial", 14))
        self.sample_text_label.pack(pady=20)

        # create input text box
        self.input_text_box = tk.Entry(master, font=("Arial", 14), width=50)
        self.input_text_box.pack(pady=20)
        self.input_text_box.bind('<Return>', self.on_input_text_enter)
        self.input_text_box.bind('<Key>', self.on_input_text)

        # create result label
        self.result_label = tk.Label(master, text="Type the above text and press Enter to calculate your typing speed.",
                                     font=("Arial", 12))
        self.result_label.pack(pady=20)

    def on_input_text_enter(self, event):
        input_text = self.input_text_box.get()
        if input_text == self.sample_text:
            end_time = time.time()
            time_taken = end_time - self.start_time
            words_per_second = len(input_text.split()) / time_taken
            self.words_per_minute = int(words_per_second * 60)
            self.result_label.configure(text=f"You typed {self.words_per_minute} words per minute.")
        else:
            self.result_label.configure(text="You did not type the correct text. Please try again.")
        self.input_text_box.delete(0, tk.END)
        self.start_time = None
        self.words_per_minute = 0

    def on_input_text(self, event):
        if self.start_time is None:
            self.start_time = time.time()


if __name__ == '__main__':
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()
