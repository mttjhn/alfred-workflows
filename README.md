Alfred Workflows
=====================
A listing of the Alfred workflows that I have collected for regular use, including a few that I have put together myself. Maintained by [@mttjhn](https://github.com/mttjhn).

## Utilities

- [Knocktounlock App](https://github.com/saschaeggi/alfred-knocktounlock) (by [@saschaeggi](https://github.com/saschaeggi))
	* Interfaces with the excellent [Knock App](http://www.knocktounlock.com) to more easily lock your Mac. I use this many times each day to replace the default `lock` command in Alfred with the Knock equivalent.
- [Kill Process](https://github.com/ngreenstein/alfred-process-killer) (by [@ngreenstein](https://github.com/ngreenstein))
	* Very handy way to quit applications, especially those that don't show up in the usual app-switcher (`Cmd-Tab`).
- [Strip clipboard text formatting](https://github.com/notDavid/alfred-workflow-stripClipboardFormatting) (by [@notDavid](https://github.com/notDavid))
	* I get really frustrated when I copy formatting along with text that I want to paste into an email, and I really didn't know that the `Cmd+Alt+Shift+V` keyboard shortcut existed until someone recently showed me, *plus* it's a pain to type and I hear it doesn't always work. Anyways, this workflow provides a quick way to strip formatting from the clipboard and paste it directly where your cursor has focus. Soooo handy!
- [Command-C App](https://github.com/mttjhn/alfred-commandc-workflow) (by [@mttjhn](https://github.com/mttjhn))
	* I recently hacked together a quick workflow for the really cool [Command-C App](https://danilo.to), based primarily on [a workflow developed by Sayz Lim](http://sayzlim.net/command-c-alfred-workflow/). When the app isn't "spinning" (I think it's trying to find my iPhone), the workflow is great. I still would like to update it to allow for sending stuff to different devices, etc. But since I only have one iPhone, I think that can wait.
	* __Update:__ now that Apple has effectively "sherlocked" Command-C with their new [Universal Clipboard](http://appleinsider.com/articles/16/06/15/universal-clipboard-for-macos-sierra-ios-10-streamlines-copypaste-between-devices) feature in macOS Sierra, this will probably hit the trash bin soon.
- [Homebrew & Cask](https://github.com/fniephaus/alfred-homebrew) (by [@fniephaus](https://github.com/fniephaus))
	* Just discovered this excellent Alfred workflow that allows you to control Homebrew simply by typing the `brew` command, complete with searching, outdated packages, etc. Very handy if you use [Homebrew](http://brew.sh) and want the tools at your fingertips via Alfred.
- [Path Swapper](https://github.com/mttjhn/alfred-workflows/tree/master/Workflows/PathSwapper) (by [@mttjhn](https://github.com/mttjhn))
	* A handy workflow that attempts to convert between Windows UNC paths and "macOS-style" paths, to make life easier for both loading remote files from emails with UNC paths, and for writing emails to coworkers with Windows computers.
- [Droplr Downloader](https://github.com/mttjhn/alfred-workflows/tree/master/Workflows/DroplrDownloader) (by [@mttjhn](https://github.com/mttjhn))
	* I built this workflow to help automate the process of downloading a screenshot/screencast from Droplr. Handy for those times when you want to attach a file to an email, instead of inserting a Droplr link. In conjunction with a folder watched by [Hazel](https://www.noodlesoft.com), this makes it easy to get at my screenshots without cluttering the Downloads folder or my Desktop.

## Programming

- [Open with Sublime Text](https://github.com/franzheidl/alfred-workflows/tree/master/open-with-sublime-text-2) (by [@franzheidl](https://github.com/franzheidl))
	* It's similar to choosing open with when browsing folders/files with Alfred, but I like the ability to type `subl` in Alfred to open the file/folder that's currently selected in Finder. And the `subl*` concept is a tad quicker, too.
	* _Note to self: it would be good to check out some of the other "Open with..." workflows in [@franzheidl's](https://github.com/franzheidl) repo._
- [Encode / Decode](https://github.com/willfarrell/alfred-encode-decode-workflow) by ([@willfarrell](https://github.com/willfarrell))
	* Really handy when you need to figure out what something is in XML or URL encoding without having to look it up. Also does base64 encoding.
- [Dash](https://github.com/Kapeli/Dash-Alfred-Workflow) (by [@Kapeli](https://github.com/Kapeli))
	* The official Alfred workflow for the excellent [Dash](https://kapeli.com/dash), a very cool offline documentation tool for Mac OSX. I've found that the Alfred workflow sometimes it gets in the way of what I'm trying to do (e.g. Google something about `bash`, and instead Alfred starts searching Dash for documentation). Otherwise, a cool and handy workflow. Might want to look for something different because of the challenges mentioned above.
- [Alfred Gist](https://github.com/phallstrom/AlfredGist) (by [@phallstrom](https://github.com/phallstrom))
    * I like using [GitHub gists](https://help.github.com/articles/about-gists/) for sharing snippets of code with my coworkers/friends. This workflow makes it easy to use a file in Alfred (or from whatever code I have on my clipboard) to quickly create a GitHub Gist with a given name and file type. 

## Productivity

- [Doing](https://github.com/EvanLovely/alfred--doing) (by [@EvanLovely](https://github.com/EvanLovely))
	* Just recently saw a post from [@ttscoff](https://github.com/ttscoff) about [doing](https://github.com/ttscoff/doing), his CLI tool for time tracking and just keeping track of what he was last doing. For me, time tracking has become a bit of a chore because I forget what I did all day long, especially with the many interruptions at work. This workflow leverages the `doing` command to make it easier to keep a running log of what I was doing just now so that I can jog my memory later when I have to enter my time at work.
	* _Note that I had to hack this workflow a bit to get it running with my non-system installed version of ruby. See [this issue logged to the workflow on GitHub](https://github.com/EvanLovely/alfred--doing/issues/1) for details._
- [Slackfred](https://github.com/fspinillo/slackfred) (by [@fspinillo](https://github.com/fspinillo))
	* Recently started using [Slack](https://slack.com) at work, and I really like it. This workflow provides the command `slk` to jump to a specific channel or DM a person, plus there are a number of other commands that I haven't tried yet to do other things like searching, setting your presence, and even clear unread messages. Cool!
- [Calendar](https://github.com/owenwater/alfred-cal) (by [@owenwater](https://github.com/owenwater))
    * One of the common things I need to look at is a tiny "month calendar" in order to quickly answer questions like "What day of the month is next Tuesday?", or "What day of the week is July 12?". This workflow makes it really easy to type `cal July` and have a visual calendar pop up where I can see everything at a glance. Bonus feature is that I can select any of the "weeks" in the calendar and hit enter to open that week in the macOS Calendar app.
- [Servers](https://github.com/mttjhn/alfred-workflows/tree/master/Workflows/Servers) (by [@jdfwarrior](https://github.com/jdfwarrior))
	* Maintains a list of "bookmarks" to remote servers, allowing you to connect to servers by simply using a quick `srv` command. Very handy for those times when I need to quickly get to a project folder on the network at work.
	* I still can't remember exactly where I found this one, but there isn't a repo on GitHub or some other site for it. I'm pretty sure it had something to do with [this Alfred thread](http://www.alfredforum.com/topic/180-connecting-to-remove-servers/). Just so that others can use it, I've uploaded the workflow and a description to this repository.
- [IssueTracker and TaskTracker Search](https://github.com/mttjhn/alfred-workflows/tree/master/Workflows/cx-issuetracker-tasktracker) (by [@mttjhn](https://github.com/mttjhn))
    * After recently having to look up a bunch of Issues in my company's internal issue tracking system for a client project, I thought I'd make a quick workflow that navigates to a URL in order to search for an Issue by number. I added support for our task tracking system as well. For now, really simple, but there's room for some improvement.

## Media

- [Rate iTunes Track](https://github.com/dklem/Alfred2-Rate-iTunes-Track) (by [@dklem](https://github.com/dklem))
    * Recently, I've started making some smart playlists in iTunes to "rediscover" older music that I haven't listened to in a long time. Every so often I come across a track I like/dislike, and I want to rate that track without stopping what I'm doing. This handy Alfred workflow makes it simple. I just type `rate <number>` with the rating between 1-5, including half-stars (e.g. `rate 4.5`). A notification pops up to say that it rated the song with the given number of stars. Very nice.