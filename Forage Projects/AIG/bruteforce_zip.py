'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile

# Use a method to attempt to extract the zip file with a given password
# def attempt_extract(zf_handle, password):
#     
#
#

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            # Write your logic here...
            # Iterate through password entries in rockyou.txt

            # Attempt to extract the zip file using each password

            # Handle correct password extract versus incorrect password attempt)

    #print("[+] Password not found in list")
  
from zipfile import ZipFile
# Use a method to attempt to extract the zip file with a given password
# def attempt_extract(zf_handle, password):
# 
#
#

from zipfile import ZipFile
# Use a method to attempt to extract the zip file with a given password
def main():
  print("[+] Begnning bruteforce")
  with ZipFile('enc.zip') as zf:
    with open('sample_data/rockyou.txt', 'rb') as f:
      for password in f:
        password - password.strip() # Already in bytes
        try:
          zf.extractall(pwd=password)
          print("[+] Password found: {password.decode()}")
          break
        except:
          print(f"[-] Failed attempt: {password.decode(errors='ignore')}")
  if __name__ == "__main__":
    main()

# Sample Code
from zipfile import ZipFile

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except:
        return False

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for p in f:
                password = p.strip()
                if attempt_extract(zf, password):
                    print("[+] Correct password: %s" % password)
                    exit(0)
                else:
                    print("[-] Incorrect password: %s" % password)

    print("[+] Password not found in list")

if __name__ == "__main__":
    main()
