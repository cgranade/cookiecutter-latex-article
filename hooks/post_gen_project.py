import os
import shutil
import json
from subprocess import check_output
class Project(object):
    document_class = "{{cookiecutter.document_class}}"
    jupyter = bool("y" in "{{cookiecutter.jupyter}}")


    def __init__(self, root):
        self.root = root

    def rm(self, *path_segments):
        os.remove(os.path.join(self.root, *path_segments))

    def cp_tex(self, tex_name, *dest):
        tex_path = check_output(["kpsewhich", tex_name]).strip()
        if not tex_name:
            raise IOError("TeX resource {} not found, might need to install it first?".format(tex_name))

        shutil.copy(tex_path, os.path.join(self.root, *dest))

if __name__ == '__main__':
    project = Project(os.getcwd())

    # Copy over LaTeX deps.
    project.cp_tex("revquantum.sty", "tex")
    if project.document_class == 'quantumarticle':
        project.cp_tex('quantumarticle.cls', 'tex')

    # Remove all placeholders.
    project.rm("fig", "placeholder.txt")
    project.rm("data", "placeholder.txt")
    project.rm("src", "placeholder.txt")

    # If we don't have Jupyter support enabled, should
    # go on and remove the environment specification.
    if not project.jupyter:
        project.rm("environment.yml")

