import os

MAX_SCORE = 5
MIN_SCORE = 0

DATA_DIR = 'db'
RATINGS_DATABASE_NAME = 'ratings.csv'
FILMS_DATABASE_NAME = 'movies.txt'
FILMS_WITH_PLOT_DATABASE_NAME = 'movies_full.csv'
LINKS_FILE_NAME = 'links.csv'
WIKILINKS_DATABASE_PATH = os.path.join(DATA_DIR, 'wikipedia')
WIKILINKS_DATABASE_NAME = 'wiki.csv'

GENRES = {'Action', 'Adult', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',
          'Documentary', 'Drama', 'Family',
          'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical', 'Mystery',
          'N/A', 'News', 'Romance',
          'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War', 'Western'}
SEP = '},{'
BASE_DIR = os.path.dirname(__file__)

PACKAGE = 'vizier'
CONFIG_DIR_NAME = 'configurations'
LOGGING_CONF_FILE_NAME = 'logging.conf'