from Bio import SeqIO


def get_contig_length(file_name: str) -> None:
    try:
        with open(file_name, 'r') as handle:
            record_iterator = SeqIO.parse(handle, "fasta")
            last_contig = None
            for contig in record_iterator:
                last_contig = contig

        print(f"Length of the last contig: {len(last_contig)}") if last_contig \
            else print("The file contains no contigs")

    except FileNotFoundError:
        print("File not found")


file_name = "contigs.fasta"

get_contig_length(file_name)
