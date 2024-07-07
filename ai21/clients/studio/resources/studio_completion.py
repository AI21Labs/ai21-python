from __future__ import annotations

from typing import List, Dict, Optional

from ai21.clients.common.completion_base import Completion
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models import Penalty, CompletionsResponse
from ai21.types import NOT_GIVEN, NotGiven


class StudioCompletion(StudioResource, Completion):
    def create(
        self,
        prompt: str,
        *,
        model: Optional[str] = None,
        max_tokens: int | NotGiven = NOT_GIVEN,
        num_results: int | NotGiven = NOT_GIVEN,
        min_tokens: int | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        top_k_return: int | NotGiven = NOT_GIVEN,
        custom_model: str | NotGiven = NOT_GIVEN,
        stop_sequences: List[str] | NotGiven = NOT_GIVEN,
        frequency_penalty: Penalty | NotGiven = NOT_GIVEN,
        presence_penalty: Penalty | NotGiven = NOT_GIVEN,
        count_penalty: Penalty | NotGiven = NOT_GIVEN,
        epoch: int | NotGiven = NOT_GIVEN,
        logit_bias: Dict[str, float] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> CompletionsResponse:
        model = self._get_model(model=model, model_id=kwargs.pop("model_id", None))
        path = self._get_completion_path(model=model, custom_model=custom_model)
        body = self._create_body(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens,
            num_results=num_results,
            min_tokens=min_tokens,
            temperature=temperature,
            top_p=top_p,
            top_k_return=top_k_return,
            custom_model=custom_model,
            stop_sequences=stop_sequences,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            count_penalty=count_penalty,
            epoch=epoch,
            logit_bias=logit_bias,
            **kwargs,
        )
        return self._post(path=path, body=body, response_cls=CompletionsResponse)


class AsyncStudioCompletion(AsyncStudioResource, Completion):
    async def create(
        self,
        prompt: str,
        *,
        model: Optional[str] = None,
        max_tokens: int | NotGiven = NOT_GIVEN,
        num_results: int | NotGiven = NOT_GIVEN,
        min_tokens: int | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        top_k_return: int | NotGiven = NOT_GIVEN,
        custom_model: str | NotGiven = NOT_GIVEN,
        stop_sequences: List[str] | NotGiven = NOT_GIVEN,
        frequency_penalty: Penalty | NotGiven = NOT_GIVEN,
        presence_penalty: Penalty | NotGiven = NOT_GIVEN,
        count_penalty: Penalty | NotGiven = NOT_GIVEN,
        epoch: int | NotGiven = NOT_GIVEN,
        logit_bias: Dict[str, float] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> CompletionsResponse:
        model = self._get_model(model=model, model_id=kwargs.pop("model_id", None))
        path = self._get_completion_path(model=model, custom_model=custom_model)
        body = self._create_body(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens,
            num_results=num_results,
            min_tokens=min_tokens,
            temperature=temperature,
            top_p=top_p,
            top_k_return=top_k_return,
            custom_model=custom_model,
            stop_sequences=stop_sequences,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            count_penalty=count_penalty,
            epoch=epoch,
            logit_bias=logit_bias,
            **kwargs,
        )

        return await self._post(path=path, body=body, response_cls=CompletionsResponse)
