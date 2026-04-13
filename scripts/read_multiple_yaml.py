import yaml

# This function opens a YAML file and reads multiple YAML documents
# open() function opens an existing file in read mode ("r")
# yaml.safe_load_all() converts multiple YAML documents into Python objects (as a list)
def read_multiple_block_of_yaml_data(filename):
    with open(f"outputs/{filename}.yaml", "r") as f:
        output = list(yaml.safe_load_all(f))
    print(output)

read_multiple_block_of_yaml_data("output_write_multiple")
