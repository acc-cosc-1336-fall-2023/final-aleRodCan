#write functions here, don't add input('') statements here!
def get_most_likely_ancestor_census(dna_string1, dna_string2):
    """
    Find all starting positions (1-based) where dna_string2 occurs as a substring in dna_string1.
    
    Parameters:
    dna_string1 (str): The main DNA sequence.
    dna_string2 (str): The substring to find in the main sequence.
    
    Returns:
    list: A list of 1-based starting positions where dna_string2 occurs in dna_string1
    """
    position = []
    len_dna2 = len(dna_string2)

    for i in range(len(dna_string1) -  len_dna2 + 1):
        if dna_string1[i:i + len_dna2] == dna_string2:
            position .append(i+1)
    
    return positions