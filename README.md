# Broken Link Crawler

Let's say I have a website and I want to find any dead links and images on this website.

```bash
$ python deadseeker.py 'https://healeycodes.github.io/'
> 404 - https://docs.python.org/3/library/missing.html
> 404 - https://github.com/microsoft/solitare2
```

It's that simple. The website is crawled, and all `href` and `src` attributes are sent a request. Errors are reported. This bot doesn't observe `robots.txt` but _you should_.

This was for a tutorial so it's scope has been kept quite small.

### It is not a clever bot. But it is a good bot.
