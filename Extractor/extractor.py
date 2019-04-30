# ===== util =====
note_names = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

def get_note_num(note_num, step):
    n = note_num + step
    while n>=12:
        n -= 12
    while n<0:
        n += 12
    return n
    
    
# ===== guesses the song most probable key for the song given it's note occurrences =====
def guess_key(note_occurrences): 
    most_common_note_index = note_occurrences.index(max(note_occurrences))
    if note_occurrences[get_note_num(most_common_note_index,3)] > note_occurrences[get_note_num(most_common_note_index,4)]:
        return f'{note_names[get_note_num(most_common_note_index,3)]}/{note_names[most_common_note_index]}m'
    else:
        return f'{note_names[most_common_note_index]}/{note_names[get_note_num(most_common_note_index,-3)]}m'