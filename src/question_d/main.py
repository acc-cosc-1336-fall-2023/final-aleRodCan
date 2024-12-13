#add import
from question_d import get_most_likely_ancestor_consensus

def main():

    dna_string1 = input("Enter the first DNA string (length <+ 1kb): ").strip()
    dna_string2 = input("Enter the second DNA string (substring, length <=16): ").strip()

    if len(dna_string1) > 1000 or len(dna_string2) > 16:
        print("Error: DNA string exceed the maximum allowed length.")
        return
    
    positions = get_most_likely_ancestor_consensus(dna_string1, dna_string2)

    if positions:
        print("Positions where dna_string2 occurs in dna_string1 (1-based index):")
        print(" ".join(map(str, positions)))
    else:
        print("No occurrence found.")

if __name__ == "__main__":
    main()