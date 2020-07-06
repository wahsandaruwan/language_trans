from googletrans import Translator

sentence = str(input("Say Something : "))

# Translator object
trans = Translator()

# Translate english to sinhala
trans_sentence = trans.translate(sentence, src = 'en', dest = 'si')

print(trans_sentence.text)