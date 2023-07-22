'''
In these tasks you will be given one or more examples of code.

- Look at each example , study it carefully.
- Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms list, item and index in your predictions.
- Run the code, compare what happens to your prediction.
- Add comments to note down and differences between your prediction and what actually happened.

'''

# Example Code 1

Sentence = [
  "Always",
  "look",
  "on",
  "the",
  "bright",
  "side",
  "of",
]
print(Sentence)  # prints the list
print(Sentence[1])  #prints "look"
Sentence.append("life")  #appends "life" to the end of the list
Sentence[4] = "sunny"  #assigns the 4th position as sunny instead of bright
print(Sentence[4])  #print sunny
print(Sentence[0] + " " + Sentence[3])  #print "Always the"
print(
  Sentence
)  #prints everything but life is at the end and bright is replaced with sunny
