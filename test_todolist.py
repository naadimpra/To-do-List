import subprocess
import sys

def test_todo_e2e():
    # Simulated user inputs
    input_data = "add Buy Milk\nadd Fix Bug\nview\nexit\n"
    
    # Run the todolist.py script with the simulated inputs
    process = subprocess.Popen(
        [sys.executable, "todolist.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    stdout, stderr = process.communicate(input=input_data)
    
    assert "Added: Buy Milk" in stdout
    assert "Added: Fix Bug" in stdout
    assert "1. Buy Milk" in stdout
    assert "2. Fix Bug" in stdout