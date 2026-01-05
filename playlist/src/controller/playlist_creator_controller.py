from src.models.repositories.music_repository import musics_repository
from src.models.entities.music import Music
import random


class PlaylistCreatorController:
    def create_playlist(self) -> dict:
        try:
            musics = self.__get_all_musics_and_verify()
            playlist = self.__create_playlist(musics)
            return self.__format_response(playlist)
        
        except Exception as exception:
            return self.__format_error_response(exception)


    def __get_all_musics_and_verify(self) -> list:
        musics = musics_repository.get_all_songs()
        if musics == []:
            raise Exception("Lista de musicas vazia!")
        return musics

    def __create_playlist(self, musics: list) -> list:
        random.shuffle(musics)
        return musics
    
    def __format_response(self, musics: list) -> dict:
        return {
            "success": True,
            "playlist": musics
        }
    
    def __format_error_response(self, error: Exception) -> dict:
            return {
                "success": False,
                "error": str(error),
            }