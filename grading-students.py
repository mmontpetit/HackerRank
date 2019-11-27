def gradingStudents(grades):
    # Write your code here
    givenGrade = []
    n = int
    for i in range(len(grades)):
        n = grades[i]

        if (n % 5):
            t = (5 - n % 5)
            if(t<3):
                n = n + (5 - n % 5);
            if(n<38):
                n = grades[i]
        givenGrade.append(n)
