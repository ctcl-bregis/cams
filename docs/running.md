## Running the Server
For development purposes, there is the "runner_dev" script in the root of the app.
The script makes a directory in /dev/shm/ and symlinks the "data" directory to it, this is done so the database is kept in memory (RAM) instead of writing to disk every time.

Later on, a script for running the app in production environments would not keep the database in memory and instead have it written to the "data" directory on disk.


### Windows and Mac
For Windows and Mac systems, CAMS is currently untested on these platforms and the provided scripts may not function on such platforms.