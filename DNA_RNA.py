class DNA:
    def __init__(self, sequence):
        self.sequence = sequence.lower() # upper or lowercase doesn't matter in uncleic acid
        self.letters = ['a', 't', 'g', 'c']

        # checking for non-DNA letters
        for i in set(self.sequence):
            if i not in self.letters:
                raise NameError('your string contains non-DNA letter: ' + i)
        # dict for reverse complement
        self.rev_dict = {'a':'t', 't':'a', 'g':'c', 'c':'g'}
        self.len = len(self.sequence)

    def gc_content(self):
        gc = (self.sequence.count('g') + self.sequence.count('c')) / self.len
        return gc

    def reverse_complement(self):
        rev_comp = ''.join([self.rev_dict[i] for i in self.sequence[::-1]])
        return rev_comp

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.len:
            result = self.sequence[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def __hash__(self):
        return hash(self.sequence)

    def __eq__(self, other):
        return self.sequence == other.sequence

    def transcribe(self):
        transcr_dict = {'a': 'a', 't': 'u', 'g': 'g', 'c': 'c'}
        transcr_str = ''.join([transcr_dict[i] for i in self.sequence])
        return RNA(transcr_str)



class RNA(DNA):
    def __init__(self, sequence):
        self.sequence = sequence.lower()
        self.letters = ['a', 'u', 'g', 'c']
        for i in set(self.sequence):
            if i not in self.letters:
                raise NameError('your string contains non-RNA letter: ' + i)

        self.rev_dict = {'a':'u', 'u':'a', 'g':'c', 'c':'g'}
        self.len = len(self.sequence)


