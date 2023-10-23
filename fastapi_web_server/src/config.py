from abc import ABC, abstractmethod


class Config(ABC):
    def __init__(
        self,
        host: str = "0.0.0.0",
        port: int = 5000,
        workers: int = 1,
        worker_class: str = "uvicorn.workers.UvicornWorker",
        worker_connections: int = 1024,
        timeout: int = 180,
        keepalive: int = 86400,
        capture_output: bool = True,
        keyfile: str = None,
        certfile: str = None,
        ca_certs: str = None,
    ):
        self._host = host
        self._port = port
        self._workers = workers
        self._worker_class = worker_class
        self._worker_connections = worker_connections
        self._timeout = timeout
        self._keepalive = keepalive
        self._capture_output = capture_output
        self._keyfile = keyfile
        self._certfile = certfile
        self._ca_certs = ca_certs

    @abstractmethod
    def to_dict(self):
        raise NotImplementedError


class GunicornConfig(Config):
    def to_dict(self):
        return {
            "bind": f"{self._host}:{self._port}",
            "workers": self._workers,
            "worker_class": self._worker_class,
            "worker_connections": self._worker_connections,
            "timeout": self._timeout,
            "keepalive": self._keepalive,
            "capture_output": self._capture_output,
            "keyfile": self._keyfile,
            "certfile": self._certfile,
            "ca_certs": self._ca_certs,
        }


class UnicornConfig(Config):
    def to_dict(self):
        return {
            "host": self._host,
            "port": self._port,
            "workers": self._workers,
        }
