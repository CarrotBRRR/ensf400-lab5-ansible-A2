# File Name: run_playbook.py

import ansible_runner
import urllib.request

with open("./secrets/id_rsa", "r") as f:
    ssh_key = f.read()

r = ansible_runner.run(private_data_dir=".", playbook='./hello.yml', inventory='./hosts.yml', ssh_key=ssh_key)

for i in range(6):
    response = urllib.request.urlopen("http://0.0.0.0")
    message = response.read().decode("utf-8")
    print(message)
