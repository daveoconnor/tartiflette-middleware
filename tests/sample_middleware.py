from tartiflette_middleware import BaseMiddleware


class ConcreteMiddlewareNoLabel(BaseMiddleware):
    async def __aenter__(self):
        pass

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass


class ConcreteMiddleware(BaseMiddleware):
    label = 'CAExample'

    async def __aenter__(self):
        pass

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass


class ConcreteWorkingMiddleware(BaseMiddleware):
    label = 'CAWorkingExample'

    async def __aenter__(self):
        await self.store_request_data('foo')

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass
