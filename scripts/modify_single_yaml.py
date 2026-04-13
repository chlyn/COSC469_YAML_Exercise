import yaml

# This function opens a YAML file, reads its contents, changes one key, and writes the updated data into a new YAML file
# open() function opens an existing file ("r" = read and "w" = write)
# yaml.safe_load() converts YAML data into a Python object (like a dictionary)
# yaml.dump() converts Python data into a single YAML document and writes it to the file
# sort_keys=False keeps the keys in their original order (instead of sorting them alphabetically)
def read_and_modify_one_block_of_yaml_data(filename, write_file, key, value):
    with open(f"outputs/{filename}.yaml", "r") as f:
        data = yaml.safe_load(f)
        
    data[key] = value
    print(data)

    with open(f"outputs/{write_file}.yaml", "w") as file:
        yaml.dump(data, file, sort_keys=False)

    print("done!")

read_and_modify_one_block_of_yaml_data("output_write_single", "output_modify_single", key="Age", value=30)
