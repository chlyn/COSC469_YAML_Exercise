import yaml
import json

# This function reads a YAML file, converts it into a Python object, and then writes it into a JSON file
# yaml.safe_load() converts YAML data into a Python object (like a dictionary)
# json.dump() converts the Python object into JSON format and writes it to a file
# indent=3 formats the JSON output for better readability
def convert_yaml_to_json(yfile, jfile):
    with open(f"{yfile}.yaml", "r") as f:
        yaml_file = yaml.safe_load(f)

    with open(f"{jfile}.json", "w") as json_file:
        json.dump(yaml_file, json_file, indent=3)

    print("done!")

convert_yaml_to_json("output_write_single", "output_convert_to_json")
