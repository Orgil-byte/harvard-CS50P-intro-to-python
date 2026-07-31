
"LOOP MEOW NUMBER OF TIMES WITH DIFFERENT APPROACHES."

# 1==================================
i=0
while(i < 3 ):
    print("Meow")
    i += 1

# 2==================================
for i in [0,1,2]:
    print("Meow")

# 3==================================
for _ in range(3):
    print("Meow")

# 4==================================
print("woff\n" * 3, end="")


"USING LOOP TO ASK ONE QUESTION UNTIL GETS RIGHT THEN WITH THAT INPUT MEOW."

while True:
    n = int(input("What is n? "))
    if(n > 0):
        break

for _ in range(n):
    print("meow")