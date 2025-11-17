import matplotlib.pyplot as plt
import os

def main():
    # students list creation
    students_text = open("data/students.txt","r")
    # dictionary with all student names as keys and ids as values
    students = {}
    for item in students_text.readlines():
        students[item[3:-1].lower()] = item[0:3]

    print(students)

    # assignment list creation; also consider making a list of student, assignment, and submission objects for practicality / error handling
    assignments_text = open("data/assignments.txt", "r")
    # dictionary with all assignments titles as keys and ids, points as values
    assignments = {}
    as_list = assignments_text.readlines()
    for i in range(0,len(as_list),3):
        assignments[as_list[i][:-1]] = as_list[i+1][:-1], as_list[i+2][:-1]
    # submission list
    submissions = os.listdir("data/submissions")
    # menu selection
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph\n")
    opt = input("Enter your selection: ")
    # option handling
    if opt == "1":
        name = input("What is the student's name: ").lower()
        if name in students:
            ids, grade = students[name], 0
            for submission in submissions:
                dr = "data/submissions/" + submission
                sub = open(dr,"r").read().split("|")
                if sub[0] == ids:
                    for title, values in assignments.items():
                        if sub[1] == values[0]:
                            weight = int(values[1])/1000
                            grade += int(sub[2]) * weight
            print(f"{grade:.0f}%")
    # try combining opt 2 with opt 3 in iterating through assignment
    elif opt == "2" or opt == "3":
        assignment = input("What is the assignment name: ")
        if assignment in assignments:
            ida, grades = assignments[assignment][0], []
            for submission in submissions:
                dr = "data/submissions/" + submission
                sub = open(dr, "r").read().split("|")
                if sub[1] == ida:
                    grades.append(int(sub[2]))
            if opt == "2":
                print(f"Min: {min(grades)}")
                print(f"Avg: {sum(grades)/len(grades):.0f}")
                print(f"Max: {max(grades)}")
            elif opt == "3":
                bins = [0,10,20,30,40,50,60,70,80,90,100]
                plt.hist(grades,bins)
                plt.show()

if __name__ == "__main__":
    main()