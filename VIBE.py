# Yazid Athmani
# CIS261
# WK10 Vibe Coding

import os

FILENAME = "student_grades.txt"

def load_records(filename):
    records = []
    if not os.path.exists(filename):
        return records
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) == 7:
                    try:
                        record = {
                            "name": parts[0],
                            "id": parts[1],
                            "test1": float(parts[2]),
                            "test2": float(parts[3]),
                            "test3": float(parts[4]),
                            "average": float(parts[5]),
                            "grade": parts[6]
                        }
                        records.append(record)
                    except ValueError:
                        continue
        print(f"Loaded {len(records)} record(s) from '{filename}'.")
    except OSError as error:
        print(f"Error loading records: {error}")
    return records

def save_records(filename, records):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for record in records:
                line = f"{record['name']}|{record['id']}|{record['test1']:.2f}|{record['test2']:.2f}|{record['test3']:.2f}|{record['average']:.2f}|{record['grade']}\n"
                file.write(line)
        print(f"Saved {len(records)} record(s) to '{filename}'.")
    except OSError as error:
        print(f"Error saving records: {error}")

def calculate_average(test1, test2, test3):
    return round((test1 + test2 + test3) / 3.0, 2)

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def add_student(records):
    print("\n" + "=" * 60)
    print("ADD NEW STUDENT")
    print("=" * 60)
    print("(Type 'ESC' at any prompt to return to menu)\n")
    
    name = input("Student name: ").strip()
    if name.upper() == "ESC":
        return
    if not name:
        print("Name cannot be empty.")
        return
    
    student_id = input("Student ID: ").strip()
    if student_id.upper() == "ESC":
        return
    if not student_id:
        print("Student ID cannot be empty.")
        return
    
    try:
        test1 = float(input("Test 1 score (0-100): "))
        test2 = float(input("Test 2 score (0-100): "))
        test3 = float(input("Test 3 score (0-100): "))
    except ValueError:
        print("Invalid input. Please enter numeric scores.")
        return
    
    average = calculate_average(test1, test2, test3)
    grade = calculate_grade(average)
    
    record = {
        "name": name,
        "id": student_id,
        "test1": test1,
        "test2": test2,
        "test3": test3,
        "average": average,
        "grade": grade
    }
    records.append(record)
    
    print(f"\n✓ Added student: {name} (ID: {student_id})")
    print(f"  Average: {average:.2f} | Grade: {grade}")
    print("=" * 60)

def display_all_students(records):
    print("\n" + "=" * 80)
    print("ALL STUDENT RECORDS")
    print("=" * 80)
    
    if len(records) == 0:
        print("No student records found.")
    else:
        print(f"{'#':<3} {'Name':<20} {'ID':<10} {'Test1':>8} {'Test2':>8} {'Test3':>8} {'Average':>10} {'Grade':>6}")
        print("-" * 80)
        for i, record in enumerate(records, 1):
            print(f"{i:<3} {record['name']:<20} {record['id']:<10} {record['test1']:>8.2f} {record['test2']:>8.2f} {record['test3']:>8.2f} {record['average']:>10.2f} {record['grade']:>6}")
        print("-" * 80)
        print(f"Total students: {len(records)}")
    print("=" * 80)

def display_statistics(records):
    print("\n" + "=" * 60)
    print("CLASS STATISTICS")
    print("=" * 60)
    
    if len(records) == 0:
        print("No records available to calculate statistics.")
    else:
        averages = [record["average"] for record in records]
        highest = max(averages)
        lowest = min(averages)
        class_avg = round(sum(averages) / len(averages), 2)
        
        highest_students = [record["name"] for record in records if record["average"] == highest]
        lowest_students = [record["name"] for record in records if record["average"] == lowest]
        
        grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        for record in records:
            grade_counts[record["grade"]] += 1
        
        print(f"Class Average:     {class_avg:.2f}")
        print(f"Highest Average:   {highest:.2f} ({', '.join(highest_students)})")
        print(f"Lowest Average:    {lowest:.2f} ({', '.join(lowest_students)})")
        print("\nGrade Distribution:")
        for grade in ["A", "B", "C", "D", "F"]:
            if grade_counts[grade] > 0:
                print(f"  {grade}: {grade_counts[grade]} student(s)")
    print("=" * 60)

def search_student(records):
    print("\n" + "=" * 60)
    print("SEARCH STUDENT BY NAME")
    print("=" * 60)
    
    if len(records) == 0:
        print("No student records available to search.")
        return
    
    query = input("Enter student name to search: ").strip()
    if not query:
        print("Search query cannot be empty.")
        return
    
    matches = [record for record in records if query.lower() in record["name"].lower()]
    
    if len(matches) == 0:
        print(f"No students found matching '{query}'.")
    else:
        print(f"\nFound {len(matches)} student(s) matching '{query}':")
        print("-" * 60)
        for record in matches:
            print(f"  Name: {record['name']}")
            print(f"  ID: {record['id']}")
            print(f"  Scores: {record['test1']:.2f}, {record['test2']:.2f}, {record['test3']:.2f}")
            print(f"  Average: {record['average']:.2f} | Grade: {record['grade']}")
            print("-" * 60)
    print("=" * 60)

def display_menu():
    print("\n" + "=" * 60)
    print("STUDENT GRADE CALCULATOR")
    print("=" * 60)
    print("1. Add New Student")
    print("2. Display All Students")
    print("3. View Class Statistics")
    print("4. Search Student by Name")
    print("5. Save and Exit")
    print("ESC. Exit without saving")
    print("=" * 60)

def main():
    print("\n" + "=" * 60)
    print("WELCOME TO THE STUDENT GRADE CALCULATOR")
    print("=" * 60)
    print("Instructions:")
    print("- Add students with their three test scores")
    print("- Grades are calculated automatically (A=90+, B=80+, C=70+, D=60+, F=below 60)")
    print("- Type 'ESC' to exit")
    print("=" * 60)
    
    records = load_records(FILENAME)
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == "1":
            add_student(records)
        elif choice == "2":
            display_all_students(records)
        elif choice == "3":
            display_statistics(records)
        elif choice == "4":
            search_student(records)
        elif choice == "5":
            save_records(FILENAME, records)
            print("\nThank you for using the Student Grade Calculator!")
            break
        elif choice == "ESC":
            print("\nExiting without saving changes.")
            print("Thank you for using the Student Grade Calculator!")
            break
        else:
            print("Invalid choice. Please select 1-5 or ESC.")

if __name__ == "__main__":
    main()