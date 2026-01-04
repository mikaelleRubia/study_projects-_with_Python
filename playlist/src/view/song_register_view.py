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


    def register_song_success(self, controller_response: dict)-> None:
        self.__clear()

        message = '''
            Musica Cadastrada com sucesso!

            * Tituto: {}
            * Qunatidade: {}

            '''.format(
                controller_response["attribute"]["title"], 
                controller_response["count"], 

            )
        print(message)

    def register_song_fail(self, controller_response: dict)-> None:
        self.__clear()

        message = '''
            Falha ao Cadastrar musica

            *Erro: {}

            '''.format(
                controller_response["error"], 
            )
        print(message)


    def __clear(self):
        os.system("cls||clear")