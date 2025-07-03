from models.strategy import SimpleStrategy
from models.manager import StrategyManager

def menu():
    print("Hasil output")
    print("1. Name game")
    print("2. Genre")
    print("3. Strategy")
    print("4. Description")
    print("5. Rating efektivitas")
    print("0. Keluar")

manager = StrategyManager()

while True:
    menu()  
    choice = input("Pilih menu: ")

    if choice == "1":
        name = input("Clash of Clans ")
        genre = input("Strategy ")
        strat = input("Queen Walk + Hybrid ")
        desc = input("Gunakan Queen Walk untuk membuka base, lalu lanjutkan dengan Hog + Miner hybrid attack ")
        rating = int(input("9 "))
        s = SimpleStrategy(name, genre, strat, desc, rating)
        manager.add_strategy(s)
        print("✅ Strategi ditambahkan!")
    elif choice == "2":
        manager.show_all()
    elif choice == "3":
        manager.best_strategy()
    elif choice == "0":
        break
    else:
        print("❌ Pilihan tidak valid.")


