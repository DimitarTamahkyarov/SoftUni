from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for i in range(len(self.photos)):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)

                return f"{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}"

        return "No more free slots"

    def display(self):
        result = []
        result.append("-" * 11)

        for row in range(len(self.photos)):
            curr_row = []
            for col in range(len(self.photos[row])):
                if self.photos[row][col] != "":
                    curr_row.append("[]")
                else:
                    break
            result.append(" ".join(curr_row))
            result.append("-" * 11)

        return "\n".join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

