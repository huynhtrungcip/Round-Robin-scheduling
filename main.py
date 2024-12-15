import tkinter as tk
from process_manager import ProcessManager
from scheduler import RoundRobinScheduler
from gantt_chart_display import GanttChartDisplay
from result_display import ResultDisplay

class RoundRobinApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Round Robin CPU Scheduling")
        self.root.geometry("900x800")
        self.root.configure(bg="#e8f2ff")

        # Tạo các khung giao diện chính
        self.process_frame = tk.Frame(self.root, bg="#e8f2ff")
        self.process_frame.grid(row=2, column=1, sticky="nsew")
        self.result_text = tk.Text(self.root, height=10, font=("Courier New", 10), bg="#e8f2ff", wrap="none")
        self.result_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        self.gantt_frame = tk.Frame(self.root, bg="#e8f2ff")
        self.gantt_frame.grid(row=4, column=0, columnspan=3, sticky="nsew")

        # Khởi tạo các thành phần chức năng
        self.gantt_chart = GanttChartDisplay(self.gantt_frame)
        self.result_display = ResultDisplay(self.result_text)
        self.process_manager = ProcessManager(self.process_frame)
        self.scheduler = RoundRobinScheduler()

        # Tạo giao diện người dùng
        self.setup_ui()

    def setup_ui(self):
        """Thiết lập giao diện chính."""
        input_frame = tk.Frame(self.root, bg="#e8f2ff")
        input_frame.grid(row=1, column=1, pady=5, sticky="nsew")
        tk.Label(input_frame, text="Number of Processes:", bg="#e8f2ff").grid(row=0, column=0, padx=5, sticky="e")
        self.process_count_entry = tk.Entry(input_frame)
        self.process_count_entry.grid(row=0, column=1, padx=5)
        tk.Label(input_frame, text="Time Quantum:", bg="#e8f2ff").grid(row=1, column=0, padx=5, sticky="e")
        self.time_quantum_entry = tk.Entry(input_frame)
        self.time_quantum_entry.grid(row=1, column=1, padx=5)

        # Nút cài đặt và reset
        tk.Button(input_frame, text="Set Processes", bg="#e8f2ff", command=self.set_processes).grid(row=2, column=0, pady=5)
        tk.Button(input_frame, text="Reset", bg="#e8f2ff", command=self.reset).grid(row=2, column=1, pady=5)

    def set_processes(self):
        """Cài đặt số lượng tiến trình và time quantum."""
        try:
            n = int(self.process_count_entry.get())
            quantum = int(self.time_quantum_entry.get())
            if n <= 0 or quantum <= 0:
                raise ValueError("Number of processes and quantum must be positive integers.")
        except ValueError as e:
            tk.messagebox.showerror("Input Error", str(e))
            return

        self.scheduler.set_parameters(n, quantum)
        self.process_manager.create_process_entries(n)

    def calculate_rr(self):
        """Thực hiện thuật toán Round Robin."""
        arrival_times, burst_times = self.process_manager.get_process_data()
        if not arrival_times or not burst_times:
            return

        results = self.scheduler.calculate(arrival_times, burst_times)
        self.result_display.display_results(results)
        self.gantt_chart.display(results["gantt_chart"])

    def reset(self):
        """Đặt lại giao diện về trạng thái ban đầu."""
        self.process_manager.clear()
        self.result_display.clear()
        self.gantt_chart.clear()
        self.process_count_entry.delete(0, tk.END)
        self.time_quantum_entry.delete(0, tk.END)

# Khởi chạy ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    app = RoundRobinApp(root)
    root.mainloop()
