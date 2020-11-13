#This variable is used in the code ahead. I'm puting it up here just in case.
nucleotide = ["A", "T", "C", "G"] 

#This function is for returning the dna sequence length.
def get_length(dna):
    return len(dna)

#This function serves to see if dna1 is larger than dna2 (it must return false even if they have equal length)
def is_longer(dna1, dna2):
    if len(dna1) > len(dna2):
        return True
    else:
        return False

#This functions is for seeing how many times a nucleotide appears in a dna sequence.
def count_nucleotides(dna, nucleotide): 
    count = 0
    for char in dna:
        if char in nucleotide:
            count = count + 1
    return count

#This is for seeing if the dna sequence 2 appears in the dna sequence 1.
def contains_sequence(dna1, dna2):
    if dna2 in dna1:
        return True
    elif dna2 not in dna1:
        return False

#This is for seeing if the dna sequence is valid (it contains just the defined nucleotides (if they are in lowercase it also returns False)).
def is_valid_sequence(dna):
    for char in dna:
        valid_sequence = True
        if char in "ATCG":
            valid_sequence == True
        else:
            valid_sequence == False
            return False
    if valid_sequence == True:
        return True
    elif valid_sequence == False:
        return False

#insert_sequence("CCGG", "AT", 2) must be equal to "CCATGG"
#insert_sequence("CCGG", "AT", 0) must be equal to "ATCCGG"
#insert_sequence("CCGG", "AT", -1) must be equal to "CCGGAT", etc.
def insert_sequence(dna1, dna2, index):
	return dna1[:index] + dna2 + dna1[index:]

#This function serves to see which is the complementary of each nucleotide.
#So: A -> T; C -> G and viceversa.
def get_complement(nucleotide):
    if nucleotide == "A":
        complement = "T"
    elif nucleotide == "T":
        complement = "A"
    elif nucleotide == "G":
        complement = "C"
    elif nucleotide == "C":
        complement = "G"
    return complement

# This function serves to see which is the complementary sequence of a dna sequence.
def get_complementary_sequence(dna_sequence):
    comp_seq = ""
    for nucleotide in dna_sequence:
        comp_seq = comp_seq + get_complement(nucleotide)
    return comp_seq
