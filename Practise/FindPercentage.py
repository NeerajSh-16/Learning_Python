'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
Sample Input :
        3
        Krishna 67 68 69
        Arjun 70 98 63
        Malika 52 56 60
        Malika
Sample Output : 56.00
'''
if __name__ == '__main__':
    # Neeraj Sharma
    # My nickname is Madhav Sharma
    # My college Roll Number is 2023PGCSCA022
    # The name of my institute is Natioanl of Technology, Jamshedpur
    # From here I'm pursuing my masters in Computer Application
    # It is a three year professioanl course
    # Holla
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum = student_marks[query_name][0] + student_marks[query_name][1] + student_marks[query_name][2]
    avg = sum/3
    print("{:.2f}".format(avg))