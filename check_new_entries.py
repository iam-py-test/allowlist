import argparse,sys,os,requests

parser = argparse.ArgumentParser()
parser.add_argument("url",help="The URL to download the allowlist from")
parser.add_argument("--file", help="A file to check against the allowlist")
parser.add_argument("--domain", help="A domain to check against the allowlist")
args = parser.parse_args()

domainstocheck = []

if args.file:
	filedomains = open(args.file).read().split("\n")
	for d in filedomains:
		if d == "" or d.startswith("#") or d.startswith("!"):
			continue
		domainstocheck.append(d)
if args.domain:
	domainstocheck.append(args.domain)

allowlist = requests.get(args.url).text.split("\n")
for d in domainstocheck:
	if d in allowlist:
		print(f"[in allowlist] {d}")
	else:
		print(f"[not in allowlist] {d}")
