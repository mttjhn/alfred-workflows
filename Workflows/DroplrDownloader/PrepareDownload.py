# encoding: utf-8

import sys
import subprocess
import os
from workflow import Workflow3, ICON_NETWORK, ICON_HOME, ICON_WARNING, ICON_ERROR, ICON_WEB, web

log = None
URL_CHECK = 'drops.mttjhn.com'

# This function gets the current clipboard contents (in text)
def getClipboard():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data

def getDroplrInfo(input):
    output = []

    r = web.get(input)

    # Check for errors!
    r.raise_for_status()

     # Parse the result!
    result = r.text

    if u'Droplr.dropProps' in result:
        # We have some JS from the page! Let's read it...
        # We'll start with the title!
        tS = result.find('title: ', result.find('Droplr.dropProps')) + 8
        tE = result.find('\'', tS)
        if tS > 0 and tE > 0:
            title = result[tS:tE]
            output.append(title)
            log.debug(title)
        # Now we'll get the file type
        fS = result.find('type: ', result.find('Droplr.dropProps')) + 7
        fE = result.find('\'', fS)
        if fS > 0 and fE > 0:
            fileType = result[fS:fE].lower()
            output.append(fileType)
            log.debug(fileType)

    return output

def main(wf):
    log.debug('Started!')
    # Get query from Alfred
    if len(wf.args):
        query = wf.args[0]
    else:
        query = None
    
    log.debug(query)
    # If the query is blank, grab the contents of the clipboard
    if query == None:
        query = getClipboard()

    log.debug(query)

    if query != None:
        # Start by trimming whitespace
        query = query.strip()
        # Let's process the URL now!
        if URL_CHECK in query:
            # Looks like we're ok to go ahead on this one.
            # TODO: Could do full URL parsing here, but this is probably good enough
            # We're already dealing with undocumented Droplr API anyways...
            output = getDroplrInfo(query)
            if len(output) > 0:
                # Looks like we found something!
                # Let's prepare the link...
                processItem = wf.add_item(title=u'Download {0} from Droplr'.format(output[1]),
                    subtitle=u'File name: {0}'.format(output[0]),
                    arg=query, 
                    icon=u'{0}.png'.format(output[1]),
                    valid=True)
            else:
                # Didn't find data, but we could still try the link!..
                processItem = wf.add_item(title=u'Download from Droplr',
                    subtitle=u'{0}'.format(query),
                    arg=query, 
                    icon=u'image.png',
                    valid=True)
            # Set the variable we're filtering for
            processItem.setvar(u'download', '1')
        else:
            invalidError = wf.add_item(title=u'Valid URL not found in clipboard!',
                subtitle=u'Please try again with a valid Droplr URL.',
                icon=ICON_ERROR,
                valid=False)

        # Send the results to Alfred as XML
        wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow3()
    log = wf.logger
    sys.exit(wf.run(main)) 