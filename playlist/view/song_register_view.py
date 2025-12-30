import os


class SongRegisterView:

    def registry_song_initial(self) -> dict:
        self.__clear()
        print("Implementar Nova Musica \n\n")

        title = input("Digite o nome da musica: ")
        artist = input("Digite o nome do artista: ")
        year = input("Digite o ano da musica: ")

        new_song_informations = {"title": title, "artist": artist, "year": year}

        return new_song_informations

    def __clear(self):
        os.system("cls||clear")
