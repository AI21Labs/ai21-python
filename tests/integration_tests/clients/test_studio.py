"""
Run this script after setting the environment variable called AI21_API_KEY
"""

from pathlib import Path
from time import sleep

import pytest
import subprocess

from tests.integration_tests.skip_helpers import should_skip_studio_integration_tests

STUDIO_PATH = Path(__file__).parent.parent.parent.parent / "examples" / "studio"


@pytest.mark.skipif(should_skip_studio_integration_tests(), reason="No key supplied for AI21 Studio. Skipping.")
@pytest.mark.parametrize(
    argnames=["test_file_name"],
    argvalues=[
        ("tokenization.py",),
        ("chat/chat_completions.py",),
        ("chat/chat_completions_jamba_instruct.py",),
        ("chat/stream_chat_completions.py",),
        ("chat/chat_documents.py",),
        ("chat/chat_function_calling.py",),
        ("chat/chat_function_calling_multiple_tools.py",),
        ("chat/chat_response_format.py",),
        ("assistant/user_defined_plans.py",),
    ],
    ids=[
        "when_tokenization__should_return_ok",
        "when_chat_completions__should_return_ok",
        "when_chat_completions_jamba_instruct__should_return_ok",
        "when_stream_chat_completions__should_return_ok",
        "when_chat_completions_with_documents__should_return_ok",
        "when_chat_completions_with_function_calling__should_return_ok",
        "when_chat_completions_with_function_calling_multiple_tools_should_return_ok",
        "when_chat_completions_with_response_format__should_return_ok",
        "when_assistant_with_user_defined_plans_should_return_ok",
    ],
)
def test_studio(test_file_name: str):
    file_path = STUDIO_PATH / test_file_name
    print(f"About to run: {file_path}")
    sleep(0.5)
    exit_code = subprocess.call(["python", file_path])
    assert exit_code == 0, f"failed to run {test_file_name}"


@pytest.mark.asyncio
@pytest.mark.skipif(should_skip_studio_integration_tests(), reason="No key supplied for AI21 Studio. Skipping.")
@pytest.mark.parametrize(
    argnames=["test_file_name"],
    argvalues=[
        ("async_chat.py",),
        ("chat/async_chat_completions.py",),
        ("chat/async_stream_chat_completions.py",),
        ("conversational_rag/conversational_rag.py",),
        ("conversational_rag/async_conversational_rag.py",),
        ("assistant/assistant.py",),
        ("assistant/async_assistant.py",),
    ],
    ids=[
        "when_chat__should_return_ok",
        "when_chat_completions__should_return_ok",
        "when_stream_chat_completions__should_return_ok",
        "when_conversational_rag__should_return_ok",
        "when_async_conversational_rag__should_return_ok",
        "when_assistant__should_return_ok",
        "when_async_assistant__should_return_ok",
    ],
)
async def test_async_studio(test_file_name: str):
    file_path = STUDIO_PATH / test_file_name
    print(f"About to run: {file_path}")
    exit_code = subprocess.call(["python", file_path])
    assert exit_code == 0, f"failed to run {test_file_name}"
