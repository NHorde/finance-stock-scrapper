


class State:
    _defaults = {
        'ticker': None
    }

    def __init__(self, test, **kwargs):
        """
        :param event:
        :type even: dict
        """
        self.test = kwargs.get("test", "test")
