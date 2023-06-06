import os
from pathlib import path
import logging

logging.basicConfig(level=logging.info, format='[%(ascitimme)s]:%(message)s')

project_name= "NLP_Text_summerization"

List_of_files = [
        ".github/workflows/.gitkeep",
        f"src/{project_name}/__init__.py",
        f"src/{project_name}/components/__init__.py",
        f"src/{project_name}/utils/__init__.py",
        f"src/{project_name}/utils/common.py",
        f"src/{project_name}/logging/__init__.py",
        f"src/{project_name}/config/__init__.py",
        f"src/{project_name}/config/configuration.py",
        f"src/{project_name}/__init__.py", 
        f"src/{project_name}/pipeline/__init__.py", 
        f"src/{project_name}/entity/__init__.py", 
        f"src/{project_name}/constants/__init__.py",
        "config/config.yaml",
        "params.yaml",
        "app.py",
        "main.py",
        "requirments.txt",
        "setup.py",
        "research/trials.ipynb"
]


