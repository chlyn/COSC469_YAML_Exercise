# COSC469: YAML Exercise

This project demonstrates how to create, write, read, modify, and convert YAML data using Python and the PyYAML library.

### Course Information
**By:** Chenilyn Joy Espineda<br>
**Course:** COSC 469-101<br>
**Instructor:** Dr. Appolo Tankeh

---

## ⭐️ Features

### I. Creating YAML in Python  
**File:** `create_yaml.py`  

Creates a Python dictionary and converts it into YAML format using `yaml.dump()` for display in the terminal.  
- `sort_keys=False` keeps the keys in the same order (not alphabetically by default)  

<br>

### II. Writing YAML to a File in Python  

#### 🔹 Single Block  
**File:** `write_single_yaml.py`  

Writes a Python dictionary into a YAML file.  
- Uses `open(..., "w")` to create/write a file  
- Uses `yaml.dump()` to convert Python data into a single YAML document  
- Output file: `output_write_single.yaml`  

#### 🔹  Multiple Blocks  
**File:** `write_multiple_yaml.py`  

Writes multiple YAML documents from a list.  
- Uses `open(..., "w")` to create/write a file  
- Uses `yaml.dump_all()` to convert multiple Python objects into YAML documents  
- Documents are separated by `---`  
- Output file: `output_write_multiple.yaml`  

<br>

### III. Reading YAML in Python

#### 🔹 Single Block  
**File:** `read_single_yaml.py`

Reads a YAML file and converts it into a Python dictionary.  
- Uses `open(..., "r")` to read a file  
- Uses `yaml.safe_load()` to convert YAML → Python  

#### 🔹 Multiple Blocks  
**File:** `read_multiple_yaml.py`  

Reads multiple YAML documents and converts them into a list of Python objects.  
- Uses `open(..., "r")` to read a file  
- Uses `yaml.safe_load_all()` and converts the result into a list

<br>

### IV. Modifying YAML in Python

#### 🔹 Single Block  
**File:** `modify_single_yaml.py`

Reads a YAML file, modifies a key value (`Age`), and writes the updated data into a new YAML file.  
- Uses `yaml.safe_load()` to read YAML  
- Updates data using dictionary assignment  
- Uses `yaml.dump()` to write updated YAML  
- Output file: `output_modify_single.yaml`  

#### 🔹 Multiple Blocks  
**File:** `modify_multiple_yaml.py`  

Modifies data within one YAML document in a list and writes all updated documents.  
- Uses `yaml.safe_load_all()` to load multiple documents  
- Converts data into a list for modification  
- Uses `.append()` to update list values  
- Uses `yaml.dump_all()` to write all YAML documents  
- Output file: `output_modify_multiple.yaml` 

<br>

### V. Converting YAML to JSON

**File:** `convert_yaml_to_json.py`

Converts YAML data into JSON format.  
- Uses `yaml.safe_load()` to convert YAML → Python  
- Uses `json.dump()` to convert Python → JSON  
- Uses `indent=3` for better readability  
- Output file: `output_convert_to_json.json` 

---

## 👉 How to Run

Run scripts from the project root directory:

```bash
python3 scripts/<FILE_NAME>.py
```

---

## 🚀 DevOps Automation

### I. GitHub to GitLab Synchronization

This project is connected between GitHub and GitLab using GitHub Actions. Every push to the `main` branch on GitHub automatically syncs the repository to GitLab.

**Workflow File Location:** `.github/workflows/sync-to-gitlab.yml`

#### Setup Steps

1. Create a new repository in GitHub
2. Create a new project in your GitLab group to receive the synced repository files
3. In GitLab, go to `User Settings → Access → Personal Access Tokens`
4. Click `Generate token`, then select `Legacy token`. 
5. Enter a token name (e.g., github-sync-cosc469-gitlab)
6. Enable the `write_repository` permission so GitHub could push updates into GitLab
7. Click `Generate token`
8. Copy the generated token
9. In GitHub, open your repository settings: `Repository → Settings → Secrets and variables → Actions`
10. Click `New repository secret`
11. Enter the secrect name (e.g., GITLAB_TOKEN)
12. Paste the GitLab token into the secret value field
13. Click `Add secret`
14. Create the workflow file `.github/workflows/sync-to-gitlab.yml` and configure the sync process
15. Push changes to the main branch to automatically sync GitHub to GitLab