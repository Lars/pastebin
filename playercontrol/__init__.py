from enum import Enum
from .mpvplayer import mpvplayer

class PlaylistEmpty(Exception):
    pass

class Status(Enum):
    STOPED = 1
    PLAYING = 2
    PAUSED = 3
    BLANKED = 4

def player(player_type, time_callback):
    if(player_type == 'mpv'):
        return mpvplayer.MpvPlayer(time_callback)