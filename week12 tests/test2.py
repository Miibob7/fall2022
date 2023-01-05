def words(thing, beginning, alt, other, bar, ice, cream,):
    for word in thing:
        if word.startswith(beginning) or alt in word or other in word or bar in word or ice in word or cream in word:
         yield word
thing = ("what","in", "not", "the", "ten", "would", "net", "mother", "flower", "Jeff", "you", "home", "house", "sight", "mother","do", "flop", "not", "with", "time", "a", "flute", "cone", "Pine", "klondike", "bar", "pop" )
for word in words(thing, "w", "y", "d","a", "k", "b",):
    print(word)