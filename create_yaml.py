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

# yaml.dump() converts Python data into YAML format
# sort_keys=False keeps your keys in the same order (not alphabetically by default)
yaml_output = yaml.dump(data, sort_keys=False)
print(yaml_output)
