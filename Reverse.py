
#Backwards Words

def rev_word(single_word):
    new_word = " "
    for x in range(len(single_word)):
        new_word += single_word[(x + 1) * -1]
    return new_word


#Backwards Sentences
 
#user input (delete '#' if you don't want to flip a file)
   #sentence = input("What do you have to say for yourself? ")

def rev_sen(sen_string):
    sentence_list = sen_string.split()
    rev_list = [ ]
    for item in range(len(sentence_list)):
        rev_list.append(sentence_list[(item + 1) * -1])
    new_string = " ".join(rev_list)
    return new_string



#making lists of backwardsWords words, backwardsly

def flip(sen_string):
    new_string = rev_sen(sen_string)
    list_a = new_string.split()
    list_b = [ ]
    for word in list_a:
        list_b.append(rev_word(word))
    final_string = "".join(list_b)
    return final_string


file_name = input("What is the case-sensitive name of your .txt file? ")

infile = open(file_name + ".txt", "r")
outfile = open("Rev_" + file_name + ".txt", "w")

contents = str(infile.read())
outfile.write(flip(contents))

infile.close()
outfile.close()

