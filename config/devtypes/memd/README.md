## Note on mbnd (Module Brand)

The part number element is derived from the associated byte entry in JEP106xx.pdf 
This is done so one would not have to come up with an acronym for each of the 1700+ entries in newer documents.

Each mbnd CIPN value is made up of:

B + <amount of 7F bytes> + <last byte>

For example: 0x7F7F7F7F7F7F7F7F7F7F7F7FE6 would become B12E6