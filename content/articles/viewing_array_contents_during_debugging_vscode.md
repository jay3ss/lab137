Title: Viewing Array Contents During Debugging in VS Code
Author: Jay Ess
Date: 2020-05-20 19:27
Tags: til, vscode, debug, c++
Status: published

After getting annoyed with adding a bunch of array indices to the watch list for
a program that I was debugging, I went in search of a better solution. I came
across [an issue on the VS Code C/C++ Tools GitHub
repo](https://github.com/Microsoft/vscode-cpptools/issues/172). Apparently, you
can use the following pattern in the watch list instead

```
*(int(*)[10])some_pointer
```

to see the contents of the array `some_pointer` of type `int`. Or, basically

```
*(<type>(*)[arrSize])arrName
```

Even better, you can use the following

```
*arrName@arrSize
```

Here's a screenshot of doing it manually

![Manually adding array elements during
debug]({static}/img/view_arr_long_way.png)

and here's a screenshot of using the shortcut

![Shortcut of viewing array elements during
debug]({static}/img/view_arr_shortcut.png)

Much better.
