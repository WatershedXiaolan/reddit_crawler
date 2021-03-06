#!/usr/bin/env python
import os
import re
import praw
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import shutil
import sys
from PIL import Image
"""
reddit = get_reddit()
subs = reddit.subreddit('Python').top(limit=5)

for sub in subs:
    res = requests.get(sub.url)
    if (res.status_code == 200 and 'content-type' in res.headers and
       res.headers.get('content-type').startswith('text/html')):
        html = res.text
"""

def get_reddit():
    return praw.Reddit(
        client_id='xxx',
        client_secret='xxxx',
        grant_type='client_credentials',
        user_agent='mytestscript/1.0'
    )


def get_top(subreddit_name):
    today = datetime.now().strftime(r'%Y-%m-%d')
    dirname = os.path.join('news-%s' % today, subreddit_name)
    os.makedirs(dirname, exist_ok=True)

    # Get top 50 submissions from reddit
    reddit = get_reddit()
    top_subs = reddit.subreddit(subreddit_name).top(limit=50)

    # Remove those submissions that belongs to reddit
    subs = [sub for sub in top_subs if not sub.domain.startswith('self.')]

    artical_count = 10
    jpg_paths = []
    png_paths = []
    while subs and artical_count > 0:
        sub = subs.pop(0)
        article = get_article(sub.url)
        print(sub.url)

        if article and artical_count > 0:
            text = '\n\n'.join(article['content'])
            filename = re.sub(r'\W+', '_', article['title']) + '.md'
            open(os.path.join(dirname, filename), 'w').write(text)
            artical_count -= 1

        image = get_image(sub.url)
        if image:
            filename = sub.url.split('/')[-1]
            if filename[-3:] == 'jpg':
                jpg_paths.append(os.path.join(dirname, filename))
            if filename[-3:] == 'png':
                png_paths.append(os.path.join(dirname, filename))

            with open(os.path.join(dirname, filename), 'wb') as out_file:
                shutil.copyfileobj(image, out_file)

    if jpg_paths != []:
        new_img = merge_images(jpg_paths)
        new_img.save(os.path.join(dirname, 'JPG.jpg'))
        remove_files(jpg_paths)

    if png_paths != []:
        new_img = merge_images(png_paths)
        new_img.save(os.path.join(dirname, 'PNG.jpg'))
        remove_files(png_paths)


def remove_files(paths):
    for f in paths:
        os.remove(f)


def merge_images(image_paths):
    images = [Image.open(x) for x in image_paths]
    widths, heights = zip(*(i.size for i in images))

    total_width = max(widths)
    max_height = sum(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (0, x_offset))
        x_offset += im.size[1]
    return new_im

def get_image(url):
    print('  - Retrieving %s' % url)
    try:
        res = requests.get(url, stream=True)
        print(res.headers.get('content-type'))
        if (res.status_code == 200 and 'content-type' in res.headers and
           res.headers.get('content-type').startswith('image/')):
            return res.raw
    except Exception:
        pass


def get_article(url):
    print('  - Retrieving %s' % url)
    try:
        res = requests.get(url)
        if (res.status_code == 200 and 'content-type' in res.headers and
                res.headers.get('content-type').startswith('text/html')):
            article = parse_article(res.text)
            print('      => done, title = "%s"' % article['title'])
            return article
        else:
            print('      x fail or not html')
    except Exception:
        pass


def parse_article(text):
    soup = BeautifulSoup(text, 'html.parser')

    # find the article title
    h1 = soup.body.find('h1')

    # find the common parent for <h1> and all <p>s.
    root = h1
    while root.name != 'body' and len(root.find_all('p')) < 5:
        root = root.parent

    if len(root.find_all('p')) < 5:
        return None

    # find all the content elements.
    ps = root.find_all(['h2', 'h3', 'h4', 'h5', 'h6', 'p', 'pre'])
    ps.insert(0, h1)
    content = [tag2md(p) for p in ps]

    return {'title': h1.text, 'content': content}


def tag2md(tag):
    if tag.name == 'p':
        return tag.text
    elif tag.name == 'h1':
        return f'{tag.text}\n{"=" * len(tag.text)}'
    elif tag.name == 'h2':
        return f'{tag.text}\n{"-" * len(tag.text)}'
    elif tag.name in ['h3', 'h4', 'h5', 'h6']:
        return f'{"#" * int(tag.name[1:])} {tag.text}'
    elif tag.name == 'pre':
        return f'```\n{tag.text}\n```'


def main():
    subreddits = ['oilandgas', 'wallstreetbets', 'apple', 'exxonmobil', 'layoff']
    for sr in subreddits:
        print('Scraping /r/%s...' % sr)
        get_top(sr)


if __name__ == '__main__':
    main()