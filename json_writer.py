import json
w_list = []
data_dict = {}


class WordType:
    def __init__(self, name):
        self.name = name
        self.file_path = str(name + ".txt")
        self.word_list = interpret_list(self.file_path)
        w_list.append(self)


def run():
    # Word types
    w_verb = WordType("verb")
    w_object = WordType("object")
    w_adjective = WordType("adjective")
    w_noun = WordType("noun")
    w_obj_indicator = WordType("obj_indicator")
    w_target_indicator = WordType("target_indicator")
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


def data_to_dict():
    for word_type in w_list:
        data_dict[word_type.name] = word_type.word_list


def write_to_json():
    json_file = open("json_file.json", "w")
    json.dump(data_dict, json_file, indent=2)


def __main__():
    run()
    data_to_dict()
    write_to_json()


__main__()
