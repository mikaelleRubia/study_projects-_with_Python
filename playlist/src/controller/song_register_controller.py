
class SongRegisterController:
    def insert(self, new_song_informations: dict) -> dict:
        # Principio da Responsabilidade Uníca
        self.__verify_songs_infos(new_song_informations)
        self.__verify_if_song_already_registere(new_song_informations)
        self.__insert_song()
        self.__format_response()
        pass

    def __verify_songs_infos(new_song_informations: dict) -> None:
        pass

    def __verify_if_song_already_registere(new_song_informations: dict) -> None:
        pass

    def __insert_song() -> None:
        pass

    def __format_response() -> None:
        pass
