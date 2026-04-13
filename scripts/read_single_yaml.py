import yaml

# This function opens a YAML file and reads its contents
# open() function opens an existing file in read mode ("r")
# yaml.safe_load() converts YAML data into a Python object (like a dictionary)
def read_one_block_of_yaml_data(filename):
    with open(f"outputs/{filename}.yaml", "r") as f:
        output = yaml.safe_load(f)
    print(output)

read_one_block_of_yaml_data("output_write_single")
