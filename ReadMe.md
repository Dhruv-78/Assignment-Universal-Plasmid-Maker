# Universal Plasmid Maker

## Project Structure


```
Assignment-Universal-Plasmid-Maker/
├── Codes/ # Python scripts
│ └── main.py  # Main Project File
| └── ori_finder.py # File with functions to finding ori
| └── site_and_markers.py # File with functions to add restriction sites and markers to plasmid
├── Input/ # Input sequence files or parameters
└── Output/ # Generated outputs

```

## Usage
<p>
Follow these steps to run the project:

1. Place input files in the Input/ directory .
2. Run the main script from the root directory:
```bash
    python Codes/main.py Input/fastafile.fa Input/designfile.txt
```
3. View results in the Output/ directory after execution.
</p>

### Solution Explanation

The solution follows a sequential and modular pipeline for plasmid construction:

1. The input DNA sequence is first analyzed to identify a valid **origin of replication (ori)**. This step ensures that the constructed plasmid can replicate autonomously in the host system.

2. Once the ori is identified, a **spacer sequence** is inserted downstream of the ori. The spacer provides separation between functional elements, helping maintain structural and functional integrity of the plasmid.

3. Next, **restriction sites and selection markers** are added based on the specifications provided in the **design file**. This allows the plasmid to be customized according to user-defined cloning and selection requirements.

4. After inserting each restriction site and marker, a **small terminal marker** is appended to indicate the end of the designed cassette and to assist in downstream validation or processing.

5. Finally, the fully constructed plasmid sequence is written to the `Output/` directory in **FASTA format**.