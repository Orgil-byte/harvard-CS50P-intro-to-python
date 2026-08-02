def main():
    #split list bolgoj baiga uchir list dotor oruulahgui
    words="hello hello hello bye bye bye bye".split(" ")

#Words dotor baiga buh usgiig maplaad jijig bolgoj bn. 
#Ard ni filter hiij bn, if eer
    lower_case_words = [word.lower() for word in words if len(word) > 4]

#Lowercase words bolson words-uudiig word: key uusgen value deer ni toolj
#butsaaj bn. Jishee ni {world: 24, etc..}
    count={word: lower_case_words.count(word) for word in lower_case_words}

    print(count)

    

main()