import trees as tr
from tqdm import tqdm

treebank_name = {
    'train': '02-21.10way.clean',
    'valid': '22.auto.clean',
    'test': '23.auto.clean_fixed'
}

fold = 'train'
pred = tr.load_ptb(f'eval-ptb-punc-{fold}/parse.txt')
treebank = tr.load_ptb('../../constituency-test-parser/data/'+treebank_name[fold], lower = False)

for tree1, tree2 in tqdm(zip(pred, treebank)):
    try:
        tr.transfer_leaves(tree1['tree'], tree2['tree'])
    except Exception as e:
        pass
    tree1['tree'] = tr.remove_labels(tr.collapse_unary_chains(tr.clean_empty(tr.standardize_punct(tree1['tree'], True))))
    if len(tree1['tree'].sent()) == 1:
        tree1['tree'] = tr.Tree('X', [tree1['tree']], None)

open(f'eval-ptb-punc-train/clean-parse.txt', 'w').write('\n'.join([str(exmp['tree']) for exmp in pred]))