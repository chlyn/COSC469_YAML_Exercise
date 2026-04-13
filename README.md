# COSC469: YAML Exercise

This project demonstrates how to create, write, read, modify, and convert YAML data using Python and the PyYAML library.

---

## Features

### 🟢 Creating YAML in Python  
**File:** `create_yaml.py`  

Creates a Python dictionary and converts it into YAML format using `yaml.dump()` for display in the terminal.  
- `sort_keys=False` keeps the keys in the same order (not alphabetically by default)  

### 🟢 Writing YAML to a File in Python  

#### Single Block  
**File:** `write_single_yaml.py`  

Writes a Python dictionary into a YAML file.  
- Uses `open(..., "w")` to create/write a file  
- Uses `yaml.dump()` to convert Python data into a single YAML document  
- Output file: `output_write_single.yaml`  

#### Multiple Blocks  
**File:** `write_multiple_yaml.py`  

Writes multiple YAML documents from a list.  
- Uses `open(..., "w")` to create/write a file  
- Uses `yaml.dump_all()` to convert multiple Python objects into YAML documents  
- Documents are separated by `---`  
- Output file: `output_write_multiple.yaml`  

### 🟢 Reading YAML in Python

#### Single Block  
**File:** `read_single_yaml.py`

Reads a YAML file and converts it into a Python dictionary.  
- Uses `open(..., "r")` to read a file  
- Uses `yaml.safe_load()` to convert YAML → Python  

#### Multiple Blocks  
**File:** `read_multiple_yaml.py`  

Reads multiple YAML documents and converts them into a list of Python objects.  
- Uses `open(..., "r")` to read a file  
- Uses `yaml.safe_load_all()` and converts the result into a list  

### 🟢 Modifying YAML in Python

#### Single Block  
**File:** `modify_single_yaml.py`

Reads a YAML file, modifies a key value (`Age`), and writes the updated data into a new YAML file.  
- Uses `yaml.safe_load()` to read YAML  
- Updates data using dictionary assignment  
- Uses `yaml.dump()` to write updated YAML  
- Output file: `output_modify_single.yaml`  

#### Multiple Blocks  
**File:** `modify_multiple_yaml.py`  

Modifies data within one YAML document in a list and writes all updated documents.  
- Uses `yaml.safe_load_all()` to load multiple documents  
- Converts data into a list for modification  
- Uses `.append()` to update list values  
- Uses `yaml.dump_all()` to write all YAML documents  
- Output file: `output_modify_multiple.yaml` 

### 🟢 Converting YAML to JSON

**File:** `convert_yaml_to_json.py`

Converts YAML data into JSON format.  
- Uses `yaml.safe_load()` to convert YAML → Python  
- Uses `json.dump()` to convert Python → JSON  
- Uses `indent=3` for better readability  
- Output file: `output_convert_to_json.json` 

---

## How to Run

Run scripts from the project root directory:

```bash
python3 scripts/<FILE_NAME>.py
```