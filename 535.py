class Codec:

    def encode(self, longUrl: str) -> str:
        if longUrl[:8] == "https://":
            shorting = longUrl[8:]
            s=''
            for simv in shorting:
                s+=chr(ord(simv)+4)
            return ('https://'+s)
        else:
            if longUrl[:7] == "http://":
                shorting = longUrl[7:]
                s=''
                for simv in shorting:
                    s+=chr(ord(simv)+4)
                return ('http://'+s)
            else:
                shorting = longUrl[6:]
                s=''
                for simv in shorting:
                    s+=chr(ord(simv)+4)
                return ('ftp://'+s)
        

    def decode(self, shortUrl: str) -> str:
        if shortUrl[:8] == "https://":
            shorting = shortUrl[8:]
            s=''
            for simv in shorting:
                s+=chr(ord(simv)-4)
            return ('https://'+s)
        else:
            if shortUrl[:7] == "http://":
                shorting = shortUrl[7:]
                s=''
                for simv in shorting:
                    s+=chr(ord(simv)-4)
                return ('http://'+s)
            else:
                shorting = shortUrl[6:]
                s=''
                for simv in shorting:
                    s+=chr(ord(simv)-4)
                return ('ftp://'+s)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
