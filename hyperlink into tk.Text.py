import tkinter as tk
import webbrowser

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hyperlinks Example")
        self.geometry(f"300x300+200+200")

        # Create text widget
        self.text_widget = tk.Text(self, wrap="word", font=("Arial", 12), padx=10, pady=10, height=100)
        self.text_widget.pack(expand=True, fill="both")

        # Insert some text with hyperlinks
        self.insert_hyperlink("Link1", "Google", "https://www.google.de")
        self.text_widget.insert("end", "\n")
        
        self.insert_hyperlink("Link2", "Yandex", "https://www.ya.ru")
        self.text_widget.insert("end", "\n")
        
        self.insert_hyperlink("Link3", "Gmail", "https://www.gmail.com")
        self.text_widget.insert("end", "\n")

    def insert_hyperlink(self, tag_name, hyperlink_text, hyperlink_url):
        """
        The function inserts a text in a tkinter text box and converts it to a hyperlink using special tags and event functions.

        :param tag_name: an uniq tag name for each hyperlink is nessesary
        :param hyperlink_text: Text
        :param hyperlink_url: a Weblink or a file link
        """
        
        # Get current cursor position
        cursor_pos = self.text_widget.index(tk.INSERT)

        # Insert hyperlink text
        self.text_widget.insert(tk.INSERT, hyperlink_text)

        # Add hyperlink tag to text
        start_idx = cursor_pos
        end_idx = f"{cursor_pos}+{len(hyperlink_text)}c"
        self.text_widget.tag_add(tag_name, start_idx, end_idx)

        # Configure hyperlink tag to be clickable
        self.text_widget.tag_configure(tag_name, foreground="blue", underline=True)

        # cursor changes to a hand when over a hyperlink
        def on_hyperlink(event):
            self.text_widget.configure(cursor="hand2")

        # cursor changes back when off a hyperlink
        def off_hyperlink(event):
            self.text_widget.configure(cursor="")

        # Define hyperlink click event
        def on_hyperlink_click(event):
            webbrowser.open(hyperlink_url)

        # Bind an event function to change cursor to hand when over hyper link text
        self.text_widget.tag_bind(tag_name, "<Enter>", on_hyperlink)
        self.text_widget.tag_bind(tag_name, "<Leave>", off_hyperlink)

        # Bind a hyperlink tag to a click event
        self.text_widget.tag_bind(tag_name, "<Button-1>", on_hyperlink_click)


if __name__ == "__main__":
    app = App()
    app.mainloop()
