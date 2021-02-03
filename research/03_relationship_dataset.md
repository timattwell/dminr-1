# Dataset Creation - Initial look at the literature
## First Thoughts
My initial thoughts on what factors into a good dataset are as follows:
- **Size** - Should be of a suitable size (What is this size? Compare to other similar datasets.)
- **Balanced** - Should contain a similar ratio of examples of each class. For example, in a dataset with 5 classes, each should make up 20% of the examples.
- **Well formatted** - Clean data in == clean data out, hopefully...
- **Intentionally designed** - Dataset examples intentionally capture particular rules that the model should follow.
- **Recent** - We want our dataset to properly reflect the current times and language
- 

## Datasets to Review (NER)
- CoNLL 2003 NER 
- WNUT 2017 Emerging Entities
- OntoNotes 5.0

## CoNLL 2003 NER [https://arxiv.org/pdf/cs/0306050.pdf]
The previous iteration of the entity connections program used CoNLL2003 as the training data. It's really the research standard when it comes to Named Entity Recognition (NER) tasks, with it being the defacto benchmark for any new model's performance in the area.  

### Data
The data annotated in CoNLL2003 comes from the Reuters Corpus, and was taken from several months in the **later half of 1996**. This resulted in the amount of english data shown below:
- Training set (Articles, Sentences, Tokens; LOC, MISC, ORG, PER):
    - 946, 14,987, 203,621
    - 7140, 3438, 6321, 6600
- Development set:
    - 216, 3,466, 51,362
    - 1837, 922, 1341, 1842
- Test set:
    - 155, 3,160, 51,943
    - 1668, 702, 1661, 1617
- Total:
    - 1,317, 21,613, 306,926
    - 10,645, 5,062, 9,323, 10,059

With just over **300k total tokens** in 21k sentences, CoNLL2003 is of a decent size. The balancing of the dataset could be a potential issue however, with the MISC tag being **represented half the frequency** of the other, more specific tags. This could lead to the optimiser of any given ML model underfitting to this particular tag. Various methods use this dataset and achieve extremely high F-scores (*94.3 for LUKE!!??*) so it seems that this balancing issue doesn't cause a significant issue for these more advanced models.

### Data Preprocessing
For all data a tokenizer (splitting sequence into tokens), a part-of-speach tagger (semantic data for each token), and a chunker (not sure tbh) were applied to the raw data. The english form of the data was *NOT* lemmatized. Or at least the paper doesn't specify that it was, unlike the german data. The named entity tagging was done **by hand**, largely following MUC(?) conventions with an added ***MISC*** flag.

### Data Format
*N.B - This is taken almost verbatim fromthe paper.*  
Basic formatting - one word per line, with empty lines representing sentence boundaries. Each line contains 4 fields: the word, its POS tag, its chunk tag, and its named entity tag. Words tagged with ***O*** are outside of named entities and the ***I-XXX*** tag is used for words inside a named entity of type ***XXX***. Whenever two entities of type ***XXX*** are immediately next to each other the first word of the second entity will be tagged ***B-XXX*** in order to show that it starts another entity. The data contains entities of four types: persons(***PER***), organisations(***ORG***), locations(***LOC***) and miscellaneous names(***MISC***). THis tagging scheme si the IOB scheme origuinally put forward by Ramshaw and MArcus (1995). We assume that named entities are non-recursive and non-overlapping. When a named entity is embedded in another enamed entity, usually only the top level entity has been annotated.

### Thoughts
The CoNLL2003 datset is really fantastic dispite its age



## WNUT 2017 Emerging Entities