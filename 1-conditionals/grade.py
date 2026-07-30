def main():
    score= int(input("score: "))
    grade= gradeCalc(score)
    print(grade)
    return grade 

def gradeCalc(score):
    if(score >= 90 ):
        return "A"
    elif(score >= 80):
        return "B"
    else:
        return "U r shit"

main()