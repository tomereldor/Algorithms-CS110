# SONG (Harmony) SIMILARITY ALGORITHM


def parseSong(filepath):
    songtitle = filepath.title().split('/')[-1:][0]
    if songtitle.lower().endswith(".txt"):
        songtitle = songtitle[:-4]
    # parsing the song extracted as text from web into meaningful information.
    # first, we will divide the content into lines.
    # first, we will divide the content into lines.
    with open(filepath) as txt:
        # seperating into lines, stripping the "\n" expression of new lines
        linelist = [line.rstrip('\n') for line in txt]

        # formatting: iterate through the last 5 rows and delete if they are
        # empty rows
        endlist = len(linelist) - 1
        for i in range(endlist, endlist - 5, -1):
            if linelist[i] == "":
                del linelist[i]

    # filtering and treating lines: seperating into different lists
    # parse sections individually:
    titlesections = []
    lyrics = []
    lyrics_section_seperator = False  # preference: if we want the lyrics to
    # indicate when a new section (verse/chorus) starts. Currently is False.
    chords = []

    for i in xrange(0, len(linelist) - 1):
        # base case: if the item is an empty line
        line = linelist[i]
        # defining variable for current line for ease of use and readability

        if line == "":
            # if the next line is also empty, Or this is simply the first or
            # last line, just skip to the next line.
            if linelist[i + 1] == "":
                continue
            # else, if the next line has content, then it must be a title of a
            # new section. improvement: treat songs were some sections do not
            # begin with a title: recognize titles if they fit a dictionary of
            # title starts. The problem with that: more costly (checking line
            # with every dictionary item) rather then just O(1) of taking the
            # first line as the title.
            else:
                # next line must be a title
                titlesections.append((linelist[i + 1]).upper())  # append to titles, as uppercase
                linelist[i + 1] = "|"
                # I currently do not want the lyrics to include names of
                # sections. but I may want to indicate a seperation between
                # sections. I will do that by changing the line into a
                # seperator mark.
                continue  # do not add the empty line anywhere

        if line == "|" and not lyrics_section_seperator:
            # removing (or keeping, if lyrics_section_seperator == True) the
            # seperator mark for lyrics:
            continue
        # Chord Lines:
        elif "2x" in line or "2X" in line or "x2" in line or "X2" in line:
            # preferred to write out all options rather than iterating through
            # a list of them or preforming line.lower() on the entire line
            # since it is less costly.
            # some chords lines have "2x" meaning, repeat twice:
            line = line.replace("2x", "")  # removing the "2x" from the line
            # get rid of redundant spaces in the chords list, and make it a
            # list of individual chords:
            chords.extend(2 * line.split())  # add it twice
        elif "  " in line:  # in all chord lines there is at least once a
            # double space! that was the most efficient way to check, more
            # efficient than comparing if the items are only chords, or Upper
            # Case, or exclude others; because this is normally found even in
            # the beginning of the line. otherwise, it is a normal chords line
            # get rid of redundant spaces in the chords list, and make it a
            # list of individual chords:
            chords.extend(line.split())
            # extending, for creating a continuous chord progression of the
            # entire section

        else:
            # Lyrics lines (all others)
            lyrics.append(line)  # this does not have to be split by section.

    # adding the chords of just this section into the full songs chords
    # list (divided by section)
    #print "Title:", songtitle
    #print "Sections:", titlesections
    #print "Original Key Chords:", chords
    #print "Lyrics: ", lyrics
    #print "____________________"

    return titlesections, chords, lyrics, songtitle

###################################################

# defining an orderes chromatic scale with EITHER flats or sharps
flats = ["Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G"]
sharps = ["G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G"]


def strip_chord_to_letter(fullchord):
    #stripping down a chord (could be F#m7) to just its base letter, including sign: F#m7 --> F#.
    # greediest: 1st item is always letter. second item is either a key
    # sign (b,#) which we need, and afterwhich (second char or 3rd)
    # begins chord type which we dont need. I will filter from the
    # least costly to the more:
    if len(fullchord) > 1:
        basechord = fullchord[:2]
        # stripping the chord to the first 2 chars, maximum needed
        # (like Eb, but still can be Em)
        if basechord[1] not in ("", "#", "b"):
            basechord = basechord[0]
    else:
        #then the chord was only the base
        basechord = fullchord
    return basechord



#creating a dic to convert ill-written tranposed chords to well written chords.
# (Some, like D#, are possible to write, but just less common than it's equivalent, Eb.
#using a dic for the best performance of O(1) lookup
available_chords_dic = {'Abb' : 'G',
                        'A##' : 'B',
                        'A#': 'Bb',
                        'Bbb': 'A',
                        'B#' : 'C',
                        'Cbb' : 'Bb',
                        'Cb' : 'B',
                        'C##': 'D',
                        'Dbb': 'C',
                        'D#' : 'Eb',
                        'D##' : 'E',
                        'Ebb': 'D',
                        'E#': 'F',
                        'E##': 'F#',
                        'Fb' : 'E',
                        'F##' : 'G',
                        'Gbb': 'F',
                        'G#' : 'Ab',
                        'G##' : 'A',
                        }


#A small function to autmatically create redundant #b chords dic:
def natural_chords_dic():
    global available_chords_dic
    chordletters = ["A","B","C","D","E","F","G"]
    chordtone = ["#b","b#"]
    for original_letter in chordletters:
        for tone in chordtone:
            bad_note = original_letter+tone
            available_chords_dic[bad_note] = original_letter
    return available_chords_dic

#run to update chords dictionary
natural_chords_dic()


def guess_key(chords):
    global flats, sharps
    # this function GUESSES the probable key in a greedy way, and is not 100%
    # certain; since I believe there is no any real way to determine the key
    # with 100% certainty anyway, so wew might as well create some efficient
    # guesses.

    # simplest, greediest method: the last chord is almost always the key.
    # probably the tonic, if the
    # song does not end on a modulated key. I will check that it was not by
    # finding the tonic chord in the first part of the song, approximating
    # first ~30% of the song
    if chords[-1] in chords[:int(len(chords) * 0.5)]:
        # debug remove and False
        key = strip_chord_to_letter(chords[-1])
        return key

    #if it is not that simple, we'll examine the next heuristics.
    common_bases = []
    #second easy metric; chords with "7" (and not m7 or min7) are likely to be a "dominant" chord.
    #later we will calculate the expected key from the dominant chord using the list of COMMON BASES.
    # I'll add any chord with 7 to the chommon bases for later inspection of occuences and scale degrees.
    for chord in chords:
        if "7" in chord and "min" not in chord and "m" not in chord:
            common_bases.append(strip_chord_to_letter(chord))

    if common_bases == []:
        # if this is not the case, the song has probably been modulated, or
        # ending on a non traditional chord; most likely the 5th (dominant),
        # because these chords websites might sometimes keep it like that.

        # I only need the first ~20% of the song to know the key more
        # efficiently. The Chorus is many times in a different key and
        # sometimes later on in the song they modulate to a different key
        # altogether, so this saves us search space.
        chordstart = chords[0:int(len(chords) * 0.3)]
        # Finding occurences of unique chords.
        uniqueChords = set(chordstart)  # remove duplicate words and sort
        chords_occurences = []
        for chord in uniqueChords:
            chords_occurences.append((chordstart.count(chord), chord))
        chords_occurences.sort(reverse=True)
        # I could also implement a heapq.nlargest here, but the lists of chords
        # of the first 20% of the song is usually incredibly small, and in
        # popular songs is usually only up to 8 items, so this is more
        # convenient and organized.
        # creating 2 lists: common 4 chords as they are, and common 4 chords
        # bases (stripping out chord type)
        for chord_occurence in chords_occurences[:4]:
            chord = chord_occurence[1]
            chord = strip_chord_to_letter(chord)
        common_bases.append(chord)

    # algorithm to assume key:
    # if 2 of the most common chords are Major and have a large 2nd
    # interval between them, meaning 2 steps, they are most likely the 4th
    # and 5th in the scale; they could lead us to the 1.

    #now, taking the common bases - either with the dominant 7,
    # or from the most common bases calculations and finding which one is the dominant:
    for i in xrange(len(common_bases)):
        for j in xrange(i + 1, len(common_bases)):
            # (checking items couples without repetition)
            chord1 = common_bases[i]
            chord2 = common_bases[j]
            if flats.index(chord1) - flats.index(chord2) in (2, -10):
                # if the chord1 is 2 steps above chord2 (like D to C), D is
                # probably dominant and C is probably subdominant
                # #-I would like to use subdominant later in analzying the chords by their "degrees".
                # I currently didn't implement that function but this is good to already determine now.
                dominant, subdominant = chord1, chord2
                tonicaindex = (flats.index(dominant) + 5) % len(flats)
                key = flats[tonicaindex]
            elif flats.index(chord2) - flats.index(chord1) in (2, -10):
                # opposite side
                dominant, subdominant = chord2, chord1
                tonicaindex = (flats.index(dominant) + 5) % len(flats)
                key = flats[tonicaindex]
            else:
                # if this has failed, I have no efficient huristic to find out key,
                # rather than it's just very likely to be the one the song started with,
                # if that one is also common throughout the song:
                if chords[0] in common_bases:
                    key = chords[0]
                else:
                #then we've exhausted our probable huristics and will ask the user
                    print "Couldn't guess key! please insert manually the key for the song with these chords:"
                    print chords
                    key = strip_chord_to_letter(raw_input("Insert Key: "))

    ##check to see the key is compatible:
    if key in available_chords_dic:
        print key , "is in available_chords_dic"
        key = available_chords_dic[key] #converting form ill-written to well-written
        print "new key: ", key


    return key


### TRANSPOSING ###
def transpose_C(chords, key):
    # if key is unknown to the user, they can use guess_key function
    # Transpose the given chords by the given index
    global flats, sharps  # getting the global variables I set
    notes = flats  # sometimes we want to prefer flats as default (i.e. Jazz
    # and popular music) and sometimes sharps (happens more in string music and
    # classical music). I will default with Flats since it is more appropriate
    # for most types of popular music.
    new_chords = []  # initializing where the new chords will be stords
    # setting transposeamount - by how much to transpose? we want to transpose
    # all to C natural currently.

    # find by how much to transpose to C
    if (key in flats):
        original_key_index = flats.index(key)
        c_index = flats.index('C')
    elif (key in sharps):
        original_key_index = sharps.index(key)
        c_index = sharps.index('C')
    else:
        print "Somehow it's a wrong key! please insert manually the key for the song with these chords:"
        print chords
        key = strip_chord_to_letter(raw_input("Insert Key: "))
        transpose_C(chords, key)
    index_change = (c_index - original_key_index) % len(flats)

    # translate:
    for chord in chords:
        # seperate letter and sign apart:
        if (chord.find("b") is True) or (chord.find("#") is True):
            chord_chunked = (chord[:2], chord[2:])  # chord letter will include the sign  # or b.
        else:
            chord_chunked = (chord[:1], chord[1:])  # otherwise, chord letter is only the letter.
        # transposing
        chordbase = chord_chunked[0]
        # we need to transpose only the chordbase.
        chordtype = chord_chunked[1]
        # whatever else is there that would be chordbase joined into the new
        # transposed chordbase.

        # change - get index before iterating every chord
        original_letter_index = None


        if (chordbase in flats):
            original_letter_index  = flats.index(chordbase)
        elif (chordbase in sharps):
            original_letter_index  = sharps.index(chordbase)
        # if chordbase not found in chordbase, this is not a proper chordbase
        if (original_letter_index  is None):
            #we probably need to convert the chord into a propper format.
            new_chords.append("".join(chord_chunked))  # just leave it as is.
        else:
            new_note = notes[(original_letter_index  + index_change) %
                             len(notes)]
            new_chord = "".join([new_note, chordtype])
            #making sure it is well written:
            if new_chord  in available_chords_dic: #if the new transposed note is malwritten,
                # change it to a well-written one:
                new_chord = available_chords_dic[new_chord]
            new_chords.append(new_chord)
    return new_chords


################## SIMILARITY COMPARISONS ################

######## LCS ######

#Similarity measure: LCS. However, if the similar chords are found in great distance,
# that doesn't really imply very high similarity. If the chords are found within 1 chord apart, that does imply some similarity.
#this is my own code from last assignment of comparing LCS DNA sequences.
def LCS(str1 , str2):
    # get strings length
    m = len(str1)
    n = len(str2)

    # building an empty "table" of size [n,m] for storing LCS values later
    table = [[None]*(n+1) for i in xrange(m+1)]

    #fill in table in bottom up fashion, using these methods:
    for i in range(m+1):
        #(using m+1 and n+1 because of 0-based indexing of range(m) stops 1 int BEFORE m)
        for j in range(n+1):
            #for the first row/column, fill the table in 0's
            if i == 0 or j == 0 :
                table[i][j] = 0

            #Now find common symbols:
            # if the symbols from both strings are equal, increment counter:
            # take the counter saved in the diagonal (upper left) cell in the table
            # and increment that counter by 1, and store that in the current cell
            elif str1[i-1] == str2[j-1]:
                table[i][j] = table[i-1][j-1]+1

            #if it is not equal, fill the current cell
            # by taking the maximum value of either the cell on top or on the left
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    max_lcs = table[m][n] #Max LCS
    avg_table_last_row = sum(table[-1])/len(table[-1]) #I wanted a measure that would reflect more of the LCSs even if they're not the longest, but still proportional to the size. This may not be the best absolute way to measure it, but I saw the last column had the greatest variability since we usually would take from the left item, so that accounts more for the process in general than just teh MAX LCS.
    # return the final value stored in the last cell (table[m][n]), which is the LCS of the strings
    return max_lcs, avg_table_last_row

#Comparison of strings. Input = list of lists.
def compare_LCS(a,b):
    maxLCScommon,avgLCScommon = LCS(a,b)
    maxLCSproportion = float(maxLCScommon)/((len(a)+len(b))/2) #calculating proportion of LCS to the entire length
    #I also want a more general measure perhaps capturing informaiton aobut more than one common subsequence
    avgLCSproportion = float(avgLCScommon)/((len(a)+len(b))/2)
    return maxLCSproportion,avgLCSproportion




##### REDUCING CHORDS LIST TO UNIQUE PROGRESSIONS ####
#to spare redundant iterations and checks through every chord in the list, we can utilize the fact that the chord progressions are comprised of mostly repeating patterns.
#I will use every unique set of 4 chords (since this is where a chord set is turning into a fuller "progression" - 3 or less is too common and not distinctive.
#I will make a set of all unique 4 chords progressions.
def uniqifyChords(chords,k):
    uniq_chords = []
    #i would ideally optimize the comparison by using something akin to Huffman coding tree structure;
    # or actually, since there are only about ~10 optional characters,
    # it could be better to create a tree with 10 children at every level (but only 4 levels)
    #so that the code first checks for the first letter comparison, then if it exists, goes down that node to compare for the 2nd letter, etc.
    #for now, I used simple lists and iteration as a prototype:....
    for i in range(0,len(chords)-(k-1)):    #iterating start_index from 0 to the last k chords, end_index from k to the end
            chordprog = "".join(chords[i:i+k])
            if chordprog not in uniq_chords:
                uniq_chords.append(chordprog)
    #I will use sorting to make the process slightly more efficient by sortig it for later applying binary search on it
    uniq_chords.sort()
    return uniq_chords


#DEBUG: BINARY SEARCH DIDN'T WORK FROM SOME UNKNOWN REASON
#define a binary search function:
#this is taken (slightly adapted) from here: http://stackoverflow.com/questions/9501337/binary-search-algorithm-in-python
def binarysearch_Bool(sequence, value):
    lo, hi = 0, len(sequence) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sequence[mid] < value:
            lo = mid + 1
        elif value < sequence[mid]:
            hi = mid - 1
        else:
            return True
    return False


def compare_progsk(chords1,chords2):
    #comparing length of lists to know which one would be more efficient to iterate on the other:
    if len(chords1) > len(chords2):
        chords_short,chords_long = chords1,chords2
    else:
        chords_short,chords_long = chords2,chords1

    equalprogs = 0  #counter
    # (using the shorter one for iteration:)
    for prog1 in chords_short:
        #performing binary search on the other list to see if the current progression is there:
        if binarysearch_Bool(chords_long,prog1) == True:
            equalprogs += 1
    #set proportion:
    #using the longer list length to define the proportion.
    propotion_equalprogs = float(equalprogs)/len(chords_long)
    return propotion_equalprogs


##### SequenceMatcher ####
from difflib import SequenceMatcher
#Using SequenceMatcher for the entire chord progression:
#From https://docs.python.org/2.7/library/difflib.html#sequencematcher-objects
#will use SequenceMatcherScore in final function.

########## COMPARING MULTIPLE SONGS #######


#comparison of multiple similarity checks and give a similarity score:
def compare_2_songs(song1,song2):
    #parsing song
    titlesections1, chords1, lyrics1,title1 = parseSong(song1)
    titlesections2, chords2, lyrics2,title2 = parseSong(song2)
    #print "Checking Similariy between: ", title1, title2

    #tranposing for standartization
    standartized_chords1 = transpose_C(chords1,guess_key(chords1))
    standartized_chords2 = transpose_C(chords2,guess_key(chords2))
    #print "     Chords of: ", title1, standartized_chords1
    #print "     Chords of: ", title2, standartized_chords2
    #computing LCS: max and avg.
    maxLCSproportion,avgLCSproportion = compare_LCS(standartized_chords1,standartized_chords2)

    #comparing exact sequence of 3 chords matches:
    uniq1_k3 = uniqifyChords(standartized_chords1,3)
    uniq2_k3 = uniqifyChords(standartized_chords2,3)
    exact_progs3Score =  compare_progsk(uniq1_k3,uniq2_k3)  #this will get a high weight

    #comparing exact sequence of 4 chords matches:
    uniq1_k4 = uniqifyChords(standartized_chords1,4)
    uniq2_k4 = uniqifyChords(standartized_chords2,4)
    exact_progs4Score =  compare_progsk(uniq1_k4,uniq2_k4) #this will get a VERY high weight, since this is a very strong indicator, if it finds such at all.

    #the AMOUNTS of unique 3 chord progressions in the song shows how much each song is repetative or not.
    #we'll add a score for how similar is the repetativeness by comparing how many unique progressions are found:
    repetativenessScore = len(uniq1_k3)/len(uniq2_k3)

    chordsSequenceMatcherScore = SequenceMatcher(False,standartized_chords1,standartized_chords2).ratio()
    #I found SequenceMatcher for UNIQUE progressions to not be very indicative, so I'm leaving it out.

    #these aren't the best measures of similarity, but this is just a prototpye to show that a more context appropriate measure would come here:
    structureSimilarityScore = SequenceMatcher(False,titlesections1,titlesections2).ratio()
    lyricsSimilarityScore = SequenceMatcher(False,lyrics1,lyrics2).ratio()

    totalScore = maxLCSproportion + avgLCSproportion + 5*exact_progs3Score + 10*exact_progs4Score + 3*chordsSequenceMatcherScore + repetativenessScore + 3*structureSimilarityScore +lyricsSimilarityScore
    return totalScore, title1, title2

#compare all unique pairs from a list
from time import time
def compare_all_pairs(lst):
    start_time = time()
    comparisons = [] #list to store results
    #comparing each UNIQUE pair
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)): #( using (i+1) to compare with items uniterated before)
            score_pair,title1,title2 = compare_2_songs(lst[i],lst[j])
            comparisons.append([score_pair,(title1,title2)])
            #print "Similarity Score of %s and %s is :" % (title1,title2), score_pair
            #print "______________________________________"
    comparisons.sort(reverse=True) #I would use quicksort of course as an improvement
    for line in comparisons:
        print line
    runningtime = time() - start_time
    print "Running Time: ", runningtime
    return comparisons

#get a list of all txt files (containing songs from chords websites)
import glob
def extract_songs_from_folder():

    folderpath = str(raw_input("insert full path of where you put the txt files of chords: "))

    if folderpath[-1] != "/":
        folderpath += "/"
    if folderpath[0] != "/":
        folderpath =  "/" + folderpath

    try:
        songslist = glob.glob(str(folderpath)+"*.txt")
    except: #catching all exceptions:
        print "Couldn't extract txt files from that path. " \
              "Are you sure you inserted the path of right folder (with txt song files) correctly?"
        print "Please input the directory in this format:"
        print "/Users/tomereldor/PycharmProjects/CS110/CS110/CS110Final/SONGSTXTS/"
        return extract_songs_from_folder()
    return songslist



###Here I would make this comparison list into a weighted graph like a minimum spanning tree, showing the similariyt between the nodes.
# I tried to for a long time but I've yet to make it work.


############### USAGE #############

# if you prefer to code in your folder as a variable, change this:
testfolderpath = "/Users/tomereldor/PycharmProjects/CS110/CS110Final/SONGSTXTS/"
testfiles = glob.glob(str(testfolderpath)+"*.txt")
print compare_all_pairs(testfiles)

#otherwise:
#compare_all_pairs(extract_songs_from_folder())
