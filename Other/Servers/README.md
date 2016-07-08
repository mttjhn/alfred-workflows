Servers ([Download](https://raw.github.com/mttjhn/alfred-workflows/master/Other/Servers/Servers.alfredworkflow))
=====================

A quick way to connect to remote servers in macOS. I think I grabbed this workflow somewhere on [this Alfred thread](http://www.alfredforum.com/topic/180-connecting-to-remove-servers/), and what I've included here works great for my needs. I can't take any credit for this workflow; it was created by [@jdfwarrior](https://github.com/jdfwarrior) and uploaded to the Alfred forum. Just wanted a place where I could better link to the workflow file.

## Requirements
1. [Alfred App 2 or 3](http://www.alfredapp.com/#download)
1. [Alfred Powerpack](https://buy.alfredapp.com/)

## Commands
- `addserver <name> <path>`
    * Accepts the input and then splits it into an array based on <space> so it can grab the name and server values separately. It checks to see if servers.json exists. If so, adds the new entry to the servers list and writes it back to the json file. If the servers.json file doesn't exist, it makes a new array (the single, new server), and writes that to a new servers.json. Echos success.
- `srv`
    * Looks for the servers.json file. If it's there, it reads the file and formats the server list as xml for Alfred feedback. If the file doesn't exist, it returns a feedback item saying that no servers are available.

Example:

- `addserver file_server afp://127.0.0.1` - Adds a "bookmark" to a server with the name "file_server" so I can connect to it later.
- `srv` - Brings up a list of the bookmarks I have created. If I choose one, it connects to the server and mounts the share as a volume. Holding `cmd` when selecting an item from the list will delete it from my "bookmarks".

## Credits
- [@jdfwarrior](https://github.com/jdfwarrior) created this and I can take no credit for his work. If he had this maintained on GitHub somewhere, I'd link there. :)
