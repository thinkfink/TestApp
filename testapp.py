###Strings

#message = 'Hello World!'

greeting = 'Hello'
name = 'Tyler'

#print(dir(name))

print(help(str.lower))

#message = greeting + ', ' + name + '. Welcome!'

message = '{}, {}. Welcome!'.format(greeting, name)

message = f'{greeting}, {name.upper}. Welcome!'

#message = message.replace('World','Universe')

print(message)
#print(message[0:5])'Hello World!'
print(message[:5])
print(message[6:])
print(message.lower())
print(message.count('l'))
print(message.find('World'))

###Lists
todo_list = [
    "buy groceries",
    "do the dishes",
    "mow the lawn"
]

#for loop
for thing in todo_list:
    print(thing.title())

#loop over thing and index
for i in range(len(todo_list)):
    print(i, todo_list[i].title())

#counter
counter = 0
for thing in todo_list:
    print(counter, thing.title())
    counter += 1

#enumerate
    for i, thing in enumerate(todo_list):
        print(i, thing.title())

###Numbers




