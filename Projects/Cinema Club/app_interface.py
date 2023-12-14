"""This is a program created with interface to stock and delete movies selected by the user in a data base ( json format )."""
"""C'est un programme crée avec une interface graphique pour stocker et supprimer des films choisis par l'utilisateur dans une base de donnée ( json fomrat )."""

from PySide6 import QtWidgets
from env.movies import get_movies
from env.movies import Movie

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Le ciné des films")
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()
        self.add_movie()
        self.delete_movie()

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self) # Tout d'abord on crée le layout.
        # On défini tous les éléments comme des buttons, des fenetres et etc.
        self.le_movieTitle = QtWidgets.QLineEdit()
        self.button_add_movie = QtWidgets.QPushButton("Ajouter un film")
        self.list_with_movies = QtWidgets.QListWidget()
        self.list_with_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.button_delete_movie = QtWidgets.QPushButton("Supprimer le(s) film(s)")
        # On ajoute tous ces éléments sur le layout.
        self.main_layout.addWidget(self.le_movieTitle)
        self.main_layout.addWidget(self.button_add_movie)
        self.main_layout.addWidget(self.list_with_movies)
        self.main_layout.addWidget(self.button_delete_movie)

    def setup_connections(self):
        self.button_add_movie.clicked.connect(self.add_movie)
        self.button_delete_movie.clicked.connect(self.delete_movie)
        self.le_movieTitle.returnPressed.connect(self.add_movie)

    def populate_movies(self):
        movies = get_movies()

        for movie in movies:
            list_item.movie = movie
            self.list_with_movies.addItem(list_item)

    def add_movie(self):
        movie_title = self.le_movieTitle.text()
        if not movie_title:
            return False

        movie = Movie(title=movie_title)
        resultat = movie.add_to_movies()
        if resultat:
            list_item = QtWidgets.QListWidgetItem(movie.title)
            list_item.movie = movie
            self.list_with_movies.addItem(list_item)
        self.le_movieTitle.setText("")

    def delete_movie(self):
        for selected_item in self.list_with_movies.selectedItems():
            movie = selected_item.movie
            movie.remove_from_movies()
            self.list_with_movies.takeItem(self.list_with_movies.row(selected_item))

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec()