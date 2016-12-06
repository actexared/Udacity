# Stage 2 Final Project by Eric Simmons

# Questions and Answers
easyAnswers = ["Trump", "Cruz", "Rubio", "Clinton"]
mediumAnswers = ["Second", "Great", "Europe", "Allies"]
hardAnswers= ["programming", "classes", "objects", "life"]

easyQuiz = ("The current GOP presidental candidates are Donald _1_ , Ted _2_ ,"
    "and Marco _3_. The female Democratic candidate is Hillary _4_. \n").title()
mediumQuiz = ("Prior to the _1_ World War, the First World War was known as the _2_ War. "
    "It was a global conflict centered in _3_ where the Axis vs. fought against the _4_. \n")
hardQuiz = ("In Object-oriented _1_, you write _2_, that represents real-word things "
    " and situations, and create _3_ based on these classes. Classes make _4_ easier. \n")

# Lists
blanks = ["_1_", "_2_", "_3_", "_4_"]
answers = [easyAnswers, mediumAnswers, hardAnswers]
quizzes = [easyQuiz, mediumQuiz, hardQuiz]

def choose_quiz():
    """choose_quiz function prompts the user to input one of the quiz selections easy/medium/hard.
If neither of those are chosen, the level choice is easy by default. The level choices selects the
corresponding level string and that string is returned."""

    if quiz_select == "easy":
        return quizzes[0]   
    elif quiz_select == "medium":
        return quizzes[1]
    elif quiz_select == "hard":
        return quizzes[2]
    else:
        print "Invalid input. We'll start with the easy quiz"
        return quizzes[0]

print "Please select a game difficulty!"
quiz_select = raw_input("To do so, type which level to play 'easy', 'medium' or 'hard': ").lower()
print "You have selected the " + quiz_select + " quiz.\n"  
print choose_quiz() + "\n"  
 

def choose_answer():
    """choose_answer will take the quiz selection list from the choose_quiz function and return with 
    the corresponding answer list"""
    
    if choose_quiz() == quizzes[0]:
        return answers[0]
    if choose_quiz() ==quizzes[1]:
        return answers[1]
    if choose_quiz() ==quizzes[2]:
        return answers[2]
        
def fill_in_the_blanks():
    """fill_in_the_blanks function plays the game. Using a while loop, the user is prompted to input their 
    answer for each blank in the lists (blanks) until all four elements have been completed. 
    The 'answer' variable will be checked against the user's response depending on which quiz level in play. 
    Another while loop is used if the user's input does not equal the variable 'answer' and will prompt the 
    user to answer again until they get the correct answer. If it is correct, it quits the loop the answer will 
    replace the blank element in the quiz.""" 
    
    quiz = choose_quiz()
    answer = choose_answer()
    answer_index = 0   
    while answer_index < len(blanks): 
        user_response = raw_input("Please fill in the correct answer for " + blanks[answer_index] + ":")
        while user_response != answer[answer_index]:
            user_response = raw_input("Incorrect response. Please fill in the correct answer for " + blanks[answer_index] + ":")
        if user_response == answer[answer_index]:
            print "That is correct!!"
            quiz = quiz.replace(blanks[answer_index], user_response)
            print quiz
            answer_index += 1
    print "Gold star lad! You have completed the quiz!"

fill_in_the_blanks()
