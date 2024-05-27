import re

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
  else:
    print('Invalid comamand : {}'.format(user_commands_str))
  print(4)
