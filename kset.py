#!/usr/bin/env python3

import os
import yaml
import getpass
from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Available environments")
table.add_column("#", justify="center", style="cyan")
table.add_column("Cluster name", style="magenta")
table.add_column("URL", justify="left", style="green", no_wrap=True)

def get_env_info(conf_path):
    with open(conf_path) as file:
        documents = yaml.full_load(file)
        return documents["clusters"][0]["name"], documents["clusters"][0]["cluster"]["server"]

def main():

    kset_directory = os.path.dirname(__file__)

    # Config files
    conf_files = [os.path.expanduser("~/.kube/config")]
    conf_files += [os.path.join(kset_directory, "configs/", conf) for conf in os.listdir(os.path.join(kset_directory, "configs/")) if conf.endswith('.conf')]

    for index, item in enumerate(conf_files):
        table.add_row(str(index + 1), get_env_info(item)[0], get_env_info(item)[1])

    print("\n")
    console.print(table)

    chosen = input("\nChoose one (or press Enter for local) > ") or "1"

    if chosen.isdigit() and 0 < int(chosen) <= len(conf_files) + 1:
        console.print("\n:OK_hand: [bold]Loading[/] ", conf_files[int(chosen)-1], "\n")
        return "export KUBECONFIG=" + conf_files[int(chosen) - 1]
    else:
        console.print("\n:cross_mark: [bold]Wrong choice:[/] environment not updated\n")
        return ""

if __name__ == "__main__":

    kset_directory = os.path.dirname(__file__)
    #username = os.getlogin() # https://bugs.python.org/issue40821
    username = getpass.getuser()
    aux_file = ".{}_aux".format(username)

    with open(os.path.join("/tmp", aux_file),"w") as f:
        f.write(main())
