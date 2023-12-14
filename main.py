import subprocess
from keyboard import press_and_release

email = str(input("Seu e-mail: "))
subprocess.call([f"ssh-keygen -t ed25519 -C \"{email}\""])
for i in range(5):
    press_and_release("enter")

subprocess.call(["eval \"$(ssh-agent -s)\""])
subprocess.call(["ssh-add ~/.ssh/id_ed25519"])

print("Your ssh key: ", subprocess.call("cat ~/.ssh/id_ed25519.pub"))
