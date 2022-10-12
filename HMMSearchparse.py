from Bio import SearchIO


class HMMsearchparse:
    def __init__(self):
        with open("HMMsearch3", "r") as self.__hmmfile:
            self.__sequence_counter = 0
            self.get_sequence_and_header()

    def get_sequence_and_header(self):
        with open("ThirdIteration.fasta", "a") as a_file:
            for result in SearchIO.parse(self.__hmmfile, "hmmer3-text"):
                for hit in result:
                    for hsp in hit:
                        evalue = getattr(hsp, "evalue")
                        for i in hsp:
                            seq = i.hit
                            fasta = seq.format("fasta")
                            a_file.writelines(fasta)


if __name__ == '__main__':
    parseobj = HMMsearchparse()