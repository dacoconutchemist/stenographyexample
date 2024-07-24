'''
Simple module for stenography in plaintext using zero-width characters ZWJ (\u200d), ZWSP (\u200b) and ZWNJ (\u200c)
Normally not worth publishing because it's low-effort but I did publish it for a reason 🌚
'''

def encode(text, secret):
    chararray = [bin(ord(i))[2:].replace('0', '\u200c').replace('1', '\u200d') for i in secret]
    mid = len(text) // 2
    return text[:mid] + '\u200b' + '\u200b'.join(chararray) + '\u200b' + text[mid:]

def decode(text):
    binary = text[text.find('\u200b')+1 : text.rfind('\u200b')].split('\u200b')
    return ''.join(chr(int(i.replace('\u200c', '0').replace('\u200d', '1'), 2)) for i in binary)

if __name__ == '__main__':
    text = "hello world"
    secret = "secret here"

    encoded = encode(text, secret)
    print(encoded)

    print(decode(encoded))
