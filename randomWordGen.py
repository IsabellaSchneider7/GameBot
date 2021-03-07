import random
adjectives = ['blue', 'green', 'yellow', 'shiny', 'tired', 'happy', 'alive', 'bored', 'bright', 'cloudy', 'good', 'bad', 'purple',
             'sad', 'angry', 'red', 'magical']
nouns = ['people', 'world', 'art', 'family', 'food', 'goose', 'tv', 'baby', 'camera', 'cat', 'pizza', 'tire', 'strawberry', 'snowflake',
         'egg', 'basketball', 'lion', 'lollipop', 'train', 'saturn', 'flag', 'piano', 'phone', 'paperclip', 'water', 'calendar', 'book',
         'chocolate', 'laptop', 'tennis', 'candy', 'snow', 'skiing', 'snowman', 'penguin', 'beach', 'ocean', 'tshirt', 'jellyfish', 'dog',
         'car', 'bed', 'bowl', 'glasses', 'watch', 'swing', 'noodles', 'pasta', 'waffles', 'fork', 'sun', 'star', 'moon', 'house']
disney_nouns =['Mickey Mouse','Snow White','Pinoccio','Dumbo','Cinderella','Alice in Wonderland','Mad Hatter','Peter Pan','Sleeping Beauty',
               'Mary Poppins','Winnie the Pooh','Robin Hood','Ariel','Belle','Aladdin','Jasmine','Jafar','Tarzan','Pumba','Timone','Simba',
               'Mike Wazowski','Skully','Pocahontas','Nemo','Dory','Lightning Mcqueen','Mr. Incredible','Elastagirl','Frozone','Jack Sparrow',
               'Davy Jones','Wall-E','Tiana','Moana','Elsa','Flyn Rider','Rapunzel','Baymax','Goofy','Donald Duck','Minie Mouse','Captain Hook',
               'Maleficent','Fairies','Cruella de Vil','Tigger','Buzz Lightyear','Woody','Shreck','Puss in Boots','Lord Farquaad','Gingerbread Man',
               'Sebastian','Gaston','Genie','Mulan','Boo','Lilo','Stitch','Chicken Little','Remy','Merida','Wreck-it Ralph','Olaf','Sadness','Anger']
verbs = ['running', 'jumping', 'spinning', 'flying', 'fighting', 'eating', 'throwing', 'fishing', 'drawing', 'building', 'baking','cooking',
         'dancing','hopping','dying','falling','boating','sailing','scuba diving','bowling','bungee jumping','canoeing','climbing','skateboarding',
         'skiing','snowboarding','sledding','surfing','skating','skydiving']

def get_rand_phrase():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    return (str(adjective) + " " + str (noun) + " " + str(verb))

def get_disney_phrase():
    character = random.choice(disney_nouns)
    return (character)

# for i in range(10):
#     print(get_rand_phrase())
