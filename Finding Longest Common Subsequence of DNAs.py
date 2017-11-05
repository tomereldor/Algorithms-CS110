

#DNAs List
DNAs_numbered = [(0,'TCGCCAATATTATATTTTTGAAGGCGTAGCTAATGTGGATACTATGTAAGTCGCAAGCTCTGCCAAACAGGGCTAATGAACAAACACTATAATGAGGAC'),
(1,'TCGCAATATATCTTTTTGGAGAGCGTAGTATGTGGATATATCTCAAGTCGCAAGCTCTGCCGAAACAGGGCATGATTAAGGAATTACTACAATGAGGAAA'),
(2,'TGCAATATAACTTTTTAGGAGCATAGTAATGTCGGATATATTTTAAGTCGCAAGCGCCGAAACAGGGCACAATGAAGAAACACTATAAAGAGGAAC'),
(3,'TGCGCATATTTTTTTCTTAGTGTAGCGTAGTATGTGGAGATTCTCAAGTCGGAAGCTGCCTTAAACAGCGCATGATCAGGATTACTACAATAGAAGGAAA'),
(4,'TGCGCAATATATCTTTTTTAGAGAGCGTAGTATTGGTATATTCCCAAGTCGGAAGCTGCTTAAATCACCATGATACATGGAATTACTACAATAGAGGAAA'),
(5,'TCGCAATATATCTTTTTGAGAGCGTAGTAATGTGGATATATCTAAGTCGCAAGCTCTGCCGAAACAGGGCATAATGAAGAAACACTATAATGAGGAAC'),
(6,'TGCGCAATATATCTTTTTTAGGAGAGCGTAGTATGTGGATATTCTCAAGTCGGAAGCTGCCTTAAACAGCGCATGATAAGGAATTACTACAATAGAGGAAA')]

#DNAs List - (simply indexed)
DNAs = [('TCGCCAATATTATATTTTTGAAGGCGTAGCTAATGTGGATACTATGTAAGTCGCAAGCTCTGCCAAACAGGGCTAATGAACAAACACTATAATGAGGAC'),
('TCGCAATATATCTTTTTGGAGAGCGTAGTATGTGGATATATCTCAAGTCGCAAGCTCTGCCGAAACAGGGCATGATTAAGGAATTACTACAATGAGGAAA'),
('TGCAATATAACTTTTTAGGAGCATAGTAATGTCGGATATATTTTAAGTCGCAAGCGCCGAAACAGGGCACAATGAAGAAACACTATAAAGAGGAAC'),
('TGCGCATATTTTTTTCTTAGTGTAGCGTAGTATGTGGAGATTCTCAAGTCGGAAGCTGCCTTAAACAGCGCATGATCAGGATTACTACAATAGAAGGAAA'),
('TGCGCAATATATCTTTTTTAGAGAGCGTAGTATTGGTATATTCCCAAGTCGGAAGCTGCTTAAATCACCATGATACATGGAATTACTACAATAGAGGAAA'),
('TCGCAATATATCTTTTTGAGAGCGTAGTAATGTGGATATATCTAAGTCGCAAGCTCTGCCGAAACAGGGCATAATGAAGAAACACTATAATGAGGAAC'),
('TGCGCAATATATCTTTTTTAGGAGAGCGTAGTATGTGGATATTCTCAAGTCGGAAGCTGCCTTAAACAGCGCATGATAAGGAATTACTACAATAGAGGAAA')]



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
 
    # return the final value stored in the last cell (table[m][n]), which is the LCS of the strings
    return table[m][n]

print "Length of LCS is ", LCS(DNAs[3], DNAs[6])

#Comparison of strings:
def compare_pairs(lst):
    lcs_comparisons = [] #list to store results
    #comparing each UNIQUE pair
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)): #( using (i+1) to compare with items uniterated before)
            result = LCS(DNAs[i], DNAs[j])
            lcs_comparisons.append([result,(i,j)])
            print "LCS of DNA strings [%s : %s] :" % (i,j) , result

    #for building the tree, I want to know the MAX LCS pair.
    max_lcs = max(lcs_comparisons)
    print "Maximum Longest Common Subsequence found for strings:", max_lcs[1], "of length: ", max_lcs[0]
    return max_lcs

compare_pairs(DNAs)

