import os
import re
import random
import math
from collections import Counter

base_dir_r = r'C:\Users\shrip\Pictures\url_downloads\SwaTest\Test Centre\\'
base_dir_w = r'C:\Users\shrip\Pictures\url_downloads\SwaTest\\'

all_regexes = ["([\(\[]).*?([\)\]])","(\s?www.(.*?).com)|(\s?www.(.*?).pk)","(\s?([A-Z]*[a-z]*[0-9]*))\.com|((\s?([A-Z]*[a-z]*[0-9]*))\.pk)"]

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

                                            # For Brackets
                                            #remov_bracketed_Data(only_name_index)
    apply_all_filters(only_name_index)
                                            #For unbracketed site names
                                            #dele_site_ref(only_name_index)

                                            #to clear songs.pk godo.pk without www
                                            #clean_incomplete_sitenames(only_name_index)

    #To avoid collision for duplicate names
    find_duplicates_in_name(only_name_index)

    # For starting and ending trimming
    trim_data(only_name_index)

    #Write to notepad for better use
    writ_to_file(only_name_index)

    #rename to disk
    renam_the_files(only_name_index)

def clean_spaces_and_number(song_names_dict):
    for k,v in song_names_dict.items():
        #x,y = os.path.splitext(v)
        #Remove numbers
        v = v.lower().translate({ord(c): None for c in '0123456789'})
        #Replace '_' with spaces
        v = v.translate({ord(c): 32 for c in '_%@-=$#&^*'})
        #Replace www and .com
        #replace multiple whitespaces with one space
        z =' '.join(v.split())
        #Same as map.put()
        only_name_index[k] = z
        #print('--> ',z)
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

    rand_num = random.random()
    if rand_num < 1:
        #print('Cool')
        rand_num = math.floor(rand_num * 100000)

    for k,ite in map_for_use.items():
        if ite == '' or ite == ' ':
            only_name_index[k] = str(rand_num)
            continue

        if ite[0] == ' ' or ite[0] == '\.':
            #print('cooler',k)
            ite = ite[2:]

def apply_all_filters(map_for_use):

    for reg in all_regexes:
        for ke, ite in map_for_use.items():

            matches = re.finditer(reg, ite, re.IGNORECASE | re.MULTILINE)
            # print(ite)
            # print('---------')
            diff = 0
            for matchNum, match in enumerate(matches):
                matchNum = matchNum + 1

                # print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                # end=match.end(), match=match.group()))

                ite = ite.replace(ite[(match.start() - diff):(match.end() - diff)], '')


                diff = match.end() - match.start()
                # print(diff)

                only_name_index[ke] = ite

def find_duplicates_in_name(map_to_use):
    '''non_dup_set = {}

    for k in range(1,len(map_to_use)):
        non_dup_set[k] = 0

    print(non_dup_set)
    print(len(map_to_use))

    for i in range(1,len(map_to_use)):
        for j in range (i,len(map_to_use)):
            count = 1
            if map_to_use[i] == map_to_use[j]:
                print('--->',i)
                print('--->',j)
                non_dup_set[i] = non_dup_set[i] + 1
                count = count + 1

    print(non_dup_set)'''

    dupl_count = Counter(map_to_use.values())

    for k,v in map_to_use.items():
        if dupl_count[v] is not 1:
            only_name_index[k] = str(abs(1-dupl_count[v])) + '. ' + v
            dupl_count[v] = dupl_count[v] - 1
    '''for ke,val in map_to_use.items():
        if val in non_dup_set and non_dup_set[val] > 0:
           only_name_index[ke] = str(p) + val
           non_dup_set[val] = non_dup_set[val] + 1
           p = p + 1
        else:
           p=1'''

    for k,v in only_name_index.items():
       only_name_index[k] = only_name_index[k].title()

def renam_the_files(map_to_use):
    for ke,val in index_pathname.items():
        path,fname = os.path.split(val)
        name,ext = os.path.splitext(fname)
        #print(path,'| |',fname,'| |',name,'| |',ext)
        joined_name = only_name_index[ke].lstrip().rstrip() + ext
        print(os.path.join(path,joined_name))
        index_pathname[ke] = os.path.join(path,joined_name)
        os.rename(val,index_pathname[ke])




read_songs(base_dir_r)




