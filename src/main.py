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
