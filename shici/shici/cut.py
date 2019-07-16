import jieba
import re

dicts = set()
with open('corpus.csv', 'r') as f:
    line = f.readline().strip()
    while line:
        if line.count('('):
            match = re.findall(r'\(.*?\)', line)
            for m in match:
                line = line.replace(m, '')
        li = jieba.cut(line)
        for l in li:
            if l:
                dicts.add(l)
                print l
        line = f.readline().strip()

