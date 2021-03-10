from tartiflette_middleware import BaseMiddleware


class HeaderAccessMiddleware(BaseMiddleware):
    label = 'UsesHeaders'

    def __init__(self, *args, **kwargs):
        BaseMiddleware.__init__(self)
        """
        This is where you can perform any setup. e.g. Initialising factories
        which are to be used in the __aenter__ call.
        """

    async def __aenter__(self):
        """
        Here is where you can access the header and use it to set self._data
        for the subsequent graphql calls in this request.
        """
        # this should match how you access a header on the request object for
        # your server. The following case matches aiohttp's method:
        header_data = self.request.headers.get('foo', None)
        # you can process the at this point, then store it, just cloning it for
        # a not very useful example
        processed_header_data = header_data[:]
        await self.store_request_data(processed_header_data)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Here is where you can perform functions that need to run when a request
        ends.  e.g. file or db session close, or blanking _data
        """
