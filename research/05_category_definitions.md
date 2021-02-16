# Entity Category Definitions
After reviewing the previous research and reciving input from the rest of the team, it's decided that we will build off of the initial four CoNLL2003 catagories, and expand them with three more. Thus, the resulting 7 classification categories will be:  
- Person
- Location
- Organisation
- Product*
- Event*
- Law*
- Misc  
_(*) marks a added category._  

The remainder of this document will outline as precisely as possible the definitions and bounds of these classification tags, while also giving rules as to the practical formatting of these tags.

## Catagory Definitions
### Person:
The person catagory should contain the name of any person - whether real or fictional. Note that this should only contain explicit named references, such as "Boris Johnson", rather than potentially ambiguously targeted pronons or other identifiers, such as "He", "The Prime Minister".

### Location:
The location catagory contains all named references to a place. This can include geopolitical entities, facilities. Similarly to the person tag, only explicit mentions should be included (this will be a common idea) - references to "there", for example, should not be included.

### Organisation:
The organisation catagory should contain any named reference to an organisation. This could be a company, charity, football team, band, government. One of the potentially more ambiguous categories, particularly for edge cases. Once again, only explicitly named references should be included.

### *Product*:
The new product catagory should include created work, tangible goods, or well defined services. Again, this needs to be carefully and thoughtfully defined to make edge cases easier to deal with. Only explicitly named references.

### *Event*:
While the previous categories here mainly focus on physical things that can be held, the event catagory contains explicity named events that can be experienced in some way. These can be past, present or future events, and may include politial rallies, wars, festivals, holidays.

### *Law*:
The law category is the least known to me. OntoNote5.0 defines its law category as "Named documents made into laws". This seems a fine definition, but should this also include other legal documents such as licenses, patents, or contracts? The differing naming and referencing conventions involving these legal documents could lead to some challenges, so should pay close attention to this category.

### Misc:
Everything else really! I forsee this being quite a small subset of the results. The general conventions apply here as much as in the other catagories. Only explicit mentions should be tagged - no implicit mentions.

## Dataset format
CoNLL2003 uses the simplest possible format. Each token from a sequence is listed line by line. following the token statement, the other information (including entity classification) is listed after it on the line, separated by whitespace. The next line contains the next token and its information, and so on. Sequences are separated by an empty line: 
- Boris I-PER  
    Johnson I-PER  
    announced O  
    the O  
    new O  
    vaccine I-PROD  
    from O  
    Biotech I-ORG  
    .  

OntoNote maintains each whitespace-separated tokenised sequence on its own line, but surrounds each entity with tag markers. Whith the same example as above, this would look like:
- \<ENAMEX TYPE="PERSON">Boris Johnson\</ENAMEX> announced the new \<ENAMEX TYPE="PRODUCT">vaccine\</ENAMEX> from \<ENAMEX TYPE="ORGANISATION">Biotech\</ENAMEX>.

WNUT2017 emerging entities are available in several formats, but its seems the most readily accesible are in the CoNLL style. This format makes the most sense to me based on the problem definition. BERT here is doing a token classification task, and the CoNLL system clearly defines the classification for each token! I think in surrounding tags system like OntoNotes 5.0 the data will need to be converted into a format fairly similar to the CoNLL format before being passed into the model anyway, and so it makes sense to go with this from the start.

## More dataset tagging specifics
One small difference I noted between the WNUT and CoNLL datasets were their methods of dealing with entitites that immediatly follow one another. This is really important to deal with for usable results in any real world use-case. CoNLL states that all entities will always start with an "I-" prefixed tag, except for an entity immediatly following another entity, in which case the first token of the second will be prefixed "B-". WNUT2017 prefixes every entity start token with a "B-" by default. In the case of a two token entity immediately following another two token entity, the two formats would work as follows:
- CoNLL
    - "I-TAG", "I-TAG", "B-TAG", "I-TAG"
- WNUT
    - "B-TAG", "I-TAG", "B-TAG", "I-TAG"  

I believe that the WNUT convention is much more helpful and explicit when 'reattaching' the tokens at the end of the process. It also allows us to potentially 'remove' punctuation from the middle of entities by simply not tagging it:
- Donald J . Trump
- "B-PER", "I-PER", "O", "I-PER"
- Donald J Trump  

In the standard CoNLL convention, if this short sequence were tagged like this, "Donald J" and "Trump" would be considered separate entities.

This raises the question: Should punctuation be included in the returned entities? The other datasets have all included it. However, during testing of the intitial system, I found that names were being returned multiple times as separate entities based on the punctuation within them. Not only would the system return Donald Trump and Donald J Trump, but also Donald J . Trump. Removing at least one source of ambiguation could have the potential to clean the results up hugely. That said, certain punctionation marks can be key parts of names, which makes a decision more difficult.

## Tag Specifics
What exactly will the tags be then? WNUT and OntoNotes use the full names for many of the categories (e.g. "B-Person", "I-Organisation"). CoNLL uses shortened tag names, which could make labelling slighly quicker if it has to be done manually. This will only work if the shortened names can be easily distinguised from each other. Thus, I propose the following (without the "B-" or "I-" prefix):
- Person - PER
- Organisation - ORG
- Location - LOC
- Product - PROD
- Event - EVNT
- Law - LAW
- Misc - MISC  

I wanted to keep them all to three characters for conformity's sake, but the 4th character really clarifies the product, event and misc tags for an observer who has no prior knowledge of the tagging system, while still being fast to type!