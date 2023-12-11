"""
Run this script after setting the environment variable called API_KEY
"""

import os
import subprocess

EXAMPLE_FILES = [
    "answer.py",
    "chat.py",
    "completion.py",
    "custom_model.py",
    # 'custom_model_completion.py',
    # 'dataset.py',
    # 'embed.py',
    "gec.py",
    "improvements.py",
    "j2_mid.py",
    "paraphrase.py",
    "segmentation_base.py",
    "tokenization.py",
    "library.py",
    "library_answer.py",
]

for file_name in EXAMPLE_FILES:
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, "../examples", file_name)
    print(f"About to run: {file_path}")
    if subprocess.call(["python", file_path]):
        raise Exception(f"failed to run {file_name}")
