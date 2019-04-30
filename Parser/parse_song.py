from Parser.entities import Song
from Parser.parsing_functions import parse_and_add_naming
from Parser.parsing_functions import parse_and_add_track


def file_to_song(filepath):
    # ===========================================================================
    # .txt file to string array
    with open(filepath) as file_input:
        file_lines = file_input.readlines()

    # ===========================================================================
    # instantiate the song
    song = Song()

    # ===========================================================================
    # iterate and strip
    for i, line in enumerate(file_lines):
        line = line.strip('\n')
        line = line.strip()  # strips whitespaces
        file_lines[i] = line  # replaces the old line with the stripped one

    # ===========================================================================
    # new list that contain only non-empty strings
    file_lines = [line for line in file_lines if len(line) > 0]

    # ===========================================================================
    # split song into sections
    name_section = []  # [list of lines]
    track_sections = []  # list of tuples ( string_with_track_name, [list of lines] )

    current_section = name_section

    for i, line in enumerate(file_lines):
        if line.startswith('Track'):
            new_track_section = (line, [])
            track_sections.append(new_track_section)
            current_section = new_track_section[1]
        else:
            current_section.append(line)

    # ===========================================================================
    parse_and_add_naming(song, name_section)
    for track_section in track_sections:
        parse_and_add_track(song, track_section)

    # ===========================================================================
    # returns song
    return song

