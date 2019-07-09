from flask import Flask, render_template, request

def user_username(u):
    if u.count(' ') > 0:
        return('Please enter a valid username')
    elif len(u) < 3:
        return('Please enter a valid username')
    elif len(u) > 20:
        return('Please enter a valid username')
    else:
        return(u)

def user_password(pw):
    num = 0
    for i in pw:
        num += 1
        if i == " ":
            return('Please enter a valid password')
    if num < 3:
        return ('Please enter a valid password')
    elif num > 20:
        return ('Please enter a valid password')
    else:
        return(pw)

def user_verify(pw, vpw):
    if (pw != vpw):
        return ('Passwords do not match')
    else:
        return(vpw)

def user_email(e):
    num_occurance = e.count('@')
    numoccurance = e.count('.')
    num_occur = e.count('.com')
    if (len(e) == 0):
        return(e)
    elif (len(e) > 20):
        return('Please enter a valid email address')
    elif num_occur > 1:    
        return('Please enter a valid email address')
    elif num_occurance > 1:
        return('Please enter a valid email address')
    elif numoccurance > 1:
        return('Please enter a valid email address')
    elif num_occur == 0:    
        return('Please enter a valid email address')
    elif num_occurance == 0:
        return('Please enter a valid email address')
    elif numoccurance == 0:
        return('Please enter a valid email address')
    else:
            return(e)
        
def login(username, password, verify, email):
    un = user_username(username)
    pw = user_password(password)
    vpw = user_verify(password, verify)
    em = user_email(email)
    if (un == username) and (pw == password) and (vpw == verify) and (em == email):
        form = render_template("welcome.html")
        return(form.format(un))
    else:
        form = render_template("signup.html")
        a = ''
        b = ''
        c = ''
        d = ''
        if un != username:
            a = un
        if pw != password:
            b = pw
        if vpw != verify:
            c = vpw
        if em != email:
            d = em
        return(form.format(a, b, c, d))
           
def main():
    UN = input("What is your username?")
    PW = input("What is your password?")
    VPW = input("Verify passwrd")
    EM = input("What is your email?(this is opptional)")
    print(login(UN, PW, VPW, EM))
    
    
if __name__ == "__main__":
    main()
    


