from itertools import count


def potato(a,b):
    return a + b
def tomato(a,b):
    return a - b
    #add comment 
    #%%
    string = "well, I am pepe, how're you doing? I am good"

    def calculate_frequencies(text):
        words = text.split()
        frequencies = {}

        for word in words:
            count = words.count(word)
            frequencies [word] = count

        return frequencies

    calculate_frequencies(string)

# %%
string = "well, I am pepe, how're you doing? I am good"

def calculate_frequencies(text):
        words = text.split()
        frequencies = {}

        for word in words:
            if word in frequencies:
                frequencies[word] = frequencies[word] + 1
            else:
                frequencies[word] = 1
        return frequencies

calculate_frequencies (string)
# %%
string = "well, I am pepe, how're you doing? I am good"

def calculate_frequencies(text):
        words = text.split()
        frequencies = {}

        for word in words:
            if word in frequencies:
                frequencies[word] = frequencies[word] + 1
            else:
                frequencies[word] = 1
        return frequencies

def show_frequencies(frequencies):
    for word in frequencies:
        print(word + " I " + frequencies[word] * "*")

show_frequencies(calculate_frequencies(string))

# %%
string = "well, I am pepe, how're you doing? I am good"

def calculate_frequencies(text):
        words = text.split()
        frequencies = {}

        for word in words:
            if word in frequencies:
                frequencies[word] = frequencies[word] + 1
            else:
                frequencies[word] = 1
        return frequencies

def show_frequencies(frequencies):

    longest = 0
    for word in frequencies:
        if len(word) > longest:
            longest = len(word)

    for word in frequencies:
        number_of_spaces = longest - len(word)
        print(word + number_of_spaces * " " + "|" + frequencies[word] * "*")

show_frequencies(calculate_frequencies(string))
# %%
