print ("Hello!")
name = input ("Type in your first name? ")
count = sum(c.isalpha() for c in name)
print("Your name has a total of", count ,"letters")
    