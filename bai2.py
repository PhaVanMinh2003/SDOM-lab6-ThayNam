import tkinter as tk
from tkinter import ttk

def create_gui():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Ứng dụng Quét")
    root.geometry("800x500")
    root.configure(bg="lightgrey")  # Đặt màu nền tùy chỉnh

    # Tạo khung chính
    main_frame = tk.Frame(root, bg="lightgrey")
    main_frame.pack(fill="both", expand=True)

    # Tạo thanh bên
    sidebar_frame = tk.Frame(main_frame, width=200, bg="lightblue", relief="sunken", borderwidth=2)
    sidebar_frame.pack(side="left", fill="y")

    # Thêm các nhãn vào thanh bên
    tk.Label(sidebar_frame, text="Trạng thái", bg="lightblue", font=("Arial", 14)).pack(pady=10)
    tk.Label(sidebar_frame, text="Cập nhật", bg="lightblue", font=("Arial", 14)).pack(pady=10)
    tk.Button(sidebar_frame, text="Quét ngay", bg="lightgreen", font=("Arial", 14)).pack(pady=10)

    # Tạo khu vực chính
    content_frame = tk.Frame(main_frame, bg="white", relief="sunken", borderwidth=2)
    content_frame.pack(side="left", fill="both", expand=True)

    # Thêm nhãn tiêu đề và phụ đề vào khu vực chính
    tk.Label(content_frame, text="Trình Quét Virus", bg="white", font=("Arial", 24)).pack(pady=20)
    tk.Label(content_frame, text="Bảo vệ máy tính của bạn khỏi các mối đe dọa", bg="white", font=("Arial", 14)).pack(pady=10)

    # Thêm các nút chức năng vào khu vực chính
    tk.Button(content_frame, text="Quét nhanh", bg="lightblue", font=("Arial", 14)).pack(pady=10)
    tk.Button(content_frame, text="Bảo vệ web", bg="lightblue", font=("Arial", 14)).pack(pady=10)

    # Thêm nhãn trạng thái
    status_label = tk.Label(root, text="Trạng thái hiện tại: Đang chờ", font=("Arial", 12), bg="lightgrey")
    status_label.pack(side="bottom", fill="x")

    # Bắt đầu vòng lặp sự kiện
    root.mainloop()

# Gọi hàm khởi động GUI
if __name__ == "__main__":
    create_gui()
