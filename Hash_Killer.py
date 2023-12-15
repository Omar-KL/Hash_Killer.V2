import re
import hashlib
from colored import fg, bg
import base64
import os

color1 = fg(196)
color2 = fg(20)
color3 = fg(200)
color4 = fg(2)
color5 = fg(11)
color6 = bg(16)
color7 = fg(52)
color8 = fg(11)
color9 = fg(165)
color10 = fg(33)
color11 = fg(92)
color12 = fg(14)
color13 = fg(15)

print(color6 + "")
print(color9 + """                       
██   ██  █████  ███████ ██   ██                    
██   ██ ██   ██ ██      ██   ██                    
███████ ███████ ███████ ███████                    
██   ██ ██   ██      ██ ██   ██                    
██   ██ ██   ██ ███████ ██   ██                    

                ██   ██ ██ ██      ██      ███████ ██████  
                ██  ██  ██ ██      ██      ██      ██   ██ 
                █████   ██ ██      ██      █████   ██████  
                ██  ██  ██ ██      ██      ██      ██   ██ 
                ██   ██ ██ ███████ ███████ ███████ ██   ██                                             

""")
print("=" * 50)
print("Made it By Omar-KL")
print("Instagram: @1_k1e")
print("Youtube: https://www.youtube.com/@magician-teq")
print("Don't use it for Illegal Purposes.. ")
print("=" * 50)

print(color12 + "[1] " + color13 + "Crack All Types Of Hashes.")
print(color12 + "[2] " + color13 + "Generate Hash.")
print(color9 + "=" * 50)

choice = input(color12 + "[+] " + color13 + "Enter Your choice: ")

if choice == "1":
    try:
        hash_functions = {
            "md5": hashlib.md5,
            "sha1": hashlib.sha1,
            "sha256": hashlib.sha256,
            "sha224": hashlib.sha224,
            "sha384": hashlib.sha384,
            "sha512": hashlib.sha512
        }

        hash_types = {
            "md5": r"^[a-f0-9]{32}$",
            "sha1": r"^[a-f0-9]{40}$",
            "sha256": r"^[a-f0-9]{64}$",
            "sha224": r"^[a-f0-9]{56}$",
            "sha384": r"^[a-f0-9]{96}$",
            "sha512": r"^[a-f0-9]{128}$"
        }

        hash_to_check = input(color1 + "[*] Enter target hash: ")
        wordlist_path = input(color1 + "[*] Enter the path to the wordlist file: ")

        hash_found = False
        for hash_type, regex in hash_types.items():
            if re.match(regex, hash_to_check):
                hash_function = hash_functions[hash_type]
                print(color8 + "=" * 50)
                print(color11 + "The hash is likely", color10 + hash_type.upper())
                try:
                    with open(wordlist_path, "r", encoding='utf-8') as wordlist:
                        for word in wordlist:
                            hash_word = hash_function(word.strip().encode('utf-8')).hexdigest()
                            if hash_word == hash_to_check:
                                print(color8 + "=" * 50)
                                print(color11 + "Found Matching Hash:", color10 + word.strip())
                                print(color8 + "=" * 50)
                                hash_found = True
                                break

                        if not hash_found:
                            print(color2 + "No matching hash found.")
                            print(color6 + "=" * 50)

                except FileNotFoundError:
                    print(color2 + "Wordlist file not found.")
                    print(color6 + "=" * 50)

                except PermissionError:
                    print(color2 + "File Permission denied.")
                    print(color6 + "=" * 50)

                except IOError as e:
                    print("Error: ", e)

                except Exception as e:
                    print("Error: ", e)

    except Exception as e:
        print("Error: ", e)

elif choice == "2":
    print(color12 + "[1] " + color13 + "Salted Hash.. ")
    print(color12 + "[2] " + color13 + "UnSalted Hash.. ")
    Saltchoice = input(color12 + "[+] " + color13 + "Select Your Choice: ")

    if Saltchoice == '1':
      try:
        def generate_salt(length=16):
          random_bytes = os.urandom(length)
          salt = base64.b64encode(random_bytes).decode("utf-8")
          return salt[:length]


        salt = generate_salt()

        hash_word = input(color12 + "[+] " + color13 + "Enter your Word To Generate Hash: ")
        hash_word_encoded = hash_word.encode("utf-8")
        hash_type = input(color12 + "[+] " + color13 + "Enter Hash type EX:(md5, sha-1, sha-224..etc): ")

        hash_Functions = {
          "md5": hashlib.md5,
          "sha-1": hashlib.sha1,
          "sha-224": hashlib.sha224,
          "sha-256": hashlib.sha256,
          "sha-384": hashlib.sha384,
          "sha-512": hashlib.sha512,
        }

        try:
          def combine_salt_and_word(salt, word):
            return salt + word


          hash_function = hash_Functions[hash_type]
          combined_string = combine_salt_and_word(salt, hash_word_encoded.decode('utf-8'))
          salted_hash = hash_function(combined_string.encode('utf-8')).hexdigest()

          print("=" * 50)
          print(color9 + f"Generated salt: {salt}")
          print(color9 + "Salted Hash : " + color12 + salted_hash)
          print("=" * 50)

        except KeyError:
          print("Unsupported hash type..")

      except Exception as e:
        print("Error: ", e)


    elif Saltchoice == '2':
        try:
            hash_word = input(color12 + "[+] " + color13 + "Enter your Word To Generate Hash: ").encode('utf-8')
            hash_type = input(color12 + "[+] " + color13 + "Enter Hash type EX:(md5, sha-1, sha-224..etc): ")

            hash_Functions = {
                "md5": hashlib.md5,
                "sha-1": hashlib.sha1,
                "sha-224": hashlib.sha224,
                "sha-255": hashlib.sha256,
                "sha-384": hashlib.sha384,
                "sha-512": hashlib.sha512,
            }

            try:
                hash_function = hash_Functions[hash_type]
                hash_gen = hash_function(hash_word).hexdigest()
                print("=" * 50)
                print(color9 + "Your hash: " + color12 + hash_gen)
                print("=" * 50)

            except KeyError:
                print("Unsupported hash type..")

            except Exception as e:
                print("Error: ", e)

        except Exception as e:
            print("Error: ", e)

    else:
        print("Invalid Choice, try again..")
