""" helper function to process string input """
# import nltk
# import click
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize as wt 
import nltk.data
from random import randint

# Blooms::Knowledge
knowledge = ['cite', 'define', 'describe', 'draw']

# Load the pretrained neural network
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# @click.command()
def classify(question):
    output = ""

    print(question)
    print(question[0])
    # tokenize the input
    tokens = tokenizer.tokenize(question)
    print(tokens)
    words = wt(question)
    tagged_tokens = nltk.pos_tag(words)

    print(words)
    print(tagged_tokens)

    for i in range(0, len(words)):
        replacements = []
        for synonymn in wordnet.synsets(words[i]):

            ## don't replace proper nouns PNN or determiners
            if tagged_tokens[i][1] == 'NNP' or tagged_tokens[i][1] =='DT':
                break
        
            word_type = tagged_tokens[i][1].lower()

            if synonymn.name().find("." + word_type + "."):
                # extract the word only
                r = synonymn.name()[0:synonymn.name().find(".")]
                replacements.append(r)
        
        if len(replacements) > 0 :
            rep = replacements[randint(0,len(replacements)-1)]
            output = output + " " + rep 
        else:
            output = output + " " + words[i]
        
    print(output)


    return "hello world from classify"

