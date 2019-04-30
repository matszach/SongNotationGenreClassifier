
class Note:

    def get_print(self):
        return f'{self.pitch} ({self.length})'

    def __init__(self, pitch, length='unknown_length'):
        self.pitch = pitch
        self.length = length


class Track:

    def print(self, track_num):
        print(f'Track {track_num} - {self.instrument} ({self.string_pattern})')

    def print_with_notes(self, track_num):
        self.print(track_num)
        for note_row in self.notes:
            note_message = []
            for n in note_row:
                note_message.append(n.get_print())
            print(note_message)

    def print_with_notes_skip_empty(self, track_num):
        self.print(track_num)
        for note_row in self.notes:
            if len(note_row) == 0:
                continue
            note_message = []
            for n in note_row:
                note_message.append(n.get_print())
            print(note_message)

    def __init__(self, instrument='unknown', string_pattern='unknown'):
        self.notes = []
        self.instrument = instrument
        self.string_pattern = string_pattern


class Song:

    def print(self):
        print(f'{self.artist} - \"{self.title}\" ({self.album})')

    def print_with_tracks(self):
        print('== Song ==')
        self.print()
        print('== Tracks ==')
        for i, t in enumerate(self.tracks):
            t.print(i + 1)

    def print_with_notes(self):
        print('== Song ==')
        self.print()
        print('== Tracks ==')
        for i, t in enumerate(self.tracks):
            t.print_with_notes(i + 1)

    def print_with_notes_skip_empty(self):
        print('== Song ==')
        self.print()
        print('== Tracks ==')
        for i, t in enumerate(self.tracks):
            t.print_with_notes_skip_empty(i + 1)
      
    def get_note_occurence(self):
        note_occ = [0 for i in range(12)]
        for track in self.tracks:
            if track.string_pattern == 'CCCCCC':
                # skip drum tracks
                continue
            for row_of_notes in track.notes:
                for note in row_of_notes:
                    note_num = note.pitch%12
                    note_occ[note_num] += 1
        return note_occ

    def __init__(self, artist='unknown', title='unknown', album='unknown', genre='unknown'):
        self.tracks = []
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre

