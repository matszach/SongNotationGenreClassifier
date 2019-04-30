from Parser.parse_song import file_to_song
import glob
import os

def get_songs(path_as_glob, notify_for_each=False, **kwargs):
    # holds all parsed songs as a object of type 'Song'
    songs = []
    genre_name = kwargs.get('genre', None)

    # for each .txt file in "songs" directory ...
    for filepath in glob.glob(path_as_glob):
        
        if notify_for_each:
            print(f'now parsing \"{filepath}\"')
            
        song = file_to_song(filepath)
        
        if genre_name!=None:
            song.genre = genre_name
            
        songs.append(song)
#         slash = '/'
        
#         new_file_title = f'Songs/{genre_name}/{song.artist.translate(slash, None)}-{song.title.translate(slash, None)}'
        
#         while(os.path.isfile(new_file_title + '.txt')):
#             new_file_title += '1'
            
#         os.rename(filepath, new_file_title+'.txt')
        
    
    return songs

