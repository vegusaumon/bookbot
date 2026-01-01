def word_count(text):
    found = text.split()
    return len(found)

def string_count(text):
    dictionary_storage = {}
    for character in text:
        lower_case = character.lower()
        if lower_case in dictionary_storage:
            dictionary_storage[lower_case] +=1
        else:
            dictionary_storage[lower_case] = 1
    return dictionary_storage
    
def helper_function_name(single_dict):
    return single_dict["num"]


def sort_dictionary(string_count):
    result = []
    for key in string_count:
        new_dict = {"char": key, "num": string_count[key]}
        result.append(new_dict)

    result.sort(reverse=True, key=helper_function_name)

    return result
