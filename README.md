# firetabs
Gets tab information from Firefox 55+

Small script to automate getting tabs from firefox's recovery file stored in ```~/.mozilla/firefox/*your profile*/sessionstore-backups/recovery.jsonlz4```
json data is compressed with lz4 compression. While I was doing this I decided to add some formatting options and extra customizations. Code is very simple
and easy to edit, good luck!

## Help
```
usage: firetabs [-h] -p PROFILE_FOLDER [-m HOME_FOLDER] [-o] [-s SPLIT_STRING] [-b BEGIN_TAB] [-e END_TAB] [-f LINE_FORMAT]

Gets tab information from Firefox 55+

optional arguments:
  -h, --help            show this help message and exit
  -p PROFILE_FOLDER, --profile-folder PROFILE_FOLDER
                        name of your firefox profile folder eg. 'gyr074sk.default-esr'
  -m HOME_FOLDER, --home-folder HOME_FOLDER
                        your home folder (might have to change on windows) eg. '/home/demouser' (default: *your home directory*)
  -o, --only-pinned-tabs
                        only return pinned tabs (default: False)
  -s SPLIT_STRING, --split-string SPLIT_STRING
                        the string that goes at the end of each line eg. ',' (default: newline)
  -b BEGIN_TAB, --begin-tab BEGIN_TAB
                        start printing tabs after this tab number, inclusive (default: 0)
  -e END_TAB, --end-tab END_TAB
                        stop printing tabs after this tab number, inclusive (default: end of tabs)
  -f LINE_FORMAT, --line-format LINE_FORMAT
                        how to format an output line
                        
                        /t = title of tab eg. 'YouTube'
                        /u = url of tab eg. 'https://docs.python.org/3/library/argparse.html'
                        /i = tab number eg. 1
                        /b = base64 favicon image eg. 'data:image/png;base64,iVBO...'
                        /p = if the tab is pinned eg. true
                        /h = if the tab is hidden eg. false
                        (default: /t @ /u)
```

## Troubleshooting / Common Problems
- It takes too long to update tabs / not updating at all
  - Goto about:config on firefox and edit ```browser.sessionstore.interval``` to be lower, default should be 10000
