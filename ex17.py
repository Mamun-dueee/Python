from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s " %(from_file, to_file)

from_obj = open(from_file)
#data_from = from_obj.read()

#print "The input file is %d byte." %len(data_from)
print "Does the output file exists? %r" % exists(to_file)

print '''
    Are u sure to copying? 
    If yes press RETURN.
    If not CTRL-C. '''
raw_input("-->")

to_obj = open(to_file, 'w')
to_obj.write(from_obj.read())

print "OK, Done All"
from_obj.close()
to_obj.close()
        