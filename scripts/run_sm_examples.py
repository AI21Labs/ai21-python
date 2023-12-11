"""
You need to be authenticated to the AWS when you run this and make sure the endpoints are there
"""

import subprocess
from pathlib import Path

SAGEMAKER_EXAMPLE_FILES = [
    "answer_sm.py",
    "completion_sm.py",
    "completion_sm_destination.py",
    "completion_sm_injected_session.py",
    "gec_sm.py",
    # 'launch_sm_model.py',
    "paraphrase_sm.py",
    "summarization_sm.py",
]

SAGEMAKER_DIR = "sagemaker"

for example_file_name in SAGEMAKER_EXAMPLE_FILES:
    if subprocess.call(
        ["python", Path("..") / "examples" / SAGEMAKER_DIR / example_file_name]
    ):
        raise Exception(f"failed to run {example_file_name}")
