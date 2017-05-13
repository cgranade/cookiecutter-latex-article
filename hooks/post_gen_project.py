import os
import shutil
import json

def delete_temp(project_root):
    """
    Delete placeholder files used to represent empty directories on the cookiecutter
    repository.
    """
    for path in [
        'fig',
        'data',
        'src'
    ]:
        os.remove(os.path.join(project_root, path, 'placeholder.txt'))

if __name__ == '__main__':
    # TODO: Include conditional for tex root.
    delete_temp(os.getcwd())




