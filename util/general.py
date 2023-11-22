import glob
import pathlib
import subprocess
import os

def get_paths(folder_path):
    return glob.glob(folder_path + '/**/*.json', recursive = True)


def get_function_bytecode(json_obj):
    return json_obj['code']


def get_functions(file_name, json_obj):
    all_functions = {}
    functions = {}
    for func in json_obj['methods']:
        is_case = False
        for annotation in func['annotations']:
            if annotation['type'] == 'org/junit/jupiter/api/Test':
                is_case = True
                break
        if not is_case:
            all_functions[file_name + "_" + func['name']] = get_function_bytecode(func)
            continue
        functions[file_name + "_" + func['name']] = get_function_bytecode(func)
    return functions, all_functions


def analyse_bytecode(folder_path, target_folder_path):
    # This function analyzes Java bytecode files (.class) using the jvm2json tool. It takes a folder path as input, finds all .class files in the specified folder and its subdirectories, and then uses the subprocess module to run the jvm2json tool to convert each .class file into a corresponding JSON file (.json).
    class_files = glob.glob(folder_path + '/**/*.class', recursive=True)
    directory = os.getcwd()

    for class_file in class_files:
        path = pathlib.Path(class_file)
        json_file = path.name
        json_file = json_file.replace('.class', '.json')
        command = [
            "C:\\Users\\jonas\\AppData\\Roaming\\local\\bin\\jvm2json.exe",
            "-s", path.resolve(),
            "-t", f"{directory}{target_folder_path}{json_file}"
        ]

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell= True)
        print(result)


def lists_equal(list1, list2):
    if list1 is None or list2 is None:
        return False

    if len(list1) != len(list2):
        return False

    for rs1, rs2 in zip(list1, list2):
        if rs1 != rs2:
            return False

    return True