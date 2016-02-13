# movie.py
# Jameson Hyde
# Retrieves and generates a list of movies to be parsed and posted
import json
import argparse
import sys
sys.path.insert(0, 'ud036_StarterCode')
import fresh_tomatoes


class Movie(object):
    """Class describing a movie
    
    Attributes:
        title (str): The title of the movie
        poster_image_url (str): A URL to the box/poster art
        trailer_youtube_url (str): A URL to the youtube.com hosted trailer
    """

    title = None
    poster_image_url = None
    trailer_youtube_url = None

    def __init__(self, title, poster_image_url=None, trailer_youtube_url=None):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
    
    #Simplified constructor that parses a JSON object to create the Movie object
    def __init__(self, json_obj):
        def as_movie(dct):
            self.title = dct['title']
            if "artURL" in dct:
                self.poster_image_url = dct['artURL']
            if "trailerURL" in dct:
                self.trailer_youtube_url = dct['trailerURL']
        json.loads(json_obj, object_hook=as_movie)

def main():
    #establish command line arguments
    parser = argparse.ArgumentParser(description='Parses a JSON file to a list of movies and generates webpage')
    parser.add_argument('json', help='Path to JSON file - see README.md for formatting or use included movies.json sample')
    args = parser.parse_args()
    content = ""
    movies = []
    #read json file
    try:
        with open(args.json) as f:
            content = f.readlines()

        if "movies" in content[0]:
            for c in content[1:-1]:
                movies.append(Movie(c.strip().rstrip(",")))
        fresh_tomatoes.open_movies_page(movies)
    except:
        raise Exception("Failed to parse movies file")

if __name__ == '__main__':
    main()