import random

count = 0

# count = count + 1 

print("Welcome to Faraz's Magic 8 Ball")

# Faraz, wrap the code below in a loop so the user can
# keep asking the magic 8 ball questions... Go!

# Challenge number 2 before we call it a day...
# create a variable to keep track of whether we should keep running
# the magic 8 ball program. Then at the end of the loop, prompt the user
# and ask he or she whether they would like to keep asking the magic 8
# ball questions. If they reply no or yes or whatever, then change the
# value of the variable, so that the loop quits running. Also, tell the
# user goodbye if they choose to exit. Go!


# Faraz, change this while loop to where it it keeps running 
# while some variable is equal to true
keep_running = True
keep_playing = "fo sho"
while keep_running == True:
    count = count + 1

    question = input("Ask me a question")

    my_list = [
        "is is certain", 
        "it is decidedly so", 
        "without a doubt",
        "Yes - definetly",
        "You may rely on it",
        "As I see it yes",
        "Most likely",
        "Outlook, good",
        "Yes.",
        "Signs point yes",
        "Reply hazy, try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful",
    ]
    random_number = random.randint(0, 19)

    # you don't want blablabla == True,
    # you wan't if this string method returns -1,
    # print yes of course!]

    '''
    if question.find("coding") >= 0:
        print("Yes, of course!")
    else:
        print(my_list[random_number])

    if question.find("code") >= 0:
        print("Yes, of course!")
    else:
        print(my_list[random_number])
    '''

    question = question.lower() # convert to lowercase for string comparison

    if question.find("coding") >= 0:
        print("Yes, of course!")
    elif question.find("code") >= 0:
        print("Yes, of course!")
    elif question.find("program") >= 0:
        print("Yes, of course!")
    elif question.find("programming") >= 0:
        print("Yes, of course!")
    else:
        print(my_list[random_number])

    if count % 3 == 0:
        #then question.input("Woud")
        keep_playing = input("Would you like to keep playing? Enter 'y' for yes, 'n' for no>>> ")
        keep_playing = keep_playing.lower()

    if keep_playing.find("n") >= 0:
        print("Goodbye!")
        # right here, is where you will turn off the loop
        keep_running = False


    # Faraz, if the user wants to stop playing, tell the user goodbye
    # and shut down the loop... Go!
