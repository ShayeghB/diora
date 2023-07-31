import sys
from tqdm import tqdm
sys.path.insert(1, '../../../')
import json
from library.tree import extract_words_from_str_tree

def run():
    spans = open(sys.argv[1], 'r').readlines()
    outputs = []
    for s in tqdm(spans):
        s = str(json.loads(s)['tree'])
        s = s.replace('[', '(. ')
        s = s.replace(']', ')')
        s = s.replace(',', '')
        o = ''
        in_word = ''
        for ch in s:
            if ch in ("'", '"') and (ch==in_word or not in_word):
                if in_word:
                    o += ')'
                    in_word = ''
                else:
                    o += '(. '
                    in_word = ch
            else:
                o+=ch
        o = o.replace('(. )', '').replace('  ', ' ').replace('\\\\', '\\')
        if o.count('(') == 0:
            o = f'(. {o})'
        outputs.append(o)
    open(sys.argv[2], 'w').write('\n'.join(outputs))

def main():
    run()

if __name__ == '__main__':
    main()