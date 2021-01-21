# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 23:50:10 2021

@author: sadio_aya5cf2
"""
from app import app
from flask import Flask, session, render_template, request, g, current_app, redirect, url_for
import sqlite3
import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db= sqlite3.connect('mydatabase.db')
        g.db.row_factory = sqlite3.Row
    return g.db

@app.route('/')
def accueil():
    return render_template ('DevApp.html')

@app.route('/valide')
def valide():
    return render_template ('valide.html')
@app.route('/pdf')
def pdf():
    return render_template ('pdf.html')
@app.route('/choix')
def choix():
    return render_template ('choix.html')

@app.route('/new', methods=('GET', 'POST'))
def new():
    #if request.method == 'POST':
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    date = request.form.get('date')
    mail = request.form.get ('mail')
    num = request.form.get('num')
    mdp = request.form.get('mdp')
    adresse = request.form.get('adresse')
    Hématie = 5.23
    Hémoglobine = 14.2
    Hématocrite = 40.8
    VGM = 78.0
    TCMH = 27.2
    CCMH = 34.9
    Leucocytes = 7.33
    PN = 3.14
    PE = 0.71
    PB = 0.03
    Lymphocytes = 2.82
    Monocytes = 0.63
    
    db = get_db()
    
    # db.execute("INSERT INTO tests(mail, hématie, hémogobline, hématocrite, VGM, TCMH, CCMH, Leucocytes, PE, PN, PB, lymphocytes, monocytes) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",  (mail, Hématie, Hémoglobine, Hématocrite, VGM, TCMH, CCMH, Leucocytes, PE, PN, PB, Lymphocytes, Monocytes))
    db.execute("INSERT INTO resultats(nom, prenom, mdp, mail, num, date, adresse) VALUES(?,?,?,?,?,?,?)" , (nom, prenom, mdp, mail, num, date, adresse))
    db.execute('INSERT INTO patients(nom, mdp, mail, num, date) VALUES (?,?,?,?,?)', (nom, mdp, mail, num, date))
    db.commit()
    test = db.execute("SELECT nom FROM resultats WHERE mail=?", (mail,)).fetchall()
    if len(test) == 1:
            return render_template('DevApp.html')
    return render_template('SignIn.html')   
 
@app.route('/login', methods=('GET', 'POST'))
def login():
    #if request.method == 'POST':
    mail = request.form.get('mail')
    mdp = request.form.get('mdp')
   
    con = sqlite3.connect("mydatabase.db") 
    #con.row_factory = sqlite3.Row
    cur = con.cursor()
    user = cur.execute("SELECT mdp FROM patients WHERE mail=?", (mail,))    
    user = user.fetchall()
    if len(user) == 1:
        return render_template('choix.html')
    return render_template('login.html')
 