from ...view.playlist_creator_view import PlaylistCreatorView
from src.controller.playlist_creator_controller import PlaylistCreatorController

def playlist_creator_process():
    playlist_creator_view = PlaylistCreatorView()
    playlist_creator_controller = PlaylistCreatorController()

    response = playlist_creator_controller.create_playlist()
    if response["success"]:
       playlist_creator_view.playlist_creator_sucess(response)
    else:
        playlist_creator_view.register_song_fail(response)
    
