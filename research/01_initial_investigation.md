# Initial Investigation of DMINR round 2

## Background
During my first time working at DMINR I was tasked with taking a user's search term, and from that finding and ranking a list of related named entities, whatever they might be. For example, a search of COVID-19 might be expected to return locations particularly hard hit, pharmaceutical companies developing vaccines, and promenant related figures. Other less odvious connections could also be included, drawing more subtle links. 

The system I developed retrieved a configurable selection of news articles, and parsing through them extracted and classified the named entities into several very general catagories (Person, Location, Organisation, Misc.). These extracted entities were then ranked based using a lightweight BM25 based statistical method, and returned to be displayed to the user on the DMINR website.  

While the system as it stands works relatively effectively, there are several problems with it which I will touch on below. Along with hoping to fix some of these problems, several new features and methods will hopefully be explored to imporove the product, making it a truly cutting edge journalist's tool that provides interesting, insightful, but most importantly reliable results, all the while being as transparent as possible. The tool should be something that journalists can trust and understand, at least on a high level.  

- Problems with the old system
    - Slow - Is written entirely in Python. While a lot of the libraries doing the heavy lifting have more performant compiled languages behind them, a lot of the text processing required to format the results and work around idiosyncracies of the outputs is done purely in Python, which means that results can take longer than hoped to return.  
    - Contains lots of 'bodges' - The code doesn't look or flow particularly nicely, with lots of messy workarounds having to be implemented to cope with weird bugs and outliers from the entity extraction module.  
    - It relies on an entirely statistical method to evaluate the "related-ness" of two entities. While BM25 is really great for being able to classify results from across an entire article that would exceed BERT's sequence length limit, it have very few tuning and optimisation opportunities, which means that it cannot be taylored and optimised for the particular task at hand.

- New ideas to be implemented
    - Use BERT to not only extract named entities, but also the relationships between them. This is the key change in the second round of this project compared to the first, but while this seems like a relatively small change alone, a plethora of new problems emerge.
        - The implementation of BERT used for the old system was taken nearly straight from the HuggingFace transformers library. It came with an token classification output layer that could classify any tokens belonging to an entity with its correct tag. This time a more advanced and complex output layer will need to be developed and implemented to include a relationship classification.  
        - A new dataset will need to be created to include relationships between entities. This is listed as a key goal of the project and will be a significant undertaking in iteself. We have the oportunity to have it verified manually by jornalists, so could be an extremely interesting and potentially influential piece of work.  
    - The speed and resource allocation of the algorithm will be very important for any commercial release of the DMINR tool. For now, most of the coding will be done in Python and related libraries. If time is available however, slow running funtions could be given a backend in a more performant language such as C or Rust using Cython.

Things discussed in future documents:  
1. 02_bert_output_layer.md - BERT output layer architecture investigation
2. 03_relationship_dataset.md - Research and thoughts on a entity and relationship extraction dataset
