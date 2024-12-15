import tkinter as tk

class ProcessManager:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.entries = []

    def create_process_entries(self, n):
        """Tạo các mục nhập tiến trình."""
        self.clear()
        for i in range(n):
            tk.Label(self.parent_frame, text=f"Process {i + 1} Arrival:", bg="#e8f2ff").grid(row=i, column=0, sticky="e")
            arrival_entry = tk.Entry(self.parent_frame)
            arrival_entry.grid(row=i, column=1)
            tk.Label(self.parent_frame, text=f"Process {i + 1} Burst:", bg="#e8f2ff").grid(row=i, column=2, sticky="e")
            burst_entry = tk.Entry(self.parent_frame)
            burst_entry.grid(row=i, column=3)
            self.entries.append((arrival_entry, burst_entry))

    def get_process_data(self):
        """Trích xuất dữ liệu từ các mục nhập."""
        try:
            arrival_times = [int(entry[0].get()) for entry in self.entries]
            burst_times = [int(entry[1].get()) for entry in self.entries]
        except ValueError:
            tk.messagebox.showerror("Input Error", "All inputs must be integers.")
            return None, None
        return arrival_times, burst_times

    def clear(self):
        """Xóa dữ liệu cũ."""
        for widget in self.parent_frame.winfo_children():
            widget.destroy()
        self.entries = []
