
import re
import string
import random
import os 

from graph import Graph, Vertex



def get_words_from_text(text_path): # Step 1
    with open(text_path, 'r') as f:
        text = f.read()

        # remove [text in brackets]
        text = re.sub(r'\[(.+)\]', ' ', text)   # this replaces any words inside square brackers with a space


        text = ' '.join(text.split())   # this removes all whitespaces, including tabs and newlines, and turns them all into just spaces
        text = text.lower()             # we make everything lower case for ease of comparisons and processing

        # we also want to remove all puncuations since leaving it in can make things a bit more complex
        text = text.translate(str.maketrans('', '', string.punctuation))   # here we translate every punctuation to an empty string

    words = text.split()    # split on spaces again
    return words



def make_graph(words):              # Step 2
    g = Graph()
    
    previous_word = None

    # we check for each word whether its in the graph already, if not then we add it
    for word in words:
        word_vertex = g.get_vertex(word)
        # if there was a previous word, then we add an edge if it does not already exist, otherwise we increment the weight of the graph
        if previous_word:
            previous_word.increment_edge(word_vertex) # this increments the weight bw the two words by 1

        # set our word to the previous word and iterate
        previous_word = word_vertex

    # We also need to generate probability mappings before composing the graph, and this is a good place to do it, right before we return the graph
    g.generate_probability_mappings()

    return g



def compose(g, words, length=50):   # Step 3
    composition = []
    word = g.get_vertex(random.choice(words))   # pick a random word to start from

    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)
    
    return composition



def main(artist):
    
    # Step 1: Get words from text
    # words = get_words_from_text('texts/hp_sorcerer_stone.txt')

    words = []

    for song_file in os.listdir(f'songs/{artist}'):
        print(song_file)
        song_words = get_words_from_text(f'songs/{artist}/{song_file}')
        words.extend(song_words)
        
    # Step 2: Make a graph using those words
    g = make_graph(words)

    # Step 3: Get the next word for x number of words (defined by the user)
    composition = compose(g, words, 100)

    # Step 4: Show the user
    return ' '.join(composition)    # returns a string where all the words are seperated by space


if __name__ == '__main__':
    print(main('green_day'))