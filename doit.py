#!/usr/bin python 2.7

import os
import xmltodict
import json

DEBUG = True
JAVABUFFER = '-Xmx2000m'
INPUTFILE = 'input.txt'


def check_requirement():
    """
    #TODO
    """
    return 0


def print_input():
    try:
        with open('input.txt', 'r') as f:
            data = f.read()
            print '[+] Input Data: \"' + data.strip() + '\"\n'        
        with open('input.txt.xml', 'w') as f:
            f.write("")
            print '[+] Outfile cleaned:', INPUTFILE + '.xml\n'        
    except:
        raise Exception("IO Error! Check input file!")


def run(cmd):
    try:
        print cmd.split(' ')
        os.popen(cmd)
    except:
        raise Exception("Error when try running ", cmd)


def lex_parser():
    """Get input from INPUTFILE
    """
    try:
        print "[+] Implementing Lexiclized Parser (included Dependency and Context-Free-Grammar representation)...\n"
        cmd = 'java -cp "*" ' + JAVABUFFER + ' edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,parse -file ' + INPUTFILE    
        run(cmd)  
        print "[+] Parsing completed\n"
    except:
        raise Exception('Failed. Quit now!!!')
    return 0


def shift_reduce():
    """Get input from INPUTFILE
    """
    try:
        print "[+] Implementing Shift Reduce Parser (included Dependency and Context-Free-Grammar representation)...\n"
        model = 'edu/stanford/nlp/models/srparser/englishSR.ser.gz'
        cmd = 'java -cp "*" ' + JAVABUFFER + ' edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,parse -parse.model ' + model + ' -file ' + INPUTFILE            
        run(cmd)  
        print "[+] Parsing completed\n"
    except:
        raise Exception('Failed. Quit now!!!')
    return 0


def neural_network_parser():
    """Get input from INPUTFILE
    """
    try:
        print "[+] Implementing Neural Network Parser (included Dependency representation)...\n"
        model = 'edu/stanford/nlp/models/parser/nndep/english_UD.gz'
        cmd = 'java -cp "*" ' + JAVABUFFER + ' edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,depparse -parse.model ' + model + ' -file ' + INPUTFILE            
        run(cmd)  
        print "[+] Parsing completed\n"
    except:
        raise Exception('Failed. Quit now!!!')
    return 0


def get_parse_tree(data):
    """for parsing xml content to console
    now, we just return parse tree
    """    
    parsetrees = []
    s_id = 0

    datadict = xmltodict.parse(data)            

    try:
        for sentence in datadict['root']['document']['sentences']['sentence']:                    
            s_id += 1
            parsetrees.append(sentence['parse'])
            # return json.dumps(datadict, indent=2)
    except:
        parsetrees.append(datadict['root']['document']['sentences']['sentence']['parse'])      # when input just contains oneline
        pass

    return parsetrees 


def gen_graph(line):
    """Make parse tree look more beauty
    """

    def gentab(tabsize):
        return '|   '  * (tabsize - 1) +  '\-- '

    line = line.replace(') ', ')')
    tabsize = 0
    graph = ''
    line += '~'
    for i in range(len(line) - 1):
        c = line[i]
        if c == '(':
            tabsize += 1
            graph += '\n'            
            graph += '|   '  * (tabsize - 1) +  '\-- '
            graph += c
        elif c == ')':
            tabsize -= 1
            graph += ')'
            if line[i+1] != '(':
                graph += '\n'
                graph += '|   '  * (tabsize - 1) +  '|   '
        else:
            graph += c   
    return graph


def read_output(cmd):
    """Read output report from INPUTFILE.xml
    """  
    OUTPUTFILE = INPUTFILE + '.xml'    
    try:
        with open(OUTPUTFILE, 'r') as f:
            data = f.read()        
            if data == "":
                raise Exception("Outfile is empty ! Check log and report to developer!!!")        
            print '[+] Output report is saved to', OUTPUTFILE, '. You can open with MS Excel for more detail or view a brief as below.'
            if cmd == "nn":
                return 0
            print "\n[+] Parse tree:"
            parsetrees = get_parse_tree(data)
            cnt = 0
            for parsetree in parsetrees:            
                print '   [' + str(cnt) + ']', parsetree, gen_graph(parsetree), '\n'
                cnt += 1
    except:
        raise Exception("Something wrongs ! Check log and report to developer!!!")
    return 0


if __name__ == '__main__':    
    check_requirement()
    if DEBUG:
        print_input()
    cmd = raw_input('Choose parser [lex/sr/nn]: ').strip()
    if cmd == 'sr':
        shift_reduce()
        read_output(cmd)
    elif cmd == 'lex':
        lex_parser()
        read_output(cmd)
    elif cmd == 'nn':
        neural_network_parser()
        read_output(cmd)        
    else:
        print "Try again! Choose correct parser, please!"    

