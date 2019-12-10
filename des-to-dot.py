#!python

# Convert a statechart diagram from a .des file into a .dot file for
# Graphviz so that the statechart can be visualised.

filename = 'digitalwatch.des'

section = None  # maintain the state of reading the .des
node = None  # what node are we processing now
source = None  # state transition source

print("digraph digitalwatch {")

with open(filename, 'r') as fh:
    # Read the .des file with (ironically) very lame state machine here.
    for s in fh.readlines():
        s = s.rstrip()
        if s.startswith('STATECHART'):
            section = 'statechart'
        elif s.startswith('TRANSITION'):
            section = 'transition'
        elif not s and section in ('statechart', 'transition'):
            # Reached end of a section...
            section = None
        elif section == 'statechart':
            if s.startswith(' ' * 8):
                print(("  %s.%s" % (node, s.split()[0])).replace('.', '_'))
            elif s.startswith(' ' * 4):
                node = s.split()[0]
        elif section == 'transition':
            s = s.split()
            if s[0] == 'S:':
                source = s[1]
            elif s[0] == 'N:':
                destination = s[1]
                print(("  %s -> %s" % (source, destination)).replace('.', '_'))
        else:
            pass
            # print section, s

print("}")
