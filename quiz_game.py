print('**WELCOME TO THE GEOQUIZ v.0.1**')
print('**NOTE: ANSWERS IN A / B / C / D**') 
confirm = input('Start?(y) ') #Asks player if he want to start
if confirm == 'y' or confirm == 'Y': #If he answered y, the game will start
    ansCor = 0 #Creates the total score variable and sets it to 0
    print('**START**')

    q1 = input('Which of these is not a South America country:\nA - Brazil\nB - Peru\nC - Fiji\nD - Argentina\n') #Shows the question and put a space for the player to put his answer
    if q1 == 'C' or q1 == 'c': #Verifies if question answer is correct
        ansCor = ansCor + 1 #Adds one point to the total

    q2 = input('Chose the option that the both most populated countries in the world:\nA - China and India\nB - China and United States\nC - India and Russian\nD - China and Canada\n')
    if q2 == 'A' or q2 == 'a':
        ansCor = ansCor + 1

    q3 = input('What is the country with highest GDP:\nA - United States\nB - China\nC - United Kingdom\nD - Russia\n')
    if q3 == 'A' or q3 == 'a':
        ansCor = ansCor + 1

    q4 = input('Which of these contries do not use euros(€):\nA - France\nB - Germany\nC - Portugal\nD - United Kingdom\n')
    if q4 == 'D' or q4 == 'd':
        ansCor = ansCor + 1

    q5 = input('What country is mostly not in the north hemisphere:\nA - Russia\nB - Australia\nC - Portugal\nD - Greenland\n')
    if q5 == 'B' or q5 == 'b':
        ansCor = ansCor + 1
print('**YOUR SCORE IS:', ansCor, 'OUT OF 5**') #Prints the score