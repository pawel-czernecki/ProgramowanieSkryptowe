import sys
import importlib

if sys.argv[1] == "cut":
    cut = importlib.import_module("cut")
    cut.cutWithParserDecorator(sys.argv[2:])
elif sys.argv[1] == "grep":
    grep = importlib.import_module("grep")
    grep.grepWithParserDecorator(sys.argv[2:])
else:
    print("Nieznana komenda")

# py .\skrypt2.py cut -d : -f 1,10,9,8,1,6 root:x:0:0:root:/root:/bin/bash bin:x:1:1:bin:/bin:/sbin/nologin daemon:x:2:2:daemon:/sbin:/sbin/nologi

# py .\skrypt2.py grep bin /usr/sbin/nologin /bin/sync /BIN/
# py .\skrypt2.py grep -i bin /usr/sbin/nologin /bin/sync /BIN/
# py .\skrypt2.py grep -w bin /usr/sbin/nologin /bin/sync /BIN/
# py .\skrypt2.py grep -i -w bin /usr/sbin/nologin /bin/sync /BIN/