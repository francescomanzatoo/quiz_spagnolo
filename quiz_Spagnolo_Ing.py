import random
import json
import os
import time

class Vocabolario:

    #constructor for saving the vocabolary into a file json
    def  __init__(self, nome_file = "vocabolario.json", voc_generale = None):
        self.nome_file = nome_file
        self.voc_generale = voc_generale
        base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "file_json")
        self.nome_file = os.path.join(base_dir, nome_file)

        # crea la cartella file_json se non esiste
        os.makedirs(base_dir, exist_ok=True)

        if (os.path.exists(self.nome_file)):
            with open(self.nome_file, "r", encoding = "utf-8") as f:
                self.parole = json.load(f)

            for parola, traduzione in self.parole.items():
                if isinstance(traduzione, str):
                    self.parole[parola] = [traduzione]
            self.salva()

        else:
            self.parole = {}
    
    #save the vocabolary
    def salva(self):
        with open(self.nome_file, "w", encoding = "utf-8") as f:
            json.dump(self.parole, f, ensure_ascii = False, indent = 4)

    #add a new word into the vocabolary, then save
    def add(self, parola, ListaTraduzione):
        if parola not in self.parole:
            self.parole[parola] = ListaTraduzione
            self.salva()
            print(f"the word {parola} ({', '.join(ListaTraduzione)}) has been added in the dictionary")
            
            if (self.voc_generale is not None):
                    if parola not in self.voc_generale.parole:
                        self.voc_generale.add(parola, ListaTraduzione)
            return
        
        traduzioni_esistenti = self.parole[parola]

        nuove_aggiunte = []
        gia_presenti = []

        for traduzione in ListaTraduzione:
            if traduzione in traduzioni_esistenti:
                gia_presenti.append(traduzione)
            else:
                traduzioni_esistenti.append(traduzione)
                nuove_aggiunte.append(traduzione)

        if nuove_aggiunte:
            print("\nNew translation added:", ", ".join(nuove_aggiunte))

        if gia_presenti:
            print("\nThese traslation were already in the dictionary:", ", ".join(gia_presenti) + "\n")

        if nuove_aggiunte:
            self.salva()

    
    
    #remove a specific word from the vocabolary, then save 
    def remove(self, parola):
        if parola in self.parole:
            del self.parole[parola] 
            self.salva()
            if (self.voc_generale is not None):
                if parola in self.voc_generale.parole:
                    self.voc_generale.remove(parola)
            return True
        else:
            print("\nWord not found\n")
            return False
    
    #quiz implementation
    def quiz(self):

        if len(self.parole) == 0:
            print("The dictionary is empty")
            return

        numero_domande = min(20, len(self.parole))
        parole_casuali = random.sample(list(self.parole.keys()), numero_domande)

        punteggio = 0

        for i, parola in enumerate(parole_casuali, 1):

            traduzioni = self.parole[parola]

            risposta = input(f"{i}) Translate: {parola}\nAnswer: ").strip()

            if risposta in traduzioni:
                print("Correct!\n")
                punteggio += 1
            else:
                print("Wrong!")
                print("Right answers:", ", ".join(traduzioni), "\n")

        print(f"Quiz completed! Score: {punteggio}/{numero_domande}\n")

    #implementation of specific quiz for a choosen category
    def quizSp(self):

        catalogue = ["lavoro", "parentele", "numeri", "luoghi", "saluti", "meteo", "animali", "informatica", "verbi", "parole generali"]
        print(catalogue)
        categoria = str(input("\nInsert the specific category for the test: \n"))
        exists = True
        i = 0
        while (exists is True):
            try:

                if (categoria == catalogue[i]):
                    exists = False
                    print("\nCategory found\nLoading...")
                    time.sleep(0.5)
                    vocSp = Vocabolario(catalogue[i] + (".json"))
                    nextRequestSp = True
                    while (nextRequestSp is True):
                        try:
                            cmdSp = int(input("\nInsert the choosen command:" + commandLineSp + "\n"))
                            if (cmdSp < 1 or cmdSp > 7):
                                print("Press a valid command, try again\n")
                            else:
                                
                                if (cmdSp == 4):
                                    nextRequestSp = False
                                vocSp.command(vocSp, cmdSp)
                                if (cmdSp == 5):
                                    print("Beginning of the multiple answer quiz\nLoading...")
                                    time.sleep(0.5)
                                    vocSp.multipleAnsQuiz()
                            
                                if (cmdSp == 7):
                                    nextRequestSp = False
                                    
                                    print("Disconnection...\n")
                                    time.sleep(0.5)

                        except ValueError as v:
                            print("Insert a valid command, try again")

                else:
                    i += 1

            except (NameError and IndexError) as n:
                print("\nCategory not founded, try again\n")
                exists = False
        
    def multipleAnsQuiz(self):

        if len(self.parole) == 0:
            print("The vocabolary is empty.")
            return

        numero_domande = min(20, len(self.parole))
        parole_casuali = random.sample(list(self.parole.keys()), numero_domande)

        punteggio = 0

        print("Select the right option (a, b, c, d)\n")

        for i, parola in enumerate(parole_casuali, 1):

            traduzioni_corrette = self.parole[parola]
            risposta_corretta = random.choice(traduzioni_corrette)

            
            tutte_traduzioni = []

            for lista in self.parole.values():
                tutte_traduzioni.extend(lista)

            tutte_traduzioni = [t for t in tutte_traduzioni if t != risposta_corretta]
            risposte_sbagliate = random.sample(tutte_traduzioni, 3)
            opzioni = risposte_sbagliate + [risposta_corretta]
            random.shuffle(opzioni)
            lettere = ["a", "b", "c", "d"]

            print(f"{i}) Translate: {parola}\n")

            for lettera, opzione in zip(lettere, opzioni):
                print(f"{lettera}) {opzione}")

            risposta = input("\nAnswer: ").lower()

            indice = lettere.index(risposta)

            if opzioni[indice] == risposta_corretta:
                print("Right!\n")
                punteggio += 1
            else:
                print(f"Wrong! Right answer: {risposta_corretta}\n")

        print(f"Quiz completed! Score: {punteggio}/{numero_domande}\n")

    
    #command function table
    def command(self, voc, cmd):
        if (cmd == 1): #add
            newWord = str(input("Insert the word in spanish:\n"))
            TransWord = str(input("Insert the correct traduction:\n"))
            TransList = [t.strip() for t in TransWord.split(",")]
            voc.add(newWord, TransList)
            
        if (cmd == 2): #remove
            removeWord = str(input("Insert the word to be removed:\n"))
            isOk = voc.remove(removeWord)
            if (isOk):
                print("\nThe word " + removeWord + " had been removed from the vocabolary\n")

        if cmd == 3: #general quiz
            if len(voc.parole) == 0:
                print("The vocabolary is empty!")
            else:
                print("Beginning of the quiz:\n")
                voc.quiz()
        
        if (cmd == 4): #specific quiz
            print("Beginning of the selected quiz:\n")
            
            voc.quizSp()


        if (cmd == 6): #print all the words of the vocabolary
                print(voc.parole)
                print("\n")
            


voc = Vocabolario()


#main block of the program
nextRequest = True
commandLine = """\n1) Add a new word into the dictionary
2) Remove a word from the dictionary
3) Start a general quiz
4) Start a specific quiz
5) Not finished yet...
6) Print all the words of the dictionary
7) Exit\n"""

commandLineSp = """\n1) Add a  new word into the specific dictionary
2) Remove a word from the specific dictionary
3) Start a specific quiz into the choosen category
4) Change the specific category 
5) Start a multiple answer quiz on the choosen category
6) Print all the words of the dictionary
7) Main menu\n"""

while nextRequest is True:
    try:
        cmd = int(input("Read the instruction, then press the choosen command:" + commandLine + "\n"))
        if (cmd < 1 or cmd > 7):
            print("Press a valid command, try again\n")
        else:
        
            
            if (cmd == 5):
                print("\nWork in progress, command not available now\n")
                
            elif (cmd == 7): # esci dal ciclo
                nextRequest = False
                print("Disconnection...\n")
                time.sleep(0.5)
            else:
                voc.command(voc, cmd)

    except ValueError as e:
        print("Press a valid command, try again\n")


#Function to implement:
        #sinonimous of the correct words
        #implement a graphic interface
        #looking for using it as a site
        #add a quiz to complete somo sentences with the write words