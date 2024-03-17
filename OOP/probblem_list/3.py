def sort_lexicon(lexicon):
    print(lexicon)
    print(lexicon.items())
    return sorted(lexicon.items())
# Sample usage:
lexicon = {
 "abracadabra": "A word uttered to perform a magical act.",
 "enchantment": "The act of casting spells or charms.",
 "mystic": "Relating to mysteries or mystical powers."
}

sorted_lexicon = sort_lexicon(lexicon)
print(sorted_lexicon)