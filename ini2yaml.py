import sys
from distutils.util import strtobool

import yaml
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader

IGNORABLE_VARS = ["inventory_file", "inventory_dir"]
output = {"all": {"children": {}}}


def convert_if_bool(obj):
    if type(obj) != str:
        return obj
    try:
        return bool(strtobool(obj))
    except ValueError:
        return obj


def parse_host(host):
    vars_dict = {}
    for var_name, var in host.vars.items():
        if host.name == "localhost":
            if not var_name in IGNORABLE_VARS:
                vars_dict[var_name] = var
        elif var != inventory.localhost.vars.get(var_name):
            vars_dict[var_name] = var
    vars_dict.update({k: convert_if_bool(v) for k, v in vars_dict.items()})
    host_dict = {host.name: vars_dict}
    return host_dict


def parse_group(group):
    group_dict = {}
    if len(group.hosts) > 0:
        group_dict["hosts"] = {}
        for host in group.hosts:
            parsed_host = parse_host(host)
            group_dict["hosts"].update(parsed_host)
    if len(group.vars) > 0:
        group_dict["vars"] = {}
        vars_dict = group.serialize()["vars"]
        vars_dict.update({k: convert_if_bool(v) for k, v in vars_dict.items()})
        group_dict["vars"].update(vars_dict)

    return group_dict


if len(sys.argv) > 1:
    inventory_path = sys.argv[1]
else:
    print("Missing inventory.ini path")
    exit(1)


loader = DataLoader()
inventory = InventoryManager(loader=loader, sources=inventory_path)

for group_name, group in inventory.groups.items():
    if group_name == "all":
        output[group_name].update(parse_group(group))
    else:
        output["all"]["children"][group_name] = parse_group(group)

print(yaml.dump(output, sort_keys=False))
