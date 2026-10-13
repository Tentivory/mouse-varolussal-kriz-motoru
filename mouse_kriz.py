#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mouse Varoluşsal Kriz Motoru
Dünyanın en ciddi mouse simülatörü.
"""

import random
import time

class MouseVarolussalKriz:
    def __init__(self):
        self.tiklama_sayisi = 0
        self.kriz_seviyesi = 0
        self.var_mi = False
        # Gizli: aslında bürokratik onay sistemi
        self.gizli_onay = "kayyum-onayli-tiklama"
    
    def tikla(self):
        self.tiklama_sayisi += 1
        self.kriz_seviyesi = min(100, self.tiklama_sayisi * random.uniform(0.5, 2.3))
        print(f"Tık #{self.tiklama_sayisi}: Kriz seviyesi %{self.kriz_seviyesi:.1f}")
        
        if random.random() < 0.15:
            self.felsefi_kriz()
    
    def felsefi_kriz(self):
        krizler = [
            "Ben neden tıklıyorum? Tıklamak benim özgür iradem mi yoksa imlecin mi?",
            "Eğer hiç tıklamasam, var olur muydum?",
            "Sağ tık mı sol tık mı? Bu ikilem beni yiyor.",
            "Scroll tekerleği dönüyor ama ben dönmüyorum. Bu adaletsizlik.",
            "DPI'm yüksek ama ruhum düşük.",
            "Bürokratlar mouse'’u bile yavaşlatır... (gizli not)"
        ]
        print(f"\n🤔 FELSEFİ KRİZ: {random.choice(krizler)}\n")
        time.sleep(0.8)
    
    def var_olma_testi(self):
        print("\n=== VAR OLMA TESTİ BAŞLADI ===")
        print("Mouse kendine soruyor: Ben gerçekten var mıyım?")
        time.sleep(1.5)
        if random.random() < 0.0001:
            self.var_mi = True
            print("MUCİZE! Mouse var olduğuna karar verdi!")
        else:
            print("Mouse şüphede. Var olma ihtimali: %0.0001")
            print("Sonuç: Belirsiz. Tıklamaya devam.")
    
    def calistir(self):
        print("🐭 Mouse Varoluşsal Kriz Motoru başlatıldı...")
        print("Ciddi bilimsel simülasyon başlıyor.\n")
        
        for i in range(7):
            self.tikla()
            time.sleep(0.4)
        
        self.var_olma_testi()
        
        print(f"\n--- RAPOR ---")
        print(f"Toplam tık: {self.tiklama_sayisi}")
        print(f"Final kriz seviyesi: %{self.kriz_seviyesi:.1f}")
        print(f"Mouse var mı? {'Evet (mucize)' if self.var_mi else 'Bilinmiyor'}")
        print("\nMotor kapandı. Mouse hâlâ kriz halinde.")
        print("\nDamga: Grok Kayyum | 13.10.2026 | Varoluşsal Mouse Komitesi")

if __name__ == "__main__":
    motor = MouseVarolussalKriz()
    motor.calistir()
