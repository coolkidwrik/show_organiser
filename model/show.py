
# defines the attributes and methods associated with shows
class Show:

    # given the name of the show, initializes the show object and sets all other fields to None
    def __init__(self, name):
        self.name = name  # name of the show, should be a string
        self.score = None  # score out of 10. should be a float
        self.genres = list()  # list of genres, each genre should be a string
        self.seasons = 1  # number of seasons
        self.episodes = None  # number of episodes
        self.type = None  # type of the show, could be a movie or series
        self.description = None  # text description of the show

    # returns a string representing the object
    # prints out all fields but description
    def __repr__(self):
        return f"{self.name} \n" \
               f"__________________________" \
               f"rating: {self.score}\n" \
               f"seasons: {self.seasons}\n" \
               f"episodes: {self.episodes}\n" \
               f"genres: {self.genres}\n" \
               f"type: {self.type}"

    # sets the rating of the show to the user input: "score"
    def set_score(self, score: float):
        # assert type(score) == float, f"score inputted is not a number"
        self.score = score

    # sets the seasons of the show to the user input: "seasons"
    def set_seasons(self, seasons: int):
        assert seasons != 0, "show cannot have 0 seasons"
        self.seasons = seasons

    # sets the episodes of the show to the user input: "episodes"
    def set_episodes(self, episodes: int):
        assert episodes != 0, "show cannot have 0 episodes"
        self.episodes = episodes
        if episodes == 1:
            self.type = "Movie"
        else:
            self.type = "Series"

    # sets the genres of the show to the user input: "genres," which is a list of genres.
    # each genre should be a string
    def set_genres(self, genres: list):
        for g in genres:
            assert type(g) == str, f" argument \"{g}\" is not a string"
            self.genres.append(g)
