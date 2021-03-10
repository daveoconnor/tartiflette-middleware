import pytest
from tartiflette_middleware.examples.standalone import\
    StandaloneMiddleware
from tartiflette_middleware.exceptions import\
    RequestDataNotStoredException


class TestStandaloneMiddleware:
    def test_standalone_example_init(self):
        service = StandaloneMiddleware()

    @pytest.mark.asyncio
    async def test_standalone_example_call_data_not_set(self):
        service = StandaloneMiddleware()
        service.request = {'fake': 'data'}
        with pytest.raises(RequestDataNotStoredException):
            await service()

    @pytest.mark.asyncio
    async def test_standalone_example_call_data_set(self):
        service = StandaloneMiddleware()
        service.request = {'fake': 'data'}
        async with service:
            pass
        assert await service() == 'foo'


