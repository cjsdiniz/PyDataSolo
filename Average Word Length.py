# Given a sentence as input, calculate and output the average word length of that sentence.
# To calculate the average word length, you need to divide the sum of all word lengths by the number of words in the sentence.
text = input("Frase: ")
words = text.split()
sw = 0
soma = 0
for i in range(len(words)):
    sw += 1
    soma += len(words[i])
    print("sw: ", sw, " soma: ", soma)
print("Average is: ", round(soma/sw))
