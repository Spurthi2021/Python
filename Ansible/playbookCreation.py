import yaml
import os

def create_ansible_playbook():
    print("Welcome to the Ansible Playbook Generator!")
    playbook = []

    # Collecting playbook details
    play_name = input("Enter the name of the playbook: ")
    hosts = input("Enter the target hosts (e.g., all): ")
    become = input("Do you want to use privilege escalation (yes/no)? ").strip().lower() == "yes"

    tasks = []
    add_task = True

    while add_task:
        print("\nDefine a new task:")
        task_name = input("Enter the name of the task: ")
        module = input("Enter the Ansible module to use (e.g., copy, yum, apt, shell): ")
        arguments = {}
        
        print("Enter module arguments as key-value pairs. Type 'done' when finished.")
        while True:
            key = input("Argument name (or 'done' to finish): ").strip()
            if key.lower() == "done":
                break
            value = input(f"Value for {key}: ").strip()
            arguments[key] = value

        task = {"name": task_name, module: arguments}
        tasks.append(task)

        add_more = input("Do you want to add another task? (yes/no): ").strip().lower()
        if add_more != "yes":
            add_task = False

    # Creating the playbook structure
    play = {
        "name": play_name,
        "hosts": hosts,
        "become": become,
        "tasks": tasks
    }
    playbook.append(play)

    # Saving the playbook to a file
    playbook_file = input("Enter the file name to save the playbook (e.g., playbook.yml): ")
    if not playbook_file.endswith(".yml"):
        playbook_file += ".yml"

    with open(playbook_file, "w") as file:
        yaml.dump(playbook, file, default_flow_style=False)
    
    print(f"\nPlaybook saved successfully as {playbook_file}!")

# Run the generator
create_ansible_playbook()
