Title: Converting a PowerPoint PPT to a PDF File
Author: Jay Ess
Date: 2020-05-01 14:26
Tags: ppt, powerpoint, til, pdf, convert
Status: published

I'm currently taking an online class and the professor gives out PowerPoint
slides as part of his lecture. I don't like the LibreOffice version of
PowerPoint (Impress) and prefer to use PDF files. So, I found a simple
one-liner from [Ask Ubuntu](https://askubuntu.com/a/104484) that's worked well
so far.

```
libreoffice --headless --invisible --convert-to pdf *.ppt
```
