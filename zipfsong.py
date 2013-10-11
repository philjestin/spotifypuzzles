#Philip Middleton
#Spotify Puzzle
#Problem ID: zipfsong

import sys

'''
zipfs_value:
This takes in total_number_of_listens and the number_of_songs
and finds the summation_total 1/i and the expected_score a song would get
is the total_number_of_listens / summation_total
This returns the value of total_number_of_listens / summation_total 
'''
def zipfs_value(total_number_of_listens, number_of_songs):
    summation_total = 0
    for i in range (1, int(number_of_songs)+1):
        summation_total += 1.0/i
    z_value = total_number_of_listens / summation_total
    return z_value

'''
compare_values:
This takes in songs, the list 'songs' and the z_value
b
'''
def compare_values(songs, z_value):
    for index,item in enumerate(songs):
        n = index+1
        expected_score = z_value/n
        quality = int(item[0]) - expected_score
        item.append(quality)
        item.append(n)

    songs.sort(key=lambda x: x[2])
    songs.reverse()
    #songs.sort(lambda x,y: cmp(y[2], x[2]))            
    return songs

'''
final_results:
Takes the formatted list and prints the top songs based on songs_to_select
'''
def final_results(songs, songs_to_select):
    songs_to_select = int(songs_to_select)
    count = 0
    while (count < songs_to_select):
        print(songs[count][1])
        count += 1

'''
'''
def main():
    songs = []
    sorted_songs = []
    z_value = 0
    total_number_of_listens = 0

    [number_of_songs,songs_to_select] = raw_input().split(" ")

    for x in range(0,int(number_of_songs)):
        line = raw_input().replace("\n","")
        line = line.split(" ")
        songs.append(line)

    for item in songs:
        total_number_of_listens += int(item[0])

    #Call zips_value
    z_value = zipfs_value(total_number_of_listens, number_of_songs)
   
    sorted_songs = compare_values(songs, z_value)
    final_results(sorted_songs, songs_to_select)


if __name__ == '__main__':
    main()