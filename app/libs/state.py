from libs.files import FileManager
from libs.event import Event

class State:
    _defaults = {
        'status': 400
    }

    def __init__(self, **kwargs):
        """
        :param event:
        :type even: dict
        """
        self.files: FileManager = FileManager(**kwargs)
        self.events: Events = Event(**kwargs)