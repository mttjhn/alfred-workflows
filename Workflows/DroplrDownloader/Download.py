import os
import sys
import urllib2

DOWNLOAD_PATH = '/Users/matthew/Temp/Screenshots/'
URL_CHECK = 'drops.mttjhn.com'

# Function to get the next file name in the folder
def getNextFileName(extension, type):
    # Set up the file name template
    template = 'Screenshot'
    if type == 'screencast':
        template = 'Screencast'
    elif type == 'file':
        template = 'File'
    # Loop through the files and look for the next number
    i = 1
    while os.path.exists(os.path.join(DOWNLOAD_PATH, '{0}{1:03d}.{2}'.format(template, i, extension))):
        i += 1
    return os.path.join(DOWNLOAD_PATH, '{0}{1:03d}.{2}'.format(template, i, extension))

def downloadFile():
    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        query = None
    if URL_CHECK in query:
        url = query + '+'
        response = urllib2.urlopen(url)
        # Parse URL for the file extension
        returnUrl = response.geturl()
        if 'filename=' in returnUrl:
            # Looks like there's a filename in the return URL!
            nS = returnUrl.find('filename=')+9
            nE = returnUrl.find('&', nS)
            urlFileName = urllib2.unquote(returnUrl[nS:nE])
            eS = urlFileName.rfind('.') + 1
            extension = urlFileName[eS:]
            # Let's infer the type from the name
            type = ''
            # Check to see if it's a screencast
            if 'Capture' in urlFileName:
                type = 'screencast'
            elif 'Shot' not in urlFileName:
                type = 'file'
        else:
            # If we can't get the file name, assume it's a PNG
            extension = 'png'
            type = ''
        fileName = getNextFileName(extension, type)
        with open(fileName, 'wr') as file:
            file.write(response.read())

# Run the file download method!
downloadFile()