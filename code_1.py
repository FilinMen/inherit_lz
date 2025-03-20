'''class CaesarCipper:

    def __init__(self,input_text,shift):
        self.input_text = input_text
        self.shift = int(shift)

    def encrypt(self):
'''
encr = []
text_spl = []

text = input()
shift = 3
for i in text: # идем по строке"self.input_text"text
    text_spl.append(i) # добавляем буквы в список 
for i in text_spl:
    num_ascii_ord = ord(i)
    print("ord",num_ascii_ord)
    shi= int(num_ascii_ord) + shift
    if shi >= 123:
        num = shi - 122
        num_2 = 96 + num
        num_ascii_chr = chr(num_2)
        encr.append(num_ascii_chr)
    elif shi >= 91:
        num = shi - 90
        num_2 = 64 + num
        num_ascii_chr = chr(num_2)
        encr.append(num_ascii_chr)
    else:
        num_ascii_chr = chr(shi)
        print("ord",num_ascii_chr)
        encr.append(num_ascii_chr)
        #надо объеденить список из отдельных элементов


