from Bio import SeqIO
fasta_file_size = 0
start_time = time.time()

for record in SeqIO.parse(fasta_file_name, 'fasta'):
  header = record.id
  meta = record.description
  sequence = record.seq
  print(header, meta, len(sequence))
  fasta_file_size += len(sequence) 
print("Total number of nucleotides:", fasta_file_size)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Code 1 executed in: {elapsed_time:.5f} seconds")
#Total number of nucleotides: 9895291908
#Code executed in: 24.29457 seconds


start_time = time.time()
def calculate_genome_size(fasta_file):
    total_length = 0
    for record in SeqIO.parse(fasta_file, 'fasta'):
        total_length += len(record.seq)
    return total_length

genome_size = calculate_genome_size(fasta_file_name)
print(f"The size of the human genome is: {genome_size} base pairs")
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Code 2 executed in: {elapsed_time:.5f} seconds")
#The size of the human genome is: 3298430636 base pairs
#Code 2 executed in: 19.15660 seconds


start_time = time.time()
!grep -v '^>' ./ncbi_dataset/data/GCF_000001405.40/GCF_000001405.40_GRCh38.p14_genomic.fna | tr -d '\n' | wc -c
end_time = time.time()
elapsed_time = end_time - start_time
print(f"with grep code executed in: {elapsed_time:.5f} seconds")
#3298430636
#with grep code executed in: 15.67284 seconds


start_time = time.time()
!awk '!/^>/ { total += length } END { print total }' ./ncbi_dataset/data/GCF_000001405.40/GCF_000001405.40_GRCh38.p14_genomic.fna
end_time = time.time()
elapsed_time = end_time - start_time
print(f"with awk code executed in: {elapsed_time:.5f} seconds")
#3.29843e+09
#with awk code executed in: 2.81582 seconds
