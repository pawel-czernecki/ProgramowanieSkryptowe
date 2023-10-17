import argparse
import importlib

main_parser = argparse.ArgumentParser(prog="skrypt3.py", description="Skrypt 3 - REALIZUJe funkcjonalność skryptu 1 i 2")
subparsers = main_parser.add_subparsers(dest="command", help="Komenda", required=True)

skrypt1_parser = subparsers.add_parser("skrypt1", help="Komenda skryptu 1")
skrypt1_parser.add_argument("text", help="Tekst")

cut_parser = subparsers.add_parser("cut", help="Komenda cut")
cut_parser.add_argument("-d", "--delimiter", help="Separator", default="\t")
cut_parser.add_argument("-f", "--fields", help="Pola")
cut_parser.add_argument("text", help="Wejście", type=str, nargs="+")

grep_parser = subparsers.add_parser("grep", help="Komenda grep")
grep_parser.add_argument("-i", "--ignore-case", help="Ignoruj wielkość liter", action="store_true")
grep_parser.add_argument("-w", "--word-regexp", help="Szukaj tylko całych słów", action="store_true")
grep_parser.add_argument("pattern", help="Wzorzec")
grep_parser.add_argument("text", help="Wejście", type=str, nargs="+")

args = main_parser.parse_args()

if args.command == "skrypt1":
    operations = importlib.import_module("operations")

    text = args.text

    print(operations.first_character(text))
    print(operations.first_two_characters(text))
    print(operations.all_characters_except_first_two(text))
    print(operations.penultimate_character(text))
    print(operations.last_three_characters(text))
    print(operations.all_characters_in_even_positions(text))
    print(operations.merge_characters_and_duplicate(text))

elif args.command == "cut":
    cut = importlib.import_module("cut")
    cut.cut(args.text, args.fields, args.delimiter)

elif args.command == "grep":
    grep = importlib.import_module("grep")
    grep.grep(args.text, args.pattern, args.ignore_case, args.word_regexp)