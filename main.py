# This chat bot uses probabilty and statistics to make an educated guess response to respond to the user. I was unable to use something like TensorFlow to use machine learning in this program because it is on Replit, and Replit does not support TensorFlow.

import re
import long_responses as long

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are in each pre-defined message.
    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    # Calculates % of recognized words the user's message.
    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100) # Returns a whole percentage
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # RESPONSES ---------------------------------------------
      
    response('Hello!', ['hello', 'hi', 'sup', 'hey'], single_response=True)
    response('I\'m doing fine, what about you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Thank you!', ['i', 'love', 'you'], required_words=['love'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response('That\'s good!', ['i\'m', 'good'], required_words=['i\'m', 'good'])
    response('Ok.', ['no'], required_words=['no'])

    # RESPONSES ------------------------------------------------
  
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list) # <- This prints all the key information about the queries. 

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input): # Gets the response that it should based, minus the characters defined by split_message
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

print("Welcome to Yessuh! I am an AI chat bot that you can talk to!\n\n")

while True: # Main loop, infinite
  request = input('Type here: ')
  print(f'\nBot: {get_response(request)} \n')
  file = open("responses.txt", "a")
  file.write(f"{request}\n")
  file.close()