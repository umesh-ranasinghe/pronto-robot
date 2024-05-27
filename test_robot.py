import subprocess
from robot import validate_and_parse_commands

def test_robot():
    result = subprocess.run(["python", "robot.py", "F1,R1,B2,L1,B3", "--debug"], capture_output=True, text=True)
    assert result.stdout.strip() == "4"

def test_validate_and_parse_commands():
    debug_mode = False
    assert validate_and_parse_commands("F1,R1,B2,L1,B3") == [('F', 1), ('R', 5), ('B', 2), ('L', 9), ('B', 3)]
