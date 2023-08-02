# CGPA Calculator App

![CGPA Calculator](https://qph.cf2.quoracdn.net/main-qimg-f6f3173e37aa2a86895c4ffae79ddbcc)

## Overview

This is a simple CGPA Calculator web app built using Python's Streamlit library. It helps students calculate their Cumulative Grade Point Average (CGPA) based on their semester grades.

## Formula

The CGPA is calculated using the following formula:

```
CGPA = (Σ(Credit Points * Grade Points)) / ΣCredit Points
```

Where:
- Σ represents summation
- `Credit Points` are the credits assigned to a course (usually between 1 to 4)
- `Grade Points` are the points corresponding to the grades obtained, based on the following table:

| Grade       | Grade Points | Marks range|
|-------------|--------------|---------------|
| O (Outstanding) | 10           | 91-100 |
| A+ (Excellent)  | 9            |81-90|
| A (Very good)   | 8            |71-80|
| B+ (Good)       | 7            |61-70|
| B (Average)     | 6            |51-60|
| C (Satisfactory)| 5            |<50|
| RA (Re-Appearance) | 0         |-|
| SA (shortage of attendance) | 0 |-|
| W (Withdrawal) | 0             |-|

## Semester Rules

The following rules are considered for each semester:
1. Courses with grades 'RA', 'SA', or 'W' are not included in the CGPA calculation.
2. Courses with grades 'O' to 'B' are included in the CGPA calculation.
3. Courses with grades 'C' are included in the CGPA calculation, but they are considered as satisfactory, and no grade points are assigned.
4. Grades are assigned based on the marks obtained as per the grade range mentioned in the table.

## How to Use the App

1. Enter the number of courses you have taken in the current semester.
2. For each course, provide the course name, credit points, and select the grade obtained from the drop-down menu.
3. Click the 'Calculate CGPA' button to see your CGPA for the current semester.

### Example

Suppose you have taken three courses this semester:
- Course 1: Calculus (4 credits) - Grade: A (8 grade points)
- Course 2: Data Science (3 credits) - Grade: B+ (7 grade points)
- Course 3: Programming Fundamentals (3 credits) - Grade: A- (7.5 grade points)

The CGPA calculation would be as follows:

```
CGPA = ((4 * 8) + (3 * 7) + (3 * 7.5)) / (4 + 3 + 3) = 7.417
```

So, your CGPA for this semester would be approximately 7.42.

## Installation

To run the app locally, follow these steps:

1. Clone this repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run the app using `streamlit run cgpa_calculator.py`.

## Feedback and Contributions

Feel free to provide feedback or contribute to the project. Open issues or submit pull requests on the [GitHub repository](https://github.com/your_username/cgpa-calculator-app).

---
