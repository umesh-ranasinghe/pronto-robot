import re

def move_forward():
  print(f"Forward")

def move_backward():
  print(f"Backward")

def turn_left():
  print(f"Turning left")

def turn_right():
  print(f"Turning right")

actions = {
    'F': move_forward,
    'B': move_backward,
    'L': turn_left,
    'R': turn_right,
}

def validate_and_parse_commands(user_commands_str):
  single_command_pattern = r'[FBLR]\d+'
  full_command_pattern = '^{0}(,{0})*$'.format(single_command_pattern)
  valid_command = re.fullmatch(full_command_pattern, user_commands_str)
    
  if valid_command:
    single_commands = re.findall(r'([FBLR])(\d+)', user_commands_str)
    parsed_commands = [(letter, int(number)) for letter, number in single_commands]
    return parsed_commands
  else:
    return None

def execute_commands(commands):
  for command in commands:
    print(command)
    action = command[0]
    execution_count = command[1]
    for i in range(execution_count):
      actions[action]()

def initialize():
  global position, facing_direction
  position = [0,0]
  facing_direction = [0,1]

if __name__ == "__main__":
#  user_commands_str = input("Enter instructions for robot :")
  user_commands_str = "F1,R1,B2,L1,B3"
  validated_commands = validate_and_parse_commands(user_commands_str)
  if validated_commands:
    print('ready to move. plan is {0}'.format(validated_commands))
    initialize()
    execute_commands(validated_commands)
  else:
    print('Invalid comamand : {}'.format(user_commands_str))
  print(4)
