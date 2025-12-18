import sys

def main():
    todo_list = []
    inputs = sys.stdin.read().splitlines()
    
    for line in inputs:
        if line.startswith("add "):
            task = line[4:]
            todo_list.append(task)
            print(f"Added: {task}")
        elif line == "view":
            if not todo_list:
                print("List is empty")
            else:
                for i, task in enumerate(todo_list, 1):
                    print(f"{i}. {task}")
        elif line == "exit":
            break

if __name__ == "__main__":
    main()