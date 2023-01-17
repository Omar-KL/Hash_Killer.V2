import re
import hashlib
from time import sleep
import os
from colored import fg, bg
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


print(color6+"")
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
               
                                                                                 """"")
print("="*50)
print("Made it By Omar-KL")
print("Instagram: @1_k1e")
print("Youtube: https://www.youtube.com/@magician-teq")
print("Don't use it for Illegal Purposes.. ")
print("="*50)
print("")


hash_to_check = input(color1+"Enter the target hash: ")
wordlist_path = input(color1+"Enter the path to the wordlist file: ")

# Create a dictionary of hash functions
hash_functions = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha224": hashlib.sha224,
    "sha384": hashlib.sha384,
    "sha512": hashlib.sha512
}

# Regular expressions to match the hash against known patterns
hash_types = {
    "md5": r"^[a-f0-9]{32}$",
    "sha1": r"^[a-f0-9]{40}$",
    "sha256": r"^[a-f0-9]{64}$",
    "sha224": r"^[a-f0-9]{56}$",
    "sha384": r"^[a-f0-9]{96}$",
    "sha512": r"^[a-f0-9]{128}$"
}

# Iterate through each hash type in the hash_types dictionary
hash_found = False
for hash_type, regex in hash_types.items():
    # Check if the hash matches the regular expression for the current hash type
    if re.match(regex, hash_to_check):
        # Get the corresponding hash function from the hash_functions dictionary
        hash_function = hash_functions[hash_type]
        print(color8+"="*50)
        print(color11+"The hash is likely",color10+ hash_type.upper())


        try:
            # Open the wordlist
            with open(wordlist_path, "r", encoding='utf-8') as wordlist:
                # Iterate through each word in the wordlist
                for word in wordlist:
                    # Calculate the hash of the word
                    hash_word = hash_function(word.strip().encode('utf-8')).hexdigest()
                    # Compare the hash of the word to the target hash
                    if hash_word == hash_to_check:
                        print(color8+"="*50)
                        print(color11+"Found Matching Hash:",color10+ word.strip())
                        print(color8+"="*50)
                        hash_found = True
                        sleep(120)
            if not hash_found:
                print(color6+"="*50)
                print(color2+"No matching hash found.")
                print(color6+"="*50)
                sleep(20)
        except FileNotFoundError:
            print(color6+"="*50)
            print(color2+"Wordlist file not found.")
            print(color6+"="*50)
            sleep(20)
        except:
            print(color6+"="*50)
            print(color3+"An error occurred while reading the wordlist file.")
            print(color6+"="*50)
            sleep(20)
        break
else:
    print(color6+"="*50)
    print(color5+"The hash type could not be determined")
    print(color6+"="*50)
    sleep(20)
