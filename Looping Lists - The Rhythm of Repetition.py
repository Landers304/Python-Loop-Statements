#Task 1: 


genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for i, genre in enumerate(genres, start=1):
    print(f"Track {i}: Listening to {genre}!")




#Task 2: 


genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

track_number = 1

while track_number <= len(genres):
    genre = genres[track_number - 1]
    print(f"Track {track_number}: Now playing {genre}")
    
    if genre == 'Hip-hop':
        print("Loop is stopped when playing hip-hop.")
        break
    
    track_number += 1




#Task 3:


genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for track_number in range(len(genres)):
    genre = genres[track_number]
    
    if genre == 'Classical':
        print(f"Track {track_number + 1}: {genre} is not suitable for the light show.")
        continue
    
    print(f"Track {track_number + 1}: {genre} - Light show is ready!")
