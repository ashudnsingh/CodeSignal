def stolenLunch(note):
    return "".join([str(ord(i)-97) if 96<ord(i)<107 else chr(int(i)+97) if 47<ord(i)<58 else i for i in note])
