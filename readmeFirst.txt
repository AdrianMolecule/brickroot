A domestication/optimization software that takes a DNA in Fasta format and produces a new DNA sequence where prohibited DNA bases (prohibited enzyme cut motifs)  are replaced.  This cause only silent mutations. The list of offending enzyme cut sites is manually maintained in a text file and can be updated with a regular text editor.
The software automatically reloads the last Fasta file that was previously used or a small default sample. The domesticated sequences are automatically saved when the user presses OK in the domestication window.
This software should be run on any sequence that needs to conform to the Biobrick stadard(s). As there are several version of BioBrick standards with different prohibited enzymes the prohibited enzyme list is editable. Normally it should contain at least Bsa1.
Optimization supports removing hairpins and changing GC content.
At this point it supports e-coli and I will add new organism support if asked as it's pretty trivial. 
Start with start :)