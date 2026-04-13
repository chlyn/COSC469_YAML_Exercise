import yaml

data = {
    "Name": "Chenilyn Joy Espineda",
    "Position": "UX Designer",
    "Location": "USA",
    "Age": "21",
    "Experience": {
        "GitHub": "Software Engineer",
        "Google": "Technical Engineer",
        "Linkedin": "Data Analyst"
    },
    "Languages": {
        "Markup": ["HTML"],
        "Programming": ["Python", "JavaScript", "Golang"]
    }
}

# This function takes Python data, opens a YAML file, and writes it into a YAML file
# open() function opens or creates a file in write mode ("w")
# yaml.dump() converts Python data into a single YAML document and writes it to the file
# sort_keys=False keeps the keys in their original order (instead of sorting them alphabetically)
def write_one_block_of_yaml_data(py_obj, filename):
    with open(f"outputs/{filename}.yaml", "w") as f:
        yaml.dump(py_obj, f, sort_keys=False)
    print("Written to file successfully")

write_one_block_of_yaml_data(data, "output_write_single")
