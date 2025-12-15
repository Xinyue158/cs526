In this assignment, I implemented the Huffman encoding and decoding algorithm in Python. The program reads an input text file, builds a frequency map of characters, constructs a Huffman tree, and compresses the input text into a binary representation. The compressed result is written to a file. The program also supports decoding, which reconstructs the original text from the compressed file and writes the reconstructed output to a new file.
To run the encoding (compression) part, open a terminal in the folder containing the files and run:
py hw7_huffman.py encode input.txt compressed.txt
The program prints the input set information, the frequency map, the Huffman tree (shown as character codes), and a compression report. It also creates the compressed file.
To run the decoding (reconstruction) part, run:
py hw7_huffman.py decode compressed.txt reconstructed.txt
The program reads the compressed file, rebuilds the Huffman tree, decodes the binary data, and writes the reconstructed text to reconstructed.txt.
To verify correctness, I compared the original input file and the reconstructed file using the Windows file comparison command:
cmd /c fc input.txt reconstructed.txt
On my computer, the system language is Chinese, so the output message appears in Chinese. The message “FC: 找不到差异” means that no differences were found between the two files, which confirms that the reconstruction is correct.
