import os
import shutil
import json
class Project(object):
    def __init__(self, root):
        self.root = root
        with open(os.path.join(self.root, "options.json")) as f:
            self.config = json.load(f)

    def rm(self, *path_segments):
        os.remove(os.path.join(self.root, *path_segments))

if __name__ == '__main__':
    project = Project(os.getcwd())

    # Remove all placeholders.
    project.rm("fig", "placeholder.txt")
    project.rm("data", "placeholder.txt")
    project.rm("src", "placeholder.txt")

    # If we don't have Jupyter support enabled, should
    # go on and remove the environment specification.
    if not "y" in project.config['jupyter']:
        project.rm("environment.yml")
