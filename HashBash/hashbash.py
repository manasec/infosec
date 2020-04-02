import hashlib
import sys
import os
from hashid import HashID

class HashBash:

    def dumphash(self, hashString, passwd):
        issolved = False
        hashdumpfile = open('hashdump.txt', 'a+')
        for ahash in hashdumpfile:
            if hashString in ahash.split(":")[1].strip():
                issolved = True
        if issolved is False:
            print ("Hash saved to hashdump.txt")
            hashdumpfile.write('%s:{}'.format(hashString) % passwd)
            hashdumpfile.write('\n')
        hashdumpfile.close()

    def hashidentify(self,hashString):
        print("\n\n\nusing 'hashID' by @psypanda to detect the hash")
        print("the hashtype is not supported but it looks like it is:::\n")
        hashID = HashID()
        outfile=sys.stdout

        g1=hashID.identifyHash(hashString)
        while True:
            try:
                outfile.write(str(next(g1)))
                print("")
            except StopIteration:
                break


    def hashBashWordlist(self, hashString, hashtype, wordlist, verbose):
        
        issolved = False
        if "md5" in hashtype:
            h = hashlib.md5
        elif "sha1" in hashtype:
            h = hashlib.sha1
        elif "sha224" in hashtype:
            h = hashlib.sha224
        elif "sha256" in hashtype:
            h = hashlib.sha256
        elif "sha384" in hashtype:
            h = hashlib.sha384
        elif "sha512" in hashtype:
            h = hashlib.sha512
        else:
            print ("\n%s is not a supported hash (md5, sha1, sha224, sha256, sha384, sha512) "% hashtype)
            self.hashidentify(hashString)
            exit(0)
        
        
        with open(wordlist, "r") as wordlist:
            for passwd in wordlist:
                passwd = passwd.strip()
                passhash = h(passwd.encode()).hexdigest()
                if verbose.lower() =='y':
                    sys.stdout.write('\r' + str(passhash) + ' ' * 20)
                    sys.stdout.flush()
                if str(passhash) == str(hashString.lower()):
                        
                    print ("\nHash is: %s" % passwd)
                    self.dumphash(passhash, passwd)
                    
                    break
                    
            else:
                print ("Reached end of wordlist")

def main():
    print("--------------...Welcome to hashbash...-----------------")
    print("Author: manasec")
    print("supported hashes- md5, sha1, sha224, sha256, sha384, sha512")
    hashtype = input("hash type:")
    hashString = input("hash:")
    wordlist = input("wordlist ? type 0 for default wordlist:")
    verbose = input("wanna see the logs?")
    
    

    # looks through saved hash file instead of hashing all Wordlist entries
    with open('hashdump.txt', 'a+') as hashdumpfile:
        for ahash in hashdumpfile:
            ahash = ahash.split(":")
            if hashString.lower() == ahash[1].strip():
                print ("\nSaved Hash is: %s" % ahash[0])
                exit()
        else:
            
            print ("\ntrying to Crack %s of type %s with wordlist %s"% (hashString,hashtype,wordlist))
            try:
                h = HashBash()
                h.hashBashWordlist(hashString, hashtype, wordlist, verbose)

            except IndexError:
                
                print ("Reached end of wordlist")
                

            except KeyboardInterrupt:
                print ("keeyboard interrupt")

            
if __name__=='__main__':
    main()


