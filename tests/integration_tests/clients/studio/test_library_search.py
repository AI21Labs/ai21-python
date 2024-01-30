from ai21 import AI21Client


def test_library_search__when_search__should_return_relevant_results(handled_file: str):
    client = AI21Client()
    response = client.library.search.create(
        query="What did Albert Einstein get a Nobel Prize for?", labels=["einstein"]
    )
    assert len(response.results) > 0
    for result in response.results:
        assert result.file_id == handled_file
