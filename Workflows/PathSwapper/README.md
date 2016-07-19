Path Swapper ([Download](https://raw.github.com/mttjhn/alfred-workflows/master/Workflows/PathSwapper/PathSwapper.alfredworkflow))
=====================

This is a quick workflow to convert Mac paths to Windows paths and vice versa. For those who work in a Windows environment and often need to "translate" a mounted directory path (e.g. `/Volumes/projects/etc`) to a more friendly Windows UNC path. This workflow can either work file action or from data on the clipboard. To use, simply browse to a file using Alfred and choose the `Paste Windows Path` option to convert the file's path to a UNC path and paste it, or copy the text you'd like to transform (either from UNC/Windows or Mac) and activate Alfred, using the `pathswap` keyword, and your clipboard will be converted, and the result pasted into the active application.

## Requirements
1. [Alfred App 2 or 3](http://www.alfredapp.com/#download)
1. [Alfred Powerpack](https://buy.alfredapp.com/)

## Commands
- `pathswap`
    * Converts the current clipboard contents from a Windows (UNC) path to a Mac path (based on a predefined list of "known" Volumes), or from a Mac "Volume-style" or SMB path back into a Windows (UNC) path. For example, `\\server\share\folder` would result in `/Volumes/share/folder`. Similarly, `smb://server/share/folder/` would translate back to `\\server\share\folder\` as well. 
    * The "volume mappings" are stored in a script in the workflow in a Javascript array. You have to edit those entries to something that makes sense for your common mounted network locations.

## Contributors
- [@mttjhn](https://github.com/mttjhn)
