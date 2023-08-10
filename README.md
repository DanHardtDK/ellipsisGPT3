# ellipsisGPT3
Code and data for the paper 
<a href=https://aclanthology.org/2023.acl-short.4.pdf>Ellipsis Dependent Reasoning: A New Challenge for Large Language Models</a>, by Daniel Hardt, ACL 2023.


**Note**: to run the above, you need to fill in an OpenAI API key in `config.cfg`.

### Get started
Create a virtual environment and install `openai` and `pandas` (see `requirements.txt`)

## Models
The paper reports results on the following GPT3 models:
<ul>
  <li>text-davinci-003</li>
  <li>text-davinci-002</li>
  <li>text-ada-001</li>
  <li>text-curie-001</li>
  <li>text-babbage-001</li>
  </ul>
  
<<<<<<< HEAD
## Run with PERL
The following command produces results for the davinci-003 model:
```bash
runModelBatch.pl text-davinci-003 100 logfile.out 5
```

This specifies 100 Yes and 100 No examples, with complete output logged to logfile.out, and there are 5 iterations (with each iteration result logged under /run), for a total of 1000 examples.

## Run with Python
The following command produces the same results as the PERL operation:
```bash
python code/ellipsisBatch.py data/examples1 text-davinci-003 100 5
```
Note that the python method does not output the logs (as in logfile.out)


## Parameters
To see the possible parameters of the Python code, run
```bash
poetry run python code/ellipsisBatch.py --help
```
Which will produce the following (or a slightly modified versions of it)

```
usage: ellipsisBatch.py [-h]
                    exampleFileList
                    {text-davinci-003,text-davinci-002,text-ada-001,text-curie-001,text-babbage-001}
                    {1,10,50,100,500}
                    {1,2,3,5,10,50}

positional arguments:
  exampleFileList                          Path to file containing list of ellipsis patterns example files
  {text-davinci-003,...,text-babbage-001}  GPT model to test
  {1,10,50,100,500}                        number of examples to test
  {1,2,3,5,10,50}                          number of iterations

optional arguments:
  -h, --help            show this help message and exit
```


### Results
To obtain summary statistics, run 
```
python code/avgBatch.py --file runs/<RUN_ID>
```

E.g., for a run started with the cmd `python code/ellipsisBatch.py data/examples1 text-davinci-002 10 3`, we can find the resulting run under `/runs`. 
Then, running the command above, produces an output akin to

```
ITERATIONS:  3
TOTAL EXAMPLES:  150
TOTAL VPE CORRECT:  124
TOTAL NO VPE CORRECT:  146
TOTAL VPE ACCURACY:  0.83
TOTAL NO VPE ACCURACY:  0.97
TOTAL ACCURACY:  0.9
                     File  VPE Correct  NO VPE Correct  Total
0            1SentAfterYN         7.33            9.67     10
1  1SentSubordBackwardsYN         6.00           10.00     10
2           1SentSubordYN         8.00            9.00     10
3                 1SentYN        10.00           10.00     10
4                 2SentYN        10.00           10.00     10

```

**Note**: Using `avgBatch` requires pandas

=======
  The following command produces results for the davinci-003 model as they were reported in the paper:
  
  <b>runModelBatch.pl text-davinci-003 100 logfile.out 5</b>
  
  This specifies 100 Yes and 100 No examples, with output logged to logfile.out, and there are 5 iterations, for a total of 1000 examples.
>>>>>>> origin/main



