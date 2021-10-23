# Bioinformatics - Project 1

### Run program
After cloning the repository, run the following command at the root folder:
```
# Run program
$ python main/main.py <CONFIG-FILE-PATH> <SEQ-1-FILE-PATH> <SEQ-2-FILE-PATH>

# Example
$ python main/main.py ./conf/config.txt ./data/protein1.fasta ./data/protein2.fasta

--- Generated sequence alignments in out.txt! ---

```
### Run unit tests
Run the following command at the root folder:
```
$ pytest
```
Testing result
```
========================================= test session starts ==========================================
platform darwin -- Python 3.8.5, pytest-6.2.2, py-1.9.0, pluggy-0.13.1
rootdir: /Users/manhlinh0403/Documents/wut/sem3/Bioinformatics/git/project1
collected 8 items                                                                                      

tests/test_nw.py ....                                                                            [ 50%]
tests/test_utils.py ....                                                                         [100%]

========================================== 8 passed in 0.10s ===========================================
```