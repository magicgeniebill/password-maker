# TODO: super secret and secure password maker for my best friend Ann
import hashlib

def secret_password_maker():
    questions = [
                 "What is Ann's Date of Birth (DD-MM-YYYY)?",
                 "What is Ann's Nationality?",
                 "What is Ann's Favorite Holiday?",
                 "Where does Ann Currently Work?", 
                 "From What University did Ann Graduate?",
                 "What City do Ann's Parents Live In?",
                 "What City are Ann and Jeanie based in?",
                 "What Place do Ann and Jeanie Visit Every Saturday?",
                 "What is Ann's Official Email Account?", # u can't find our emails from github right...  
                 "What is Ann's Throwaway Email Account?",
                 "What Food is Ann Allergic to?"
                 ]
    m = hashlib.sha256()
    for question in questions:
        x = input(question+'\n').lower().strip()
        m.update(x.encode())
    return m.hexdigest()

if __name__ == '__main__':
    print(secret_password_maker())
