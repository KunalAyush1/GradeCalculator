from statistics import compute_mean_and_std
from grading_policy import get_relative_grading_policy
from grading_engine import assign_grade
from input_layer import extract_marks_from_csv


def get_manual_marks_with_count() -> list:
    """
    Collects marks manually by first asking number of students.
    """
    try:
        n = int(input("Enter number of students: ").strip())
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Invalid number of students.")
        return None

    marks = []
    for i in range(1, n + 1):
        try:
            m = float(input(f"Enter marks for student {i}: ").strip())
            marks.append(m)
        except ValueError:
            print("Invalid marks entered.")
            return None

    return marks


def main():
    print("===== Grade Calculator v0.0.1 =====\n")
    print("Choose input mode:")
    print("1. CSV file (full class)")
    print("2. Manual entry (full class)")
    print("3. Single-student grading (known Mean & SD)")

    choice = input("\nEnter choice (1/2/3): ").strip()

    policy = get_relative_grading_policy()

    
    if choice == "1":
        file_path = input("Enter path to CSV file: ").strip()
        try:
            marks = extract_marks_from_csv(file_path)
            mean, std_dev = compute_mean_and_std(marks)
        except Exception as e:
            print("Error:", e)
            return

        print("\nGrades")
        print("------")
        for idx, m in enumerate(marks, start=1):
            grade, points = assign_grade(m, mean, std_dev, policy)
            print(f"Student {idx:02d}: Marks = {m:.2f} → Grade = {grade}, Points = {points}")

    
    elif choice == "2":
        marks = get_manual_marks_with_count()
        if marks is None:
            return

        try:
            mean, std_dev = compute_mean_and_std(marks)
        except Exception as e:
            print("Error:", e)
            return

        print("\nGrades")
        print("------")
        for idx, m in enumerate(marks, start=1):
            grade, points = assign_grade(m, mean, std_dev, policy)
            print(f"Student {idx:02d}: Marks = {m:.2f} → Grade = {grade}, Points = {points}")


   
    elif choice == "3":
        try:
            mean = float(input("Enter class mean: ").strip())
            std_dev = float(input("Enter class standard deviation: ").strip())
            marks = float(input("Enter student's marks: ").strip())
            if std_dev < 0:
                raise ValueError
        except ValueError:
            print("Invalid input.")
            return

        grade, points = assign_grade(marks, mean, std_dev, policy)

        print("\nResult")
        print("------")
        print(f"Marks : {marks:.2f}")
        print(f"Grade : {grade}")
        print(f"Points: {points}")

    else:
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    main()