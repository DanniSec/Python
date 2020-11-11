import os
import argparse
import time
import subprocess
import glob

global king
global flag
global kill
global spam


def main():

    parser = argparse.ArgumentParser(description='Auto KoTH help menu')

    group = parser.add_mutually_exclusive_group() 
    group.add_argument("-p", "--pts", action="store_true")
    group.add_argument("-n","--nyan", help="show nyancat to everyone" ,action="store_true")
    group.add_argument("-g","--get", help="installs nyancat", action="store_true")

    parser.add_argument("-f","--flag", type=str, help="[flag name] | (without .txt) mostly flags will be called flag.txt or root.txt" , metavar="")
    parser.add_argument("-k","--king", metavar="" , help="[Your THM nickname]" ,type=str)
    parser.add_argument("-K","--kill", metavar="", help="[PID of target]", type=int)
    parser.add_argument("-s","--spam", metavar="", help="[PTS NUMBER]", type=int)
    args = parser.parse_args()

    if args.get:
        os.system("git clone https://github.com/klange/nyancat.git && cd nyancat")
        time.sleep(1)
        os.system("make && cd src")
        time.sleep(1)
        os.system("chmod +x nyancat")
        if args.nyan:
            os.system("./nyancat | wall")

    #Currently working
    if args.kill:
        os.system(f"kill -9 {args.kill}")
        print(f"Successfully killed PID: {args.kill}")
    
    #Currently working    
    if args.spam:
       print(f"F@cking up terminal at pts/{args.spam} ...")
       os.system(f"cat /dev/urandom > /dev/pts/{args.spam}")
        
    #Currently working but some work still in progress
    if args.pts:
        os.system("ps aux | grep pts")
        PID = os.popen("echo $$").read()
        pts = os.popen("tty").read()
        print(f"\n Your PID: {PID}")
        print(f" Your pts: {pts}")

    #Currently working    
    if args.king:
        os.system(f"echo '{args.king}' > /root/king.txt")
        time.sleep(0.5)
        print("\nEdited successfully")    
        print(f"\nKing flag changed to:")
        os.system("cat /root/king.txt")
       
    elif args.flag:
        print(f"Found files with name '{args.flag}'")
        os.system(f"find / 2>/dev/null | grep {args.flag}")
        os.system(f"find / 2>/dev/null | grep {args.flag} > found_flag_paths.txt")

        print("\nChecking for actual flags...")

        #Doesnt skip unwanted paths - need fix
        df = "found_flag_paths.txt"

        with open(df, "r") as paths:
        	lines = paths.readlines()
		
        #blacklist
	class wrong_paths:	
        	path1 = glob.glob("/usr/share/**/src/cmd/go/testdata/script/test_flag.txt", recursive=True)
        	path2 = glob.glob("/usr/share/**/src/cmd/go/testdata/script/modfile_flag.txt", recursive=True)


        with open(df, "w") as paths:
        	for line in lines:
		    if line.strip("\n") != wrong_paths:
                        paths.write(line)

        
        print("Flags:")
        
        for flags_paths in lines:
            os.system(f"cat {flags_paths}")
        paths.close()


    else:
        print("To list all options use 'autokoth.py -h' ")

if __name__ == '__main__':
    main()
