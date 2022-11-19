# Introduction
Codenamed: "Rainbow Trout" 

CAMS means Computer Asset Management System, it was created in the need of a specialized asset/inventory management system software. 

CAMS is heavily inspired by the fully custom-made inventory management software, commonly referred to as just "IMS", used by the small computer resale company 2nd Life Inc. of Richmond, Virginia, United States where I was employed formerly. The IMS used by 2nd Life Inc. was written using the Ruby on Rails framework.

This project is what originally introduced me to Python and programming in general. I am still realitively a beginner to Python and programming.

Intended Use: CAMS is fully custom to what I need out of an asset management system and may not be suitable for most applications. 

## Requirements
CAMS is server-side software, no software is required to be installed on client systems other than just a browser. See below for browser requirements.

### Client (browser) requirements
- HTML5
- Cookies
- ***Other details TBD***

### Software (server-side)

Required Dependencies:
- Python 3.x (specific minimum version unknown for now, tested with 3.9 and later)
- Python Flask
- Flask-WTF
- Flask-SQLAlchemy
- Jinja2

#### Operating System
CAMS was written mainly for use on FreeBSD and Linux-based operating systems. 

CAMS may *not* run on Microsoft Windows without code modification, specifically with how file paths are written. 

### Hardware (server-side)
CAMS is mainly tested and written on systems using the x86-64 CPU architecture. While mainly untested, it may run on other CPU architectures such as ARM, MIPS and 32-bit x86, as long as the required software are available for such platforms.

So far, CAMS is single-threaded and therefore does not make use of more than one processor core/thread.





