#!/usr/bin python 2.7

import os
import xmltodict
import json

DEBUG = True
JAVABUFFER = '-Xmx1500m'
INPUTFILE = 'input.txt'

def check_requirement():
    """
    #TODO
    """
    return 0

def print_input():
    with open('input.txt', 'r') as f:
        data = f.read()
        print '[+] Input Data: \"' + data + '\"\n'        

def run(cmd):
    print cmd.split(' ')
    os.popen(cmd)

def lex_parser():
    """
    Get input from INPUTFILE
    """
    try:
        print "[+] Implementing Lexiclized Parser...\n"
        cmd = 'java -cp "*" ' + JAVABUFFER + ' edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,parse -file ' + INPUTFILE    
        run(cmd)  
        print "[+] Parsing completed\n"
    except:
        raise Exception('Failed. Quit now!!!')
    return 0

def shift_reduce():
    """
    Get input from INPUTFILE
    """
    try:
        print "[+] Implementing Shift Reduce Parser...\n"
        model = 'edu/stanford/nlp/models/srparser/englishSR.ser.gz'
        cmd = 'java -cp "*" ' + JAVABUFFER + ' edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,parse -parse.model ' + model + ' -file ' + INPUTFILE            
        run(cmd)  
        print "[+] Parsing completed\n"
    except:
        raise Exception('Failed. Quit now!!!')
    return 0

def neural_network_parser():
    """
    Get input from INPUTFILE
    """
    try:
        print "[+] Implementing Neural Network Parser...\n"
        model = 'edu/stanford/nlp/models/parser/nndep/english_UD.gz'
        cmd = 'java -cp "*" ' + JAVABUFFER + ' edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,parse -parse.model ' + model + ' -file ' + INPUTFILE    
        run(cmd)  
        print "[+] Parsing completed\n"
    except:
        raise Exception('Failed. Quit now!!!')
    return 0

def get_parse_tree(data):
    """
    for parsing xml content to console
    now, we just return parse tree
    """
    datadict = xmltodict.parse(data)
    parsetree = datadict['root']['document']['sentences']['sentence']['parse']
    # return json.dumps(datadict, indent=2)
    return parsetree

def read_output():
    """
    Read output report from INPUTFILE.xml
    """  
    OUTPUTFILE = INPUTFILE + '.xml'
    print '[+] Output report is saved to', OUTPUTFILE, '. You can open with MS Excel for more detail or view a brief as below.'
    with open(OUTPUTFILE, 'r') as f:
        data = f.read()
        #print "[+] OUTPUT:", data
        print "[+] Parse tree:\n" + get_parse_tree(data)
    return 0

if __name__ == '__main__':    
    check_requirement()
    if DEBUG:
        print_input()
    cmd = raw_input('Choose parser [lex/sr/nn]: ').strip()
    if cmd == 'sr':
        shift_reduce()
        read_output()
    elif cmd == 'lex':
        lex_parser()
        read_output()
    elif cmd == 'nn':
        neural_network_parser()
        read_output()        
    else:
        print "Try again! Choose correct parser, please!"    

