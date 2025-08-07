import random, sys, tkinter
from tkinter import messagebox, Label, Button, ttk, Text
import os

gui = tkinter.Tk()
gui.geometry('1000x600')
gui.title('Milionerzy')


class Pytanie:
    def __init__(self, pytanie, odpA, odpB, odpC, odpD, dobra):
        self.pytanie = pytanie
        self.odpA = odpA
        self.odpB = odpB
        self.odpC = odpC
        self.odpD = odpD
        self.dobra = dobra
        self.calePytanie = pytanie, odpA, odpB, odpC, odpD, dobra


class Kolejka:
    def UtworzKolejke():
        with open("Latwe.txt") as P1:
            Latwe = P1.read().split(">")
        
        with open("Srednie.txt") as P2:
            Srednie = P2.read().split(">")
        
        with open("Trudne.txt") as P3:
            Trudne = P3.read().split(">")

        pytania = []
        random.shuffle(Latwe)
        for i in range(4):
            pyt = Latwe[0].split(";")
            pyt = Pytanie(pytanie=pyt[1], odpA=pyt[2], odpB=pyt[3], odpC=pyt[4], odpD=pyt[5], dobra=pyt[6])
            pytania.append(pyt)
            Latwe.remove(Latwe[0])

        random.shuffle(Srednie)
        for i in range(4):
            pyt = Srednie[0].split(";")
            pyt = Pytanie(pyt[1], pyt[2], pyt[3], pyt[4], pyt[5], pyt[6])
            pytania.append(pyt)
            Srednie.remove(Srednie[0])

        random.shuffle(Trudne)
        for i in range(4):
            pyt = Trudne[0].split(";")
            pyt = Pytanie(pyt[1], pyt[2], pyt[3], pyt[4], pyt[5], pyt[6])
            pytania.append(pyt)
            Trudne.remove(Trudne[0])
            
        return pytania


class Sprawdz:
    def SprawdzOdpowiedz(numer, odp, pytania, gwarantowane):
        if odp == pytania[numer-1].dobra:
            return True
        else:
            messagebox.showinfo(title="Źle", message=f"Niestety odpowiedziałeś źle. Wygrałeś {gwarantowane} złotych.")
            return False


class Nastepne:
    def CzyGraszDalej(numer, masz, gwarantowane, pytania, mam50teraz):
        if numer == 3 or numer == 8:
            messagebox.showinfo(title='Gwarantowane', 
                                message=f'Masz gwarantowane: {gwarantowane} złotych. Możesz bezpiecznie grać dalej.')
        
        if numer == 13:
            messagebox.showinfo(title="Wygrałeś", message="Dziękuję, wygrałeś milion złotych!")
            return False

        koniec = messagebox.askyesno(title="Gramy?", 
                                    message="Odpowiedziałeś poprawnie! Czy chcesz usłyszeć kolejne pytanie?")
        return koniec


class Gra:
    def __init__(self):
        self.numer = 1
        self.masz = 0
        self.graszo = 500
        self.gwarantowane = 0
        self.pytania = []
        self.mam50 = 0
        self.mamtel = 0
        self.mampub = 0
        self.mam50teraz = 0
        self.odp = None
        
        self.guiEtGra = None
        self.guiEtMasz = None
        self.guiEtGwar = None
        self.guiEtNumer = None
        self.guiEt = None
        self.guiGuzA = None
        self.guiGuzB = None
        self.guiGuzC = None
        self.guiGuzD = None
        self.guiEtKolo1 = None
        self.guiEtKolo2 = None
        self.guiEtKolo3 = None
        self.guiGuz5050 = None
        self.guiGuzPub = None
        self.guiGuzTel = None
        self.guiEtImie = None
        self.inputtxt = None
        self.guiRank = None
        self.guiRezygnuj = None

        self.aktywneOdpowiedzi = ['a', 'b', 'c', 'd'] 

    def OkienkoStart(self):
        start = messagebox.askyesno(title='Czy chcesz rozpocząć?', 
                                    message='Czy chcesz zacząć grę o milion?')
        return start

    def AktualizujStan(self):
        kwoty = [0, 500, 1000, 2000, 5000, 10000, 20000, 40000, 75000, 125000, 250000, 500000, 1000000, 'NA']
        kwoty2 = [0, 0, 1000, 1000, 1000, 1000, 1000, 40000, 40000, 40000, 40000, 40000, 'NA']
        
        self.numer += 1
        self.masz = kwoty[self.numer-1]
        self.graszo = kwoty[self.numer]
        self.gwarantowane = kwoty2[self.numer-1]
        self.guiEtKolo1.config(text=f'Pomoc 50/50:')
        self.guiEtKolo2.config(text=f'Telefon do przyjaciela: ')
        self.guiEtKolo3.config(text=f'Głos publiczności: ')

    def Wyczysc(self):
        if self.guiEtGra: self.guiEtGra.destroy()
        if self.guiEtMasz: self.guiEtMasz.destroy()
        if self.guiEtGwar: self.guiEtGwar.destroy()
        if self.guiEtNumer: self.guiEtNumer.destroy()
        if self.guiEt: self.guiEt.destroy()
        if self.guiGuzA: self.guiGuzA.destroy()
        if self.guiGuzB: self.guiGuzB.destroy()
        if self.guiGuzC: self.guiGuzC.destroy()
        if self.guiGuzD: self.guiGuzD.destroy()
        if self.guiEtKolo1: self.guiEtKolo1.destroy()
        if self.guiEtKolo2: self.guiEtKolo2.destroy()
        if self.guiEtKolo3: self.guiEtKolo3.destroy()
        if self.guiGuz5050: self.guiGuz5050.destroy()
        if self.guiGuzPub: self.guiGuzPub.destroy()
        if self.guiGuzTel: self.guiGuzTel.destroy()
        if self.guiEtImie: self.guiEtImie.destroy()
        if self.inputtxt: self.inputtxt.destroy()
        if self.guiRank: self.guiRank.destroy()
        if self.guiRezygnuj: self.guiRezygnuj.destroy()

    def Zrezygnuj(self):
        imie = self.inputtxt.get(1.0, "end-1c") if self.inputtxt else ""
        Ranking.Dodaj(imie, self.masz)
        jeszczeraz = messagebox.askyesno(title="Dziękuję", 
                                        message=f"Dziękuję, wygrałeś {self.masz} złotych. Czy chcesz zagrać jeszcze raz?")
        self.Wyczysc()
        return jeszczeraz

    def Rozpocznij(self):
        self.Wyczysc()
        self.__init__() 
        
        if not self.OkienkoStart():
            gui.destroy()
            return
            
        self.pytania = Kolejka.UtworzKolejke()
        
        
        self.guiEtGra = tkinter.Label(gui, text='Wygraj milion złotych!')
        self.guiEtGra.place(y=10, x=390)

        self.guiEtMasz = tkinter.Label(gui, text=f'Twoja obecna wygrana: {self.masz} złotych')
        self.guiEtMasz.place(y=60, x=160)

        self.guiEtGwar = tkinter.Label(gui, text=f'Kwota gwarantowana to: {self.gwarantowane} złotych')
        self.guiEtGwar.place(y=60, x=470)

        self.guiEtNumer = tkinter.Label(gui, text='Pytanie 1')
        self.guiEtNumer.place(y=110, x=90)

        self.guiEt = tkinter.Label(gui, text=self.pytania[0].pytanie)
        self.guiEt.place(y=130, x=90)

        self.guiGuzA = tkinter.Button(gui, text=self.pytania[0].odpA, 
                                    command=lambda: self.Klik('a'), height=1, width=50)
        self.guiGuzA.place(x=70, y=180)

        self.guiGuzB = tkinter.Button(gui, text=self.pytania[0].odpB, 
                                    command=lambda: self.Klik('b'), height=1, width=50)
        self.guiGuzB.place(x=470, y=180)

        self.guiGuzC = tkinter.Button(gui, text=self.pytania[0].odpC, 
                                    command=lambda: self.Klik('c'), height=1, width=50)
        self.guiGuzC.place(x=70, y=230)

        self.guiGuzD = tkinter.Button(gui, text=self.pytania[0].odpD, 
                                    command=lambda: self.Klik('d'), height=1, width=50)
        self.guiGuzD.place(x=470, y=230)

        self.guiEtKolo1 = tkinter.Label(gui, text='Pomoc 50/50:')
        self.guiEtKolo1.place(y=300, x=10)

        self.guiEtKolo2 = tkinter.Label(gui, text='Telefon do przyjaciela:')
        self.guiEtKolo2.place(y=330, x=10)

        self.guiEtKolo3 = tkinter.Label(gui, text='Głos publicznosci:')
        self.guiEtKolo3.place(y=360, x=10)

        self.guiGuz5050 = tkinter.Button(gui, text='Pomoc 50/50:', command=self.Kolo5050, height=1, width=40)
        self.guiGuz5050.place(x=10, y=400)

        self.guiGuzTel = tkinter.Button(gui, text='Telefon do przyjaciela', command=self.Telefon, height=1, width=40)
        self.guiGuzTel.place(x=310, y=400)

        self.guiGuzPub = tkinter.Button(gui, text='Głos publicznosci', command=self.Publicznosc, height=1, width=40)
        self.guiGuzPub.place(x=610, y=400)

        self.guiEtImie = tkinter.Label(gui, text="Podaj swoje imię (do rankingu)")
        self.guiEtImie.place(x=300, y=450)
        
        self.inputtxt = tkinter.Text(gui, height=1, width=10)
        self.inputtxt.pack()
        self.inputtxt.place(x=600, y=450)
    
        self.guiRank = tkinter.Button(gui, text="Zobacz ranking", command=Ranking.Wyswietl)
        self.guiRank.place(x=400, y=500)

        self.guiRezygnuj = tkinter.Button(gui, text="Zrezygnuj z dalszej gry", command=self.Rezygnuj)
        self.guiRezygnuj.place(x=600, y=500)

    def Rezygnuj(self):
        if self.Zrezygnuj():
            self.Rozpocznij()
        else:
            gui.destroy()

    def Klik(self, odp):
        if Sprawdz.SprawdzOdpowiedz(self.numer, odp, self.pytania, self.gwarantowane):
            self.AktualizujStan()
            if Nastepne.CzyGraszDalej(self.numer, self.masz, self.gwarantowane, self.pytania, self.mam50teraz):
                self.mam50teraz = 0
                self.aktywneOdpowiedzi = ['a','b','c','d']
                self.guiEtMasz.config(text=f'Twoja obecna wygrana: {self.masz} złotych')
                self.guiEtGwar.config(text=f'Kwota gwarantowana to: {self.gwarantowane} złotych')
                self.guiEtNumer.config(text=f'Pytanie {self.numer}')
                
                self.guiEt.config(text=self.pytania[self.numer-1].pytanie)
                self.guiGuzA.config(text=self.pytania[self.numer-1].odpA)
                self.guiGuzB.config(text=self.pytania[self.numer-1].odpB)
                self.guiGuzC.config(text=self.pytania[self.numer-1].odpC)
                self.guiGuzD.config(text=self.pytania[self.numer-1].odpD)
            else:
                self.Zrezygnuj()
        else:
            if self.Zrezygnuj():
                self.Rozpocznij()
            else:
                gui.destroy()

    def Kolo5050(self):
        poprawna = self.pytania[self.numer-1].dobra
        if self.mam50 == 1:
            self.guiEtKolo1.config(text='Koło 50/50:     Wykorzystałeś to koło!')
        else:
            self.mam50teraz = 1
            odpowiedzi = ['a', 'b', 'c', 'd']
            zle = [odp for odp in odpowiedzi if odp != poprawna]
            zla_odp = random.choice(zle)
            self.aktywneOdpowiedzi = [poprawna, zla_odp]
            random.shuffle(self.aktywneOdpowiedzi)

            self.guiEtKolo1.config(text=f'Pomoc 50/50:     Wybierz: {self.aktywneOdpowiedzi[0]} lub {self.aktywneOdpowiedzi[1]}')
            self.mam50 = 1

    def Telefon(self):
        poprawna = self.pytania[self.numer-1].dobra
        if self.mamtel == 1:
            self.guiEtKolo2.config(text='Telefon do Przyjaciela:     Wykorzystałeś to koło!')
        elif self.mam50teraz == 1:
            p = random.randint(0, 100)
            if p < 70:
                self.guiEtKolo2.config(text=f'Telefon do Przyjaciela:     Przyjaciel podpowiada ci odpowiedź: {poprawna}')
            else:
                podpowiedz = [odp for odp in self.aktywneOdpowiedzi if odp != poprawna][0]
                self.guiEtKolo2.config(text=f'Telefon do Przyjaciela:     Przyjaciel podpowiada ci odpowiedź: {podpowiedz}')

        else:
            p = random.randint(0, 100)
            if p < 41:
                self.guiEtKolo2.config(text=f'Telefon do Przyjaciela:     Przyjaciel podpowiada ci odpowiedź: {poprawna}')
            else:
                
                opcje = ['a', 'b', 'c', 'd']
                opcje.remove(poprawna)
                self.guiEtKolo2.config(text=f'Telefon do Przyjaciela:     Przyjaciel podpowiada ci odpowiedź: {random.choice(opcje)}')
        self.mamtel = 1

    def Publicznosc(self):
        poprawna = self.pytania[self.numer-1].dobra
        if self.mampub == 1:
            self.guiEtKolo3.config(text='Głos publiczności:     Wykorzystałeś to koło!')
        else:
            self.mampub = 1
            if self.mam50teraz:
                poprawne_procent = random.randint(60, 85)
                tekst = 'Głos publiczności:   '
                for odp in self.aktywneOdpowiedzi:
                    if odp == poprawna:
                        tekst += f'{odp}: {poprawne_procent}% '
                    else:
                        tekst += f'{odp}: {100 - poprawne_procent}% '
                self.guiEtKolo3.config(text=tekst)
            else:
                
                poprawne_procent = random.randint(40, 70)
                reszta = 100 - poprawne_procent
                rozklad = [random.randint(0, reszta) for _ in range(3)]
                suma = sum(rozklad)
                if suma > reszta:
                    factor = reszta / suma
                    rozklad = [int(x * factor) for x in rozklad]
                rozklad.append(reszta - sum(rozklad))
                
                tekst = (f'Głos publiczności:   '
                        f'A: {rozklad[0]}% B: {rozklad[1]}% '
                        f'C: {rozklad[2]}% D: {rozklad[3]}%')
                self.guiEtKolo3.config(text=tekst)


class Ranking:
    def Wyswietl():
        os.system("notepad.exe ranking.txt")  

    def Dodaj(imie, wynik):
        if not imie:
            imie = "Anonim"
            
        try:
            with open("ranking.txt", "r") as f:
                wpisy = [linia.strip() for linia in f.readlines() if linia.strip()]
        except FileNotFoundError:
            wpisy = []

        nowy_wpis = f"{imie.ljust(20, '.')}{wynik}"
        wpisy.append(nowy_wpis)
        
        wpisy.sort(key=lambda x: int(x.split('.')[-1]) if x.split('.')[-1].isdigit() else 0, reverse=True)
        
        with open("ranking.txt", "w") as f:
            f.write("\n".join(wpisy))


if __name__ == "__main__":
    gra = Gra()
    gra.Rozpocznij()
    gui.mainloop()