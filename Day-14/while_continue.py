# Smart looping techniques: continue, pass, break

sentence = 'AI is the future of technology.'

for word in sentence.split():
    # print(word)
    if word in ['the', 'of', 'in']:
        continue # Skip the current iteration and move to the next one
    print(word, end=' ')

while True:
    prompt = input('Enter a prompt for the model: ')
    if len(prompt) < 5 :
        print('Prompt too short. Try again!')
        continue
    print(f'Processing your prompt: {prompt}')
    break

# pass - A null operation.
# It is used when a statement is required syntactically, but you do not want to execute any commands or code.
# It's often used as a placeholder.

for model in range(5):
    pass