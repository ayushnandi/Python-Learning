
def word_count(fname):
    with open (fname) as f :
        return Counter (f.read().split())
print(word_count('exe.txt'))