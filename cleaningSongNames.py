import os
import re
import random
import math

base_dir_r = r'C:\Users\shrip\OneDrive\Music\\'
base_dir_w = r'C:\Users\shrip\Pictures\url_downloads\SwaTest\\'

#Global map to store the dirty name as key and the clean name as value

index_pathname = {}
only_name_index = {}


def read_songs(dir_to_r):
    song_names_dict = {}
    song_names = []
    i=0
    for root, dirs, files in os.walk(dir_to_r, topdown=True):
        for filenames in files:
            i=i+1
            filepath = os.path.join(root, filenames)

            #Fill the list
            song_names.append(filenames)
            b, ext = os.path.splitext(filenames)

            #Only for songs, not the picture covers
            if str(ext) != '.jpg':
                #Index with entire filepath
                index_pathname[i] = filepath

                #Index with name except extension
                only_name_index[i] = b

    clean_names(only_name_index)



def clean_names(song_names_dict):

    #Abstraction
    clean_spaces_and_number(only_name_index)
    #For Brackets
    pattern_matchng(only_name_index)

    #For starting and ending trimming
    trim_data(only_name_index)

    #Write to notepad for better use
    writ_to_file(only_name_index)


def clean_spaces_and_number(song_names_dict):
    for k,v in song_names_dict.items():
        #x,y = os.path.splitext(v)
        #Remove numbers
        v = v.lower().translate({ord(c): None for c in '0123456789'})
        #Replace '_' with spaces
        v = v.translate({ord(c): 32 for c in '_%@-'})
        #Replace www and .com
        #replace multiple whitespaces with one space
        z =' '.join((v).split())
        #Same as map.put()
        only_name_index[k] = z
        #print('--> ',z)
    return

#How to write Reg Ex expression to remove everything written in [ ]
#Only remove characters written in () if there is a '.' inside (.)
def pattern_matchng(clean_name_map):
    regex = r"([\(\[]).*?([\)\]])"
    for ke, ite in clean_name_map.items():
        matches = re.finditer(regex, ite, re.IGNORECASE | re.MULTILINE)
        #print(ite)
        #print('---------')
        diff = 0
        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1

            #print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                                #end=match.end(), match=match.group()))

            ite = ite.replace(ite[(match.start() - diff):(match.end() - diff)], '')
            #print(ite)

            diff = match.end() - match.start()
            #print(diff)

        clean_name_map[ke] = ite
    return

#FOr testing purposes, write to a file
def writ_to_file(song_names_dict):
    fil_to_w_dir = base_dir_w + 'all_songs.txt'
    file_w = open(fil_to_w_dir, 'w')
    file_w.write('\n---------------------------------------------------------------------------- \n \n')
    for k,v in song_names_dict.items():
        file_w.write('key :')
        file_w.write(str(k))
        file_w.write(' | ')

        file_w.write('val: ')
        file_w.write(v)
        file_w.write(' | ')
        file_w.write(' | ')
        file_w.write(index_pathname[k])
        file_w.write('\n')
    file_w.close()

def trim_data(map_for_use):
    regex = r"(\s?www.(.*?).com)|(\s?www.(.*?).pk)"
    rand_num = random.random()
    if rand_num < 1:
        print('Cool')
        rand_num = math.floor(rand_num * 100000)

    for k,ite in map_for_use.items():
        if ite == '' or ite == ' ':
            only_name_index[k] = str(rand_num)
            continue

        if ite[0] == ' ' or ite[0] == '\.':
            print('cooler',k)
            ite = ite[2:].lstrip()

def pattern_match(regex,map_to_operate):

read_songs(base_dir_r)




