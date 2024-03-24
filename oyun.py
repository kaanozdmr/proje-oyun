import random
class savasci:
    def __init__(self, ad, can, kaynak, hasar, dusman_mi, menzil, x, y, alan, sira):
        self.ad = ad
        self.can = can
        self.kaynak = kaynak
        self.hasar = hasar
        self.dusman_mi = dusman_mi
        self.menzil = menzil
        self.x = x
        self.y = y
        self.alan = alan
        self.sira = sira

    def atak(self):
        pass


class Muhafiz(savasci):
    def __init__(self, x, y, alan,sira):
        super().__init__("Muhafız", 80, 10, 20, True, (1, 1, 1), x, y, alan,sira)


class okcu(savasci):
    def __init__(self, x, y, alan,sira):
        super().__init__("Okçu", 30, 20, 60, False, (2, 2, 2), x, y, alan,sira)


class topcu(savasci):
    def __init__(self, x, y, alan,sira):
        super().__init__("Topçu", 30, 50, 100, False, (2, 2, 0), x, y, alan,sira)


class atli(savasci):
    def __init__(self, x, y, alan,sira):
        super().__init__("Atlı", 40, 30, 30, True, (0, 0, 3), x, y, alan,sira)


class saglikci(savasci):
    def __init__(self, x, y, alan,sira):
        super().__init__("Sağlıkçı", 100, 10, 50, False, (2, 2, 2), x, y, alan,sira)


class oyuncu:
    def __init__(self, ad):
        self.ad = ad
        self.kaynak = 200
        self.savasci_list = []
        self.savasci_sayisi = 0
        self.muhafiz_sayisi = 0
        self.okcu_sayisi = 0
        self.topcu_sayisi = 0
        self.atli_sayisi = 0
        self.saglikci_sayisi = 0

    def ekle_savasci(self, savasci, konum):
        self.savasci_list.append((savasci, konum))



class dünya:
    def __init__(self, size):
        self.size = size
        self.matris = [['-' for _ in range(size)] for _ in range(size)]
        self.oyuncular = []

    def add_oyuncu(self, oyuncu):
        self.oyuncular.append(oyuncu)
    def print_dünya(self):
        # Sütun numaralarını yazdır
        print("    ", end="")
        for i in range(self.size):
            print(f"{i + 1:<4}", end="")
        print("\n")

        # Tablo içeriğini oluştur
        for y in range(self.size):
            print(f"{y + 1:<2}|", end="")
            for x in range(self.size):
                if self.matris[x][y] == '-':
                    print(f"{'.' :^3}|", end="")
                else:
                    cell = self.matris[x][y]
                    print(f"{cell.ad[0]}{cell.sira:<2}|", end="")
            print("\n")
    def yerleskeler(self, savasci,oyuncu):
        yerleske = []
        for i in range(self.size):
            for j in range(self.size):
                if self.matris[i][j] == '-':
                    if (i > 0 and self.matris[i - 1][j] != '-') or \
                            (i < self.size - 1 and self.matris[i + 1][j] != '-') or \
                            (j > 0 and self.matris[i][j - 1] != '-') or \
                            (j < self.size - 1 and self.matris[i][j + 1] != '-') or \
                            (j < self.size - 1 and i < self.size - 1 and self.matris[i + 1][j + 1] != '-') or \
                            (j > 0 and i > 0 and self.matris[i - 1][j - 1] != '-') or \
                            (i < self.size - 1 and j > 0 and self.matris[i + 1][j - 1] != '-') or \
                            (i > 0 and j < self.size - 1 and self.matris[i - 1][j + 1] != '-'):
                        yerleske.append((i+1, j+1))
        print(f"yerleişim yerleri {savasci.ad}: {yerleske}")


class Game:
    def __init__(self):
        self.dünya = None
        self.oyunucu_say = 0
        self.sira = 0
        self.oyunucu_index = 0


    def ekran(self):
        while True:
            print("1: 16x16")
            print("2: 24x24")
            print("3: 32x32")
            print("4: boyut gir")
            size = int(input("dünya boyutunu seçiniz: "))
            if size == 1:
                self.dünya = dünya(16)
                break
            elif size == 2:
                self.dünya = dünya(24)
                break
            elif size == 3:
                self.dünya = dünya(32)
                break
            elif size == 4:
                size = int(input("İstediğiniz dünya boyutunu giriniz: "))
                if size < 8 or size > 32:
                    print("Geçerli bir boyut giriniz")
                else:
                    self.dünya = dünya(size)
                    break
            else:
                print("Geçersiz boyut girdiniz!")
                break

        while True:
            print("1: 1 Oyuncu")
            print("2: 2 Oyuncu")
            print("3: 3 Oyuncu")
            print("4: 4 Oyuncu")
            size = int(input("oyuncu sayısını seçiniz: "))
            if size == 1:
                size = int(16)
                self.oyunucu_say = 1
                break
            elif size == 2:
                self.oyunucu_say = 2
                break
            elif size == 3:
                self.oyunucu_say = 3
                break
            elif size == 4:
                self.oyunucu_say = 4
                break
            else:
                print("geçersiz oyuncu sayısı!")
                break

        for i in range(self.oyunucu_say):
            print(f"{i + 1}. oyuncunun adını girin: ",end="")
            oyuncu_ad = input()

            self.dünya.add_oyuncu(oyuncu(oyuncu_ad))


        for i in range(self.oyunucu_say):
            x = random.randint(0, self.dünya.size - 1)
            y = random.randint(0, self.dünya.size - 1)
            self.dünya.matris[x][y] = Muhafiz(x=x, y=y, alan=self.dünya.size, sira=self.dünya.oyuncular[i].muhafiz_sayisi + 1)
            self.dünya.oyuncular[i].muhafiz_sayisi += 1

        self.sıra_tablo()

    def sıra_tablo(self):
        while True:
            print(f"Sıra {self.dünya.oyuncular[self.oyunucu_index].ad} oyuncusunda.")
            self.sira += 1
            self.dünya.print_dünya()

            self.sıra()

            if self.konrtol():
                break

            self.oyunucu_index = (self.oyunucu_index + 1) % self.oyunucu_say

    def sıra(self):
        oyuncu = self.dünya.oyuncular[self.oyunucu_index]
        print(f"{oyuncu.ad}, elinizde {oyuncu.kaynak} kaynak var.")

        while True:
            action = input("Savaşçı eklemek için 'E', pas geçmek için 'P' girin: ").upper()

            if action == 'E':
                if oyuncu.kaynak >= 10:
                    print("1: muhafız")
                    print("2: okçu")
                    print("3: atlı")
                    print("4: topçu")
                    print("5: sağlıkçı")
                
                    savasci_tip = input("Eklemek istediğiniz savaşçı türünü seçiniz ")
                    if savasci_tip == '1':
                        savasci = Muhafiz(x=0, y=0, alan=self.dünya.size, sira=oyuncu.muhafiz_sayisi + 1)
                        oyuncu.muhafiz_sayisi += 1
                    elif savasci_tip == '2':
                        savasci = okcu(x=0, y=0, alan=self.dünya.size,sira=oyuncu.okcu_sayisi + 1)
                        oyuncu.okcu_sayisi += 1
                    elif savasci_tip == '3':
                        savasci = atli(x=0, y=0, alan=self.dünya.size,sira=oyuncu.atli_sayisi + 1)
                        oyuncu.atli_sayisi += 1
                    elif savasci_tip == '4':
                        savasci = topcu(x=0, y=0, alan=self.dünya.size,sira=oyuncu.topcu_sayisi + 1)
                        oyuncu.topcu_sayisi += 1
                    elif savasci_tip == '5':
                        savasci = saglikci(x=0, y=0, alan=self.dünya.size,sira=oyuncu.saglikci_sayisi + 1)
                        oyuncu.saglikci_sayisi += 1


                    else:
                        print("Geçersiz savaşçı türü!")
                        continue


                    self.dünya.yerleskeler(savasci, oyuncu)

                    x = int(input("X koordinatını girin: "))
                    y = int(input("Y koordinatını girin: "))

                    x = x - 1
                    y = y - 1
                    savasci.x = x
                    savasci.y = y

                    if self.geçerli_yerleşim(x, y):
                        self.dünya.matris[x][y] = savasci
                        oyuncu.ekle_savasci(savasci, (x, y))
                        oyuncu.kaynak -= savasci.kaynak
                        break
                    else:
                        print("Geçersiz konum!")
                else:
                    print("Yeterli kaynağınız yok!")
            elif action == 'P':
                break
            else:
                print("Geçersiz eylem!")

    def geçerli_yerleşim(self, x, y):
        if self.dünya.matris[x][y] != '-':
            return False

        for i in range(max(0, x - 1), min(self.dünya.size, x + 2)):
            for j in range(max(0, y - 1), min(self.dünya.size, y + 2)):
                if self.dünya.matris[i][j] != '-':
                    return True

        return False

    def konrtol(self):
        if self.sira >= 3:
            savaşçı_say = sum(1 for oyuncu in self.dünya.oyuncular if oyuncu.savasci_list)
            if savaşçı_say <= 1:
                print("Oyun bitti, kazanan yok.")
                return True

        return False


game = Game()
game.ekran()