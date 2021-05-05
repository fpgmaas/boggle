# Boggle Solver

![](Boggle-Board-2-450x400.png)

### Problem definition

This repository contains a Python script that takes as input an arbitrary grid of letters and finds all words in the grid according to the rules of Boggle. The list of accepted words is the list provided by [OpenTaal](https://github.com/OpenTaal/opentaal-wordlist).

A working example can be found in `notebooks/main.ipynb`. 

## Example

```python
boggle_string = 'abcdefghijklmnop'
boggle_grid = BoggleGrid(np.resize([x for x in boggle_string],(4,4)))
boggle = Boggle(boggle_grid,word_list)
all_words = boggle.solve()

print('--- BOGGLE ---\n')
print(boggle_grid)

print('\n\n--- ALL WORDS ---\n')
print([word['word'] for word in all_words])

--- BOGGLE ---

[['i' 'p' 'r' 'a']
 ['c' 's' 'o' 'l']
 ['t' 'j' 'e' 'd']
 ['f' 'v' 'u' 'x']]


--- ALL WORDS ---

['isp', 'pro', 'pol', 'pos', 'por', 'pst', 'pis', 'ral', 'rol', 'roe', 'ros', 'ale', 'ars', 'cis', 'sol', 'sop', 'soa', 'sip', 'sic', 'ode', 'oed', 'opi', 'ors', 'led', 'lex', 'lev', 'les', 'los', 'lor', 'lar', 'jeu', 'jol', 'joe', 'esp', 'elo', 'dux', 'des', 'deo', 'del', 'dol', 'dos', 'dop', 'dor', 'vel', 'prol', 'pole', 'poes', 'poel', 'pose', 'post', 'piso', 'rode', 'roes', 'rost', 'sela', 'sjeu', 'sjor', 'lest', 'laos', 'judo', 'duel', 'does', 'doel', 'dors', 'dorp', 'vues', 'vest', 'veld', 'velo', 'roest', 'solde', 'solex', 'sjoel', 'spoed', 'spoel', 'judex', 'duvel', 'dorst', 'dorps', 'postje', 'sodeju', 'judoles']
```