from util.interpreter import *
from util.general import *
import json
import os
import argparse

def analyse(test_byte_code, all_byte_codes, name): 
    interpret = Interpreter(test_byte_code, True, all_byte_codes)
    (l, s, pc) = [], [], 0
    interpret.memory = []
    ret = interpret.run((l, s, pc))
    with open(f'.\\trace-output\\{name}.txt', 'w') as f:
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
    
    if args.test:
    #if True:
        class_files = glob.glob(".\\output\\*.json", recursive=False)
        directory = os.getcwd()

        all_byte_codes = {}
        test_byte_codes = {}

        for class_file in class_files:
            if not class_file == ".\\output\\NoDependencyTest.json":
                continue
            path = pathlib.Path(class_file).name
            with open(f"{directory}\\output\\{path}", 'r') as file:
                json_obj = json.load(file)
                out1, out2= get_functions(os.path.basename(path).split(".")[0], json_obj)
                test_byte_codes.update(out1)
                all_byte_codes.update(out2)
        
        for key, test_byte_code in test_byte_codes.items():
            analyse(test_byte_code, all_byte_codes, key)

        print("analysis done")
        return
    
    print("No arguments parsed - Done")
    return


if __name__ == '__main__':
    main()
