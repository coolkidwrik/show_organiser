import show as s


# class that describes a list of shows
class ShowList:

    # creates a list of shows object with the necessary attributes
    def __init__(self):
        self.shows = list()
        self.length = 0  # number of shows in the list
        self.average = 0  # average score of all the shows
        self.episodes = 0  # number of episodes in all shows
        self.series = 0  # number of series in the list
        self.movies = 0  # number of movies in the list

    # return a string representing the shows in the list
    def __repr__(self):
        shows = ""
        for s in self.shows:
            shows = shows + f"{s}\n"
        return shows

    # adds "show" to the list of shows and updates all fields accordingly
    def add_show(self, show: s):
        self.shows.append(show)
        self.length += 1
        self.average = (self.average * (self.length - 1) + show.score) / self.length
        self.episodes += show.episodes
        if show.type == "Movie":
            self.movies += 1
        else:
            self.series += 1
