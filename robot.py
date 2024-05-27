import re, argparse


def move_forward():
    global position
    position[0] += facing_direction[0]
    position[1] += facing_direction[1]
    if debug_mode:
        print(f"\t\tForward {position}")


def move_backward():
    global position
    position[0] -= facing_direction[0]
    position[1] -= facing_direction[1]
    if debug_mode:
        print(f"\t\tBackward {position}")


def turn_left():
    if debug_mode:
        print("\t\tTurning left")
    global facing_direction
    facing_direction = [-facing_direction[1], facing_direction[0]]


def turn_right():
    if debug_mode:
        print("\t\tTurning right")
    global facing_direction
    facing_direction = [facing_direction[1], -facing_direction[0]]


actions = {
    "F": move_forward,
    "B": move_backward,
    "L": turn_left,
    "R": turn_right,
}


def validate_and_parse_commands(user_commands_str):
    single_command_pattern = r"[FBLR]\d+"
    full_command_pattern = "^{0}(,{0})*$".format(single_command_pattern)
    valid_command = re.fullmatch(
        full_command_pattern, user_commands_str
    )  #  match the whole user command with the accepted pattern

    if valid_command:
        if debug_mode:
            print(f"Command validated : {user_commands_str}")
        single_commands = re.findall(r"([FBLR])(\d+)", user_commands_str)
        parsed_commands = [
            (action_letter, int(action_count))
            for action_letter, action_count in single_commands
        ]  #  extract action and the number of times it should be executed
        return parsed_commands
    else:
        return None


def execute_commands(commands):
    for command in commands:
        if debug_mode:
            print(f"\tExecuting : {command}")
        action = command[0]
        execution_count = command[1]

        if action in ["L", "R"]:
            execution_count = execution_count % 4  #  avoid full circle turns
        for i in range(execution_count):
            actions[action]()


def initialize():
    global position, facing_direction
    position = [0, 0]
    facing_direction = [0, 1]


def find_min_distance_to_return():
    return abs(position[0]) + abs(position[1])


def parse_input_arguments():
    parser = argparse.ArgumentParser(
        description="""This program receives a string of commands 
    and will output the robot's distance from it's starting point.  
    This distance will be the minimum amount of units the robot 
    will need to traverse in order to get back to it's starting point.
    
    Example command string: F1,R1,B2,L1,B3"""
    )
    parser.add_argument(
        "command_string", type=str, help="Navigation commands in comma seperated format"
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="Enable debug output"
    )
    args = parser.parse_args()
    global debug_mode
    debug_mode = args.debug
    return args.command_string


if __name__ == "__main__":
    user_commands_str = parse_input_arguments()
    validated_commands = validate_and_parse_commands(user_commands_str)

    if validated_commands:
        initialize()
        execute_commands(validated_commands)
        print(find_min_distance_to_return())
    else:
        print("Invalid comamand : {}".format(user_commands_str))
