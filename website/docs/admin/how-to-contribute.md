---
sidebar_position: 1
---

# [Coast Train Team] How to contribute

Contributions are welcome, and they are greatly appreciated! Credit will always be given.

Here's how to set up for local development.

1. Fork the dash_doodler repo on Github  https://github.com/dbuscombe-usgs/CoastTrain

2. Clone your fork locally:

```shell
git clone git@github.com:your_name_here/CoastTrain.git
```

3. Create a branch for local development:

```shell
git checkout -b name-of-your-bugfix-or-feature
```

Now you can make your changes locally.

## Write a blog post

Docusaurus creates a **page for each blog post**, but also a **blog index page**, a **tag system**, an **RSS** feed...


Create a file at `blog/2021-02-28-greetings.md`:

```md title="blog/2021-02-28-greetings.md"
---
slug: greetings
title: Greetings!
author: Dan Buscombe
author_title: Coast Train Contributor
author_url: https://github.com/dbuscombe-usgs
tags: [greetings]
---

Congratulations, you have made your first post!

Feel free to play around and edit this post as much you like.
```

A new blog post is now available at `http://localhost:3000/blog/greetings`.


## Edit docs

* To edit the content of the frontpage: `src/components/HomepageFeatures.js`
* To edit Project Information pages, go to the subfolders of `docs/`
* To rename sidebar names, edit the `_category_.json` file in each subfolder in `docs/`
* To edit blog pages, go to the subfolders of `blogs/`
* Start here for instructions on how to use docusaurus: https://docusaurus.io/docs/installation

To check the webpage locally, use

```shell
yarn start
```

The webpage will load at http://localhost:3000/CoastTrain.


## Ready to contribute?


5. Commit your changes and push your branch to GitHub:

```shell
git add .
git commit -m "Your detailed description of your changes."
git push origin name-of-your-forked-repo
```

6. Submit a pull request through the GitHub website: https://github.com/dbuscombe-usgs/CoastTrain

7. Ask for help if any of the above is confusing or does not work.
