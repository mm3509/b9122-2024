import string
import datetime
import hashlib
import os
import pathlib
import uuid
from requests import get
import subprocess
import sys


RECIPIENT = "mm3509"
RESET_UNI ="reset-uni"
ARGS = [
    RESET_UNI
]


UNI_FILE = ".uni.txt"

MACOS = "macOS"
WINDOWS = "windows"
LINUX = "linux"
OS = MACOS

if "darwin" == sys.platform:
    OS = MACOS
elif sys.platform in ["linux", "linux2"]:
    OS = LINUX
elif sys.platform.startswith("win"):
    OS = WINDOWS
else:
    print("Unknown Operating System, defaulting to macOS")


def get_uni():
    
    if os.path.exists(UNI_FILE):
        with open(UNI_FILE) as f:
            uni = f.read(-1).strip()

        if uni:
            return uni
        
    uni = ""
    while not uni:
        uni = input("Please enter your UNI: ").strip()
        if "" == uni:
            print("You didn't enter anything. Please enter your UNI.")
        
    with open(UNI_FILE, "w+") as f:
        f.write(uni)
    return uni


def get_ip():
    return get('https://api.ipify.org').content.decode('utf8')


def print_version():
    fp = ".version.txt"
    if not os.path.exists(fp):
        print("No version defined")
        return

    with open(fp) as f:
        version = f.read().strip()

    msg = "*" * 20
    msg += "\n" * 2
    msg += "Success! You did well. Software version: " + version
    msg += "\n" * 2
    msg += "*" * 20
    print(msg)


def get_salt():
    fp = ".salt.txt"
    if not os.path.exists(fp):
        salt = str(uuid.uuid4()).split("-")[0]
        with open(fp, "w+") as f:
            f.write(salt)
        return salt

    with open(fp) as f:
        return f.read(-1).strip()


def get_time():
    return datetime.datetime.now().strftime("%H:%M:%y%m%d")


def generate_hashcode(fields):
    sha1 = hashlib.sha1()
    sha1.update("".join(fields).encode("ascii"))
    return sha1.hexdigest()
    

def mark_attendance(class_code=None):

    # VS Code does not run this file from its directory, so change dir.
    current_dir = pathlib.Path(__file__).resolve().parent
    os.chdir(str(current_dir))
    
    print_version()

    if 5 != datetime.datetime.today().weekday():
        print("You have the right software and you can run this, but you'll" +
              " need to be in class to validate it")
        #return
    
    uni = get_uni()
    ip_address = get_ip()
    mac_address = str(uuid.getnode())
    salt = get_salt()
    timestamp = get_time()

    while True:
        class_code = input("Please enter the classroom code: ")
        if 4 == len(class_code) and all(c in string.ascii_letters + string.digits for c in class_code):
            break
        print("Class code should be 4 characters, please try again")

    specs = [uni, ip_address, mac_address, salt, timestamp, class_code]
    hashcode = generate_hashcode(specs)
    specs.append(hashcode)
    body = "_".join(specs)

    link = ("mailto:%s@columbia.edu?" +
            "subject=Attendance&body=%s") % (RECIPIENT, body)
    print(link)

    if MACOS == OS:
        cmd = "open '%s'"
    elif WINDOWS == OS:
        cmd = 'start "" "%s"'
    elif LINUX == OS:
        cmd = "xdg-open '%s'"
    else:
        assert False, "Unknown OS!"

    try:
        subprocess.check_output(cmd % link, shell=True)
    except subprocess.CalledProcessError:
        print("*" * 20)
        print()
        print("Unable to start a new email, please send manually.")
        print()
        print("*" * 20)


    print("If the email did not open, please send an email with subject" +
          " 'Attendance' and a single line in the body of the email " +
          " to %s@columbia.edu:" % RECIPIENT)
    print("-" * 10)
    print(body)
    print("-" * 10)                                


def main():
    args = sys.argv[1:]
    error_msg = ("This code takes at most one argument from the" +
                 " following list: " + ",".join(ARGS))
    if 1 < len(args):
        raise ValueError(error_msg)

    if 1 == len(args):
        arg = args[0]
        if arg not in ARGS:
            raise ValueError(error_msg)

        if RESET_UNI == arg and os.path.exists(UNI_FILE):
            os.unlink(UNI_FILE)

    mark_attendance()


if "__main__" == __name__:
    main()
