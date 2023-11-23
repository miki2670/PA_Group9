import json
import subprocess
import os
from pathlib import Path
from glob import glob
import jello

def get_all_files_from_folder(directory):
    results = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            results.append(file_path)

    return results

directory_path = './src/main/java/org/group9/'
file_list = get_all_files_from_folder(directory_path)
classes = Path("target/classes")

def jvmToJsonOriginal():
    for f in classes.glob("**/*.class"):
        result = f.relative_to(classes)
        decompiled = "bytecode/original" / result.with_suffix("").with_suffix(".json")
        decompiled.parent.mkdir(parents=True, exist_ok=True)
        result = subprocess.check_output(["jvm2json", "-s", f])

        parsed_json = json.dumps(json.loads(result)) 

        with open(decompiled, 'w') as df:
            subprocess.run(["jello", "-"], input=parsed_json, text=True, stdout=df)

def jvmToJsonChanged():
    for f in classes.glob("**/*.class"):
        result = f.relative_to(classes)
        decompiled = "bytecode/changed" / result.with_suffix("").with_suffix(".json")
        decompiled.parent.mkdir(parents=True, exist_ok=True)
        result = subprocess.check_output(["jvm2json", "-s", f])

        parsed_json = json.dumps(json.loads(result)) 

        with open(decompiled, 'w') as df:
            subprocess.run(["jello", "-"], input=parsed_json, text=True, stdout=df)
