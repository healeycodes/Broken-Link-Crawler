This was for my **[tutorial](https://healeycodes.github.io/python/beginners/tutorial/webdev/2019/04/02/dead-link-bot.html)** on building a dead link checker so it's scope has been kept quite small.

# Broken Link Crawler

![Desktop](https://github.com/healeycodes/Broken-Link-Crawler/blob/master/bot-in-action.gif)

Let's say I have a website and I want to find any dead links and images on this website.

```bash
$ python deadseeker.py 'https://healeycodes.github.io/'
> 404 - https://docs.python.org/3/library/missing.html
> 404 - https://github.com/microsoft/solitare2
```

It's that simple. The website is crawled, and all `href` and `src` attributes are sent a request. Errors are reported. This bot doesn't observe `robots.txt` but _you should_.



### It is not a clever bot. But it is a good bot.

<br>

Accepting (small) PRs and issues!
