# Semantic Similarity Chatbot

By [Allison Parrish](http://www.decontextualize.com/)

This is a little snippet of sample code that I wrote for implementing a chatbot
based on semantic similarity.

## Installation

You can just cut and paste the code, if you want!

Or you can install via `pip`:

    pip install https://github.com/aparrish/semanticsimilaritychatbot/archive/master.zip

Other Python modules you'll need to have installed:

* [simpleneighbors](https://github.com/aparrish/simpleneighbors)
* [numpy](http://www.numpy.org/)
* [spacy](https://spacy.io/)

Note that you'll need to download a spaCy [model](https://spacy.io/models/)
with word vectors for this chatbot to feel like it's doing anything useful. The
default model for English *does not include word vectors*, so you'll need to
download a model that does. For English, I recommend the `large` model:

    python -m spacy download en_core_web_lg

## Usage

TK

## License

See `LICENSE` in this repository.
