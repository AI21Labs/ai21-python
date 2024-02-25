import subprocess

import pytest
from pathlib import Path

SAGEMAKER_DIR = "sagemaker"

SAGEMAKER_PATH = Path(__file__).parent.parent.parent.parent / "examples" / SAGEMAKER_DIR


# @pytest.mark.skip(reason="SageMaker integration tests need endpoints to be running")
@pytest.mark.parametrize(
    argnames=["test_file_name"],
    argvalues=[
        ("answer.py",),
        ("completion.py",),
        ("gec.py",),
        ("paraphrase.py",),
        ("summarization.py",),
    ],
    ids=[
        "when_answer__should_return_ok",
        "when_completion__should_return_ok",
        "when_gec__should_return_ok",
        "when_paraphrase__should_return_ok",
        "when_summarization__should_return_ok",
    ],
)
def test_sagemaker(test_file_name: str):
    file_path = SAGEMAKER_PATH / test_file_name
    print(f"About to run: {file_path}")
    exit_code = subprocess.call(["python", file_path])
    assert exit_code == 0, f"failed to run {test_file_name}"
