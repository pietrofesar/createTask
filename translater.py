def getLanguage(languages):
    while True:
        print(' '.join(languages))
        language = input('Which language would you like to translate to: ').capitalize()
        if language in languages:
            return language.lower()
        else:
            print('Invalid language entry')


def getColor(colors):
    while True:
        print(' '.join(colors))
        color = input('Which color to translate(type name)? ')
        if color in colors:
            return color
        else:
            print('Invalid color entry')

        
def main():
    languages = ['French', 'Spanish']
    colors = ['black', 'red', 'green', 'pink', 'yellow', 'orange', 'blue', 'brown', 'white']
    french = {'black' : 'noir/noire', 'red' : 'rouge', 'green' : 'vert/verte', 'pink' : 'rose', 'yellow' : 'juane', 
              'orange' : 'orange', 'blue' : 'blue/bleue', 'brown' : 'marron', 'White' : 'blanc/blanche'}
    spanish = {'black' : 'negro', 'red' : 'rojo', 'green' : 'verde', 'pink' : 'rosa', 'yellow' : 'amarillo', 
               'orange' : 'naranja', 'blue' : 'azul', 'brown' : 'marron', 'White' : 'blanco'}
  
    while True:
        language = getLanguage(languages)
        print()
        color = getColor(colors)
        print()
        print(vars()[language][color])
        resume = input('Press x to exit, any other key to continue: ')
        if resume == 'x':
            print('Goodbye! :)')
            break
        

main()







    
