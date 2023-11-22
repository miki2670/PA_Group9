from util.interpreter import *
from util.general import *
import json
import os
import argparse

def analyse(java_class): 
    stdout = OutputBuffer()
    ret = run_method(java_class, "test1", [], None, stdout)
    with open(f'.\\trace-output\\test1.txt', 'w') as f:
        f.write(ret)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--compilejava", help="Compile java to json", action='store_true')
    parser.add_argument("-t", "--test", help="Test file to analyse", action='store_true')

    args = parser.parse_args()

    if args.compilejava:
        folder_path = ".\\target\\test-classes"
        folder_path_target = "\\output\\"
        analyse_bytecode(folder_path, folder_path_target)
        print("compile done")
        return
    
    #if args.test:
    if True:
        class_files = glob.glob(".\\output\\*.json", recursive=False)
        directory = os.getcwd()

        byte_codes = {}

        for class_file in class_files:
            if not class_file == ".\\output\\NoDependencyTest.json":
                continue
            path = pathlib.Path(class_file).name
            with open(f"{directory}\\output\\{path}", 'r') as file:
                json_obj = json.load(file)
                byte_codes[path] = JavaClass(json_dict=json_obj)
        
        for key, byte_code in byte_codes.items():
            analyse(byte_code)

        print("analysis done")
        return
    
    print("No arguments parsed - Done")
    return


if __name__ == '__main__':
    main()
