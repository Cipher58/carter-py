from setuptools import setup, find_packages

setup(
    name="Eureka-py",
    version="0.0.1",
    packages=find_packages(),
    install_requires = [
    "aiohttp==3.8.4",
    "aioresponses==0.7.4",
    "asynctest==0.13.0",
    "python-dotenv==1.0.0",
    "Requests==2.28.2",
    "responses==0.23.1",
    "setuptools==65.5.0"
    ],
    author="LazyLyrics, Cipher58, Ethan-Barr",
    author_email="hello.eurekaai@gmail.com",
    description="A wrapper for the Eureka API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LazyLyrics/carter-py",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License"
    ],
)
