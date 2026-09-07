def enroll_student(*students, min_grade=50, department="Computer Science", **kwargs):
    print(f"Min grade: {min_grade}")
    print(f"Department: {department}")

    print(("\nEnrolled Students: "))
    for student in students:
        print(f" - {student}")

        print(f"\nAdditional Information:")
    for key, value in kwargs.items():
        print(f"{key}:{value}")
    print("---End of enrollment---")

def main():
    enroll_student("Alice", "Bob")
    print("------------------------")

    enroll_student("Helen", "Carol", "Nick", academic_year=2026, semester="Fall")
    print("------------------------")

    enroll_student("John", "Dave", min_grade=70, department="Maths", academic_year=2026, semester="Spring")


if __name__ == "__main__":
    main()