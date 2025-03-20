class CaesarCipper:

    def __init__(self,input_text,shift):
        self.text = input_text
        self.shift = int(shift)

    def encrypt(self):

        encr = [] #шифрованный текст поэлементно 
        text_spl = [] #разбиение текста на элементы

        for i in self.text:# разделение текста на отдельные буквы
            text_spl.append(i) # добавляем буквы в список 
        self.len = len(text_spl)
        for i in text_spl: #перевод букв в ascii и сдвигаем алфавит на значение shift
            num_ascii_ord = ord(i)
            shi= int(num_ascii_ord) + self.shift
            if shi >= 97:
                if shi >= 123:
                    num = shi - 122
                    num_2 = 96 + num
                    num_ascii_chr = chr(num_2)
                    encr.append(num_ascii_chr)
                else:
                    num_ascii_chr = chr(shi)
                    encr.append(num_ascii_chr)  
            elif shi >= 91:
                num = shi - 90
                num_2 = 64 + num
                num_ascii_chr = chr(num_2)
                encr.append(num_ascii_chr)
            else:
                num_ascii_chr = chr(shi)
                encr.append(num_ascii_chr)    
        
        self.final_encr = "".join(encr) #encrypt word
        print("Шифровка",self.final_encr)



    def decrypt(self):

        shift_decr = self.shift * (-1) #shift для дешифровки
        decr_text = [] #разбиваем зашифрованный текст на буквы
        decr = [] #расшифрованный текст

        for i in self.final_encr: # идем по строке
            decr_text.append(i) # добавляем буквы в список 
        for i in decr_text:
            num_ascii_ord = ord(i)
            shi= int(num_ascii_ord) + shift_decr
            if shi >= 97:
                if shi >= 123:
                    num = shi - 122
                    num_2 = 96 + num
                    num_ascii_chr = chr(num_2)
                    decr.append(num_ascii_chr)
                else:
                    num_ascii_chr = chr(shi)
                    decr.append(num_ascii_chr)  
            elif shi >= 91:
                num = shi - 90
                num_2 = 64 + num
                num_ascii_chr = chr(num_2)
                decr.append(num_ascii_chr)
            else:
                num_ascii_chr = chr(shi)
                decr.append(num_ascii_chr)

        final_decr = "".join(decr) #decrypt word

        print("Расшифровка",final_decr)

    def __del__(self): #деструктор

        print("del done")

class VernamCipper(CaesarCipper):

    def __init__(self, input_text, shift, key_word):
        super().__init__(input_text, shift)
        self.key = key_word

    def encrypt(self):

        self.len = len(self.text)    
        encr = [] #шифрованный текст поэлементно 
        text_spl = [] #разбиение текста на элементы
        text_key = []
        bin_num = []
        bin_hello = [] #шифр hello
        self.bin_key_apple = [] #шифр apple

        for i in self.text:# разделение текста на отдельные буквы
            text_spl.append(i) # добавляем буквы в список 
        for i in self.key:# разделение текста на отдельные буквы
            text_key.append(i) # добавляем буквы в список 
        for i in text_spl: #перевод букв в ascii и сдвигаем алфавит на значение shift
            num_ascii_ord = ord(i)
            bin = format(num_ascii_ord,"08b")#двоичная запись буквы слова
            bin_hello.append(bin)
        for i in text_key:    
            bin_key_word = ord(i)
            bin_key = format(bin_key_word,"08b")#двоичная запись буквы ключа 
            self.bin_key_apple.append(bin_key)
        for i in range(self.len):
            bin_hello_1 = bin_hello[i]
            bin_key_1 = self.bin_key_apple[i]
            for i in range(8):
                num1 = int(bin_hello_1[i])
                num2 = int(bin_key_1[i])
                if num1 == 1:
                    if num2 == 1:
                        bin_num.append(0)
                    else:
                        bin_num.append(1)
                elif num1 == 0:
                    if num2 == 1:
                        bin_num.append(1)
                    else:
                        bin_num.append(0)
        encrpt = "".join(map(str,bin_num))
        self.result = [bin_num[i:i+8] for i in range(0, len(bin_num), 8)]
        print("Шифровка",encrpt)

    def decrypt(self):
        
        decr = []
        normal = []
        bin_num = []
        for i in range(self.len):
            bin_hello_1 = self.result[i]
            bin_key_1 = self.bin_key_apple[i]
            for i in range(8):
                num1 = int(bin_hello_1[i])
                num2 = int(bin_key_1[i])
                if num1 == 1:
                    if num2 == 1:
                        bin_num.append(0)
                    else:
                        bin_num.append(1)
                elif num1 == 0:
                    if num2 == 1:
                        bin_num.append(1)
                    else:
                        bin_num.append(0)
        self.result = [bin_num[i:i+8] for i in range(0, len(bin_num), 8)]
        for i in range(self.len):
            num = self.result[i]
            num1 = "".join(map(str,num))
            decr.append(num1)
        for i in range(self.len):
            norm = chr(int(decr[i], 2))
            normal.append(norm)
        final_decr = "".join(normal) #decrypt word
        print("Расшифровка",final_decr)

        

def main(): 
    
    input_text = input("Введите текст который вы хотите зашифровать:")
    shift = input("Введите ключ для шифрования:")
    key_word = input("Введите ключ для шифрования(букву):")

    caesarcipper = CaesarCipper(input_text,shift)
    vernamcipper = VernamCipper(input_text,shift,key_word)

    caesarcipper.encrypt()
    caesarcipper.decrypt()
    vernamcipper.encrypt()
    vernamcipper.decrypt()


if __name__ == "__main__":
    main()

