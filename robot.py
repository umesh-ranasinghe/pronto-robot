def validate_user_commands(user_commands_str):
  is_valid_command = re.fullmatch('^[FBLR]\d+(,[FBLR]\d+)*$', user_commands_str)
  if is_valid_command:
    print('valid_command')
  else:
    print('invalid command')

def initialize():
  global position, facing_direction
  position = [0,0]
  facing_direction = [0,1]

if __name__ == "__main__":
#  user_commands_str = input("Enter instructions for robot :")
  user_commands_str = "F1,R1,B2,L1,B3"
  validate_user_commands(user_commands_str)
  initialize()
  print(4)
