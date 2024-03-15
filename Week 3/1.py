def get_words_ends_with_letter(sentence, character):
    sentence_list = sentence.split(".")
    result = []

    print(sentence_list)

    for sentence_i in sentence_list:
        word_list = sentence_i.split(" ")
        sentence_words = []
        words_count = 0

        for word_i in word_list:
            if len(word_i) >= 1:
                if word_i[-1] == character:
                    sentence_words.append(word_i)
                    words_count += 1
        
        if words_count > 0:
            sentence_words.append(words_count)
            result.append(tuple(sentence_words))

    return result
    

print(get_words_ends_with_letter("Print only the words that end with the chosen letter in those sentences. Example can contains one or more sentences.", "s"))