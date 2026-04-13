import yaml

# This function opens a YAML file, reads its contents, modifies a value inside one of multiple YAML documents, and writes the updated data into a new YAML file
# open() function opens an existing file ("r" = read and "w" = write)
# yaml.safe_load_all() converts multiple YAML documents into Python objects (as a list)
# yaml.dump_all() converts a list of Python objects into multiple YAML documents in one file, separated by "---"
# sort_keys=False keeps the keys in their original order (instead of sorting them alphabetically)
def read_modify_save_yaml_data(filename, index, key, value, write_file):
    with open(f"outputs/{filename}.yaml", "r") as f:
        data = yaml.safe_load_all(f)
        loaded_data = list(data)
        
    loaded_data[index][key].append(value)

    with open(f'outputs/{write_file}.yaml', "w") as file:
        yaml.dump_all(loaded_data, file, sort_keys=False)

    print(loaded_data)

read_modify_save_yaml_data("output_write_multiple", 0, "accessModes", "ReadOnlyMany", "output_modify_multiple")
