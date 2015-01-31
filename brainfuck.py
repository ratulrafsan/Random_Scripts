import sys

cleanup = lambda code: ''.join([i for i in code if i in "><+-.,[]"]) #Strip non-brainfuck elements.

def while_tracer(code):
    braketmap = dict()
    stack = []
    for position, char in enumerate(code):
        if char == "[":
            stack.append(position)
        elif char == "]":
            startpos = stack.pop()
            braketmap[startpos] = position
            braketmap[position] = startpos
    return braketmap

def interpreter(code):
    code = cleanup(code)
    braketmap = while_tracer(code)
    band = [0]
    band_pointer = 0
    pointer = 0

    while pointer < len(code):
        c = code[pointer]
        if c == ">": #move to the right cell.
            band_pointer += 1
            if band_pointer == len(band):
                band.append(0)
        elif c == "<": #move to left cell.
            if band_pointer > 0:
                band_pointer -= 1
        elif c == ".": #output current cell.
            print chr(band[band_pointer]),
        elif c == ",": #take input in current cell.
            char = sys.stdin.read(1)
            if ord(char) < 2**8:
                band[band_pointer] = ord(char)
            else:
                print "non-ASCII chars not allowed!!"
                sys.exit(3)
        elif c == "[" and band[band_pointer] == 0:
            pointer = braketmap[pointer] #Skip to closing braket
            continue
        elif c == "]" and band[band_pointer] != 0:
            pointer = braketmap[pointer] #Skip to starting braket
            continue
        elif c == "+": #increment cell value.
            band[band_pointer] = (band[band_pointer]+1) % 2**8
        elif c == "-": #decrement cell value
            band[band_pointer] = (band[band_pointer]-1) % 2**8

        pointer += 1

def execute(ifile):
    with open(ifile) as bf:
        interpreter(bf.read())

def main():
    if len(sys.argv) != 2 or not isinstance(sys.argv[1], str):
        print "[ERROR]: Invalid type or number of arguments!"
        print "Usage: python {0} filename".format(sys.argv[0])
        sys.exit(1)
    else:
        execute(sys.argv[1])

if __name__ == "__main__":
    main()