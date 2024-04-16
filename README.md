# bookmark-explorer

there's a lot of neat stuff locked up in my bookmarks, and I want to find it! I've gone through periods of "bookmark all the things" and then guess what? I've never looked back at them! Maybe once or twice, been intimidated/disappointed by them, and then decided to ignore them going forwards.

To my mind, the primary thing that sucks about current bookmark systems is that they really only care about storing the page titles, with *maybe* some sort of file/tag organization. I don't want to have to do the manual work of organizing everything myself! I want the computer to do that for me, and now, I think it can.

## plan

step 1: strip out extraneous, useless content in the page source (using [python-readability}(http://github.com/buriy/python-readability))
step 2: grab the first N tokens, and generate a lower-dimensionality embedding from them with a local LLM.
step 3: stuff them in a vector DB.

Now, we can search semantically inside that vector DB with either selected search terms, or find relevant material for a selected bookmark!

## implementation details

I think for my own use, I'll implement this as a web server that integrates with an ultra-simple browser extension. That lets me provide a delightful, flexible UI for browsing.


### stack choices and reasoning

- LLM/semantic search library: [txtai](https://github.com/neuml/txtai)
- web backend: Python flask for the backend (integrates well with txtai, which is my chosen tool for generating the embeddings/semantic search functionality.)
- web frontend: React.js (the leading front-end framework, and a tool I want to get more familiar with.)
- browser extension: vanilla JS, initially with the Firefox API but later with the Chromium API for maximum reach.

## struggles so far:

first steps:

- I need a web server that can accept some json and perform a get request on the URL (just print the html it gets.)
- then we need to run the readability algorithm on it. (print out the text.)
- then we stash that text (or at least the first bit of it) into txtai
