
from student import Student


def add_student(students: list, student_id: str, name: str, age: int, grade: str) -> list:
    """Thêm sinh viên mới vào danh sách."""
    for s in students:
        if s.student_id == student_id:
            print(f"Ma sinh vien {student_id} da ton tai!")
            return students

    new_student = Student(student_id, name, age, grade)
    students.append(new_student)
    print(f"Da them sinh vien: {new_student}")
    return students


def main():
    print("=" * 50)
    print("STUDENT MANAGER - DevOps Lab 5")
    print("=" * 50)

    students = [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21"),
    ]

    students = add_student(
        students, "SV004", "Pham Thi D", 22, "K19"
    )

    for student in students:
        print(f"  {student}")

    print(f"\nTotal: {len(students)} students")


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