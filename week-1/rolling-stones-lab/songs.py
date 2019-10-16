#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 17:15:52 2019

@author: flatironschool
"""
# import csv

text_file = open('top-500-songs.txt', 'r')
       # read each line of the text file
       # here is where you can print out the lines to your terminal and get an idea
    #for how you might think about re-formatting the data
lines = text_file.readlines()
songs = []
#for each line in the list of lines
for line in lines:
    #remove the \n treat before and after as seperate strings
    song = line.strip('\n')
    #remove the \t from the front and back as seperate strings 
    songs.append(song.split('\t'))

songs_as_dicts = []
for song in songs:
    #create dict keys and assign them the empty song_as_dict dictionary
    song_as_dict = {}
    song_as_dict['rank'] = song[0]
    song_as_dict['name'] = song[1]
    song_as_dict['artist'] = song[2]
    song_as_dict['year'] = song[3]
    songs_as_dicts.append(song_as_dict)
    
print(songs_as_dicts[0])