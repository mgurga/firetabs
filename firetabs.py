
import argparse, json, os, lz4.block
from pathlib import Path

parser = argparse.ArgumentParser(description="Gets tab information from Firefox 55+", formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument("-p", "--profile-folder", type=str, required=True, help="name of your firefox profile folder eg. 'gyr074sk.default-esr'")
parser.add_argument("-m", "--home-folder", type=str, help="your home folder (might have to change on windows) eg. '/home/demouser' (default: %(default)s)", default=str(Path.home()))
parser.add_argument("-o", "--only-pinned-tabs", help="only return pinned tabs (default: %(default)s)", action='store_true')
parser.add_argument("-s", "--split-string", type=str, help="the string that goes at the end of each line eg. ',' (default: newline)", default="\n")
parser.add_argument("-b", "--begin-tab", type=int, help="start printing tabs after this tab number, inclusive (default: %(default)s)", default=0)
parser.add_argument("-e", "--end-tab", type=int, help="stop printing tabs after this tab number, inclusive (default: end of tabs)", default=None)
parser.add_argument(
	"-f", "--line-format", 
	type=str, 
	help=
	"""how to format an output line\n
/t = title of tab eg. 'YouTube'
/u = url of tab eg. 'https://docs.python.org/3/library/argparse.html'
/i = tab number eg. 1
/b = base64 favicon image eg. 'data:image/png;base64,iVBO...'
/p = if the tab is pinned eg. true
/h = if the tab is hidden eg. false
(default: %(default)s)""",
	default="/t @ /u"
)

args = parser.parse_args()

jsonrecoverypath = "/.mozilla/firefox/" + args.profile_folder + "/sessionstore-backups/recovery.jsonlz4"

try:
	jsonrecovery = open(args.home_folder + jsonrecoverypath, "rb")
except FileNotFoundError:
	print("recovery.jsonlz4 does not exist")
magic = jsonrecovery.read(8)
jdata = json.loads(lz4.block.decompress(jsonrecovery.read()).decode("utf-8"))
jsonrecovery.close()

def formatoutput(tabdata, tabindex, tabnum):
	out = args.line_format

	if "pinned" in tabdata:
		out = out.replace("/t", "")
		out = out.replace("/p", "true")
	else:
		out = out.replace("/t", tabdata["entries"][tabindex]["title"])
		out = out.replace("/p", "false")

	if "hidden" in tabdata == True:
		out = out.replace("/h", "true")
	else:
		out = out.replace("/h", "false")

	out = out.replace("/u", tabdata["entries"][tabindex]["url"])
	out = out.replace("/i", str(tabnum))
	out = out.replace("/b", tabdata["image"])

	return out

for win in jdata["windows"]:
	tabnum = 0
	if args.end_tab == None:
		args.end_tab = len(win["tabs"])
	for tab in win["tabs"]:
		i = int(tab["index"]) - 1
		url = tab["entries"][i]["url"]
		outstring = formatoutput(tab, i, tabnum)

		if tabnum >= args.begin_tab and tabnum <= args.end_tab:
			if "pinned" in tab and args.only_pinned_tabs == True:
				print(outstring + args.split_string)
			elif args.only_pinned_tabs == False:
				print(outstring + args.split_string)

		tabnum = tabnum + 1
