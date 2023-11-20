import os
import json
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

def get_parser(language_name):
    # Configure this function based on your specific setup
    LANGUAGE = tree_sitter.Language('build/my-languages.so', language_name)
    parser = tree_sitter.Parser()
    parser.set_language(LANGUAGE)
    return parser

parser = get_parser('java')

def parse_code(parser, code):
    return parser.parse(code)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def get_all_files_from_folder(directory):
    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

def traverse(node, final_json):
    if node.type == "program":
        name = ""
        inner_classes = []
        content = ""
        realizations = ""
        inheritance = ""
        aggregation = []
        imports = []
        package = ""
        for child in node.children:
            class_name = extract_class_names(child)
            implements = extract_inheritance(child)
            extends = extract_inheritance(child)
            class_content = extract_class_content(child)
            class_imports = extract_class_imports(child)
            class_package = extract_class_package(child)
            if class_name:
                name = class_name
            if implements:
                realizations = implements.lower() if "implements" in implements.lower() else ""
            if extends:
                inheritance = extends.lower() if "extends" in extends.lower() else ""
            if class_content:
                content = class_content
                classes = re.findall(r'(?:[A-Z][a-zA-Z1-9]*) (?:[a-z][a-zA-Z1-9]*) =', content)
                aggregation = [c.split()[0] for c in classes] if classes else []
                inner_class = [m.children[2].text for m in child.body_node.children if m.type == 'class_declaration']
                inner_classes = inner_class
            if class_imports:
                imports.append(class_imports)
            if class_package:
                package = class_package
        final_json.append({
            'className': name,
            'innerClasses': inner_classes,
            'realizations': realizations,
            'inheritance': inheritance,
            'aggregation': aggregation,
            'classContent': content,
            'imports': imports,
            'package': package
        })

def extract_class_names(node):
    if node.type == "class_declaration":
        return node.children[2].text  # Assuming the class name is the third child
    return None

def extract_inheritance(node):
    if node.type == "class_declaration":
        return node.children[3].text  # Assuming the inheritance is the fourth child
    return None

def extract_class_content(node):
    if node.type == "class_declaration":
        return node.text
    return None

def extract_class_imports(node):
    if node.type == "import_declaration":
        return node.text
    return None

def extract_class_package(node):
    if node.type == "package_declaration":
        return node.text
    return None

files = get_all_files_from_folder('./src/main/java/org/group9/')
final_json = []

for file_path in files:
    content = read_file(file_path)
    tree = parse_code(parser, content)
    traverse(tree.root_node, final_json)

with open('./test.json', 'w') as json_file:
    json.dump(final_json, json_file)
