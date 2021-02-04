mod ds;

fn main() {

    let corpus = vec![
        vec!["hello", "world", "how", "are", "you", "today"],
        vec!["my", "wife", "is", "jo", "and", "you", "should", "say", "hello"]
    ];


    let (idx, dlt) = ds::build_data_structures(corpus);
    //let doc = "The “brown” fox can't jump 32.3 feet, right?";
    //let tokenizer = RegexpTokenizer::default();
    //let doc: Vec<String> = tokenizer.tokenize(doc)
    //    .map(|word| word.to_string())
    //    .collect();

    idx.print();

    dlt.print();

    //println!("Total words in IF: {}", inv_file.total_words());
}
