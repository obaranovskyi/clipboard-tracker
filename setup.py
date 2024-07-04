import codecs
import os

from setuptools import find_packages, setup

curr_location = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(curr_location, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name="clipboard-tracker",
    version="1.0.0",
    description="Track your clipboard history and save it to a file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/obaranovskyi/clipboard-tracker",
    author="Oleh Baranovskyi",
    author_email="oleh.baranovskyi.dev.acc@gmail.com",
    license="MIT",
    classifiers=[
        "License :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["clipboard==0.0.4", "pyperclip==1.9.0"],
    entry_points={
        "console_scripts": ["clipboard_tracker=clipboard_tracker.__main__:main" ]
    },
)
