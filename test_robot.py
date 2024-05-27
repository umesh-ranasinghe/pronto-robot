import subprocess


def test_robot_valid_command():
    result = subprocess.run(["python", "robot.py", "F1,R1,B2,L1,B3"], capture_output=True, text=True)
    assert result.stdout.strip() == "4"


def test_robot_invalid_command():
    result = subprocess.run(["python", "robot.py", "F1L,R1"], capture_output=True, text=True)
    assert result.stdout.strip() == "Invalid comamand : F1L,R1"
