results=["mario", "luigi"]

#element nemne
results.append("princess")
results.append(["1", "3"])
#ustgana
results.remove(["1", "3"])
#extend buyu oruulsan listeer sungana. Append shuud
#listeer oruuldag bol extend list dotor baiga elementuudiig nemne.
results.extend(["1", "3"])
#index eer nemne. orgil hamgiin ehend orson baigaa.
results.insert(0, "orgil")
#erguulne. Orgil hamgiin suul bga
results.reverse()



print(results)