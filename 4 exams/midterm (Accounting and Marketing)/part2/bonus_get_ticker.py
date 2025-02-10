import hashlib
import string


def propose_ticker(uni):
    sha1 = hashlib.sha1()
    sha1.update(str(uni).encode("ascii"))
    hexadecimal_code = sha1.hexdigest()
    letters = [c for c in hexadecimal_code if c in string.ascii_lowercase]
    uppercase = "".join(letters).upper()
    print("Your ticker code must include these letters: ",
          " ".join(uppercase[:3]))
    

if __name__ == "__main__":
    uni =input("Please enter your UNI: ")
    propose_ticker(uni)
