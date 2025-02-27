from project.song import Song
class Album:
    def __init__(self, name: str, *songs: Song):
        self.name = name
        self.published = False
        self.songs = [*songs]

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the albums."

        self.songs.append(song)
        return f"Song {song.name} has been added to the albums {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot remove songs. Album is published."

        s = next((s for s in self.songs if s.name == song_name), None)
        if s:
            self.songs.remove(s)
            return f"Removed song {s.name} from albums {self.name}."

        return f"Song is not in the albums."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        return f"Album {self.name}\n" + "\n"'== '.join(Song.get_info(song) for song in self.songs)
