from tartiflette_middleware import BaseMiddleware


class StandaloneMiddleware(BaseMiddleware):
    label = 'Standalone'

    def __init__(self):
        BaseMiddleware.__init__(self)
        """
        This is where you can perform any setup. e.g. Initialising factories
        which are to be used in the __aenter__ call.
        """

    async def __aenter__(self):
        """
        Here is where you can access the header and use it to set self._data
        to set  the subsequent graphql calls in this request.
        """
        await self.store_request_data('foo')
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Here is where you can perform functions that need to run when a request
        ends.  e.g. file or db session close.
        """
        pass
