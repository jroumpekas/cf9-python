from ast import main


def upscale_grades(students_grades):
 return {name : (grade + 1 if grade <= 9 else grade) for name, grade in students_grades.items()}

def filter_grades(students_grades):
   return {name: grade for name, grade in students_grades.items() if grade >= 5}

def categorize_grades(students_grades):
   passed = {name : grade for name, grade in students_grades.items() if 5 <= grade <= 10}
   failed = {name : grade for name, grade in students_grades.items() if grade < 5}
   honors = {name : grade for name, grade in students_grades.items() if grade == 10}
   return passed, failed, honors

def calculate_average(students_grades):
   if students_grades:
      return sum(students_grades.values()) / len(students_grades)
   return 0
  


def main():
    """
    Main function to demonstrate the usage of dictionary comprehensions 
    and map/filter-like operations to transform and filter a list of student grades.
    """
    # Original dictionary of students with their grades
    students_grades = {
        "Alice": 7,
        "Bob": 5,
        "Charlie": 9,
        "David": 10,
        "Eve": 3,
        "Frank": 6,
        "Grace": 8,
        "Heidi": 4,
        "Ivan": 10,
        "Judy": 2
    }
 
if __name__ == "__main__":
   main() 