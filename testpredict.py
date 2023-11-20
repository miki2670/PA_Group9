import os
import time
#import dependencyAnalysis
import tree_sitter
from tree_sitter import Language, Parser


Language.build_library(
  # Store the library in the `build` directory
  'build/my-languages.so',

  # Include one or more languages
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

# Example usage:
directory_path = './src/main/java/org/group9/'
file_list = get_all_files_from_folder(directory_path)

def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def get_parser(language_name):
    # Configure this function based on your specific setup
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

testsToRerun = set()

def compare_trees(tree1, tree2):
    global testsToRerun
    # Implement the comparison logic here
    class_names1 = extract_class_names(tree1)
    if len(class_names1) > 0:
        testsToRerun = testsToRerun.union(set(class_names1))

    print("tests to rerun: ", testsToRerun)

# Initialize a parser for the language (replace 'my-language' with your language, e.g., 'c')
parser = get_parser('java')

# Initialize a dictionary to store the last known code and tree for each file path
last_known_data = {path: {'code': read_file(path), 'tree': parse_code(parser, read_file(path))} for path in file_list}

# Now enter a loop that watches for changes
while True:
    for file_path in file_list:
        # Check for changes in the file's modification time
        current_code = read_file(file_path)
        if current_code != last_known_data[file_path]['code']:
            current_tree = parse_code(parser, current_code)
            compare_trees(last_known_data[file_path]['tree'], current_tree)

            # Update the last known code and tree for this file path
            last_known_data[file_path]['code'] = current_code
            last_known_data[file_path]['tree'] = current_tree

    # Wait for some time before checking again
    time.sleep(1)  # for example, check every second


