# Pelican Blog template

Template for Pelican Blog with Papyrus theme.

## Informations

- Platform: [Pelican](https://github.com/getpelican/pelican) - a static site generator that requires no database or server-side logic.

- Theme: [Papyrus](https://github.com/pelican-themes/papyrus) -  a fast, clean, responsive theme for Pelican.

## Test on local

### Install requirements

Install `stork-search` (or see its [documentation here](https://stork-search.net/docs/install)):

```bash
cargo install stork-search --locked
```

Install core packages:

```bash
pip install pelican markdown beautifulsoup4 pelican-search
```

### Development server
I assumed that you are working on the blog directory. Use this command to build and run the development server:
```bash
pelican --autoreload --listen --ignore-cache
```

## Deploy on Netlify

### Site settings

Build settings will be placed on `pelicanconf-netlify.py`, the most one thing to change is `SITEURL`, which must be set base on your site name, or site domain.

To change more settings, please see [Pelican documentation](https://docs.getpelican.com/en/latest/settings.html).

### Upload to Netlify

1. First, your need to have a [Netlify](https://netlify.com) account.

2. Create a new site, and upload the blog source code. You can find more [details here](https://docs.netlify.com/).

3. Set the deploy configurations like this:

    - Build command: `rustup default stable && cargo install stork-search --locked && pip install beautifulsoup4 pelican-search && pelican content -o output -s pelicanconf-netlify.py`

    - Publish directory: `output`

4. If you connect the site with Git, whenever you push the code to repo, Netlify will deploy your blog.
