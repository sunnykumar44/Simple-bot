import re
import long_resp as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainity=0
    has__required_words=True


    for word in user_message:
        if word in recognised_words:
            message_certainity+=1

    percentage=float(message_certainity)/float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has__required_words=False
            break
    if has__required_words or single_response:
        return int(percentage*100)
    else:
        return 0
    
def check_all_messages(message):
    highest_prob_list={}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response]= message_probability(message, list_of_words, single_response,required_words)


    response('Hello!', ['hello','hi','sup','heyo'], single_response=True)
    
    response('Wish you a very Good Morning master,how would you like to use me',['good','morning','bot'],required_words=['good','morning'])

    response('I\'m doing fine, and you?',['how','are','you','doing'],required_words=['how','you'])
    
    response('Trying to answer your questions!',['what','are','you','doing'],required_words=['what','doing'])
    
    response('Thank you!',['i','love','code','baby'],required_words=['code','baby'])

    response('I can try to answer most of your questions,execuse if I stuck in between.',['how','can','you','help'],required_words=['you','help'])

    response(long.R_EATING,['what','you','eat'],required_words=['you','eat'])

    best_match=max(highest_prob_list, key=highest_prob_list.get)

    

    return long.unknown() if highest_prob_list[best_match]<1 else best_match

def get_response(user_input):
    split_message=re.split(r'\s+|[,;?!.-@]\s*', user_input.lower())
    response=check_all_messages(split_message)
    return response

while True:
    print('Bot: ' + get_response(input('You: ')))