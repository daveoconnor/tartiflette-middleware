from tartiflette_middleware.exceptions import\
    RequestNotSetException, RequestDataNotStoredException

class TestExceptions:
    def test_request_not_set_exception(self):
        msg = 'No request set on this hook.'
        assert str(RequestNotSetException()) == msg

    def test_request_data_not_stored_exception(self):
        msg = 'No data stored on this request.'
        assert str(RequestDataNotStoredException()) == msg
