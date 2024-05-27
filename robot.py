import re

def move_forward():
  global position
  position[0] += facing_direction[0]
  position[1] += facing_direction[1]
  print(f"Forward {position}")

def move_backward():
  global position 
  position[0] -= facing_direction[0]
  position[1] -= facing_direction[1]
  print(f"Backward {position}")

def turn_left():
  print("Turning left")
  global facing_direction
  facing_direction = [-facing_direction[1], facing_direction[0]]

def turn_right():
  print("Turning right")
  global facing_direction
  facing_direction = [facing_direction[1], -facing_direction[0]]

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
    
    if action in ['L','R']:
      execution_count = execution_count%4
    for i in range(execution_count):
      actions[action]()

def initialize():
  global position, facing_direction
  position = [0,0]
  facing_direction = [0,1]

def find_min_distance_to_return():
    return abs(position[0]) + abs(position[1])
  
if __name__ == "__main__":
#  user_commands_str = input("Enter instructions for robot :")
  user_commands_str = "F1,R5,B2,L9,B3"
  validated_commands = validate_and_parse_commands(user_commands_str)
  
  if validated_commands:
    print('ready to move. plan is {0}'.format(validated_commands))
    initialize()
    execute_commands(validated_commands)
    print(find_min_distance_to_return())
  else:
    print('Invalid comamand : {}'.format(user_commands_str))
