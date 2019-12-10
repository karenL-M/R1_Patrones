from abc import ABC, abstractmethod

class Pelicula(Reproducible):
       def reproduccion(self):
        pass
class Reproducible():
    @abstractmethod
    def reproduccion(self):
        pass
   
class AlbumPelicula(Reproducible):
    def __init__(self):
    def reproduccion(self):
        for cant in self._cantidad:
            cant.reproduccion()
    def add(self, reproducible):
        self._cant.add(reproducible)
    def remove(self, reproducible):
        self._cant.discard(reproducible)

class Terror(Pelicula):
    def reproduccion(self):
        print('Reproducción solo sin entrar a tu Album')

class Comedia(Pelicula):
    def reproduccion(self):
        print('Reproducción solo sin entrar a tu Album')


class Infantil(Pelicula):
    def reproduccion(self):
        print('Reproducción solo sin entrar a tu Album')

def main():
    movie = Movie()
    album = AlbumPeliculas()
    album.add(movie)
    album.reproduccion()

if __name__ == "__main__":
    main()
