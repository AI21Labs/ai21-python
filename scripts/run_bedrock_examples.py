"""
You need to be authenticated to the AWS when you run this
"""

import subprocess
from pathlib import Path

SAGEMAKER_EXAMPLE_FILES = [
    "completion_bedrock_destination.py",
]

BEDROCK_DIR = "bedrock"

for example_file_name in SAGEMAKER_EXAMPLE_FILES:
    if subprocess.call(["python", Path("..") / "examples" / BEDROCK_DIR / example_file_name]):
        raise Exception(f"failed to run {example_file_name}")
