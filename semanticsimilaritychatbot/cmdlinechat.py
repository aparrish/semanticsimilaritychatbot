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
parser.add_argument('--load-prefix', type=str,
        help="prefix for saved files",
        default="sscb")
args = parser.parse_args()

stderr("loading spacy model", args.spacy_model)
nlp = spacy.load(args.spacy_model)
stderr("done")

stderr("loading chatbot", args.load_prefix)
bot = SemanticSimilarityChatbot.load(args.load_prefix, nlp)
stderr("done.")

stderr("processing input from stdin...")

while True:
    inputstr = input("> ")
    print(bot.response_for(inputstr))

