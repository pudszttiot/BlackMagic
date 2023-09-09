import tkinter as tk
from tkinter import filedialog
import black
from io import StringIO

class BlackFormatterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Black Formatter")

        self.load_button = tk.Button(self.root, text="Load Python File", command=self.load_file)
        self.load_button.pack(pady=10)

        self.text_widget = tk.Text(self.root, wrap=tk.WORD)
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        self.format_button = tk.Button(self.root, text="Format Code", command=self.format_code)
        self.format_button.pack(pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            with open(file_path, "r") as file:
                original_code = file.read()
            self.text_widget.delete("1.0", tk.END)
            self.text_widget.insert("1.0", original_code)

    def format_code(self):
        original_code = self.text_widget.get("1.0", tk.END)
        formatted_code = self.format_with_black(original_code)
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", formatted_code)

    @staticmethod
    def format_with_black(code):
        try:
            formatted_output = StringIO()
            blackened_code = black.format_str(code, mode=black.FileMode(line_length=88))
            formatted_output.write(blackened_code)
            formatted_code = formatted_output.getvalue()
            return formatted_code
        except Exception as e:
            return f"Error formatting code: {e}"

if __name__ == "__main__":
    root = tk.Tk()
    app = BlackFormatterApp(root)
    root.mainloop()
