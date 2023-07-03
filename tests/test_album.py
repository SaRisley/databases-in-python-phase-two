from lib.album import * 

def test_album_constructs():
    album = Album("test_title", 2023, 1)
    assert album.title == "test_title"
    assert album.release_year == 2023
    assert album.artist_id == 1