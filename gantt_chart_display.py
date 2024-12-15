import tkinter as tk

class GanttChartDisplay:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame

    def display(self, gantt_chart):
        """Vẽ biểu đồ Gantt."""
        for widget in self.parent_frame.winfo_children():
            widget.destroy()
        canvas = tk.Canvas(self.parent_frame, bg="#fff", height=80)
        canvas.pack(fill="both", expand=True)
        start_x = 10
        for process_id, start, end in gantt_chart:
            duration = end - start
            canvas.create_rectangle(start_x, 10, start_x + 50 * duration, 50, fill="#5DADE2")
            canvas.create_text(start_x + 25 * duration, 30, text=f"P{process_id + 1}")
            start_x += 50 * duration

    def clear(self):
        """Xóa biểu đồ."""
        for widget in self.parent_frame.winfo_children():
            widget.destroy()
