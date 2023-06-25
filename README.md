# CAMS "Rainbow Trout"

CAMS means CAMS Asset Management System, it was created in the need of a specialized asset/inventory management system software. Formerly CAMS was Computer Asset Management System but was changed to CAMS Asset Managment System as it can be used for more than just computers. 

CAMS is heavily inspired by the fully custom-made inventory management software, commonly referred to as just "IMS", used by the computer resale company 2nd Life Inc. of Richmond, Virginia, United States where I am employed from time to time. The IMS used by 2nd Life Inc. was written using the Ruby on Rails framework.

This project is what originally introduced me to Python and programming in general. I am still realitively a beginner to Python and programming in general.

Intended Use: CAMS is fully custom to what I need out of an asset management system and may not be suitable for most other applications. 

## Requirements

### Hardware (server)
CAMS may run on any platform that Python 3.8 and later supports, including but not limited to x86, x86-64, mips32, mips64, armv7l (32-bit, e.g. Raspberry Pi 2 and earlier, Banana Pi F2P/F2S) and armv8 (64-bit, e.g. Raspberry Pi 3 and 4). A minimum of **512MB of system memory (RAM) is recommended**. Depending on the environment, it may run on systems with less memory.

### Software (server)
CAMS is developed entirely on Debian GNU/Linux and Linux Mint. Functionality on Windows platforms is not guaranteed.

As Django 4.2 is currently the only dependency in "requirements.txt", the minimum Python version required is **3.8** as stated in the [Django documentation](https://docs.djangoproject.com/en/4.2/faq/install/).

### Software (client)
Due to the lack of login system and user settings at the moment, support for cookies is not required. Also, JavaScript is not required to use the features of the web application. HTML5 support is recommended.

## Setup
*Section To-Do*

## Configuration
The configuration file in config/database/entry.csv defines the form fields and database models used by the application. The included file is rather basic but can be modified to add more fields.

### When to use --build
./runner_dev can accept one command-line flag, --build

When --build is used, the script removes all of the built Python files, rebuilds such files and does any migrations. This may lead to data loss so it is recommended to back up the database before doing this.

When to use --build:

- After adding, removing or editing themes under config/themes/
- (Until dynamic models are implemented) After editing anything in config.json

*Rest of Section To-Do*

### Printing
CAMS can make identification tags for parts and devices.

For the best results, printing at 200, 400, 600, 800, 1000 or 1200 DPI is recommended.



