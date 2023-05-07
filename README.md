# ellipsisGPT3
Code and data for paper on ellipsis-dependent reasoning:
Ellipsis Dependent Reasoning: A New Challenge for Large Language Models, to appear at ACL 2023

To produce
The paper reported results on the following GPT3 models:
<ul>
  <li>text-davinci-003</li>
  <li>text-davinci-002</li>
  <li>text-ada-001</li>
  <li>text-curie-001</li>
  <li>text-babbage-001</li>
  </ul>
  
  The following command produces results for the davinci-003 model:
  
  <b>runModelBatch.pl text-davinci-003 100 logfile.out 5</b>
  
  This specifies 100 Yes and 100 No examples, with output logged to logfile.out, and there are 5 iterations, for a total of 1000 examples.

  Note: to run the above, you need to fill in an openai key, in the program ellipsisBatch.py
  
  
  
  


