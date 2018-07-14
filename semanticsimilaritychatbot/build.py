from semanticsimilaritychatbot import SemanticSimilarityChatbot

import sys, argparse
import spacy

def stderr(*args):
    print(*args, file=sys.stderr)

parser = argparse.ArgumentParser(
        description="Utility to build a chatbot from a plain text file")
parser.add_argument('--spacy-model', type=str,
        help="spacy model file to use",
        default="en_core_web_lg")
parser.add_argument('--save-prefix', type=str,
        help="prefix for saved files",
        default="sscb")
parser.add_argument('--n-trees', type=int,
        help="number of trees in approx nearest neighbor index",
        default=50)
args = parser.parse_args()

stderr("loading spacy model", args.spacy_model)
nlp = spacy.load(args.spacy_model)
stderr("done")

bot = SemanticSimilarityChatbot(nlp, 300)

stderr("processing input from stdin...")
lastline = None
for line in sys.stdin:
    line = line.strip()
    # empty lines mean "end of conversation"
    if line == "":
        lastline = None
        continue
    if lastline is not None:
        bot.add_pair(lastline, line)
    lastline = line

stderr("building index...")
bot.build(args.n_trees)

stderr("saving with prefix", args.save_prefix)
bot.save(args.save_prefix)

stderr("done.")


