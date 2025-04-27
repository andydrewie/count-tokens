from setuptools import setup

setup(
    name="count-tokens",
    version="0.1.0",
    py_modules=["count_tokens"],
    install_requires=["tiktoken", "tqdm"],
    entry_points={
        "console_scripts": [
            "count-tokens = count_tokens:main"
        ],
    },
)
