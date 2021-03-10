from unittest.mock import MagicMock

import pytest
from tartiflette_middleware import BaseMiddleware
from tartiflette_middleware.base_middleware import \
    RequestDataNotStoredException, RequestNotSetException
from tests.sample_middleware import ConcreteWorkingMiddleware,\
    ConcreteMiddlewareNoLabel, ConcreteMiddleware


class TestBaseMiddleware:
    def test_init_missing_label(self):
        with pytest.raises(TypeError):
            temp_hook = ConcreteMiddlewareNoLabel()

    def test_init(self):
        conc_hooks = ConcreteMiddleware()
        assert conc_hooks.handler is None
        assert conc_hooks.request is None

    @pytest.mark.asyncio
    async def test_request_not_set_exception(self):
        temp_hook = ConcreteMiddleware()
        with pytest.raises(RequestNotSetException):
            await temp_hook()

    def test__ns_label(self):
        conc_hooks = ConcreteWorkingMiddleware()
        assert conc_hooks._ns_label == (
                BaseMiddleware._lib_label + '-'
                + ConcreteWorkingMiddleware.label
        )

    def test_properties_setters(self):
        conc_hooks = ConcreteMiddleware()
        conc_hooks.handler = MagicMock()
        conc_hooks.request = MagicMock()
        # noinspection PyTypeHints
        assert isinstance(conc_hooks._handler, MagicMock)
        # noinspection PyTypeHints
        assert isinstance(conc_hooks._request, MagicMock)
        # noinspection PyTypeHints
        assert isinstance(conc_hooks.handler, MagicMock)
        # noinspection PyTypeHints
        assert isinstance(conc_hooks.request, MagicMock)

    def test_concrete_is_async_context_manager(self):
        conc_hooks = ConcreteMiddleware()
        with pytest.raises(AttributeError):
            with conc_hooks:
                assert True

    @pytest.mark.asyncio
    async def test_concrete_is_async_context_manager(self):
        conc_hooks = ConcreteMiddleware()
        conc_hooks.request = {}
        async with conc_hooks:
            pass

    def test_requires_aenter(self):
        with pytest.raises(TypeError):
            class NoAenter(BaseMiddleware):
                async def __aexit__(self):
                    pass

            na = NoAenter()

    def test_requires_aexit(self):
        with pytest.raises(TypeError):
            class NoAexit(BaseMiddleware):
                async def __aenter(self):
                    pass

            na = NoAexit()

    @pytest.mark.asyncio
    async def test__call__no_data_set(self):
        temp_hooks = ConcreteMiddleware()
        temp_hooks.request = {'fake': 'data'}
        with pytest.raises(RequestDataNotStoredException):
            await temp_hooks()

    @pytest.mark.asyncio
    async def test__call__data_set(self):
        temp_hooks = ConcreteWorkingMiddleware()
        temp_hooks.request = {}
        async with temp_hooks:
            pass
        assert await temp_hooks() == 'foo'
