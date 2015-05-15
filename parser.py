# Line Parser
    # First Section is space delimited between writings and [Reading]
    # Writing Parser
        # Second Char of first block to first space of first block
        # Take substring and delimit by ;
        # Return as an array of writings
    # Reading Parser
        # Pass in string from first chunk
        # Get substring between [ and ]
        # Split substring by ;
        # Return as array of strings (these are the readings) pure kana
import codecs

def open_file(filename=None):
    if filename is None:
        return codecs.open('edict2', encoding='euc-jp')
    else:
        return codecs.open(filename, encoding='euc-jp')

def parse_line(line=None):
    if line is None:
        return
    else:
        tokens = line.split("/")
        first_chunk_parser(tokens[0].strip())
        print(tokens)

def first_chunk_parser(firstChunk=None):
    if firstChunk is None:
        return
    else:
        chunkTokens = firstChunk.split(" ")
        kanji_parser(chunkTokens[0])
        reading_parser(chunkTokens[1])
        

def kanji_parser(kanjiPart=None):
    if kanjiPart is None:
        return
    else:
        return kanjiPart[1:].split(';')

def reading_parser(readingPart=None):
    if readingPart is None:
        return
    else:
        return readingPart[readingPart.index('['):readingPart.index(']')].split(';')
        
        

        
if __name__ == '__main__':
    file = open_file()
    for line in file:
        parse_line(repr(line))
        #print(repr(line))
