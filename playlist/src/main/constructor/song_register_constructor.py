from ...view.song_register_view import SongRegisterView
from src.controller.song_register_controller import SongRegisterController

def song_register_process():
    song_register_view = SongRegisterView()
    song_register_controller = SongRegisterController()

    new_song = song_register_view.registry_song_initial()
    response = song_register_controller.insert(new_song)

    if response["success"]:
        song_register_view.register_song_success(response)
    else:
        song_register_view.register_song_fail(response)

    
