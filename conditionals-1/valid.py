def main_bad_code():
    gender = input("gender? ")
    age = int(input("age? "))
    if(gender == "male"):
        if(age >=21):
            return "good"
        elif(age<=21):
            return "bad"
        else:
            return "enter valid age"
    elif(gender == "female"):
        if(age >=21):
            return "great"
        elif(age<=21):
            return "kind of okay"
        else:
            return "enter valid age"
    else:
        return("enter valid gender")

def main_good_code():
    gender = input("gender? ")
    if not (gender == "male" or gender == "female"):
        return "enter valid age"
    age = int(input("age? "))
    if not (age >=  21 or age <= 21):
        return "enter valid age"

    if(gender=="male" and age >=21):
        return "good"
    elif(gender=="male" and age <=21):
        return "bad"
    elif(gender == 'female' and age >=21):
        return "great"
    else:
        return "kind of okay"