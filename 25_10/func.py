import re
def word_count(text):
    text = text.lower()

    word_dict = {}
    words = re.findall(r'\b\w+\b', text)

    for word in words:
        if word in word_dict:
            word_dict[word] +=1
        else:
            word_dict[word] =1

    return word_dict

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
result = word_count(text)
print(result)
