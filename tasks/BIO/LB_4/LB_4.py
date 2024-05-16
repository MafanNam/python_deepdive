from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

assembly_file = "contigs.fasta"
output_file = "longest_contigs.fasta"

longest_length = 0
longest_id = ""
longest_seq = None

for record in SeqIO.parse(assembly_file, "fasta"):
    scaffold_length = len(record.seq)
    if scaffold_length > longest_length:
        longest_length = scaffold_length
        longest_id = record.id
        longest_seq = record.seq

longest_record = SeqRecord(longest_seq, id=longest_id)

with open(output_file, "w") as output_handle:
    SeqIO.write([longest_record], output_handle, "fasta")

print("The longest scaffold is saved to a file:", output_file)
print("The length of the longest scaffold:", longest_length)
