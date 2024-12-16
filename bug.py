def function_with_unclosed_file(filename):
    f = open(filename, 'w')
    f.write('some data')
    # Forgot to close the file!