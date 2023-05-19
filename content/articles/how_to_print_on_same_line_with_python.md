Title: How to Print on the Same Line with Python
Author: Jay Ess
Date: 2019-12-17 16:00
Modified: 2020-05-01 15:51
Tags: python, print
Status: published

Today, I was downloading about 1,600 images and wanted to be able to keep track
of how many images I had downloaded so far and what image that I was currently
downloading. This is typically very easy with Python, but I decided to print
everything on the same line so that I my terminal wouldn't get cluttered with
`print` statements. This is where I encountered my issue.

The format of the string that I was printing started out as

```python
print(f'\rImage\t{count}', end='', flush=True)
```

where

- `\r`: is the carriage return which resets the line position to the beginning
of the line
- `count`: the number of the image that I was downloading
- `end`: the character that `print` will append to the string that it's printing
- `flush`: tells `print` whether or not it should forcibly flush the stream

Basically, what's going to happen is that when the string is printed it will
print the string and put the cursor back at the beginning of the line. If this
where done in a loop (probably using `time.sleep` too), then you'd get the
effect of the one line counting up. Neat!

```python
import time

for count in range(1000):
    print(f'\rCount\t{count}', end='', flush=True)
    time.sleep(0.01)
```

We can put this into a function to make it a little easier to read

```python
def print_same_line(msg):
    print('\r', msg, end='', flush=True, sep='')
```

In the function above, we need to use the `sep` keyword so that when we use
this function a space isn't added between the `\r` character and our string
causing an offset. Now we can use a loop like above and have our code be a bit
more readable (we also don't need the `\r` character at the beginning of our
string).

```python
import time

for count in range(1000):
    print_same_line(f'Count\t{count}')
    time.sleep(0.01)
```

This worked pretty great, but I encountered trouble when I was reading URLs
from a file and was printing them to the terminal.

```python
import pathlib
import time
import urllib.request as request

path = pathlib.Path('img')
SLEEP = 0.1 # seconds
urls_file = 'images.txt'

with open(urls_file) as urls:
    for count, url in enumerate(urls):
        msg = '\t'.join(['Image', str(count), url.strip()])
        print_same_line(msg)

        fname = url.strip().split('/')[-1]
        request.urlretrieve(url, path/fname)

        time.sleep(SLEEP)


    print(f'\nDone! Downloaded {count} images')
```

which resulted in the unexpected output of

```bash
Image	1	https://example.com/image-1.jpg
Image	2	https://example.com/image-2.jpg
Image	3	https://example.com/image-3.jpg
Image	4	https://example.com/image-4.jpg
Image	5	https://example.com/image-5.jpg
Image	6	https://example.com/image-6.jpg
...
```

It took me longer than I'd like to admit to figure out what went wrong. If you
look at the line where I grab the file name (`fname`) from the URL, you'll see
that I call the `strip` method. Why? Each line of the file had a `\n` character
at the end of it. Even though I did it for the file name I **did not** do it
for the printing of the URL. This one little mistake cost me probably 90 to 120
minutes...

Once I fixed it, however, it worked like a charm. Below is the fixed example

```python
import pathlib
import time
import urllib.request as request


path = pathlib.Path('img')
SLEEP = 0.1 # seconds
urls_file = 'images.txt'

with open(urls_file) as urls:
    for count, url in enumerate(urls):
        url = url.strip()
        print_same_line(f'Image\t{count+1}\t{url}')

        fname = url.split('/')[-1]
        request.urlretrieve(url, path/fname)

        time.sleep(SLEEP)


print(f'\nDone! Downloaded {count} images')
```

