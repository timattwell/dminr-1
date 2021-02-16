# Entity Classification Tagging
The model works by breaking up a sequence into individual tokens. Normally the sequence would be a sentence, and the resulting tokens would be each individual word, or part of word. Each of these tokens is then classified. If the model predicts that the token is not part of a named entity, then it will be assigned a null tag, usually **'O'** or similar. However, if the prediction says that the token does belong to a named entity, then we have some options. The simplest would be to treat the problem as a simple boolian operation - a true or false statement. However this squanders much of the classification power of complex neural network based prediction models. Instead it would be ideal to not only determine whether a token is *part* of a named entity, but also *what type* of entity it is.

## How many entity classification categories?
A naive approach would be to simply say: *"As many as possible"*.  

Realistically this wouldn't work, as the amount of data examples required to train a model using such an approch would increase the cost greatly. So here are some Pros and Cons of large catagory sets (pros/cons for smaller sets are essentially just the inverse of these):  

- Pros:
    - Has the potential to give more information to the end user
    - Can be more specific and targeted to a particular usage environment
- Cons:
    - Requires more example data to train the model
    - More difficult to build a balanced training dataset
    - Potentially less flexible as the model will not be as general

So we want a balance. A balance that gives us a range of categories that divide up the potential entities in a way helpful for the application, without the negatives making *too much* of an impact on the implementation or usefulness of the information.  

## *What do other datasets do then?*
- [CoNLL2003 NER](https://arxiv.org/pdf/cs/0306050.pdf)
    - The most used dataset for benchmarking new models and methods, and for training general systems. Takes corpus from news sources from 1996.
    - Uses four entity classification categories:
        - Person
        - Organisation
        - Place
        - Misc
    - Documentation doesn't really expand on the specific definitions of these, which I suppose makes sense seeing how general they are. They are pretty self-explanatory.

- [OntoNotes 5.0](https://catalog.ldc.upenn.edu/docs/LDC2013T19/OntoNotes-Release-5.0.pdf)
    - A project to annotate a corpus from several genres (newsm broadcast, talk shows, weblogs, usenet newsgroups and conversational telephone speech) with syntax and structural information. They aimed to go beyond previous annotation attempts and include as much information as possible while still remaining as general as possible.
    - Uses the named entity categories as follows:
        - PERSON - People, including fictional
        - NORP - Nationalities, religious or political groups
        - FACILITY - Buildings, airports, highways, bridges, etc.
        - ORGANISAION - Companies, agencies, institutions, etc.
        - GPE - Countries, cities, states.
        - LOCATION - Non-GPE locations, mountain ranges, bodies of water, etc.
        - PRODUCT - Vehicles, weapons, foods, etc. (Not services)
        - EVENT - Named hurricanes, battles, wars, sports events, etc.
        - WORK OF ART - Titles of books, songs, etc.
        - LAW - Named documents made into laws.
        - LANGUAGE - Any named language
    - This is an extremely large and complex corpus that takes from a diverse range of sources. However, many of these are casual and informal, and differ greatly from the information we might get from something like companies house or open corporate

- [WNUT 2017](https://www.aclweb.org/anthology/W17-4418.pdf)
    - Introduction makes the point of taylored datasets being important in achieving high performance in a given operational area. WNUT dataset created to establish a benchmark for models to recognise and extract "rare or emerging" entities.
    - Raw corpus taken from a range of sources (WNUT2015, twitter, reddit, YouTube comments, StackExchange)
    - The entity categories used were:
        - **person** - Names of people. Dont mark people that don;t have their own name. Include punctuation in the middle of names. Fictional people can be included, as long as they're referenced by name.
        - **location** - Names that are locations. Don't mark locations that don't have their own name. Include punctualtion in the middle of names. Fictional locations can be include, as long as they're referred to by name.
        - **corporation** - Names of corporations.
        - **product** - Name of products. Fictional products can be included, as long as they're referred to by name. It's got to be something you can touch, and it's got to be the offical name.
        - **creative-work** - Names of creative works. The workshould be created by a human, and referred to by its specific name.
        - **group** - Names of groups. Don't mark groups that don't have a specific, unique name, or companies (which should be marked **corporation**).

- [ACE05](https://www.semanticscholar.org/paper/The-ACE-2005-(-ACE-05-)-Evaluation-Plan-Evaluation-Ntroduction/3a9b136ca1ab91592df36f148ef16095f74d009e)
    - Couldn't find a place to actually read the related paper to get more context as to the creation of and genres within the dataset, but I could access the tables containing the entity categories.
    - Entity categories and subtypes:
        - FAC (Facility) - Airport, Building-Grounds, Path, Plant, Subarea-Facility
        - GPE (Geo-Political Entity) - Continent, County-or-District, GPE-Cluster, Nation, Population-Centre, Special, State-or-Province
        - LOC (Location) - Address, Boundary, Celestial, Land-Region-Natural, Region-General, Region-International, Water-Body
        - ORG (Organization) - Commercial, Educational, Entertainment, Government, Media, Medical-Science, Non-Governmental, Religious, Sports
        - PER (Person) - Group, Indeterminate, Individual
        - VEH (Vehicle) - Air, Land, Subarea-Vehicle, Underspecified, Water
        - WEA (Weapon) - Biological, Blunt, Chemical, Exploding, Nuclear, Projectile, Sharp, Shooting, Underspecified
    - Entity Classes:
        - SPC - A particular, specific and unique real world entity
        - GEN - A kind or type of entity rather than a specific entity
        - NEG - A negatively quantified (usually generic) entity
        - USP - An underspecified entity (e.g. modal/uncertain/...)
    - Also classifies mentions:
        - NAM (Name) - A proper name reference to the entity
        - NOM (Nominal) - A common noun reference to the entity
        - PRO (Pronominal) - A pronominal reference to the entity
    - The abstract states that the ACE program is dedicated to the development of technologies that automatically infer meaning from language data.
    - While several of the datasets mentioned have included additional semantic information about the tokens, none have included word *reference* data in such a way as this. This reflects on the purpose of ACE to encode *meaning* more than just read named entities. This seems ideal to make the most of the data we have ("When Tim went to the shop he bought some milk", both "Tim" and "he" could count towards the same entity mention). In practice this is a much more difficult task for the model to predict, and so even extremely complex architectures built for precisely this task barely crest an F-score of 80. (The current system sits in the mid 90s)

## Where do we stand?
Going through these 4 popular  datasets with a fine toothed comb has bought a lot of things up. Many of those things are beyond the scope of the question "What categories should we used" however, and so I'll save that for a future document. Unfortunatly none of the papers went into the thought process behind the selection of entity classification categories used, but I think it is possible to see some connections between the specificness of the categories and the stated purpose and goals of the dataset.  
In my opinion, a good way to approach the decision would be to start with the four CoNLL categories and branch out from there where more specific classification is required. For example, adding in a **'product'** tag as a subset of **'MISC'** might be helpful to the end user, but having a **'vehicle'** or **'weapon'** tag might just bloat the output and leave the user with information that has been spread and diluted over too many categories.






