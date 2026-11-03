"""Student Manager - DevOps Lab 5"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)---)
from student import Student

def main():
    students = []
    print("=== CHUONG TRINH QUAN LY SINH VIEN ===")
    s1 = Student("SV01", "Nguyen Van A", 20, "KTPM01")
    students.append(s1)
    while True:
        print("\n--- MENU ---")
        print("1. Xem danh sach sinh vien")
        print("0. Thoat")
        choice = input("Chon: ").strip()
        if choice == "1":
            for s in students: print(s)
        elif choice == "0":
            break

if __name__ == "__main__":
    main()
def search_student(students: list, keyword: str) -> list:
    """Tìm kiếm sinh viên theo tên hoặc mã.

    Args:
        students: Danh sách sinh viên
        keyword: Từ khóa tìm kiếm

    Returns:
        Danh sách sinh viên khớp với từ khóa
    """
    results = []
    keyword_lower = keyword.lower()

    for s in students:
        if keyword_lower in s.name.lower() or keyword_lower in s.student_id.lower():
            results.append(s)

    if results:
        print(f"🔍 Tìm thấy {len(results)} sinh viên với từ khóa '{keyword}':")
        for s in results:
            print(f"  {s}")
    else:
        print(f"❌ Không tìm thấy sinh viên nào với từ khóa '{keyword}'")

    return results