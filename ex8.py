formatter = "%r %r %r %r "

print formatter %(1,2,3,4)
print formatter %("One", "Two", "Three" , "Four")
print formatter %(True, False, True , False)
print formatter %(formatter, formatter, formatter, formatter)
print formatter %(
    "I am Al Mamun Siddiki",
    "I am a DUan.",
    "I a'm also an EEEean.", #as the string has '(a'm), thus in output double                               quate is appeared.
    "I live in SH hall."
            
)