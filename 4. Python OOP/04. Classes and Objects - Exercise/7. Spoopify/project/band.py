from project import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        searched_album = next((searched_album for searched_album in self.albums if searched_album.name == album_name),
                              None)
        if searched_album:
            if searched_album.published:
                return f"Album has been published. It cannot be removed."
            self.albums.remove(searched_album)
            return f"Album {searched_album.name} has been removed."

        return f"Album {album_name} is not found."

    def details(self):
        return f"Band {self.name}\n" + "\n".join(album.details() for album in self.albums)
