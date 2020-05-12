text = input()
words = text.split()
for word in words:
    # finish the code here
    if word[:7] == "http://" or word[:8] == "https://" or word[:4] == "www." or word[:7] == "HTTP://" or word[:8] == "HTTPS://" or word[:4] == "WWW.":
        print(word)
