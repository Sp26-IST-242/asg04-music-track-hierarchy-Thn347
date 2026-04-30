"""
A collection class that holds MusicTrack objects (Songs and Podcasts).

Design notes:
  • _tracks is kept private (single underscore) and exposed as a *copy*
    through the `tracks` property to protect encapsulation.
  • clear_playlist() uses list.clear() rather than rebinding to None or a new
    list, so the internal object reference stays valid.
  • sort_by_release_year() delegates to list.sort(), which in turn calls
    MusicTrack.__lt__ — the comparison logic defined in Part 3 pays off here.
  • __str__ uses a generator expression with str.join() for a concise
    multi-line string without building an intermediate list manually.
"""
from music_track import MusicTrack


class Playlist:
    def __init__(self):
        self._tracks: list[MusicTrack] = []

    @property
    def tracks(self) -> list[MusicTrack]:
        # Return a defensive copy
        return list(self._tracks)

    def add_track(self, track: MusicTrack) -> None:
        self._tracks.append(track)

    def clear_playlist(self) -> None:
        # Must NOT set _tracks to None
        self._tracks.clear()

    def sort_by_release_year(self) -> None:
        # Relies on MusicTrack.__lt__
        self._tracks.sort()

    def __str__(self) -> str:
        if not self._tracks:
            return ""
        return "\n".join(str(t) for t in self._tracks)
