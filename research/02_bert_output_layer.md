# BERT Output Layer for Entity and Relationship Extraction  

## Background - why?
In the previous iteration of the entity connections program, BERT's only task was to sift though all the text thrown at it, and spit back named entities. This made for a rather trivial task - the output could just be of the same shape as the input sequence, and consist of tags classifying each token as either 'O'(not a named entity) or one of several catagories of entity such as LOC, PER, ORG, or MISC. These tags could be preceeded by a further 'B-' or 'I-' to help the system know if a multi-token entity was beginning. All just a trivial token classification problem.  

This isn't all we will be asking from BERT in this iteration. This time we will be asking for not only an entity classification, but also a relationship classification between entities. If we could be sure that there would be only one entity pair per sequence then the output layer could remain fairly trivial still, remaining similar to the previous iteration but including a further classification to determine the relationship. Unfortunatly this will not be the case. As with any real world data, it will be messy. We will encounter sequences with many entity pairs, and some with none. Our system needs to be able to deal with this. As far as I have been able to gather from my admittedly fairly limited reading, there are two main potential high level methods we could use:  

1. Multiple rounds of single relationship extraction - 






how to link a search term with related pairs from bert?