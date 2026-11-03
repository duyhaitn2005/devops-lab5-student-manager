"""
Student Manager - DevOps Lab 5
Module: Main Application
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from student import Student

def search_student(students: list, keyword: str) -> list:
    """Tìm kiếm sinh viên theo tên hoặc mã.

    Args:
        students: Danh sách sinh viên
        keyword: Từ khóa tìm kiếm

    Returns:
        list: Danh sách sinh viên khớp với từ khóa
    """
    keyword_lower = keyword.lower().strip()
    return [
        s for s in students 
        if keyword_lower in s.student_id.lower() or keyword_lower in s.name.lower()
    ]

def main():
    students = []
    print("=== CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN (DevOps Lab 5) ===")
    
    s1 = Student("SV01", "Nguyen Van A", 20, "KTPM01")
    s2 = Student("SV02", "Tran Thi B", 21, "CNTT02")
    students.extend([s1, s2])

    while True:
        print("\n--- MENU ---")
        print("1. Xem danh sách sinh viên")
        print("2. Thêm sinh viên")
        print("3. Tìm kiếm sinh viên")
        print("0. Thoát")
        
        choice = input("Nhập lựa chọn của bạn: ").strip()
        
        if choice == "1":
            print("\n--- Danh sách sinh viên ---")
            if not students:
                print("Danh sách trống.")
            else:
                for s in students:
                    print(s)
        elif choice == "2":
            sid = input("Nhập mã sinh viên: ").strip()
            name = input("Nhập họ tên: ").strip()
            try:
                age = int(input("Nhập tuổi: ").strip())
            except ValueError:
                print("Tuổi phải là số nguyên!")
                continue
            grade = input("Nhập lớp: ").strip()
            students.append(Student(sid, name, age, grade))
            print("=> Thêm sinh viên thành công!")
        elif choice == "3":
            kw = input("Nhập tên hoặc mã SV cần tìm: ").strip()
            results = search_student(students, kw)
            if results:
                print(f"=> Tìm thấy {len(results)} kết quả:")
                for r in results:
                    print(r)
            else:
                print("Không tìm thấy sinh viên phù hợp.")
        elif choice == "0":
            print("Thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()