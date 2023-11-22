import os
import time
import dependencyAnalysis as Analyzer
import tree_sitter
from tree_sitter import Language, Parser

Language.build_library(
  'build/my-languages.so',
  [
    './tree-sitter-java'
  ]
)

def get_all_files_from_folder(directory):
    results = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            results.append(file_path)

    return results

directory_path = './src/main/java/org/group9/'
file_list = get_all_files_from_folder(directory_path)

def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def get_parser(language_name):
    LANGUAGE = tree_sitter.Language('build/my-languages.so', language_name)
    parser = tree_sitter.Parser()
    parser.set_language(LANGUAGE)
    return parser

def parse_code(parser, code):
    return parser.parse(code)

def extract_class_names(tree):
    cursor = tree.walk()
    class_names = []

    def traverse(node):
        if node.type == 'class_declaration' or node.type == 'interface_declaration':
            for child in node.children:
                if child.type == 'identifier':
                    class_names.append(child.text.decode('utf-8'))
                    break
        for child in node.children:
            traverse(child)

    traverse(tree.root_node)
    return class_names

changedClasses = set()
testClassesToRerun = set()

def compare_trees(tree1, tree2):
    global changedClasses
    global testClassesToRerun
    class_names1 = extract_class_names(tree1)
    if len(class_names1) > 0:
        changedClasses = changedClasses.union(set(class_names1))

    print("Changed classes: ", changedClasses)

    for testClass in Analyzer.decode_byte_strings(Analyzer.dependencies_json):
        isTestDependent = any(item in changedClasses for item in testClass['fields'])

        if isTestDependent:
            testClassesToRerun = testClassesToRerun.union(set([testClass['className']]))

    print ("Test classes to re-run: ", testClassesToRerun)

parser = get_parser('java')

# dictionary to store the last known code and tree for each file path
last_known_data = {path: {'code': read_file(path), 'tree': parse_code(parser, read_file(path))} for path in file_list}

# loop that watches for changes
while True:
    for file_path in file_list:
        # changes in the files
        current_code = read_file(file_path)
        if current_code != last_known_data[file_path]['code']:
            current_tree = parse_code(parser, current_code)
            compare_trees(last_known_data[file_path]['tree'], current_tree)

            # update last known code and tree for this file path
            last_known_data[file_path]['code'] = current_code
            last_known_data[file_path]['tree'] = current_tree

    time.sleep(1) 


