from src.models.repositories.music_repository import musics_repository
from src.models.entities.music import Music

class SongRegisterController:
    def insert(self, new_song_informations: dict) -> dict:
        # Principio da Responsabilidade Uníca
        try: 
            self.__verify_songs_infos(new_song_informations)
            self.__verify_if_song_already_registere(new_song_informations)
            self.__insert_song(new_song_informations)
            return self.__format_response(new_song_informations)
        except Exception as exception:
            return self.__format_error_response(exception)

    def __verify_songs_infos(self, new_song_informations: dict) -> None:
        if len(new_song_informations["title"]) > 100:
            raise Exception("Titulo de musica com mais de 100 caracteres") 
        year = int(new_song_informations["year"])
        if year >=2026:
            raise Exception("Ano da musica invalida")
         

    def __verify_if_song_already_registere(self, new_song_informations: dict) -> None:
        song_title = new_song_informations["title"]

        response = musics_repository.find_music(song_title)
        if response is not None:
            raise Exception("Musica já cadastrada!")


    def __insert_song(self, new_song_informations: dict) -> None:
        new_music =  Music(
            title = new_song_informations["title"],
            artist = new_song_informations["artist"],
            year = int(new_song_informations["year"]))
        
        musics_repository.insert_music(new_music)

    def __format_response(self, new_song_informations: dict) -> dict:
        return {
            "success": True,
            "count": 1,
            "attribute": {
                "title": new_song_informations["title"]
            }

        }
    
    def __format_error_response(self, error: Exception) -> dict:
            return {
                "success": False,
                "error": str(error),
            }