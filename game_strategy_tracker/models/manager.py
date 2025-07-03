import os
import json
from models.strategy import SimpleStrategy

class StrategyManager:
    def __init__(self, filename=None):
        base_path = os.path.dirname(__file__)  # ambil path saat ini (models/)
        default_path = os.path.abspath(os.path.join(base_path, "..", "strategies.json"))
        self.filename = filename if filename else default_path
        self.strategies = self.load_data()

    def add_strategy(self, strategy):
        self.strategies.append(strategy)
        self.save_data()

    def show_all(self):
        if not self.strategies:
            print("❌ Belum ada strategi yang disimpan.")
            return
        for i, s in enumerate(self.strategies, 1):
            print(f"\n[{i}] {s.get_info()}")
            print(f"Strategi: {s.strategy_name}")
            print(f"Deskripsi: {s.description}")
            print(f"Rating: {s.rating}/10 | Evaluasi: {s.evaluate()}")

    def best_strategy(self):
        if not self.strategies:
            print("❌ Belum ada strategi terbaik.")
            return
        best = max(self.strategies, key=lambda s: s.rating)
        print("\n✅ Strategi terbaik:")
        print(f"{best.strategy_name} - {best.rating}/10")
        print(best.description)

    def save_data(self):
        data = [vars(s) for s in self.strategies]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)

    def load_data(self):
        print(f"📂 Membaca file dari path: {self.filename}")
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return [SimpleStrategy(**item) for item in data]
        except Exception as e:
            print("❌ Gagal membaca JSON:", e)
            return []
