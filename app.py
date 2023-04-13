from classes import *
from langparser import *

tokens = parse("""
while(True)
{
    print("Yeeeeee");
    sleep(1);
}
print(Deneme);
""")

i = 0
for token in tokens:
    print(str(token))
    i += 1