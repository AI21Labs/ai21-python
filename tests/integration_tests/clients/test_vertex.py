"""
Run this script after setting the environment variable called AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
"""

import subprocess
from pathlib import Path

import pytest

from tests.integration_tests.skip_helpers import should_skip_vertex_integration_tests

VERTEX_DIR = "vertex"

VERTEX_PATH = Path(__file__).parent.parent.parent.parent / "examples" / VERTEX_DIR


@pytest.mark.skipif(should_skip_vertex_integration_tests(), reason="No keys supplied for Vertex. Skipping.")
@pytest.mark.parametrize(
    argnames=["test_file_name"],
    argvalues=[
        ("chat_completions.py",),
        ("async_chat_completions.py",),
    ],
    ids=[
        "when_chat_completions__should_return_ok",
        "when_async_chat_completions__should_return_ok",
    ],
)
def test_vertex(test_file_name: str):
    file_path = VERTEX_PATH / test_file_name
    print(f"About to run: {file_path}")
    exit_code = subprocess.call(["python", file_path])
    assert exit_code == 0, f"failed to run {test_file_name}"
