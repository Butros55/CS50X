import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    dfile = sys.argv[1]
    with open(dfile) as file:
        reader = csv.DictReader(file)
        database = list(reader)

    sfile = sys.argv[2]
    with open(sfile) as file:
        sequence = file.read()

    STR = list(database[0].keys())[1:]
    STR_counts = {}

    for i in range(len(database[0]) - 1):
        STR_counts[STR[i]] = (longest_match(sequence, STR[i]))

    for i in range(len(database)):
        for j in range(len(STR_counts)):
            intd = int(database[i][STR[j]])
            if STR_counts[STR[j]] == intd:
                if j == len(STR_counts) - 1:
                    res = database[i]["name"]
                    print(f"{res}")
                    quit(0)
            elif STR_counts[STR[j]] != intd:
                break
    else:
        print("no match")

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
