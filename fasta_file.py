def read_fasta_file(fasta_file_name):
  ''' Read fasta file and return header2sequence and header2meta dictionaries.
  '''
header2sequence = {}
header2meta = {}
sequence_lines = []
header = None

with open(fasta_file_name) as fh:
  for line in fh:
    line = line.strip()
    if line.startswith(">"): 
     if header:
      print(f"We are going to add header {header} and {len(''.join(sequence_lines))} ")
      header2sequence[header] = ''.join(sequence_lines)
      header, sequence_lines = None, [] 
     header, *meta_info = line[1:].split()
     meta_info = ' '.join(meta_info)
     header2meta[header] = meta_info
     print(header,'|', meta_info)
     sequence_lines = []
    else:
      line = line.strip()
      sequence_lines.append(line)

if header:
  print(f"we are going to add header {header} and {len(''.join(sequence_lines))}")
  header2sequence[header] = ''.join(sequence_lines)
  header, sequence_lines = None, [] 


def inter_fasta_file(fasta_file_name):
''' Iter over fasta file and yield header, meta information from header and sequence
''' 

  sequence_lines = []
  header = None
  meta = None
  with open(fasta_file_name) as fh:
    for line in fh:
      line = line.strip()
      if line.startswith(">"):
       if header:
        yield header, meta, ''.join(sequence_lines)
        header2sequence[header] = ''.join(sequence_lines)
        header, sequence_lines = None, []
       header, *meta_info = line[1:].split()
       meta = ' '.join(meta_info)
       sequence_lines = []
      else:
        line = line.strip()
        sequence_lines.append(line)

  if header:
   yield header, meta, ''.join(sequence_lines)
