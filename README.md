<div align="center">
  <img src="cams_logo_jan112024.svg" alt="CAMS Asset Management System"/>
</div>

# CAMS "Rainbow Trout"

CAMS Asset Management System, or just CAMS, is a fully custom inventory management software made for mainly organizing computer hardware. I have started to learn how to write Python to start working on the project in late 2021. The idea was from created the need of a specialized asset/inventory management system software to organize the vast amount of computers and computer parts that I had. The idea for using ID numbers and tags for my own hardware has originated in likely 2017 though I have not had a proper system to keep track of assets since then.

CAMS is based off the fully custom-made inventory management software, commonly referred to as just "IMS", used by the computer resale company 2nd Life Inc. of Richmond, Virginia, United States where I was employed formerly. Unlike CAMS, 2nd Life IMS was written using Ruby on Rails. CAMS is also inspired by the inventory software [PartKeepr](https://github.com/partkeepr/PartKeepr).

Formerly CAMS meant Computer Asset Management System but now CAMS referrs to CAMS Asset Managment System since the software can be used to manage other types of assets if configured so.

While writing this software, I am still new to Python and programming in general, there may be unoptimized code, security vulnerabilities or errors in the code. I would appreciate any ideas for improvements, this can be done with the "Issues" tab of the GitHub repository. 

Intended Use: CAMS is fully custom to what I need out of an asset management system and may not be suitable for most other applications. 

## Requirements

### Software (server)
CAMS is developed entirely on Debian GNU/Linux and Linux Mint. Functionality on Windows platforms is not guaranteed.

Requirements for a specific version of Python 3 may change as dependencies are added or removed

### Software (client)
HTML5, maybe CSS3, JavaScript and cookie support are required.

## Setup
*Coming soon*

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



