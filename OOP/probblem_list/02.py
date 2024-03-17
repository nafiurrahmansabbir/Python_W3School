

def xoxo(lexicon,key,value):
    if key not in lexicon:
        lexicon[key]=value
        print(f"{key} is suxxesfully added")
    else:
        print(f"{key} already exsist")
        
def main():
    lexicon = {
    "abracadabra": "A word uttered to perform a magical act.",
    "enchantment": "The act of casting spells or charms.",
    "mystic": "Relating to mysteries or mystical powers."
    }
    key='XoXo'
    value='It\'s my compute name'
    
    xoxo(lexicon,key,value)
    key='XoXo'
    value='It\'s my compute name'
    
    xoxo(lexicon,key,value)
    
if __name__=="__main__":
    main()