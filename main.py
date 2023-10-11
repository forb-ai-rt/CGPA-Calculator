import streamlit as st

grade_to_point = {
    "O": 10,
    "A+": 9,
    "A": 8,
    "B+": 7,
    "B": 6,
    "C": 5,
}
grades = list(grade_to_point.keys())

def calculate_cgpa(grades, course_credits):
    total_credit_points = 0
    total_credits = 0

    for course, grade in grades.items():
        credit_points = get_credit_points(grade)
        credits = course_credits.get(course, 0)

        total_credit_points += credit_points * credits
        total_credits += credits

    if total_credits == 0:
        return 0

    cgpa = total_credit_points / total_credits
    return cgpa

def get_credit_points(grade):
    # Define your grade to credit point mapping here
    # For example:
    grade_points = {
        'A+': 4.0,
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'C-': 1.7,
        'D+': 1.3,
        'D': 1.0,
        'F': 0.0,
    }

    return grade_points.get(grade, 0.0)

def main():
    # Course grades as a dictionary
    grades = {
        'Math': 'A',
        'Science': 'B+',
        'History': 'A-',
        # Add more courses and grades here
    }

    # Course credits as a dictionary
    course_credits = {
        'Math': 4,
        'Science': 3,
        'History': 3,
        # Add more courses and credits here
    }

    cgpa = calculate_cgpa(grades, course_credits)
    print(f"Your CGPA is: {cgpa:.2f}")

if __name__ == "__main__":
    main()

def maximum_cgpa(course_data):
    total_credit_points = 0
    total_credits = 0

    for course in course_data:
        credit_points = grade_to_point.get(course["grade"], 0)
        credits = course["credit"]
        total_credit_points += credit_points * credits
        total_credits += credits

    # Calculate the maximum grade points for courses with grades from O to B+
    max_grade_points = 0
    for grade in grade_to_point.keys():
        if grade_to_point[grade] <= 7:  # Consider only grades from O to B+
            max_grade_points += grade_to_point[grade]

    if total_credits == 0:
        return 0

    # Calculate the maximum achievable CGPA
    max_cgpa = (total_credit_points + max_grade_points) / total_credits
    return max_cgpa

def main():
    st.title("CGPA Calculator")
    num_courses = st.number_input("Enter the number of courses you have taken:", min_value=0, step=1, value=0)

    course_data = []
    for i in range(num_courses):
        st.write(f"\nCourse {i+1}:")
        course_name = st.text_input(f"Enter the course name for Course {i+1}:")
        credit_key = f"credit_{i}"  # Create a unique key for each course's credit input
        credit = st.number_input("Enter the credit points (between 1 to 4):", min_value=1.0, max_value=4.0, step=1.0, value=1.0, key=credit_key)
        grade_key = f"grade_{i}"  # Create a unique key for each course's grade input
        grade = st.selectbox("Select the grade obtained:", grades, key=grade_key)

        course_data.append({
            "course_name": course_name,
            "credit": credit,
            "grade": grade
        })

    if st.button("Calculate CGPA"):
        cgpa = calculate_cgpa(course_data)
        st.write(f"\nYour CGPA for this semester is: {cgpa:.2f}")

    if st.button("Calculate Maximum CGPA"):
        max_cgpa = maximum_cgpa(course_data)
        st.write(f"\nMaximum achievable CGPA: {max_cgpa:.2f}")

if __name__ == "__main__":
    main()

