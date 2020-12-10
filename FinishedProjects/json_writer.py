import json
from interpreter import WordType
w_list = []
data_dict = {}


def run():
    # Word types
    w_action = WordType("action")
    w_object = WordType("object")
    w_target = WordType("target")
    w_ignore = WordType("ignore")

    # with open("word_types.txt") as fh:
    #     fh.write(dict_w_verb)
    print("dumped")


def interpret_list(file_path):
    fh = open(file_path).readlines()
    stripped_list = []

    # iterate through the lists and get rid of end characters
    for word in fh:
        new_word = word.rstrip()
        stripped_list.append(new_word)
    return stripped_list


def data_to_dict(_list):
    for word_type in _list:
        data_dict[word_type.name] = word_type.word_list
    write_to_json()


def write_to_json():
    json_file = open("data.json", "w")
    json.dump(data_dict, json_file, indent=2)


def __main__():
    run()
    data_to_dict(w_list)


__main__()
