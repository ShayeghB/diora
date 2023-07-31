from tqdm import tqdm
import sys
sys.path.insert(1, '../../../')
from library.tree import extract_words_from_str_tree
import re

fold = 'train'
ref = f'../../../data/ptb-{fold}-gold-filtered.txt'
src = f'./eval-ptb-punc-{fold}/clean-parse.txt'

refs = open(ref).readlines()
srcs = open(src).readlines()
srcs_sents = [' '.join(extract_words_from_str_tree(s)).lower() for s in srcs]

outputs = []
for ref_line in tqdm(refs):
    ref_sent = ' '.join(extract_words_from_str_tree(ref_line)).lower()
    pattern = r'(?<=\d),(?=\d{3})'
    ref_sent = re.sub(pattern, '', ref_sent)
    if ref_sent not in srcs_sents:
        print('---', Exception(ref_sent))
        outputs.append('')
    else:
        i = srcs_sents.index(ref_sent)
        outputs.append(srcs[i].strip())


open(f'eval-ptb-punc-{fold}/diora.txt', 'w').write('\n'.join(outputs))