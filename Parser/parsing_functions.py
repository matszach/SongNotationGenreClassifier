from Parser.entities import Track
from Parser.entities import Note
from Parser.pattern_bank import pitch_pattern_bank
from string import digits



# ===========================================================================
def parse_and_add_naming(song, name_section):
    for line in name_section:
        # finds title
        if line.startswith('Title: '):
            name = line.replace('Title:', '')
            name = name.strip('\'\" ')  # strip quotes and whitespaces
            song.title = name

        # finds artist
        elif line.startswith('Artist: '):
            name = line.replace('Artist:', '')
            name = name.strip('\'\" ')
            song.artist = name

        # finds album
        elif line.startswith('Album: '):
            name = line.replace('Album:', '')
            name = name.strip('\'\" ')
            song.album = name


# ===========================================================================
def parse_and_add_track(song, track_section):
    # instantiate a track
    track = Track()

    # find track instrument name
    track.instrument = get_track_name(track_section[0])

    # parse track's notes
    parse_notes(track, track_section[1])

    # add the track to the song
    song.tracks.append(track)


def get_track_name(track_naming_string):
    name = track_naming_string.replace('Track', '')
    name = ''.join([c for c in name if not c.isdigit() and c is not ':'])
    name = name.strip()
    if len(name) == 0:
        name = 'unknown'  # a track named "Track 1" etc. would result in an empty name otherwise
    return name


def parse_notes(track, note_section):
    # string pattern
    pattern = get_string_pattern(note_section)
    track.string_pattern = pattern
    # separate spring chains
    # initiate tuples ( string_note_char, [tab_chain_of_that_string] )
    symbols_with_tab_chains = [(x, []) for x in pattern]
    rot = 0
    while rot < len(note_section):
        for i in range(len(pattern)):
            symbols_with_tab_chains[i][1].append(note_section[rot])
            rot += 1
    # cleanup to tuples ( string_base_note_pitch, tab_chain_as_one_string )
    cleanup_tab_chains(symbols_with_tab_chains)
    # encode track's notes and add them to the track
    parse_notes_for_track(track, symbols_with_tab_chains)


def get_string_pattern(note_section):
    # group first symbols from each line in note section
    leading_symbols = []
    for line in note_section:
        leading_symbols.append(line[0])
    # test every possible pattern length except 0
    for x in range(1, len(leading_symbols)):
        # establish test_pattern consisting of first x characters
        test_patten = ''.join(leading_symbols[:x])
        # join leading symbols into a string, then replace every occurrence of test_pattern with '' (empty string)
        symbols = ''.join(leading_symbols).replace(test_patten, '')
        # if, after the replacing, there's nothing left in the symbols string,
        # that means that the pattern is valid and can be returned
        if len(symbols) == 0:
            if test_patten.__eq__('C'):
                test_patten = 'CCCCCC'  # exception for drum tab notation (those are marked as "CCCCCC")
            return test_patten
    # if no pattern found, and for loop finished (which should be impossible) - raise an exception
    raise Exception('pattern not found')


def cleanup_tab_chains(symbols_with_tab_chains):
    # get the track note pattern
    note_pattern = [pair[0] for pair in symbols_with_tab_chains]
    # compare track's pattern to the ones from the pattern_bank
    for hcpattern in pitch_pattern_bank:
        # if match found -> override the note name with it's base pitch (pitch of an "0th" note on that string)
        if note_pattern == hcpattern[0]:
            for i in range(len(symbols_with_tab_chains)):
                symbols_with_tab_chains[i] = (hcpattern[1][i], symbols_with_tab_chains[i][1])  # tuples are immutable
            break  # break loop if a match was found
    else:
        # if no match found and the loop completed -> raise an exception
        # raise Exception('matching pattern not found')
        pattern_to_string = ''.join(note_pattern)
        print(f'* no matching pattern found for \"{pattern_to_string}\", applying a default pattern *')
        default_pattern = pitch_pattern_bank[0]
        for i in range(len(symbols_with_tab_chains)):
                symbols_with_tab_chains[i] = (default_pattern[1][i], symbols_with_tab_chains[i][1])
        

    # join tab notation for each string into a single character chain
    for i, pairing in enumerate(symbols_with_tab_chains):
        tab_chain = ''
        for tab_row in pairing[1]:
            # strip first and last character (no leading string note and no double vertical lines)
            tab_row = tab_row[1:-1]
            tab_chain = tab_chain + tab_row
            symbols_with_tab_chains[i] = (pairing[0], tab_chain)  # tuples are immutable


# ===========================================================================
def parse_notes_for_track(track, tab_chain):
    notes = []  # track's notes field
    current_bar = []  # separated section, waiting for the bar to finish to pass the correct note length
    bar_length = 0  # incremented once for every symbol parsed
    for i in range(len(tab_chain[0][1])):
        current_notes = []  # list of all the notes played at once on this track
        for j in range(len(tab_chain)):
            # if the read character is a digit, that means that a note was found
            if tab_chain[j][1][i] in digits:
                # if the previous character was also a digit - skip, the note has already been parsed
                if tab_chain[j][1][i-1] in digits:
                    continue
                # if the next character is also a digit - parse the note, it has been written down as a 2 digit number
                # ( 3 digit notation should not occur )
                if tab_chain[j][1][i+1] in digits:
                    note_pitch = tab_chain[j][0] + int(tab_chain[j][1][i])*10 + int(tab_chain[j][1][i+1])
                    n = Note(note_pitch)
                # the note has been written down as a single digit
                else:
                    note_pitch = tab_chain[j][0] + int(tab_chain[j][1][i])
                    n = Note(note_pitch)
                current_notes.append(n)
        # section of notes played at the same time passed to current bar
        current_bar.append(current_notes)
        bar_length += 1
        # if " | " symbol found, that means that the current bar is finished
        if tab_chain[0][1][i] == '|':
            # pass each set of simultaneous notes to track's notes
            for k, note_set in enumerate(current_bar):
                # look forward and get the length of a note_set
                set_note_length = 1
                for l in range(k+1, len(current_bar)):
                    # if the next set is empty, increment note length
                    if len(current_bar[l]) == 0:
                        set_note_length += 1
                    # if the next not-empty note_set found, then the note length has also been found
                    else:
                        break
                # add note length for each note
                for note in note_set:
                    note.length = f'{set_note_length}/{bar_length-1}'
                notes.append(note_set)
            # reset bar
            current_bar = []
            bar_length = 0
    # pass the notes to the track
    track.notes = notes

