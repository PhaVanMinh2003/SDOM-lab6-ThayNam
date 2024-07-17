import tkinter as tk
from tkinter import ttk

def submit_data():
    # Lấy giá trị từ các trường nhập
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    job_title = entry_job_title.get()
    age = entry_age.get()
    nationality = entry_nationality.get()

    # Lấy giá trị từ các hộp kiểm và hộp quay số
    registered = chk_registered.get()
    courses_completed = spin_courses_completed.get()
    semester = spin_semester.get()

    # Kiểm tra trạng thái của hộp kiểm Điều khoản và Điều kiện
    if chk_terms_accepted.get() == 1:
        terms_accepted = "Đã chấp nhận"
    else:
        terms_accepted = "Chưa chấp nhận"

    # Hiển thị thông tin được in ra bảng điều khiển
    print("Thông tin người dùng:")
    print(f"Tên: {first_name}")
    print(f"Họ: {last_name}")
    print(f"Chức danh: {job_title}")
    print(f"Tuổi: {age}")
    print(f"Quốc tịch: {nationality}")
    print()
    print("Thông tin đăng ký:")
    print(f"Trạng thái đăng ký: {'Đã đăng ký' if registered else 'Chưa đăng ký'}")
    print(f"Số khóa học đã hoàn thành: {courses_completed}")
    print(f"Học kỳ: {semester}")
    print()
    print(f"Điều khoản và Điều kiện: {terms_accepted}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Đăng ký thông tin")
root.geometry("500x400")

# Khung thông tin người dùng
frame_user_info = ttk.LabelFrame(root, text="Thông tin người dùng")
frame_user_info.pack(padx=10, pady=10, fill="both", expand=True)

tk.Label(frame_user_info, text="Tên:").grid(row=0, column=0, sticky="w")
entry_first_name = ttk.Entry(frame_user_info)
entry_first_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_user_info, text="Họ:").grid(row=1, column=0, sticky="w")
entry_last_name = ttk.Entry(frame_user_info)
entry_last_name.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_user_info, text="Chức danh:").grid(row=2, column=0, sticky="w")
entry_job_title = ttk.Entry(frame_user_info)
entry_job_title.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_user_info, text="Tuổi:").grid(row=3, column=0, sticky="w")
entry_age = ttk.Entry(frame_user_info)
entry_age.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame_user_info, text="Quốc tịch:").grid(row=4, column=0, sticky="w")
entry_nationality = ttk.Entry(frame_user_info)
entry_nationality.grid(row=4, column=1, padx=5, pady=5)

# Khung đăng ký
frame_registration = ttk.LabelFrame(root, text="Đăng ký")
frame_registration.pack(padx=10, pady=10, fill="both", expand=True)

chk_registered = tk.IntVar()
tk.Checkbutton(frame_registration, text="Đã đăng ký", variable=chk_registered).grid(row=0, column=0, sticky="w")

tk.Label(frame_registration, text="Số khóa học đã hoàn thành:").grid(row=1, column=0, sticky="w")
spin_courses_completed = tk.Spinbox(frame_registration, from_=0, to=10)
spin_courses_completed.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_registration, text="Học kỳ:").grid(row=2, column=0, sticky="w")
spin_semester = tk.Spinbox(frame_registration, from_=1, to=8)
spin_semester.grid(row=2, column=1, padx=5, pady=5)

# Khung Điều khoản và Điều kiện
frame_terms_conditions = ttk.LabelFrame(root, text="Điều khoản và Điều kiện")
frame_terms_conditions.pack(padx=10, pady=10, fill="both", expand=True)

chk_terms_accepted = tk.IntVar()
tk.Checkbutton(frame_terms_conditions, text="Tôi chấp nhận các Điều khoản và Điều kiện", variable=chk_terms_accepted).grid(row=0, column=0, sticky="w")

# Nút Gửi
btn_submit = ttk.Button(root, text="Gửi", command=submit_data)
btn_submit.pack(pady=10)

# Bắt đầu vòng lặp sự kiện
root.mainloop()