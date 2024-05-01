from Bio import SeqIO


def find_max_length_diff_scaffolds(fasta_file: str) -> tuple:
    scaffolds = list(SeqIO.parse(fasta_file, "fasta"))

    max_length_diff = 0
    max_length_diff_scaffolds = None

    for i in range(len(scaffolds) - 1):
        curr_length_diff = abs(len(scaffolds[i]) - len(scaffolds[i + 1]))
        if curr_length_diff > max_length_diff:
            max_length_diff = curr_length_diff
            max_length_diff_scaffolds = (scaffolds[i], scaffolds[i + 1])

    return max_length_diff_scaffolds, max_length_diff


fasta_file = str(input("Enter the name file(in fasta format): "))
print('-' * 50)

try:
    max_length_difference_scaffolds, max_length_difference = find_max_length_diff_scaffolds(fasta_file)

    if max_length_difference_scaffolds:
        print("Scaffolds for which the discrepancy in lengths is the largest:")
        print('-' * 50)
        print(f"{max_length_difference_scaffolds[0].id} : {len(max_length_difference_scaffolds[0])}")
        print(f"{max_length_difference_scaffolds[1].id} : {len(max_length_difference_scaffolds[1])}")
        print('-' * 50)
        print(f"The difference in length: {max_length_difference}")
    else:
        print("The file does not contain scaffolds")
except FileNotFoundError:
    print("File not found")
