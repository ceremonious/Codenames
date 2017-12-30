# Codenames
Finds clues for the popular game Codenames. 

Given a list of words, the goal is to find a single word that connects as many words in the list as possible such that someone guessing would be able to identify those words.
For example, given the list of words: [Hood, Plate, Cross, Cell, Straw, Press, Thumb, Bottle, Elevator]

The word "button" could be used to connect press, thumb and elevator. 

This solver attempts to find clues from a list of words using the word2vec representations that can be found here https://nlp.stanford.edu/projects/glove/.
