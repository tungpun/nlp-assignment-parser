#!/usr/bin7 python 2.7
# -*- coding: utf-8 -*-

import os
import xmltodict
import json
import re
import random

DEBUG = True
JAVABUFFER = '-Xmx2000m'
INPUTFILE = 'input.txt'


def basic_color(code):    
    def inner(text, bold=True):
        c = code
        if bold:
            c = "1;%s" % c
        return "\033[%sm%s\033[0m" % (c, text)
    return inner


def term_color(code):    
    def inner(text):
        c = code
        return "\033[38;5;%sm%s\033[0m" % (c, text)
    return inner
    
    
black = basic_color('30')
red = basic_color('31')
green = basic_color('32')
yellow = basic_color('33')
blue = basic_color('34')
magenta = basic_color('35')
cyan = basic_color('36')
tred = term_color('31')


def check_requirement():
    """
    #TODO
    """
    return 0


def print_input():
    try:
        with open('input.txt', 'r') as f:
            data = f.read()
            print cyan('[+] Input Data: ') + data.strip()[:200] + '...\n'        
        with open('input.txt.xml', 'w') as f:
            f.write("")
            print cyan('[+] Outfile cleaned:'), INPUTFILE + '.xml\n'        
    except Exception, e:
        if DEBUG:
            print e 
        raise Exception("IO Error! Check input file!")


def run(cmd):
    try:
        #print cmd.split(' ')
        os.popen(cmd)
    except Exception, e:
        if DEBUG:
            print e 
        raise Exception("Error when try running ", cmd)


def lex_parser():
    """Get input from INPUTFILE
    """
    try:
        print cyan("[+] Implementing Lexiclized Parser (included Dependency and Context-Free-Grammar representation)...\n")
        cmd = 'java -cp "*" ' + JAVABUFFER + ' edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,parse -file ' + INPUTFILE    
        run(cmd)  
        print cyan("[+] Parsing completed\n")
    except Exception, e:
        if DEBUG:
            print e 
        raise Exception('Failed. Quit now!!!')
    return 0


def shift_reduce():
    """Get input from INPUTFILE
    """
    try:
        print cyan("[+] Implementing Shift Reduce Parser (included Dependency and Context-Free-Grammar representation)...\n")
        model = 'edu/stanford/nlp/models/srparser/englishSR.ser.gz'
        cmd = 'java -cp "*" ' + JAVABUFFER + ' edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,parse -parse.model ' + model + ' -file ' + INPUTFILE            
        run(cmd)  
        print cyan("[+] Parsing completed\n")
    except Exception, e:
        if DEBUG:
            print e 
        raise Exception('Failed. Quit now!!!')
    return 0


def neural_network_parser():
    """Get input from INPUTFILE
    """
    try:
        print cyan("[+] Implementing Neural Network Parser (included Dependency representation)...\n")
        model = 'edu/stanford/nlp/models/parser/nndep/english_UD.gz'
        cmd = 'java -cp "*" ' + JAVABUFFER + ' edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,depparse -parse.model ' + model + ' -file ' + INPUTFILE            
        run(cmd)  
        print cyan("[+] Parsing completed\n")
    except Exception, e:
        if DEBUG:
            print e 
        raise Exception('Failed. Quit now!!!')
    return 0


def vietnamese_pcfg():
    """Get input from INPUTFILE
    """
    try:
        print cyan("[+] Implementing Vietnamese PCFG...\n")
        model = 'edu/stanford/nlp/models/parser/nndep/english_UD.gz'
        cmd = 'java -cp "*" ' + JAVABUFFER + ' edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,parse -parse.model VietNamesePCFG -file ' + INPUTFILE          
        run(cmd)  
        print cyan("[+] Parsing completed\n")
    except Exception, e:
        if DEBUG:
            print e 
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

    line = line.replace('  ', ' ')
    line = line.replace(') ', ')')    
    line = line.replace(' (', '(')        
    #print "\n", line
    tabsize = 0
    graph = ''
    line += '~'
    for i in range(len(line) - 1):
        c = line[i]
        if c == '(':
            tabsize += 1
            graph += '\n'            
            graph += '|   '  * (tabsize - 1) +  '|-- '
            #graph += c
        elif c == ')':
            tabsize -= 1
            """
            graph += ')'
            if line[i+1] != '(':
                graph += '\n'
                graph += '|   '  * (tabsize - 1) +  '|   '
            """
        elif c == ' ':
            graph += ' --- '
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
            
            print cyan('[+] Output report is saved to' + OUTPUTFILE + '. You can open with MS Excel for more detail or view a brief as below.')
            if cmd == "nn":
                return 0
            print cyan("\n[+] Parse tree:")

            try:
                parsetrees = get_parse_tree(data)                   
                cnt = 0
                for parsetree in parsetrees:            
                    parsetree = parsetree.encode('utf-8')
                    #print '   [' + str(cnt) + ']', parsetree.encode('utf-8'), '\n'
                    print '   [' + str(cnt) + ']', parsetree, gen_graph(parsetree), '\n'
                    cnt += 1
            except Exception, e:
                if DEBUG:
                    print e
                print "     not available..."
                pass

    except Exception, e:
        if DEBUG:
            print e        
        raise Exception("Something wrongs ! Check log and report to developer!!!")

    return 0


promt_message = cyan("""\n    Select from the menu:""") + blue("""
        [1] Lexiclized Parser
        [2] Shift Reduce Parser
        [3] Neural Network Parser
        [4] Vietnamese PCFG
        [0] Quit Parser Wrappe\n\n""") + green("""    Parser Wrapper> """)

def print_cover():
    os.system('clear')
    raw = ("""

         .d8888b.                                      .d8888b.                      .d8888b.         d8888 
        d88P  Y88b                                    d88P  Y88b                    d88P  Y88b       d88888 
        888    888                                         .d88P                    888    888      d88P888 
        888        888d888  .d88b.  888  888 88888b.      8888"                     888            d88P 888 
        888  88888 888P"   d88""88b 888  888 888 "88b      "Y8b.                    888           d88P  888 
        888    888 888     888  888 888  888 888  888 888    888       888888       888    888   d88P   888 
        Y88b  d88P 888     Y88..88P Y88b 888 888 d88P Y88b  d88P                    Y88b  d88P  d8888888888 
         "Y8888P88 888      "Y88P"   "Y88888 88888P"   "Y8888P"                      "Y8888P"  d88P     888 
                                             888                                                            
                                             888                            | Neutral Language Processing               
                                             888                            | Parser Wrapper               
    """).split('\n')
    
    for line in raw:
        color = basic_color(str(random.randint(31, 36)))
        print color(line)
    

if __name__ == '__main__':    
    
    while (True):
        print_cover()
        check_requirement()
        if DEBUG:
            print_input()    
        cmd = raw_input(promt_message).strip()
        if cmd == '2':
            shift_reduce()
            read_output(cmd)
        elif cmd == '1':
            lex_parser()
            read_output(cmd)
        elif cmd == '3':
            neural_network_parser()
            read_output(cmd)        
        elif cmd == '4':
            vietnamese_pcfg()
            read_output(cmd)        
        elif cmd == '0':
            quit()
        else:
            print blue("Try again! Type correct input, please!")

