use std::collections::HashMap;
use vtext::tokenize::*;

struct InvertedFile {
    index: HashMap<String, u32>,
}

impl InvertedFile {
    fn new() -> InvertedFile {
        InvertedFile {
            index: HashMap::new(),
        }
    }

    fn add_word(&mut self, word: String) {
        if let Some(x) = self.index.get_mut(&word) {
            *x += 1;
        } else {
            self.index.insert(word, 1);
        }
    }

    fn add_doc(&mut self, doc: Vec<String>) {
        doc.iter().for_each(|word| self.add_word(word.to_string()))
    }

    fn total_words(&self) -> u32 {
        self.index.values().sum()
    }

    fn print(&self) {
        for (key, val) in self.index.iter() {
            println!("key: {}, val: {}", key, val);
        }
    }
}



fn main() {

    let mut inv_file = InvertedFile::new();

    let doc = "The “brown” fox can't jump 32.3 feet, right?";
    let tokenizer = RegexpTokenizer::default();
    let doc: Vec<String> = tokenizer.tokenize(doc)
        .map(|word| word.to_string())
        .collect();

    inv_file.add_doc(doc);

    inv_file.print();

    println!("Total words in IF: {}", inv_file.total_words());
}
