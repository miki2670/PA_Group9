import os
import time
import dependencyAnalysis as Analyzer
import tree_sitter
import interpreter as Interpreter
import jvmtojson as JvmToJson
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

def extract_method_names(tree):
    method_names = set()

    def traverse(node):
        if node.type == 'method_declaration':
            for child in node.children:
                if child.type == 'identifier':
                    method_names.add(child.text.decode('utf-8'))

        for child in node.children:
            traverse(child)

    traverse(tree.root_node)
    return method_names

def extract_package_name(tree):
    def traverse(node):
        if node.type == 'package_declaration':
            parts = (node.text.decode('utf-8')).split()
            index = parts.index('package')
            package_name = '.'.join(parts[index + 1:]).rstrip(';')
            return package_name.replace('.', '/')
        for child in node.children:
            result = traverse(child)
            if result:
                return result

    return traverse(tree.root_node)

def extract_class_name(tree):
    def traverse(node):
        if node.type == 'class_declaration' or node.type == 'interface_declaration':
            for child in node.children:
                if child.type == 'identifier':
                    return child.text.decode('utf-8')
        for child in node.children:
            result = traverse(child)
            if result:
                return result

    return traverse(tree.root_node)

def walk_tree(node, code):
    methods = {}
    def inner_walk_tree(inner_node):
        for child in inner_node.children:
            if child.type == 'method_declaration':
                method_name = child.child_by_field_name('name')
                if method_name:
                    method_name_text = method_name.text.decode('utf8')
                    methods[method_name_text] = code[child.start_byte:child.end_byte]
            inner_walk_tree(child)
    inner_walk_tree(node)
    return methods

changedClasses = set()
testClassesToRerun = set()

def compare_trees(original_tree, changed_tree, original_code, changed_code):
    global changedClasses
    global testClassesToRerun

    changed_package = extract_package_name(changed_tree)
    changed_class = extract_class_name(changed_tree)

    old_methods = walk_tree(original_tree.root_node, original_code)
    new_methods = walk_tree(changed_tree.root_node, changed_code)

    modified = []
    for method_name in old_methods:
        if old_methods[method_name] != new_methods[method_name]:
            modified.append(method_name)

    print("Modified methods:", modified)

    changedClasses = changedClasses.union(set(changed_class))

    print("Changed classes:", changedClasses)

    for testClass in Analyzer.decode_byte_strings(Analyzer.dependencies_json):
        isTestDependent = any(item in changedClasses for item in testClass['fields'])

        if isTestDependent:
            testClassesToRerun.add(testClass['className'])

    print("Test classes to re-run:", testClassesToRerun)

    for changed_method in modified:
        print("---", "("+changed_package+"/"+changed_class+","+changed_method+")", "--- INTERPRETING ORIGINAL")
        trace_of_original_method = Interpreter.bytecode_interp((changed_package+"/"+changed_class, changed_method), print, False)
        JvmToJson.jvmToJsonChanged()
        print("---", "("+changed_package+"/"+changed_class+","+changed_method+")", "--- INTERPRETING CHANGES")
        trace_of_changed_method = Interpreter.bytecode_interp((changed_package+"/"+changed_class, changed_method), print, True)
        print("ORIGINAL METHOD TRACE: ", trace_of_original_method)
        print("CHANGED METHOD TRACE: ", trace_of_changed_method)
        print("--- done ---")

        if (trace_of_original_method != trace_of_changed_method):
            print ("Change detection analysis is sound")
    
parser = get_parser('java')

# dictionary to store the last known code and tree for each file path
last_known_data = {path: {'code': read_file(path), 'tree': parse_code(parser, read_file(path))} for path in file_list}

# loop that watches for changes
while True:
    for file_path in file_list:
        current_code = read_file(file_path)
        if current_code != last_known_data[file_path]['code']:
            current_tree = parse_code(parser, current_code)
            # Pass both the tree and the corresponding code as a string
            compare_trees(last_known_data[file_path]['tree'], current_tree, last_known_data[file_path]['code'].decode('utf-8'), current_code.decode('utf-8'))

            # Update the last known data
            last_known_data[file_path]['code'] = current_code
            last_known_data[file_path]['tree'] = current_tree

    time.sleep(1)


