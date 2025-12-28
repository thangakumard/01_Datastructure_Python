print("********** isalnum() Method Examples **********")
"abc123".isalnum()     # True
"abc 123".isalnum()    # False
"".isalnum()           # False
print("********** isalpha() Method Examples **********")
"Python".isalpha()     # True
"Python3".isalpha()    # False
"".isalpha()           # False

print("********** isdigit() Method Examples **********")

"123".isdigit()        # True
"²".isdigit()          # True
"12a".isdigit()        # False

print("********** isdecimal() Method Examples **********")
"123".isdecimal()      # True
"²".isdecimal()        # False
"Ⅳ".isdecimal()        # False

print("********** isnumeric() Method Examples **********")
"123".isnumeric()      # True
"Ⅳ".isnumeric()       # True
"½".isnumeric()        # True

print("********** isnumeric() Method Examples **********")
"hello".islower()      # True
"hello1".islower()     # True
"Hello".islower()      # False
"123".islower()        # False

print("********** isupper() Method Examples **********")
"HELLO".isupper()      # True
"HELLO1".isupper()     # True
"Hello".isupper()      # False

print("********** istitle() Method Examples **********")
"Hello World".istitle()    # True
"Hello world".istitle()    # False
"HELLO World".istitle()    # False

print("********** isspace() Method Examples **********")
"   ".isspace()        # True
"\n\t".isspace()       # True
" a ".isspace()        # False

print("********** isascii() Method Examples **********")
"ABC123".isascii()     # True
"ñ".isascii()          # False

print("********** isidentifier() Method Examples **********")
"my_var".isidentifier()    # True
"1abc".isidentifier()      # False
"for".isidentifier()       # True (keyword, but valid identifier format)

print("********** isprintable() Method Examples **********")
"Hello!".isprintable()     # True
"Hello\n".isprintable()    # False
" ".isprintable()          # True
