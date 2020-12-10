import json


def get_problem(saved_problem):
    print(saved_problem, end="")
    problem = input("\nWhat is your problem in a few words?\n")
    return str(saved_problem + problem)


def describe_problem(saved_description):
    print(saved_description, end="")
    description = input("\nWhat is your problem in detail?\n")
    return str(saved_description+description)


def solve_problem(saved_problem):
    print(saved_problem, end="")
    solution = input("\nWhat can you do to solve it?\n")
    return str(saved_problem + solution)


def is_worried() -> bool:
    still_worried = input("\nAre you still worried y/n\n").lower()
    if still_worried == "y":
        return True
    elif still_worried == "n":
        return False
    else:
        print("Please input either y or n\n")
        is_worried()


def save_problem(problem, description, solution):
    solved_problem = {
        "Problem": problem,
        "Description": description,
        "Solution": solution
    }
    return solved_problem


def write_to_database(problem_dict):
    saved_dict = {}
    # open read the problems from the file
    with open("problems.json", mode="r") as rf:
        try:
            saved_dict = json.load(rf)
        except json.decoder.JSONDecodeError:
            saved_dict = {}

        # add the current session to the end
        saved_dict[problem_dict["Problem"]] = problem_dict

    # open the file to write our new dictionary
    with open("problems.json", mode="w") as wf:
        json.dump(saved_dict, wf, indent=2)


def do_next_problem() -> bool:
    keep_working = input("\nWould you like to work through another problem right now? y/n\n").lower()
    if keep_working == "y":
        return True
    elif keep_working == "n":
        return False
    else:
        print("Please input either y or n\n")
        do_next_problem()


def __main__():
    problem_dict = {
        "Problem": "",
        "Description": "",
        "Solution": ""
    }
    # work on the problem until it is solved
    while True:
        problem = get_problem(problem_dict["Problem"])
        description = describe_problem(problem_dict["Description"])
        solution = solve_problem(problem_dict["Solution"])
        problem_dict = save_problem(problem, description, solution)

        if not is_worried():
            break


    write_to_database(problem_dict)

    if do_next_problem():
        __main__()


__main__()

