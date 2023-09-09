import tkinter as tk
from tkinter import filedialog, scrolledtext
import black
from io import StringIO
from tkinter import ttk

class BlackFormatterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Black Formatter")
        
        # Apply a simple theme
        style = ttk.Style()
        style.theme_use("clam")

        self.frame1 = ttk.Frame(self.root)
        self.frame1.pack(padx=10, pady=10, fill="both", expand=True)

        self.load_button = ttk.Button(self.frame1, text="Load Python File", command=self.load_file)
        self.load_button.pack(pady=5, anchor="w")

        self.text_widget = scrolledtext.ScrolledText(self.frame1, wrap=tk.WORD)
        self.text_widget.pack(fill="both", expand=True)

        self.format_button = ttk.Button(self.frame1, text="Format Code", command=self.format_code)
        self.format_button.pack(pady=5, anchor="e")

        self.save_button = ttk.Button(self.frame1, text="Save Formatted Code", command=self.save_file)
        self.save_button.pack(pady=5, anchor="e")

        self.feedback_label = ttk.Label(self.root, text="", foreground="red")
        self.feedback_label.pack(pady=5)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            with open(file_path, "r") as file:
                original_code = file.read()
            self.text_widget.delete("1.0", tk.END)
            self.text_widget.insert("1.0", original_code)
            self.feedback_label.config(text="File loaded successfully.")

    def format_code(self):
        original_code = self.text_widget.get("1.0", tk.END)
        formatted_code = self.format_with_black(original_code)
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", formatted_code)
        self.feedback_label.config(text="Code formatted successfully.", foreground="green")

    def save_file(self):
        formatted_code = self.text_widget.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(formatted_code)
            self.feedback_label.config(text="File saved successfully.", foreground="green")

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
