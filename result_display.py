class ResultDisplay:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def display_results(self, results):
        """Hiển thị kết quả."""
        self.text_widget.delete(1.0, tk.END)
        for process_id, data in enumerate(results["gantt_chart"], 1):
            self.text_widget.insert(tk.END, f"Process {process_id}: {data}\n")

    def clear(self):
        """Xóa hiển thị."""
        self.text_widget.delete(1.0, tk.END)
