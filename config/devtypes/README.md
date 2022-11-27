This directory, devtypes, is for configuration data that applies to database tables, form data/choices and part number generation. 

Each internal name, not the name displayed to the end user, is a four-letter acronym.

The complexity of each device type varies greatly, some types such as servers and desktops are expected to contain over 30 fields.

## devtypes.csv

### Column: name
Name that is displayed to the user

### Column: table
Name used internally, also the name of the directory within this one to use

### Column: cipn
Either "True" or "False", indicating support for Component Internal Part Number generation.

## Device Type Directory Contents

### cols.csv
Each device type contains a file named "cols.csv" which such information, other CSV files are mainly used for dropdown data, referred to in the "cols.csv" file.

#### Column: datatype

- autointeger: Integer data type, is not included in forms or is editable by the end user, used as the CAMS device ID
- integer: Whole number, minimum and maximum values are defined by the "min" and "max" columns respectively
- text: String value
- dropdown: String value that has predefined values, ddfile column links the file with dropdown choices

Currently not implemented but planned to be added soon:

- multiple
- boolean
- macaddress
- ipaddress
- url

TODO: rest of this