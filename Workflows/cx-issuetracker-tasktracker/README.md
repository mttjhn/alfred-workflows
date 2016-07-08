cx-issuetracker-tasktracker ([Download](https://raw.github.com/mttjhn/alfred-workflows/master/Workflows/cx-issuetracker-tasktracker/cx-issuetracker-tasktracker.alfredworkflow))
=====================

A quick way to search for Issues or Tasks in the Computronix IssueTracker or TaskTracker systems. Really only useful for staff at Computronix (or anyone logging an issue in our IssueTracker) system, but it simply uses a URL to search for an issue/task by number.

## Requirements
1. [Alfred App 2 or 3](http://www.alfredapp.com/#download)
1. [Alfred Powerpack](https://buy.alfredapp.com/)

## Commands
- `issue <number>`
    * Accepts only number input, and this command searches the CXUSA IssueTracker site.
- `issue-cx <number>`
    * Accepts only number input, and this command searches the Computronix IssueTracker site.
- `task <number>`
    * Accepts only number input, and this command searches the CXUSA TaskTracker site.
- `task-cx <number>`
    * Accepts only number input, and this command searches the Computronix TaskTracker site.

Example:

- `issue 8500` - Opens a URL in your default browser that will search for the given IssueTracker number and open it. If you're not logged into IssueTracker, you'll be presented with a logon screen.
- `task 10500` - Opens a URL in your default browser that will search for the given TaskTracker number and open it. If you're not logged into TaskTracker, you'll be presented with a logon screen.


## Contributors
- [@mttjhn](https://github.com/mttjn)