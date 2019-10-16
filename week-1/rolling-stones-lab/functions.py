import csv
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
# %matplotlib inline

with open('data.csv') as f:
    catalogue = csv.DictReader(f)
    top_500 = []
    for row in catalogue:
        top_500.append(row)

#    print(top_500)
        
#Find by name - Takes in a string that represents the name of an album. 
#Should return a dictionary with the correct album, or return None.
#

    def search_name(album_name):
        for album in top_500:
            if album_name == album['album']:
                #print(album)
                return album
        return None
    
 #   print(search_name('The Stone Roses'))
        
#Find by rank - Takes in a number that represents the rank in the list of 
#top albums and returns the album with that rank. If there is no album with that 
#rank, it returns None.
#
    def search_rank(album_rank):
        for album in top_500:
            if album_rank == album['number']:
                #print(album)
                return album
        return None
    
#    print(search_rank('498'))
    
#Find by year - Takes in a number for the year in which an album was 
#released and returns a list of albums that were released in that year. 
#If there are no albums released in the given year, it returns an empty list.
#
    def search_year(album_year):
        years_albums = []
        for album in top_500:
            if album_year == album['year']:
                #print(album)
                years_albums.append(album)
                
        return years_albums
    
#    print(len(search_year('1990')))
    
#Find by years - Takes in a start year and end year. 
#Returns a list of all albums that were released on or between the start and 
#end years. If no albums are found for those years, then an empty list is returned.
#
    def start_end_year(start, end):
        era_albums = []
        for album in top_500:
            if (int(album['year']) >= start) and (int(album['year']) <= end):
                #print(album)
                era_albums.append(album)
                
        return era_albums
        
#    print(len(start_end_year(1989, 1990)))
        
#Find by ranks - Takes in a start rank and end rank. 
#Returns a list of albums that are ranked between the start and end ranks. 
#If no albums are found for those ranks, then an empty list is returned.
    
    def start_end_rank(start, end):
        ranks_albums = []
        for album in top_500:
            if (int(album['number']) >= start) and (int(album['number']) <= end):
                #print(album)
                ranks_albums.append(album)
                
        return ranks_albums

 #   print(start_end_rank(1, 10))    
    
##   All titles - Returns a list of titles for each album.
        
    def all_titles():
        titles = []
        for album in top_500:
            titles.append(album['album'])
        return titles
    
#    print(all_titles())
#    print(len(all_titles()))
    
#    All artists - Returns a list of artist names for each album. 
    def all_artists():
        artists = []
        for album in top_500:
#            print(album['album'])
            artists.append(album['artist'])
        return artists
#    print(len(all_artists()))
#    print(len(all_artists()))
    

#Artists with the most albums - Returns the artist with the highest amount of
#albums on the list of top albums
#
    def most_albums():
        total_artist_list = all_artists()
        unique_artists = dict.fromkeys(sorted(set(total_artist_list)),0)
        
        # creating counts of albums by artist
        for artist in unique_artists:
            unique_artists[artist] = total_artist_list.count(artist)
        
        # finding artist with highest count
        max_albums = 0
        max_artists = []
        for artist in unique_artists:
            if unique_artists.get(artist) == max_albums:
                #adds artists if it has the same number as the max
                max_artists.append(artist)
            #if the number of albums is greater than the previous artists
            elif unique_artists.get(artist) > max_albums:
                #reset the list of artists to be empty
                max_artists = []
                #add the new artists to the newly emptied list
                max_artists.append(artist)
                #set the max albums equal to the list of artists with the most
                max_albums = unique_artists.get(artist)
        return max_artists
        
    
#    print(most_albums())
    
#Most popular word - Returns the word used most in amongst all album titles
#
    def most_pop_word():
        #use the list of all the album titles
        total_album_titles = all_titles()
        #split the individual albums titles into indiv words
        words = []
        clean_titles = []
        for title in total_album_titles:
            clean_titles.append(title)
            words.extend(title.split())
        
        for word in words:
            #replace , & / with ''
            if word == '&':    
                words.remove('&')
            if word == '/':
                words.remove('/')
            #corner cases end of starts with punct
            #words.replace(word, word.strip('?'))
            
        # make dictionary of unique words
        unique_words = dict.fromkeys(sorted(set(words)),0)

        # get counts of words
        for word in unique_words:
            unique_words[word] = words.count(word)
            
        # find which word is the most common in the list
        max_count = 0
        max_words =[]
        for word in unique_words:
            if unique_words.get(word) == max_count:
                #adds artists if it has the same number as the max
                max_words.append(word)
            #if the number of albums is greater than the previous artists
            elif unique_words.get(word) > max_count:
                #reset the list of artists to be empty
                max_words = []
                #add the new artists to the newly emptied list
                max_words.append(word)
                #set the max albums equal to the list of artists with the most
                max_count = unique_words.get(word)
        return max_words
        
#    print(most_pop_word())
#Histogram of albums by decade - Returns a histogram with each decade pointing 
#to the number of albums released during that decade.
#
    def album_decades():
        years = []
        #add each album year in our top 500 list to the years list  
        for album in top_500:   
            years.append(int(album['year']))
        #find the lowest year in the years list 
        start = min(years)
        # include trailing decade and round down
        end = round(max(years) + 5, -1) 
        current_start = start
        current_end = round(start, -1) - 1
#        decades = []
        dec_bins = []
        

        while current_end < end:
#            decades.append(str(current_start) + '-' + str(current_end))
            dec_bins.append(current_start)
            current_start = current_end + 1
            current_end += 10
       
        dec_bins.append(end) # include end of last decade
        print(dec_bins)
        
        
        return plt.hist(years, edgecolor = 'black', bins = dec_bins)
        
#    album_decades()
      
#Barplot by genre - Returns a barplot with each genre pointing to the number 
#of albums that are categorized as being in that genre.
    def genre_count():
        genres = []
        clean_genres = []
        for album in top_500:   
            #add album genre unclean to genres list
            genres.append(album['genre'])
        
        for genre in genres:
            # seperate each genre by ,
            current_album = genre.split(',')
            clean_album_genres = []
            #we are getting rid of extraneous instances
            for current_genre in current_album:
                current_genre = current_genre.strip()
                current_genre = current_genre.strip('&')
                current_genre = current_genre.strip()
                clean_album_genres.append(current_genre)
            #add all of the clea_album_genres tot he clean_genres list 
            clean_genres.extend(clean_album_genres)
        
        # make dictionary of unique genres
        unique_genres = dict.fromkeys(sorted(set(clean_genres)),0)

        # get counts of words
        for genre in unique_genres:
            unique_genres[genre] = clean_genres.count(genre)
        
#        print(unique_genres)
         
        x= unique_genres.keys()
        y= unique_genres.values()
        plt.bar(x, y, color = 'green')
        
        plt.xticks(rotation = 'vertical')
    genre_count()
    
    
    
    
    