from unittest.mock import Mock
from tartiflette_middleware import Middleware
from .sample_middleware import ConcreteWorkingMiddleware


class TestMiddleware:
    def test_init(self):
        manager = ConcreteWorkingMiddleware()
        mock_middleware = Mock()
        mock_middleware.get_hooks_service_middleware = Mock(return_value='foo')
        hook = Middleware(
            context_manager=manager,
            server_middleware=mock_middleware
        )
        assert hook.service is manager
        assert hook.middleware == 'foo'


