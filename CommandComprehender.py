"""
Command Comprehender
    summary: be able to get a command in a sentence and then understand what
    it wants and do something with it
"""

from os import write

# File Names
verb_fileName = "verbs.txt"
object_fileName = "objects.txt"
adjective_filename = "adjectives.txt"
noun_fileName = "nouns.txt"
obj_indicator_fileName = "objIndicators.txt"
target_indicator_fileName = "targetIndicators.txt"
# Lists
verb_list = open(verb_fileName, mode='r').readlines()
object_list = open(object_fileName, mode='r').readlines()
adjective_list = open(adjective_filename, mode='r').readlines()
noun_list = open(noun_fileName, mode='r').readlines()
obj_indicator_list = open(obj_indicator_fileName).readlines()
target_indicator_list = open(target_indicator_fileName).readlines()

list_holder = [verb_list, object_list, adjective_list, noun_list,
               obj_indicator_list, target_indicator_list]


def interpret_list():
    # iterate through the lists and get rid of end characters
    for i_list in list_holder:
        i = 0
        for line in i_list:
            i_list[i] = line.rstrip()
            i += 1


def get_command():
    command = input("What is your command?\n").lower()
    disect_command(command)


def disect_command(command):
    word_list = []
    start_num = 0
    end_num = 0

    for word in command:
        # If there is a space then that is one word
        if word == " ":
            word_list.append(command[start_num:end_num])

            # Move the start num to the letter after the space
            start_num = end_num + 1
        end_num += 1

    # No space at the end of the file so add that as a word also
    word_list.append(command[start_num:end_num])
    determine_word_type(word_list)


def determine_word_type(word_list):
    for word in word_list:
        if word in verb_list:
            print(word, "is a verb!")
        elif word in object_list:
            print(word, "is an object!")
        elif word in noun_list:
            print(word, "is a noun!")
        elif word in adjective_list:
            print(word, "is an adjective!")
        elif word in obj_indicator_list:
            print(word, "is an object indicator!")
        elif word in target_indicator_list:
            print(word, "is a target indicator!")
        else:
            get_word_type(word)


def get_word_type(word):
    print("\no:object, n:noun, a:adjective, v:verb, 1: object indicator, 2: target indicator")
    wordType = input("What type of word is " + str(word) + "?\n").lower()

    # Get input then add new word to appropriate list
    if wordType == 'o':
        object_list.append(word)
        write_to_file(object_fileName, word)
    elif wordType == 'n':
        noun_list.append(word)
        write_to_file(noun_fileName, word)
    elif wordType == 'a':
        adjective_list.append(word)
        write_to_file(adjective_filename, word)
    elif wordType == 'v':
        verb_list.append(word)
        write_to_file(verb_fileName, word)
    elif wordType == '1':
        obj_indicator_list.append(word)
        write_to_file(obj_indicator_fileName, word)
    elif wordType == '2':
        target_indicator_list.append(word)
        write_to_file(target_indicator_fileName, word)
    else:
        print("I didn't recognize your input please use only o,n,a,v,1,2")
        get_word_type(word)


def write_to_file(file_name, new_word):
    with open(file_name, mode='a') as open_file:
        open_file.write(new_word)


def __main__():
    interpret_list()
    get_command()


__main__()
