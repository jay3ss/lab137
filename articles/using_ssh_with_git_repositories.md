Title: Using SSH with Git Repositories
Author: Jay Ess
Date: 2020-05-01 14:26
Tags: til, git, ssh
Status: published

If you've setup your [git account to use
SSH](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh),
then should be pretty straightforward. My usual workflow was to `git clone` the
URL of the repository, but I decided to use SSH instead because I was annoyed
with having to always enter my credentials. This is how to do it.

*Note*:For the most part, I use GitHub but just replace `github.com` with
whatever service you're using.

## Cloning a Repository

```
git clone git@github.com:<username>/<reponame>.git
```

## Changing the Remote to Use SSH

If you've already cloned a repo without using SSH, then you can [modify the
branch to use SSH](https://stackoverflow.com/a/11201143/3562890)

```
git remote set-url origin git@github.com:<username>/<reponame>.git
```
