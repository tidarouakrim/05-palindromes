"importe le module unicodedata"
import unicodedata

def ispalindrome(s):
    'vérifie si une chaine de caractère est un palindrome'
    s = unicodedata.normalize('NFD', s) # Décompose les caractères
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn') # Supprime les accents
    for i in [' ','+','.',',','?','!',':',';','_','-',"'",'()']:
        s = s.replace(i,'') #Supprime les ponctuations et espaces
    s = s.upper() #Met tout en majuscule
    return s == s[::-1]  #Vérifie si c'est un palindrome
      # votre code ici


#### Fonction principale


def main():
    'appels à la fonction secondaire'

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
