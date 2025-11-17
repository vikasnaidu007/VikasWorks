# COMMON STRING METHODS

x = 10
s = 'abc'
print(type(x), type(s))

# STRING CASE CONVERSIONS

model_output = 'ai IS the future of everything!'

# Convert the string to uppercase
print(model_output.upper())

print(model_output.lower())

print(model_output)

print(model_output.capitalize())

# STRING STRIPPING

response = ' ?? Hello, human! ?? '
# Remove leading and trailing whitespace characters
print(response.strip())

# Remove specific leading and trailing characters (' ??')
print(response.strip(' ??'))

# STRING REPLACEMENT
text = 'ML is a critical component of modern AI. ML techniques are advancing rapidly.'

# Replace occurrences of 'ML' with 'machine learning'
updated_text = text.replace('ML', 'machine learning')
print(updated_text)
print(text)

# STRING COUNTING
text = 'AI is the FUture. Embrace the future of AI!'
print(text.lower().count('future'))

# STRING SPLITTING
statement = 'AI breakthrough at every step'

# Split the string into a list of words
words = statement.split()
print(words)
print(type(words))

# STRING JOINING
terms = ['AI', 'ML', 'GenAI', 'LLM', 'NLP']

# Join the list elements into a single string, separated by ', '
ml_words = ', '.join(terms)
print(ml_words)

# STRING PREFIX AND SUFFIX REMOVAL
url = 'https://example.com'
# Remove 'https://' from the beginning of the URL

cleaned_url = url.removeprefix('https://')
print(cleaned_url)

filename = 'state_of_ai_2025.pdf'
# Remove '.pdf' from the end of the filename

cleaned_filename = filename.removesuffix('.pdf')
print(cleaned_filename)
