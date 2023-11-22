import os
import json
import re
import tree_sitter
from tree_sitter import Language, Parser

Language.build_library(
  'build/my-languages.so',
  [
    './tree-sitter-java'
  ]
)

def get_parser(language_name):
    LANGUAGE = tree_sitter.Language('build/my-languages.so', language_name)
    parser = tree_sitter.Parser()
    parser.set_language(LANGUAGE)
    return parser

parser = get_parser('java')

def parse_code(parser, code):
    return parser.parse(code)

def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def get_all_files_from_folder(directory):
    results = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            results.append(file_path)

    return results

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
        class_fields = []
        for child in node.children:
            class_name = extract_class_names(child)
            implements = extract_inheritance(child)
            extends = extract_inheritance(child)
            class_content = extract_class_content(child)
            class_imports = extract_class_imports(child)
            class_package = extract_class_package(child)
            fields = extract_fields(child)
            if class_name:
                name = class_name
            if implements:
                realizations = implements.lower() if "implements" in str(implements.lower()) else ""
            if extends:
                inheritance = extends.lower() if "extends" in str(extends.lower()) else ""
            if class_content:
                content = class_content
                classes = re.findall(r'(?:[A-Z][a-zA-Z1-9]*) (?:[a-z][a-zA-Z1-9]*) =', str(content))
                aggregation = [c.split()[0] for c in classes] if classes else []
                if (hasattr(child, "body_node")):
                    inner_class = [m.children[2].text for m in child.body_node.children if m.type == 'class_declaration']
                    inner_classes = inner_class
            if class_imports:
                imports.append(class_imports)
            if class_package:
                package = class_package
            if fields:
                class_fields = fields
        final_json.append({
            'className': name,
            'fields': class_fields,
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
        if (node.children[2].type == "identifier"):
            return node.children[2].text
        else: 
            return node.children[1].text
    return None

def extract_inheritance(node):
    if node.type == "class_declaration" and len(node.children) > 3 and ("implements" in str(node.children[3].text) or ("extends" in str(node.children[3].text))):
        return node.children[3].text
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

def extract_fields(node):
    fields = []
    if node.type == "class_declaration":
        for child in node.children:
            if child.type == "class_body":
                for child2 in child.children: 
                    if child2.type == "field_declaration":
                        for child3 in child2.children:
                            if child3.type == "type_identifier":
                                fields.append(child3.text)
    return fields

files = get_all_files_from_folder('./src/test/java/')
dependencies_json = []

for file_path in files:
    content = read_file(file_path)
    tree = parse_code(parser, content)
    traverse(tree.root_node, dependencies_json)

def decode_byte_strings(obj):
    if isinstance(obj, bytes):
        return obj.decode('utf-8')
    elif isinstance(obj, list):
        return [decode_byte_strings(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: decode_byte_strings(value) for key, value in obj.items()}
    else:
        return obj

with open('./test.json', 'w') as json_file:
    json.dump(decode_byte_strings(dependencies_json), json_file)

