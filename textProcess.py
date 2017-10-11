""" helper function to process string input """
import click
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize as wt 
from nltk.tokenize import sent_tokenize as sent_token
from nltk.text import Text
import nltk.data
from random import randint

# Blooms::Knowledge
knowledge = ['cite', 'define', 'describe', 'draw', 'enumerate', 'identify', 'indicate', 'label', 'list', 'match', 'meet', 'name', 'outline', 'point', 'quote', 'read', 'recall', 'recite', 'recognize', 'record', 'repeat', 'reproduce', 'reveiw', 'select', 'state', 'study', 'tabulate', 'trace', 'write']
application = ['determine', 'apply', 'calculate', 'acquire', 'adapt', 'allocate', 'alphabetize', 'apply', 'ascertain', 'assign', 'attain', 'avoid', 'calculate', 'capture', 'change', 'classify', 'complete', 'compute', 'construct', 'customize', 'demonstrate', 'depreciate', 'derive', 'diminish', 'discover', 'draw', 'employ', 'examine', 'exercise', 'explore', 'expose', 'express', 'factor', 'graph', 'handle', 'illustrate', 'interconvert', 'investigate', 'manipulate', 'modify', 'operate', 'personalize', 'plot', 'practice', 'predict', 'prepare', 'price', 'process', 'produce', 'project', 'provide', 'relate', 'round', 'sequence', 'show', 'simulate', 'sketch', 'solve', 'subscribe', 'tabulate', 'transcribe', 'translate', 'use']
comprehension = ['add', 'approximate', 'articulate', 'associate', 'characterize', 'clarify', 'classify', 'compare', 'compute', 'contrast', 'convert', 'defend', 'describe', 'detail', 'differentiate', 'discuss', 'distinguish', 'elaborate', 'estimate', 'example', 'explain', 'express', 'extend', 'extrapolate', 'factor','generalize', 'give', 'infer', 'interact', 'interpolate', 'interpret', 'observe', 'paraphrase', 'picture', 'predict', 'review', 'rewrite', 'subtract', 'summarize', 'translate', 'visualize']
analysis = ['analyze', 'audit', 'blueprint', 'breadboard', 'breakdown', 'characterize', 'classify', 'compare', 'confirm', 'contrast', 'correlate', 'detect', 'diagnose', 'diagram', 'differentiate', 'discriminate', 'dissect', 'distinguish', 'document', 'ensure', 'examine', 'explain', 'explore', 'file', 'group', 'identify', 'illustrate', 'infer', 'interrupt', 'inventory', 'investigate', 'layout', 'manage', 'maximize', 'minimize', 'optimize', 'order', 'outline', 'prioritize', 'proofreed', 'query', 'relate', 'select', 'separate', 'size', 'divide', 'subdivide', 'train', 'transform']
synthesis = ['abstract', 'animate', 'arrange', 'assemble', 'budget', 'categorize', 'code', 'combine', 'compile', 'compose', 'construct', 'cope', 'correspond', 'create', 'cultivate', 'debug', 'depict', 'design', 'develop', 'devise', 'dictate', 'enhance', 'explain', 'facilitate', 'format', 'formulate', 'generalize', 'generate', 'handle', 'improve', 'incorporate', 'integrate', 'interface', 'join', 'lecture', 'model', 'modify', 'network', 'organize', 'outline', 'overhaul', 'plan', 'portray', 'prepare', 'prescribe', 'produce', 'program', 'rearrange', 'reconstruct', 'relate', 'reorganize', 'revise', 'rewrite', 'specify', 'summarize', 'write']
evaluation = ['appraise', 'assess', 'compare', 'conclude', 'contrast', 'counsel', 'criticize', 'critique', 'defend', 'determine', 'discriminate', 'estimate', 'evaluate', 'explain', 'grade', 'hire', 'interpret', 'judge', 'justify', 'measure', 'predict', 'prescribe', 'rank', 'rate', 'recommend', 'release', 'select', 'summarize', 'support', 'test', 'validate', 'verify']

# Load the pretrained neural network
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

## PRE: list(string) or string
## POST: bloom Tag
def classify(question):
    tokenized_question = wt(question)
    bloomsHash = {}   
    knowledge_keys = countKeys(tokenized_question, knowledge)
    bloomsHash['knowledge'] = knowledge_keys
    application_keys = countKeys(tokenized_question, application)
    bloomsHash['application'] = application_keys
    comprehension_keys = countKeys(tokenized_question, comprehension)
    bloomsHash['comprehension'] = comprehension_keys
    analysis_keys = countKeys(tokenized_question, analysis)
    bloomsHash['analysis'] = analysis_keys
    synthesis_keys = countKeys(tokenized_question, synthesis)
    bloomsHash['synthesis'] = countKeys(tokenized_question, bloomsHash)
    evaluation_keys = countKeys(tokenized_question, bloomsHash)
    bloomsHash['evaluation'] = evaluation_keys
    print(bloomsHash)


def countKeys(tokens, keywords):
    ## initialize keyword hash
    keyHash = {}
    for key in keywords:
        keyHash[key] = 0 
    ## search and count 
    for token in tokens:
        t = token.lower()
        for key in keywords:
            t.count(key)
            keyHash[key] = keyHash[key] + t.count(key)
    return keyHash


# PRE: QUESTION is a string
# POST: rewrites the sentence by replacing original statement with synonymns
def synReplace(question):
    output = ""

    # tokenize the input
    tokens = tokenizer.tokenize(question)
    words = wt(question)
    tagged_tokens = nltk.pos_tag(words)

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
        
    # print(output)
    return output

