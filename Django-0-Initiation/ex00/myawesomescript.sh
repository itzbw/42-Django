#/bin/sh

#checks if the first command-line argument ($1) is empty (-z)
if [ -z "$1" ]; then
    echo "Need Args: $0 <bit.ly URL>"
    exit 1
fi 

#if there are args
#only the headers (-I) of the URL provided as an argument ($1), following redirects (-L) silently (-s)
#then Extracts the second field after splitting on spaces
#the final URL after following redirects

curl -sIl $1 | grep Location | cut -d ' ' -f 2
# curl -si -X GET $1 | grep "href" | cut -d \" -f 2