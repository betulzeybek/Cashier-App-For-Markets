ALT_ISIL_DEGERI=8250
yakit_birim_fiyati= float(input("yakıt birim fiyatını giriniz:"))
su_sicakligi= float(input("su sıcakğını giriniz:"))
bina_metrekare= float(input("binanın toplam metre karesini giriniz:"))
bina_aylik_isinma_gideri= float(input("binanın aylık ısınma giderini giriniz:"))
binanin_harcadigi_su= float(input("binanın aylık su harcamasını giriniz:"))
daire_metrekare= float(input("dairenizin metre karesini giriniz:"))
daire_sicak_su_tuketimi= float(input("dairenizin su tüketim miktarını giriniz:"))

bina_su_isitma_gideri= ((1200*(su_sicakligi-10)*yakit_birim_fiyati/ALT_ISIL_DEGERI)*binanin_harcadigi_su)
bina_ortaksu_isitma_gideri= (bina_aylik_isinma_gideri-bina_su_isitma_gideri)
daire_su_isitma_gideri= (bina_su_isitma_gideri*daire_sicak_su_tuketimi/binanin_harcadigi_su)
daire_ortak_isinma_gideri= (bina_ortaksu_isitma_gideri*daire_metrekare/bina_metrekare)
daire_toplam_isinma_gideri= (daire_ortak_isinma_gideri+daire_su_isitma_gideri)

print(f'Binanın su ısıtma gideri: {bina_su_isitma_gideri:.2f}')
print(f'Bina ortak su ısıtma gideri: {bina_ortaksu_isitma_gideri:.2f}')
print(f'Dairenin su tüketim miktarı: {daire_sicak_su_tuketimi:.2f}')
print(f'Daire su isinma gideri: {daire_su_isitma_gideri:.2f}')
print(f'Daire ortak alan ısınma gideri: {daire_ortak_isinma_gideri:.2f}')
print(f'Daire toplam isima gideri: {daire_toplam_isinma_gideri:.2f}')
