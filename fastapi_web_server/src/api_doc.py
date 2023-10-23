class ApiDoc:
    def __init__(self, title: str = "Web Server", description: str = "", version: str = "1.0.0"):
        self._title = title
        self._description = description
        self._version = version

    def to_dict(self):
        return {"title": self._title, "description": self._description, "version": self._version}
