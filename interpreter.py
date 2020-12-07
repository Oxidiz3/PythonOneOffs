"""
Command Comprehender
    summary: be able to get a command in a sentence and then understand what
    it wants and do something with it
"""
import json

data_dict = {}
word_type_names = ["action", "object", "target", "actor", "ignore"]
command_hint_length = 2

class WordType:
    def __init__(self, name, d_saved_words):
        self.name = name
        try:
            self.word_list = d_saved_words[name]
        except KeyError:
            self.word_list = []
        data_dict[self.name] = self


    def to_dict(self):
        return {
            self.name: self.word_list
        }


def read_json_file():
    with open("data.json", mode="r+") as json_file:
        return json.load(json_file)


def declare_word_types(read_dict):
    for name in word_type_names:
        WordType(name, read_dict)


def get_command():
    command = input("What is your command? Or x to stop\n").lower()
    return command


def disect_command(command):
    command_word_list = []
    start_num = 0
    end_num = 0

    for word in command:
        # If there is a space then that is one word
        if word == " ":
            command_word_list.append(command[start_num:end_num])

            # Move the start num to the letter after the space
            start_num = end_num + 1
        end_num += 1

    # Do once at the end so it gets the last word
    command_word_list.append(command[start_num:end_num])
    return command_word_list


def determine_word_type(command_word_list) -> list:
    l_saved_words = []
    l_unsaved_words = []

    for key in data_dict:
        # get every word in the dictionary
        for word in data_dict[key].word_list:
            l_saved_words.append(word)

    # Create a list of all saved words
    for word in command_word_list:
        # see if word is in the list of all saved words
        if word in l_saved_words or word in l_unsaved_words:
            print(word, "has been saved")
        else:
            l_unsaved_words.append(word)

    return l_unsaved_words


def get_word_type(l_unsaved_words):
    # ask user to input the matching first letters
    for word in l_unsaved_words:
        # set a new line
        print("\n")
        # label each list from 0 to length
        wi = 0
        # print out data type hints
        for keys in data_dict:
            print(keys[0:command_hint_length] + ":" + keys, end="")

            # if not at the end yet then add a comma
            if wi < len(data_dict) - 1:
                print(", ", end="")

            wi += 1


        indicator_letters = input("\nWhat type of word is " + str(word) + "?\n").lower()
        # then append word using matching list number
        for key in data_dict:
            if indicator_letters == key[0:command_hint_length].lower():
                data_dict[key].word_list.append(word)


def write_to_json():
    new_dict = {}
    for key in data_dict:
        new_dict.update(data_dict[key].to_dict())

    with open("data.json", "w") as write_file:
        json.dump(new_dict, write_file, indent=2)


def __main__():
    # setup data
    d_saved_words = read_json_file()
    declare_word_types(d_saved_words)

    # receive input
    command = get_command()

    if command.lower() == "x":
        exit()
    # interpret input
    command_word_list = disect_command(command)
    l_unsaved_words = determine_word_type(command_word_list)
    get_word_type(l_unsaved_words)

    # save data
    write_to_json()
    __main__()


__main__()
