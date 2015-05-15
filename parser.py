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
        print(tokens)
        

        
if __name__ == '__main__':
    file = open_file()
    for line in file:
        parse_line(repr(line))
        #print(repr(line))
