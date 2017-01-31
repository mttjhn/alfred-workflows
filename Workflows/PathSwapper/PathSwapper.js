app = Application('System Events');
app.includeStandardAdditions = true;
myClip = app.theClipboard();

// IMPORTANT SETUP: Change this to adjust your default paths!
knownVolumes = [
    ['projects', '\\\\lindsey.cxusa.com\\projects'],
    ['applications', '\\\\lindsey.cxusa.com\\applications'],
    ['public', '\\\\lindsey.cxusa.com\\public']
];

knownSources = [
    ['\\\\lindsey.cxusa.com\\projects', 'projects'],
    ['\\\\lindsey\\projects', 'projects'],
    ['\\\\lindsey.cxusa.com\\applications', 'applications'],
    ['\\\\lindsey\\applications', 'applications']
    ['\\\\lindsey.cxusa.com\\public', 'public'],
    ['\\\\lindsey\\public', 'public']
];

// Set output to the clipboard, just in case the logic fails
output = myClip;

if(myClip.trim().length >= 3) {
    tempClip = myClip.trim();
    if (tempClip.substring(0, 1) === '\\') {
		volumeProcessed = false;
        // We likely have a windows path! Let's cross-reference it with our array above!
		sourceXref = searchSources(tempClip);
		if (sourceXref) {
            // We found something! Good, let's replace it in our path.
            output = searchReplace(tempClip.toLowerCase(), sourceXref[0].toLowerCase(), '/Volumes/' + sourceXref[1]);
            // And replace the rest of the slashes
            output = searchReplace(output, '\\', '/');
            volumeProcessed = true;
        }
		
		if (!volumeProcessed) {
		    output = searchReplace(tempClip, '\\', '/');
		}
		
		// Note that we could make this much simpler and just do an SMB path, but we won't.
		// output = 'smb:' + output;
    }
	else if (tempClip.substring(0, 1) === '/') {
		// We likely have a copied Mac path!
		volumeProcessed = false;
		pathContents = tempClip.split('/');
		// First, check if we have a /Volume/ (note that array begins with an empty result for some reason...)
		if (pathContents.length > 0 && pathContents[1].toLowerCase().trim() === 'volumes') {
		    // We have a /Volumes/ path! Let's figure out what volume.
			if (pathContents[2]) {
			    windowsPath = searchVolumes(pathContents[2].trim());
				if (windowsPath) {
				    //We got a windows path! Let's replace the Volumes stuff...
					output = searchReplace(tempClip, '/Volumes/' + pathContents[2], windowsPath);
					// And replace the rest of the slashes
					output = searchReplace(output, '/', '\\');
					volumeProcessed = true;
				}
			}
	    }
		// If we couldn't find anything, we'll just flip the slashes
		if (!volumeProcessed) {
		    output = searchReplace(tempClip, '/', '\\');
		}
	}
	else if(tempClip.substring(0, 3) === 'smb') {
	    output = searchReplace(tempClip, 'smb:', '');
		output = searchReplace(output, '/', '\\');
	}
}

console.log('Output: ' + output);
app.setTheClipboardTo(output);


// This function searches the knownVolumes collection for a volume with the given name and returns the Windows server-share
function searchVolumes(searchName) {
    // Searches the volumes collection and returns the Windows equivalent
	for (var i = 0; i < knownVolumes.length; i++) {
        if (knownVolumes[i]) {
		    match = knownVolumes[i];
			if (match[0] && match[0].toLowerCase() === searchName.toLowerCase()) {
			    return match[1];
			}
		}
    }
}

// This function searches the given path for a Windows server-share in the knownSources collection
function searchSources(searchPath) {
    // Searches the volumes collection for Windows paths and returns the Mac equivalent
	for (var i = 0; i < knownSources.length; i++) {
        if (knownSources[i]) {
		    match = knownSources[i];
			if (match[0] && searchPath.toLowerCase().indexOf(match[0].toLowerCase()) >= 0) {
			    return match;
			}
		}
    }
}

// This function replaces text
function searchReplace(text, search, replace) {
  replaced = text.split(search).join(replace);
  return replaced;
}
