import os
from pathlib import Path


def get_project_path() -> Path:
    script_path = os.path.realpath(__file__)
    return Path(script_path).parent.parent


def get_md_template_path() -> Path:
    return get_project_path() / 'template' / 'template.md'
