"""
Run this script after setting the environment variable called AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
"""

import subprocess
from pathlib import Path

import pytest

from tests.integration_tests.skip_helpers import should_skip_bedrock_integration_tests

BEDROCK_DIR = "bedrock"

BEDROCK_PATH = Path(__file__).parent.parent.parent.parent / "examples" / BEDROCK_DIR


@pytest.mark.skipif(should_skip_bedrock_integration_tests(), reason="No keys supplied for AWS. Skipping.")
@pytest.mark.parametrize(
    argnames=["test_file_name"],
    argvalues=[
        ("completion.py",),
        ("async_completion.py",),
        ("chat/chat_completions.py",),
        ("chat/async_chat_completions.py",),
    ],
    ids=[
        "when_completion__should_return_ok",
        "when_async_completion__should_return_ok",
        "when_chat_completions__should_return_ok",
        "when_async_chat_completions__should_return_ok",
    ],
)
def test_bedrock(test_file_name: str):
    file_path = BEDROCK_PATH / test_file_name
    print(f"About to run: {file_path}")
    exit_code = subprocess.call(["python", file_path])
    assert exit_code == 0, f"failed to run {test_file_name}"
