import yaml

data = [
    {
    'apiVersion': 'v1',
    'kind':'persistentVolume',
    'metadata': {'name':'mongodb-pv', 'labels':{'type':'local'}},
    'spec':{'storageClassName':'hostpath'},
    'capacity':{'storage':'3Gi'},
    'accessModes':['ReadWriteOnce'],
    'hostpath':{'path':'/mnt/data'}
    },

    {
    'apiVersion': 'v1',
    'kind':'persistentVolume',
    'metadata': {'name':'mysql-pv', 'labels':{'type':'local'}},
    'spec':{'storageClassName':'hostpath'},
    'capacity':{'storage':'2Gi'},
    'accessModes':['ReadWriteOnce'],
    'hostpath':{'path':'/mnt/data'}
    }
]

# This function takes Python data, opens a YAML file, and writes it into a YAML file
# open() function opens or creates a file in write mode ("w")
# yaml.dump_all() converts a list of Python objects into multiple YAML documents in one file, separated by "---"
# sort_keys=False keeps the keys in their original order (instead of sorting them alphabetically)
def write_multiple_block_of_yaml_data(py_obj, filename) :
    with open(f"{filename}.yaml", "w",) as f :
        yaml.dump_all(py_obj,f,sort_keys=False)
    print('written to file successfully')
write_multiple_block_of_yaml_data(data, 'output_write_multiple')
