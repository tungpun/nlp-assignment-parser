## Introduction
This is our assignment for NLP's course
Supported parser: Lexiclized Parser, Shift-Reduce Parser, Neural Network Parser

## HOW TO USE
* Clone this repo
* Github does not allow pushing big file to its service, so you should download some files: [stanford-srparser-2014-10-23-models.jar](http://nlp.stanford.edu/software/stanford-srparser-2014-10-23-models.jar), [stanford-corenlp-2015-04-20-models.jar](http://nlp.stanford.edu/software/stanford-corenlp-2015-04-20-models.jar)
* Run `python doit.py` (python2.7)

## Sample output

```
~ python doit.py
[+] Input Data: "By default, output files are written to the current directory."

Choose parser [lex/sr]: sr
['java', '-cp', '"*"', '-Xmx1500m', 'edu.stanford.nlp.pipeline.StanfordCoreNLP', '-annotators', 'tokenizarse', '-parse.model', 'edu/stanford/nlp/models/srparser/englishSR.ser.gz', '-file', 'input.txt']
Adding annotator tokenize
TokenizerAnnotator: No tokenizer type provided. Defaulting to PTBTokenizer.
Adding annotator ssplit
Adding annotator pos
Reading POS tagger model from edu/stanford/nlp/models/pos-tagger/english-left3words/english-left3words-d... done [3.8 sec].
Adding annotator parse
Loading parser from serialized file edu/stanford/nlp/models/srparser/englishSR.ser.gz ... done [157.0 se

Ready to process: 1 files, skipped 0, total 1
Processing file /root/nlp/parser/stanford-corenlp-full-2015-04-20/input.txt ... writing to /root/nlp/parorenlp-full-2015-04-20/input.txt.xml {
  Annotating file /root/nlp/parser/stanford-corenlp-full-2015-04-20/input.txt [03:11.4 minutes]
} [03:11.274 minutes]
Processed 1 documents
Skipped 0 documents, error annotating 0 documents
Annotation pipeline timing information:
TokenizerAnnotator: 0.1 sec.
WordsToSentencesAnnotator: 0.0 sec.
POSTaggerAnnotator: 0.2 sec.
ParserAnnotator: 190.7 sec.
TOTAL: 191.0 sec. for 12 tokens at 0.1 tokens/sec.
Pipeline setup: 0.2 sec.
Total time for StanfordCoreNLP pipeline: 191.5 sec.
[+] Parsing completed

[+] Output report is saved to input.txt.xml . You can open with MS Excel for more detail or view a brief
[+] Parse tree: (ROOT (S (PP (IN By) (NP (NN default))) (, ,) (NP (NN output) (NNS files)) (VP (VBP are)ten) (PP (TO to) (NP (DT the) (JJ current) (NN directory))))) (. .))) </
```


XML Report Output
![Output](http://i.imgur.com/6blLub9.jpg)
