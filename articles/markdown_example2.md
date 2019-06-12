Title: Markdown Examples Part 2
Author: Jay Ess
Date: 2019-01-03 12:00
Tags: markdown

Images can be displayed in Markdown.
Text within the square brackets is the image name. The path to the image goes between the round brackets.
The {static} tag indicates the image is stored in the content folder. This setting can be changed in pelicanconf.py.

![python logo]({static}/python_icon.png)

Links to downloadable content such as PDF files are written similarly to image files but with no ! symbol at the beginning.

[Pelican Documenation]({static}/pelican.pdf)

A link to a different blog post on our website is written exactly the same.
Text within the square brackets can be clicked on to travel to the website between the curly brackets.
The {filename} tag indicates we want to follow the link to a webpage rather than the static file it was generated from.

[First Post]({filename}/articles/markdown_example1.md)

Or we can link to another external website by supplying the web address.

[Python Package Index](https://pypi.org)
