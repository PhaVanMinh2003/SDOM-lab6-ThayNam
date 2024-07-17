import tkinter as tk
from tkinter import ttk

# Hàm khởi động GUI
def create_gui():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("FPS Recorder")
    root.geometry("600x300")
    root.configure(bg="lightblue")  # Đặt màu nền tùy chỉnh

    # Thêm nhãn tiêu đề
    title_label = tk.Label(root, text="FPS Recorder", font=("Arial", 24), bg="lightblue")
    title_label.pack(pady=20)

    # Thêm khung cho đầu vào FPS và nhãn
    fps_frame = tk.Frame(root, bg="lightblue")
    fps_frame.pack(pady=10)
    fps_label = tk.Label(fps_frame, text="FPS:", bg="lightblue")
    fps_label.pack(side="left", padx=5)
    fps_entry = tk.Entry(fps_frame)
    fps_entry.pack(side="left", padx=5)

    # Thêm các nút "Tạm dừng", "Bắt đầu" và "Kết thúc"
    buttons_frame = tk.Frame(root, bg="lightblue")
    buttons_frame.pack(pady=10)
    pause_button = tk.Button(buttons_frame, text="Tạm dừng")
    pause_button.pack(side="left", padx=5)
    start_button = tk.Button(buttons_frame, text="Bắt đầu")
    start_button.pack(side="left", padx=5)
    end_button = tk.Button(buttons_frame, text="Kết thúc")
    end_button.pack(side="left", padx=5)

    # Thêm nhãn trạng thái
    status_label = tk.Label(root, text="Trạng thái: Chưa ghi", font=("Arial", 12), bg="lightblue")
    status_label.pack(pady=20)

    # Bắt đầu vòng lặp sự kiện
    root.mainloop()

# Gọi hàm khởi động GUI
if __name__ == "__main__":
    create_gui()
