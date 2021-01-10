# Exercise 1

### Setup

There are two files in this direction:
* *sample_ids.tsv*: A two-column, tab-separated text file where each row contains different identifiers for the same sample. One identifier is simply a number from 1-15 (Sample_id_1). The second identifier (Sample_id_2) indicates which treatment group the samples belong to (i.e., A, B, or C).

* *exercise1_table.tsv*: A three-column, tab-separated text file that contains the measured values for 2 different variables as well as the numbered sample sample id (i.e., 1-15).

### Goal

Your goal is to write a python script that prints the contents of *exercise1_table.tsv* with the numbered sample identifiers (i.e., Sample_id_1) replaced by the more informative sample identifiers (i.e., Sample_id_2).

For this exercise, use only the python standard library.

### Expected Output

```
Sample_Id_2	var1	var2
A1  19	95
A2	12	74
A3	15	6
A4	10	65
A5	19	98
B1	8	61
B2	20	56
B3	19	37
B4	0	2
B5	7	23
C1	3	79
C2	5	97
C3	14	72
C4	9	84
C5	16	46
```

