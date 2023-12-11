from openai import OpenAI


def supported_resources():
    from ai21 import (
        Completion,
        Dataset,
        CustomModel,
        Paraphrase,
        Tokenization,
        Summarize,
        SummarizeBySegment,
        Segmentation,
        Improvements,
        GEC,
        SageMaker,
        Chat,
    )

    return {
        "completion": Completion,
        "tokenization": Tokenization,
        "dataset": Dataset,
        "customModel": CustomModel,
        "paraphrase": Paraphrase,
        "summarization": Summarize,
        "summarizeBySegment": SummarizeBySegment,
        "segmentation": Segmentation,
        "improvements": Improvements,
        "gec": GEC,
        "sagemaker": SageMaker,
        "chat": Chat,
    }
