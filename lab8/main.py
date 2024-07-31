import tkinter as tk
from tkinter import filedialog, messagebox, font, simpledialog

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("800x600")

        self.text_area = tk.Text(self.root, undo=True, wrap='none')
        self.text_area.pack(fill=tk.BOTH, expand=1)
        
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)
        self.file_menu.add_command(label="New Window", accelerator="Ctrl+Shift+N", command=self.new_window)
        self.file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)
        self.file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        self.file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Page Setup", command=self.page_setup)
        self.file_menu.add_command(label="Print", accelerator="Ctrl+P", command=self.print_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=self.exit_app)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=self.paste_text)
        self.edit_menu.add_command(label="Delete", command=self.delete_text)

        self.format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)
        self.format_menu.add_command(label="Word Wrap", command=self.toggle_word_wrap)
        self.format_menu.add_command(label="Font", command=self.change_font)

        self.view_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="View", menu=self.view_menu)
        self.view_menu.add_command(label="Zoom In", accelerator="Ctrl+Up", command=self.zoom_in)
        self.view_menu.add_command(label="Zoom Out", accelerator="Ctrl+Down", command=self.zoom_out)
        self.view_menu.add_command(label="Status Bar", command=self.toggle_status_bar)

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="View Help", command=self.view_help)
        self.help_menu.add_command(label="Send Feedback", command=self.send_feedback)
        self.help_menu.add_command(label="About Notepad", command=self.about_notepad)

        self.status_bar_visible = True
        self.create_status_bar()
        self.bind_shortcuts()

    def bind_shortcuts(self):
        self.root.bind_all("<Control-n>", lambda event: self.new_file())
        self.root.bind_all("<Control-N>", lambda event: self.new_window())
        self.root.bind_all("<Control-o>", lambda event: self.open_file())
        self.root.bind_all("<Control-s>", lambda event: self.save_file())
        self.root.bind_all("<Control-S>", lambda event: self.save_as_file())
        self.root.bind_all("<Control-p>", lambda event: self.print_file())
        self.root.bind_all("<Control-q>", lambda event: self.exit_app())
        self.root.bind_all("<Control-z>", lambda event: self.text_area.edit_undo())
        self.root.bind_all("<Control-y>", lambda event: self.text_area.edit_redo())
        self.root.bind_all("<Control-x>", lambda event: self.cut_text())
        self.root.bind_all("<Control-c>", lambda event: self.copy_text())
        self.root.bind_all("<Control-v>", lambda event: self.paste_text())
        self.root.bind_all("<Control-Up>", lambda event: self.zoom_in())
        self.root.bind_all("<Control-Down>", lambda event: self.zoom_out())

    def create_status_bar(self):
        self.status_bar = tk.Label(self.root, text="Status Bar", anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        self.update_status_bar()

    def update_status_bar(self):
        if self.status_bar_visible:
            line, col = self.text_area.index(tk.INSERT).split('.')
            self.status_bar.config(text=f"Line: {line} | Column: {col}")

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def new_window(self):
        new_root = tk.Tk()
        Notepad(new_root)
        new_root.mainloop()

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", 
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        if hasattr(self, 'file_path') and self.file_path:
            with open(self.file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            self.file_path = file_path
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def page_setup(self):
        # Page setup logic here
        messagebox.showinfo("Page Setup", "Page setup is not implemented yet.")

    def print_file(self):
        # Print file logic here
        messagebox.showinfo("Print", "Print is not implemented yet.")

    def exit_app(self):
        self.root.quit()

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

    def delete_text(self):
        self.text_area.delete("sel.first", "sel.last")

    def toggle_word_wrap(self):
        current_wrap = self.text_area.cget("wrap")
        if current_wrap == "none":
            self.text_area.config(wrap="word")
        else:
            self.text_area.config(wrap="none")

    def change_font(self):
        font_families = list(font.families())
        font_family = simpledialog.askstring("Font Family", "Enter font family:")
        font_size = simpledialog.askinteger("Font Size", "Enter font size:")
        if font_family and font_size:
            self.text_area.config(font=(font_family, font_size))

    def zoom_in(self):
        current_font = self.text_area.cget("font")
        font_name, font_size = current_font.split()
        new_size = int(font_size) + 2
        self.text_area.config(font=(font_name, new_size))
        self.update_status_bar()

    def zoom_out(self):
        current_font = self.text_area.cget("font")
        font_name, font_size = current_font.split()
        new_size = int(font_size) - 2
        self.text_area.config(font=(font_name, new_size))
        self.update_status_bar()

    def toggle_status_bar(self):
        self.status_bar_visible = not self.status_bar_visible
        if self.status_bar_visible:
            self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        else:
            self.status_bar.pack_forget()

    def view_help(self):
        # View help logic here
        messagebox.showinfo("Help", "Help information is not implemented yet.")

    def send_feedback(self):
        # Send feedback logic here
        messagebox.showinfo("Send Feedback", "Feedback feature is not implemented yet.")

    def about_notepad(self):
        messagebox.showinfo("About Notepad", "Notepad v1.0\nAuthor: Your Name")

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
