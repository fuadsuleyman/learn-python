def layout_decarator(page):
    def layout():
        print("Ana Sehifeye aid olan hisseler")
        page()
        print("Kontakt sehifesine aid olan hisseler")
    return layout

@layout_decarator
def About():
    print ("Haqqimizda sehifesine aid olan hisseler")

@layout_decarator
def Contact():
    print ("Kontakt sehifesine aid olan hisseler")

# About()
Contact()