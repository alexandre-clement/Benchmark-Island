from main import *

import os
import subprocess
import glob
import shutil


class changeDir:
    def __init__(self, new_path):
        self.newPath = os.path.expanduser(new_path)

    # Change directory with the new path
    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)
        return self

    # Return back to previous directory
    def __exit__(self, e_type, value, traceback):
        os.chdir(self.savedPath)


def play_all_map():
    with changeDir(Path.java_path) as change:
        subprocess.call(["mvn", "clean", "install", ], shell=True)
        pass

    for json_file in glob.glob(os.path.join(change.newPath, "map/*.json")):
        print("_" * 90)
        print()
        print(os.path.basename(json_file))
        print()
        with changeDir(Path.java_path) as change:
            os.system("mvn exec:java -Dexec.args=" + json_file)
            pass
        shutil.copy(os.path.join(change.newPath, Path.outputs_folder, Path.default_name), Path.source_path)
        shutil.move(os.path.join(Path.source_path, Path.default_name), os.path.join(Path.source_path + os.path.basename(json_file)))
        print()
        print(os.path.basename(json_file) + " copy done")
        print()


if __name__ == '__main__':
    play_all_map()
