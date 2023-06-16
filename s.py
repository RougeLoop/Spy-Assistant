import subprocess
import os
import requests
import wikipedia
import wolframalpha

# Konfigurasi API untuk WolframAlpha
app_id = "9UW29V-R426KY2X53"
client = wolframalpha.Client(app_id)

# Fungsi untuk mengucapkan teks menggunakan espeak
def speak(text):
    os.system('espeak -s 150 -v en-us-wavenet-e "{}"'.format(text))

# Fungsi untuk kalkulator
def Calculate():
    os.system('clear')
    os.system("figlet -d figlet-fonts -f 'ANSI Shadow.flf' S.py ver: 1.2")
    speak("Please enter the first number.")
    num1 = float(input("First number: "))
    speak("Please enter the second number.")
    num2 = float(input("Second number: "))
    speak("Please select an operation")
    print ('Operation: +, -, ×, ÷')
    operation = input("Operation: ")
    if operation == "+":
        result = num1 + num2
        print ("the result is", result)
        speak("The result is {}".format(result))
        os.system('clear')
    elif operation == "-":
        result = num1 - num2
        print ("the result is", result)
        speak("The result is {}".format(result))
        os.system('clear')
    elif operation == "×":
        result = num1 * num2
        print ("the result is", result)
        speak("The result is {}".format(result))
        os.system('clear')
    elif operation == "÷":
        if num2 == 0:
            print ("You cannot divide by Zero.'")
            speak("I'm sorry, you cannot divide by zero.")
            os.system('clear')
        else:
            result = num1 / num2
            print ("the result is", result)
            speak("The result is {}".format(result))
            os.system('clear')
    else:
        speak("I'm sorry, I didn't understand the operation you selected.")
        os.system('clear')

# Fungsi untuk mencari informasi terkait topik dari Wikipedia
def search_wikipedia(query):
    os.system('clear')
    os.system("figlet -d figlet-fonts -f 'ANSI Shadow.flf' S.py ver: 1.2")
    try:
        wikipedia.set_lang("en")
        summary = wikipedia.summary(query, sentences=3)
        print(summary)
        speak(summary)
        os.system('clear')
    except Exception as e:
        speak("I'm sorry, I couldn't find information on that topic.")
        os.system('clear')

# Fungsi untuk mencari jawaban dari pertanyaan umum menggunakan WolframAlpha
def search_wolframalpha(query):
    os.system('clear')
    os.system("figlet -d figlet-fonts -f 'ANSI Shadow.flf' S.py ver: 1.2")
    try:
        res = client.query(query)
        answer = next(res.results).text
        print(answer)
        speak(answer)
        print ("Want detailed answer?(Wikipedia)")
        wolfram1 = input("Answer (Y/N):")
        if wolfram1 == "Y":
            search_wikipedia(query)
        elif wolfram1 == "N":
            True
        os.system('clear')
    except Exception as e:
        speak("I'm sorry, I couldn't find an answer to that question.")
        os.system('clear')

# Menjalankan program
if __name__ == '__main__':
   os.system('clear')
   os.system('figlet System ON.')
   speak("System on.")
   os.system('figlet Welcome Sir.')
   speak("Welcome sir.")
   while True:
        os.system('clear')
        os.system("figlet -d figlet-fonts -f 'ANSI Shadow.flf' S.py ver: 1.2")
        speak("What would you like me to do?")
        print ("Calculate, Wikipedia, Ask Spy, Author, Exit")
        action = input("Action: ")
        if action == "Calculate":
            Calculate()
        elif action == "Wikipedia":
            speak("What do you want to know from Wikipedia?")
            query = input("Query: ")
            search_wikipedia(query)
        elif action == "Ask Spy":
            speak("What question do you want me to answer?")
            query = input("Query: ")
            search_wolframalpha(query)
        elif action == "Author":
            subprocess.run(['am', 'start', '-a', 'android.intent.action.VIEW', '-d', 'https://wa.me/6281295628298'])
        elif action == "Exit":
            os.system('clear')
            os.system('figlet Goodbye, Sir')
            speak("Goodbye, sir")
            os.system('clear')
            quit()
        elif action == "dev":
            os.system('clear')
            print ('███████╗   ╔════╗      ')
            print ('██╔════╝   ║    ║║     ║')
            print ('███████╗   ║    ║ ║   ║')
            print ('╚════██║═══║════╝  ║ ║')
            print ('███████║   ║        ║')
            print ('╚══════╝ ∆ ║        ║')
            print ("Hello sir, what would you like to do?")
            speak("Hello sir, what would you like to do?")
            print ("Edit script, Build new script, Delete other script, Go to chatgpt, Back.")
            dev = input("Action: ")
            if dev == "Edit script":
                os.system('clear')
                os.system('nano s.py')
            elif dev == "Build new script":
                name = input("Name of new file: ")
                language = input("Programming language. (ex: py, js, json, etc): ")
                os.system('nano {}.{}'.format(name, language))
            elif dev == "Delete other script":
                script = input("Script name (ex: loop.py): ")
                os.system('rm {}'.format(script))
            elif dev == "Go to chatgpt":
                subprocess.run(['am', 'start', '-a', 'android.intent.action.VIEW', '-d', 'https://chat.openai.com'])
                quit()
            elif dev == "Back":
                True
            else:
                speak("I'm sorry, I didn't understand the action you selected")
                os.system('clear')
        else:
            speak("I'm sorry, I didn't understand the action you selected")
            os.system('clear')

