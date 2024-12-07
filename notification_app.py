import tkinter as tk
from tkinter import messagebox
from plyer import notification
from datetime import datetime, timedelta
from threading import Timer

class NotificationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notification App")
        self.root.geometry("400x300")

        # Title label and entry
        self.title_label = tk.Label(root, text="Notification Title:")
        self.title_label.pack(pady=5)
        self.title_entry = tk.Entry(root, width=50)
        self.title_entry.pack(pady=5)

        # Message label and entry
        self.message_label = tk.Label(root, text="Notification Message:")
        self.message_label.pack(pady=5)
        self.message_entry = tk.Entry(root, width=50)
        self.message_entry.pack(pady=5)

        # Time label and entry
        self.time_label = tk.Label(root, text="Time (in seconds):")
        self.time_label.pack(pady=5)
        self.time_entry = tk.Entry(root, width=50)
        self.time_entry.pack(pady=5)

        # Submit button
        self.submit_button = tk.Button(root, text="Set Notification", command=self.set_notification)
        self.submit_button.pack(pady=10)

        # Notifications list label
        self.notifications_label = tk.Label(root, text="Scheduled Notifications:")
        self.notifications_label.pack(pady=5)

        # Notifications list box
        self.notifications_listbox = tk.Listbox(root, width=50, height=10)
        self.notifications_listbox.pack(pady=5)

    def set_notification(self):
        title = self.title_entry.get()
        message = self.message_entry.get()
        try:
            delay = int(self.time_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Time must be a number.")
            return

        if not title or not message or delay <= 0:
            messagebox.showerror("Invalid Input", "All fields must be valid and time must be positive.")
            return

        notification_time = datetime.now() + timedelta(seconds=delay)
        self.notifications_listbox.insert(tk.END, f"{notification_time.strftime('%H:%M:%S')} - {title}: {message}")

        Timer(delay, self.send_notification, args=(title, message)).start()
        messagebox.showinfo("Success", "Notification set successfully!")

    def send_notification(self, title, message):
        notification.notify(
            title=title,
            message=message,
            app_name="Notification App"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = NotificationApp(root)
    root.mainloop()
