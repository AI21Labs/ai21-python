"""
Run this script after setting the environment variable called AI21_API_KEY
"""

import os
from pathlib import Path

import pytest
import subprocess

STUDIO_PATH = Path(__file__).parent.parent.parent / "examples" / "studio"


@pytest.mark.parametrize(
    argnames=["test_file_name"],
    argvalues=[
        ("answer.py",),
        ("chat.py",),
        ("completion.py",),
        ("embed.py",),
        ("gec.py",),
        ("improvements.py",),
        ("paraphrase.py",),
        ("segmentation.py",),
        ("summarize.py",),
        ("summarize_by_segment.py",),
        ("tokenization.py",),
        # ("custom_model.py", ),
        # ('custom_model_completion.py', ),
        # ("dataset.py", ),
        # ("library.py", ),
        # ("library_answer.py", ),
    ],
    ids=[
        "when_answer__should_return_ok",
        "when_chat__should_return_ok",
        "when_completion__should_return_ok",
        "when_embed__should_return_ok",
        "when_gec__should_return_ok",
        "when_improvements__should_return_ok",
        "when_paraphrase__should_return_ok",
        "when_segmentation__should_return_ok",
        "when_summarize__should_return_ok",
        "when_summarize_by_segment__should_return_ok",
        "when_tokenization__should_return_ok",
        # "when_custom_model__should_return_ok",
        # "when_custom_model_completion__should_return_ok",
        # "when_dataset__should_return_ok",
        # "when_library__should_return_ok",
        # "when_library_answer__should_return_ok",
    ],
)
def test_studio(test_file_name: str):
    file_path = STUDIO_PATH / test_file_name
    print(f"About to run: {file_path}")
    exit_code = subprocess.call(["python", file_path])
    assert exit_code == 0, f"failed to run {test_file_name}"
