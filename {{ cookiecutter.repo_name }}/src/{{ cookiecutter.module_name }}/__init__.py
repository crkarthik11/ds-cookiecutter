# flake8: noqa: F401
try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"
