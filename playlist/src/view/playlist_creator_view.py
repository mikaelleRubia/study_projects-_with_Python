import os


class PlaylistCreatorView:
    def playlist_creator_sucess(self, controller_response: dict)-> None:
        self.__clear()

        print("PlayList Criada com Sucesso! \n\n")

        for music in controller_response["playlist"]:
            message = '''
                    Nome da musica: {}
                    Nome do artista: {}
                    Ano da musica: {}

                    '''.format(music.title,
                               music.artist,
                               music.year)
            print(message)

    def register_song_fail(self, controller_response: dict)-> None:
        self.__clear()

        message = '''
            Falha ao criar playlist

            *Erro: {}

            '''.format(
                controller_response["error"], 
            )
        print(message)

    def __clear(self):
        os.system("cls||clear")