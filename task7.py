def replace_long_words(text):
    
    words = text.split()
    
    brovardan_words = []
    for word in words:
        if len(word) >= 5:
        
            brovardan_words.append('#' * len(word))
        else:
            
            brovardan_words.append(word)
    
    
    return ' '.join(brovardan_words)


input_text = input("Matnro vorid namo: ")

result = replace_long_words(input_text)
print(result)
