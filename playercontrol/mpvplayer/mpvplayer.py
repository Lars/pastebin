
import mpv

class MpvPlayer():
    player = None
    videos = []
    time_callback = None

    def __init__(self, time_callback) -> None:
        self.time_callback = time_callback
        self.player = mpv.MPV()
        self.player.fullscreen = True
        self.player.loop = True
        self.player.observe_property('time-pos', self.time_observer)
        pass

    def set_videos(self, videos):
        self.videos = []
        if type(videos) is list:
            self.videos = videos
        elif type(videos) is str:
            self.videos.append(videos)
    
    def set_callback(self, callback_function):
        self.time_callback = callback_function
    
    #@mpv.MPV.propety_observer('time-pos')
    def time_observer(self, _name, value):
        if(value != None):
            self.time_callback(value)
    
    def seek_to(self, position):
        self.player.seek(position,reference='absolute')
    
    def play(self):
        if len(self.videos) == 0:
            raise PlaylistEmpty
        for entry in self.videos:
            self.player.playlist_append(entry)
        self.player.playlist_pos = 0
