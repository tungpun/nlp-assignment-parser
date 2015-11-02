## Introduction
This is our assignment for NLP's course

Supported parsers:
* Lexiclized Parser
* Shift-Reduce Parser
* Neural Network Parser
* Vietnamese PCFG

## How to use
* Clone this repository
* Github does not allow pushing big file to its service, so you should manually download some files: [stanford-srparser-2014-10-23-models.jar](http://nlp.stanford.edu/software/stanford-srparser-2014-10-23-models.jar), [stanford-corenlp-2015-04-20-models.jar](http://nlp.stanford.edu/software/stanford-corenlp-2015-04-20-models.jar)
* Install `Java 1.8+`
* Run `python doit.py` (python2.7)

## Sample output

```
~ python doit.py

[+] Input Data: "By default, output files are written to the current directory.

         .d8888b.                                      .d8888b.                      .d8888b.         d8888
        d88P  Y88b                                    d88P  Y88b                    d88P  Y88b       d88888
        888    888                                         .d88P                    888    888      d88P888
        888        888d888  .d88b.  888  888 88888b.      8888"                     888            d88P 888
        888  88888 888P"   d88""88b 888  888 888 "88b      "Y8b.                    888           d88P  888
        888    888 888     888  888 888  888 888  888 888    888       888888       888    888   d88P   888
        Y88b  d88P 888     Y88..88P Y88b 888 888 d88P Y88b  d88P                    Y88b  d88P  d8888888888
         "Y8888P88 888      "Y88P"   "Y88888 88888P"   "Y8888P"                      "Y8888P"  d88P     888
                                             888
                                             888
                                             888

    Select from the menu:
        [1] Lexiclized Parser
        [2] Shift Reduce Parser
        [3] Neural Network Parser
        [4] Vietnamese PCFG
        [0] Quit Parser Wrapper

    Parser Wrapper> 2
[+] Implementing Shift Reduce Parser (included Dependency and Context-Free-Grammar representation)...

['java', '-cp', '"*"', '-Xmx2000m', 'edu.stanford.nlp.pipeline.StanfordCoreNLP', '-annotators', 'tokenize,ssplit,pos,parse', '-parse.model', 'edu/stanford/nlp/models/srparser/englishSR.ser.gz', '-file', 'input.txt']
Adding annotator tokenize
TokenizerAnnotator: No tokenizer type provided. Defaulting to PTBTokenizer.
Adding annotator ssplit
Adding annotator pos
Reading POS tagger model from edu/stanford/nlp/models/pos-tagger/english-left3words/english-left3words-distsim.tagger ... done [2.6 sec].
Adding annotator parse
Loading parser from serialized file edu/stanford/nlp/models/srparser/englishSR.ser.gz ... done [52.3 sec].

Ready to process: 1 files, skipped 0, total 1
Processing file /root/nlp/parser/stanford-corenlp/input.txt ... writing to /root/nlp/parser/stanford-corenlp/input.txt.xml {
  Annotating file /root/nlp/parser/stanford-corenlp/input.txt [50.447 seconds]
} [51.557 seconds]
Processed 1 documents
Skipped 0 documents, error annotating 0 documents
Annotation pipeline timing information:
TokenizerAnnotator: 0.1 sec.
WordsToSentencesAnnotator: 0.0 sec.
POSTaggerAnnotator: 0.5 sec.
ParserAnnotator: 49.8 sec.
TOTAL: 50.4 sec. for 804 tokens at 15.9 tokens/sec.
Pipeline setup: 0.2 sec.
Total time for StanfordCoreNLP pipeline: 51.8 sec.
[+] Parsing completed

[+] Output report is saved to input.txt.xml . You can open with MS Excel for more detail or view a brief as below.

[+] Parse tree:
   [0] (ROOT (S (PP (IN By) (NP (NN default))) (, ,) (NP (NN output) (NNS files)) (VP (VBP are) (VP (VBN written) (PP (TO to) (NP (DT the) (JJ current) (NN directory))))) (. .)))
(ROOT(S(PP(IN By)(NP(NN default)))(, ,)(NP(NN output)(NNS files))(VP(VBP are)(VP(VBN written)(PP(TO to)(NP(DT the)(JJ current)(NN directory)))))(. .)))

|-- ROOT
|   |-- S
|   |   |-- PP
|   |   |   |-- IN --- By
|   |   |   |-- NP
|   |   |   |   |-- NN --- default
|   |   |-- , --- ,
|   |   |-- NP
|   |   |   |-- NN --- output
|   |   |   |-- NNS --- files
|   |   |-- VP
|   |   |   |-- VBP --- are
|   |   |   |-- VP
|   |   |   |   |-- VBN --- written
|   |   |   |   |-- PP
|   |   |   |   |   |-- TO --- to
|   |   |   |   |   |-- NP
|   |   |   |   |   |   |-- DT --- the
|   |   |   |   |   |   |-- JJ --- current
|   |   |   |   |   |   |-- NN --- directory
|   |   |-- . --- .

```


XML Report Output
![Output](http://i.imgur.com/6blLub9.jpg)

> Find me on [Twitter](https://twitter.com/tungpun_)
