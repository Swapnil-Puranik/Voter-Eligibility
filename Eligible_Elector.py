#Voter eligibility Project - COgnizant externship

age = int(input("How old are you? ")) #Taking input and converting it to int
if age<0: # handling the edge case, what if the user enters negative number
    print("That's not a valid age!")
elif age>=18: # this will handle the case for when age is 18 and above
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    print("Oops! You’re not eligible yet. But hey, only ",18-age, "more years to go!")