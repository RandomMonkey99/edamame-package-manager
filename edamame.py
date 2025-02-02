import sys
import wget as wg
command = sys.argv[1]
args = sys.argv[2:]

if command == None:
    print("Welcome to edamame-package manager")
    print("Commands:")
    print("    get  : install a package or file from the web")
    print("    list : list all disponible packages")
    print("    add  : add a pac kage or file with a pr on github")

if command == "get":
    wg.download(f"https://")