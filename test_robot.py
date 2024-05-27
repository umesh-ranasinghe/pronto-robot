import subprocess

def test_robot():
    result = subprocess.run(["python", "robot.py", "F1,R1,B2,L1,B3", "--debug"], capture_output=True, text=True)
    assert result.stdout.strip() == "4"
