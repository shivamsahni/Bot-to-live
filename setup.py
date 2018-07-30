
from setuptools import setup


setup(
    name="Bot using wit",
    version = "1.0.0-snapshot",
    install_requires = [
        'Flask',
        'pymessenger',
        'gunicorn',
        'wit'
    ]

)