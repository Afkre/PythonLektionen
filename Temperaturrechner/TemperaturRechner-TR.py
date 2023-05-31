# Tkinter modülünü "tk" adıyla içe aktarıyoruz
import tkinter as tk

# Hesaplama işlemini gerçekleştiren fonksiyonu tanımlıyoruz
def calculate(event):
    # Çıktıyı varsayılan değere ve siyah renge ayarlıyoruz
    output.config(text="Ausgabe", foreground="black")
    try:
        # Kullanıcıdan alınan girişi float tipine dönüştürüyoruz
        value = float(inp.get())
        # Celsius değerini Fahrenheit'a dönüştürüyoruz
        fahrenheit = (value * 9 / 5) + 32
        # Sonucu çıktı etiketine yazdırıyoruz
        output.config(text=f'{value}°C ergeben {fahrenheit}°F')
    except:
        # Hata durumunda hata mesajını çıktı etiketine yazdırıyoruz ve kırmızı renge ayarlıyoruz
        output.config(text="Eingabe fehlerhaft", foreground="red")
# Tkinter modülünü "tk" adıyla içe aktarıyoruz
import tkinter as tk

# Hesaplama işlemini gerçekleştiren fonksiyonu tanımlıyoruz
def calculate(event):
    # Çıktıyı varsayılan değere ve siyah renge ayarlıyoruz
    output.config(text="Ausgabe", foreground="black")
    try:
        # Kullanıcıdan alınan girişi float tipine dönüştürüyoruz
        value = float(inp.get())
        # Celsius değerini Fahrenheit'a dönüştürüyoruz
        fahrenheit = (value * 9 / 5) + 32
        # Sonucu çıktı etiketine yazdırıyoruz
        output.config(text=f'{value}°C ergeben {fahrenheit}°F')
    except:
        # Hata durumunda hata mesajını çıktı etiketine yazdırıyoruz ve kırmızı renge ayarlıyoruz
        output.config(text="Eingabe fehlerhaft", foreground="red")

# Tkinter penceresini oluşturuyoruz
window = tk.Tk()
# Pencere başlığını ayarlıyoruz
window.title("Temperaturberechnung")
# Pencerenin yeniden boyutlandırılabilirliğini devre dışı bırakıyoruz
window.resizable(False, False)
# Pencere boyutunu ve konumunu ayarlıyoruz
window.geometry("250x200+50+50")
# Pencereyi araç penceresi olarak ayarlıyoruz
window.attributes('-toolwindow', True)

# Başlık etiketini oluşturuyoruz ve pencereye ekliyoruz
header = tk.Label(window, text="Temperaturberechnung von °C in F")
header.pack()

# Giriş kutusunu oluşturuyoruz ve odaklanıyoruz
inp = tk.Entry(window, width="30")
inp.focus()
inp.pack()

# Hesaplama düğmesini oluşturuyoruz ve olay bağlamını yapılandırıyoruz
btn = tk.Button(window, text="berechnen", width="25")
btn.bind('<Button>', calculate)
btn.pack(pady=15)

# Çıktı etiketini oluşturuyoruz
output = tk.Label(window, text="Ausgabe")
output.pack()

# Pencereyi çalıştırıyoruz (ana döngü)
window.mainloop()

# Tkinter penceresini oluşturuyoruz
window = tk.Tk()
# Pencere başlığını ayarlıyoruz
window.title("Temperaturberechnung")
# Pencerenin yeniden boyutlandırılabilirliğini devre dışı bırakıyoruz
window.resizable(False, False)
# Pencere boyutunu ve konumunu ayarlıyoruz
window.geometry("250x200+50+50")
# Pencereyi araç penceresi olarak ayarlıyoruz
window.attributes('-toolwindow', True)

# Başlık etiketini oluşturuyoruz ve pencereye ekliyoruz
header = tk.Label(window, text="Temperaturberechnung von °C in F")
header.pack()

# Giriş kutusunu oluşturuyoruz ve odaklanıyoruz
inp = tk.Entry(window, width="30")
inp.focus()
inp.pack()

# Hesaplama düğmesini oluşturuyoruz ve olay bağlamını yapılandırıyoruz
btn = tk.Button(window, text="berechnen", width="25")
btn.bind('<Button>', calculate)
btn.pack(pady=15)

# Çıktı etiketini oluşturuyoruz
output = tk.Label(window, text="Ausgabe")
output.pack()

# Pencereyi çalıştırıyoruz (ana döngü)
window.mainloop()
