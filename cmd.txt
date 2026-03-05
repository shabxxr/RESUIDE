sort -k1 misc-access.log | awk -F'GET /' '{print $2}' | cut -d' ' -f1 | tr -d '\n'


7z e <filename>
python3 -m venv volatile
source volatile/bin/active
pip install volataility3
vol -f 
memory.raw windows.cmdline
strings <filename.raw> | grep schtasks
strings -el <filename.raw> | grep -i adobeupdater
strings -el <filename.raw> | grep -i artifact
vol -f memory.raw windows.envars

