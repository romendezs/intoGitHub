def to_camel_case(text):
    
    splitted = text.split("_")
    result = []
    for word in splitted:
        print(word)
        
        if not word[0].isupper() and word != splitted[0]:
            result
        else:
            result.append(word)  
    
    return "".join(result)

print(to_camel_case("hola_Esto_es_una_prueba"))
print("Hola")