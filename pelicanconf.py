COPYRIGHT = '2025'
SUBTITLE = "Blog"
SUBTEXT = '''A fast and responsive theme built for the <a class="underline" 
href="https://blog.getpelican.com/">Pelican</a> site generator.<br>
The theme is inspired from <a class="underline" 
href="https://github.com/adityatelange/hugo-PaperMod">Hugo-PaperMod</a>. 
It is styled using <a class="underline" 
href="https://tailwindcss.com/">Tailwind CSS</a>. 
It supports dark mode and built in search function.
'''

# Basic Settings

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = "Uncategorised"

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

DOCUTILS_SETTINGS = {
	
}

DELETE_OUTPUT_DIRECTORY = True

OUTPUT_PATH = "output/"
PATH = "content"
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["articles"]

OUTPUT_SOURCES = False

PLUGINS = ['readtime', 'search', 'neighbors', 'pelican-toc']
PLUGIN_PATHS = ['plugins']

SITENAME = 'Demo Blog'
SITEURL = "http://localhost:8000"

STATIC_PATHS = []

SUMMARY_MAX_LENGTH = 100
SUMMARY_MAX_PARAGRAPHS = None
SUMMARY_END_SUFFIX = '…'

PORT = 8000

# URL Settings

RELATIVE_URLS = False

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'

# Time and Date

TIMEZONE = "Asia/Ho_Chi_Minh"

DEFAULT_DATE = None
DEFAULT_DATE_FORMAT = "%d/%m/%Y"

# Template pages

DIRECT_TEMPLATES = (('index', 'search', 'tags', 'categories', 'archives'))

# Metadata

AUTHOR = 'Nguyen Hieu Thanh'
DEFAULT_METADATA = {}

# Feed Settings

# Pagination

DEFAULT_PAGINATION = 10
PAGINATED_TEMPLATES = { 'index': None, 'tag': None, 'category': None, 'author': None, 'archives': 24 }

# Translations

DEFAULT_LANG = "vi"

# Themes

THEME = "themes/Papyrus"
THEME_STATIC_PATHS = ["static"]
SITESUBTITLE = 'Blog cá nhân của Nguyen Hieu Thanh'
GITHUB_URL = "https://github.com/domnht"
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/")
    # ("You can modify those links in your config file", "#"),
)
SOCIAL = (
    ('github', 'https://github.com/domnht'),
    ('facebook', 'https://facebook.com/domnht'),
    ('instagram', 'https://instagram.com/domnht'),
)

# Site search plugin
SEARCH_MODE = "output"
SEARCH_HTML_SELECTOR = "main"

# Table of Content Plugin
TOC = {
    'TOC_HEADERS'       : '^h[1-3]', # What headers should be included in
                                     # the generated toc
                                     # Expected format is a regular expression
    'TOC_RUN'           : 'true',    # Default value for toc generation,
                                     # if it does not evaluate
                                     # to 'true' no toc will be generated
    'TOC_INCLUDE_TITLE': 'false',    # If 'true' include title in toc
}

# Article share widgets
SHARE = (
    ("twitter", "https://twitter.com/intent/tweet/?text=Features&amp;url="),
    ("linkedin", "https://www.linkedin.com/sharing/share-offsite/?url="),
    ("reddit", "https://reddit.com/submit?url="),
    ("facebook", "https://facebook.com/sharer/sharer.php?u="),
    ("whatsapp", "https://api.whatsapp.com/send?text=Features - "),
    ("telegram", "https://telegram.me/share/url?text=Features&amp;url="),
)
