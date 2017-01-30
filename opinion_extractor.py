import sys
sys.path.append(r'T:\Departments\Informatics\LanguageEngineering')

def opinion_extractor(aspect_token, parsed_sentence):
    
    opinions = []
    advmod_opinions = []

    for dependant in parsed_sentence.get_dependants(aspect_token):
        if dependant.deprel == "amod":
            for second_dependant in parsed_sentence.get_dependants(dependant):
                if second_dependant.deprel == "advmod":
                    advmod_opinions += [second_dependant.form + "-" + dependant.form]
            if advmod_opinions == []:
                opinions += [dependant.form]
            else:
                opinions += advmod_opinions
    #Checking for negatives
    for dependant in parsed_sentence.get_dependants(aspect_token):
        if dependant.deprel == "neg" and advmod_opinions == []:
            i = 0
            for x in opinions:
                opinions[i] = "not-" + opinions[i]
                i += 1
        elif dependant.deprel == "neg" and advmod_opinions != []:
            j = 0
            for x in opinions:
                opinions[j] = "not-" + opinions[j]
                j += 1
    advmod_opinions = []    
    head_token = parsed_sentence.get_head(aspect_token)
    if aspect_token.deprel == "nsubj" and head_token.pos == "JJ":
        if parsed_sentence.get_dependants(head_token):
            for dependant in parsed_sentence.get_dependants(head_token):
                if dependant.deprel == "advmod":
                    advmod_opinions += [dependant.form + "-" + head_token.form]
                
            if advmod_opinions == []:
                opinions += [head_token.form]
            else:
                opinions += advmod_opinions  
                        
    #Checking for negatives
    for dependant in parsed_sentence.get_dependants(head_token):
        if dependant.deprel == "neg" and advmod_opinions == []:
            i = 0
            for x in opinions:
                opinions[i] = "not-" + opinions[i]
                i += 1
        elif dependant.deprel == "neg" and advmod_opinions != []:
            j = 0
            for x in opinions:
                opinions[j] = "not-" + opinions[j]
    advmod_opinions = []
    conj_opinions = []
    
    
    for dependant in parsed_sentence.get_dependants(head_token):
        if dependant.deprel == "conj":
            for dep in parsed_sentence.get_dependants(dependant):
                if dep.deprel == "advmod":
                    advmod_opinions = [dep.form+"-"+dependant.form]
            if advmod_opinions == []:
                conj_opinions += [dependant.form]
            else:
                conj_opinions += advmod_opinions
    #Checking for negatives
    
    for dependant in parsed_sentence.get_dependants(head_token):
        if dependant.deprel == "conj":
            for dep in parsed_sentence.get_dependants(dependant):
                if dep.deprel == "neg" and advmod_opinions == []:
                    i = 0
                    for x in conj_opinions:
                        conj_opinions[i] = "not-" + conj_opinions[i]
                        i += 1
                elif dep.deprel == "neg" and advmod_opinions != []:
                    g = 0
                    for j in conj_opinions:
                        conj_opinions[g] = "not-" + conj_opinions[g]
                        g += 1
    opinions += conj_opinions
    
   
 
    return opinions