"""
Run this script after setting the environment variable called AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
"""

import os
from pathlib import Path

import pytest
import subprocess

BEDROCK_DIR = "bedrock"

BEDROCK_PATH = Path("../../") / "examples" / BEDROCK_DIR


@pytest.mark.parametrize(
    argnames=["test_file_name"],
    argvalues=[
        ("completion.py",),
    ],
    ids=[
        "when_completion__should_return_ok",
    ],
)
def test_bedrock(test_file_name: str):
    file_path = BEDROCK_PATH / test_file_name
    print(f"About to run: {file_path}")
    exit_code = subprocess.call(["python", file_path])
    assert exit_code == 0, f"failed to run {test_file_name}"
