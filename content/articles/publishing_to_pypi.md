Title: Publishing to PyPI
Author: Jay Ess
Date: 2023-06-07 11:54
Tags: Python, publishing, code, til
Status: published

*NOTE: I don't do this very often so there could be a lot of incorrect information
in this post. I'm mainly writing this for myself for future reference. But, if
someone else finds this useful then that makes me happy.*

Publishing to PyPI is an easy way to distribute your code to the masses. It can,
however, be a little tricky to get your package uploaded. Here's how I just did
it with my package [PyAutoReloadServer](//pypi.org/project/pyautoreloadserver/).

## Setting Up Your Project

However you structure your project, you'll need something to tell PyPI what's
in your package and how to set the package up. I created a `setup.py` file for
that:

```python
# setup.py

import pathlib
from setuptools import setup, find_packages


here = pathlib.Path(__file__).parent
readme = (here / "README.md").read_text()

extras_require = (here / "requirements.txt").read_text().splitlines()


setup(
    name="pyautoreloadserver",
    version="0.0.1",
    author="Jay Ess",
    description="A simple HTTP server that reloads when a file change is detected",
    url="https://github.com/jay3ss/pyautoreloadserver",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
    extras_require={"dev": extras_require},
    entry_points={
        "console_scripts": [
            "pyautoreloadserver = pyautoreloadserver.cli:main",
        ],
    },
    package_dir={
        "tests": "tests",
        "pyautoreloadserver": "pyautoreloadserver",
    },
)
```

You can read all about what to put in your own `setup.py` file
[here](//docs.python.org/3/distutils/setupscript.html). I like to use code to
keep things like the `long_description` and `extras_require` attributes up-to-date
automatically. But, you do you.

Now, make an account on [PyPI's website](//pypi.org) and then get an
[API key](https://pypi.org/help#apitoken) that you'll use to upload your package.
I made a `~/.pypirc` file to hold all of the information that I'll need to upload
my packages. Here's what it looks like (with some info redacted):

```shell
# ~/.pypirc

[distutils]
index-servers =
    pypi
    pypitest

[pypitest]
repository = https://test.pypi.org/legacy/
username = __token__
password = <api-key>

[pypi]
username = __token__
password = <api-key>
```

There's couple of things going on in the file above and you should checkout the
[docs](//packaging.python.org/en/latest/specifications/pypirc/) for it. But, in
the meantime here's some of the important bits from the docs

> The `distutils` section defines an `index-servers` field that lists the name of
> all sections describing a repository.

> Each section describing a repository defines three fields:

> - `repository`: The URL of the repository.
> - `username`: The registered username on the repository.
> - `password`: The password that will used to authenticate the username.

The `[distutils]`'s `index-servers` field is where you define additional
repositories. Note that my `~/.pypirc` file doesn't have a `repository` field
for the `pypi` section. That's because the default value for that field for the
`[pypi]` section is `https://upload.pypi.org/legacy`. Also, if you're using an
API token like I am then for the `username` field you literally put `__token__`
as the value. It took me an embarrassingly long time to figure that one out.

## Building the Package for Distribution

There are a multiple ways to build a Python package for distribution. The two
that I come across the most are directly using a `setup.py` script (which is
[strongly discouraged](//blog.ganssle.io/articles/2021/10/setup-py-deprecated.html)
and deprecated) or using the [`build`](//pypi.org/project/build/) package. I'm
going to use the `build` package.

I was having trouble using `build` the command `python -m build` and had to
modify it slightly

```shell
python -m build --no-isolation --wheel

# this can be simplified by using -n and -w, respectively
```

which seemed to work. The `--no-isolation` flag prevents `build` from using an
isolated virtual environment (and makes the build time shorter) and the `--wheel`
flags tells `build` to create a wheel and a `build/` and `dist/` directory.

## Publishing the Package

Next, use [`twine`](//twine.readthedocs.io/en/stable/) to publish the package.
Twine is the official PyPI upload tool so it should work for you. You'll first
want to test publishing your package to ensure that everything goes right. Using
`twine` it's pretty easy to test uploading.

```shell
python -m twine upload -r pypitest dist/* --verbose
```

The `-r` flag tells `twine` which repository we want to upload to (`pypitest`
here) and then `dist/*` is the location of the wheel. The `--verbose` flag gives
us more output from `twine` so if there's a problem we can have a better idea
what it is.

If everything went well go ahead and move on to uploading to PyPI. The command
for that is exactly the same as loading to the test PyPI repository, but instead
we use the value `pypi` for the `-r` flag

```shell
python -m twine upload -r pypi dist/* --verbose
```

If nothing went wrong your package should be live on PyPI. Have a question? Leave
a comment (if I've re-enabled comments) or leave an issue or pull request on the
site's [repo](//github.com/jay3ss/jay3ss.github.io).
