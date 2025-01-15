
def extra():
    print("List of Extra Command in Tiffany's Command")
    print("1. search <pattern> - Temukan jejak; cari file atau direktori berdasarkan nama")
    print("2. tree - Peta akar; tampilkan struktur direktori sebagai pohon megah")
    print("3. find_large <size> - Perburuan raksasa; cari file yang lebih besar dari ukuran tertentu dalam KB")
    print("4. size - menampilkan ukuran file yang ingin ditelusuri")
    print("5. kobo - Panggil keceriaan; lihat gambar chibi lucu Kobo Kanaeru")
    print("6. pantun - Nikmati seni berpantun; buat pantun menghibur dan menginspirasi")
    print("7. treec - Peta akar; tampilkan struktur direktori utama yaitu (C) sebagai pohon megah")


kobo = """
............---------------------:.................................----------------------...........
...........:---------------------:................................:----------------------...........
...........:---------------------:................................:---------------------:...........
...........:---------------------.................:--:............:---------------------............
............--------------------:................:----:............--------------------:............
:...........:------------------.:+%*=---==*%+:..--------...........:-------------------.............
--...........:---------------.:%*:.::::::-:::-**..::..-+*#*=:.......:-----------------..............
---...........:------------:.%*::::-::::-=====---***----::::::-#-....:--------------:...............
----............:--------:.-%=:::=-:-==========**--==-----:::::..-+:...:----------:................:
-----...............::::..:%-:::=**=:....:=*#+*--==---==++++-::....-=.......:::...................:-
-----:...............=****-=:::=#:.......:-++#**#**+#=.......+-::::::+............................--
------:...............-*:.:-::-%-...:+#*+=---::::::::-=**:::-:=+::::::*:..=......................---
------:..................:*-::-%.-#+=-::::::::::.:::::::::==.:.+:::::::.:=:.....................:---
-------...................*-:.:@*-::::::::::::....::::-:::..-*.-=:::::+*:....:--................----
-------..............-::%-:-.=*:::::..::::::......::::=+:::..:++=.:::.:#*+..:----..............:----
-------............:----:.:##-::::...::::::::::::.-::::+*::::::-*-..++::+::-------:............-----
------:...........:-----:.=*:::=::::-=:::::::::::.-=----+*-:::-:-+*..*-..:---------:...........-----
------:..........:-----::#*:::=----=*-::::::::.....-=-:.=:*-:::-:=++-...:-----------:..........-----
------..........:-----:.++*:--=---:*+:::...........+-..:.-=*-::-::=#...:-------------:.........:----
-----..........:------:-*+-:-=+-:::++..-......*:.-*#-+..##:*#::-::==-.:---------------:.........----
----..........:-:.----:=*+..:=:.:..*:*:+*::*-*++-+:::::*##::=-:-:::+%.:-----:=::-------:........:---
--:..........:-:-*:..:.:#....:+.:%--*:::::::.::+::=:-*%#+-:::%:=::.++#:..:..==%:--------..........--
:............--::#.+#**+.--..==#=++#%%#=:.......:#%#%#**#%%#++===-:+:+-+###+.-#*+-:-----:...........
............::.:+**:::=+#:.:+=-#@%#++++*#........+::::::::-:=-*:.-+*:+-:::-=-:..=+--.---:...........
............:.#:.....:-++*+=*#%*-::::::.....:-===-:.:::::-:::-::.=+-:*+*+====+*%%*+*=----...........
...........::=:.::....:-=#--++=:-::::::..+=========:..::::::::=::---:*--====+++=++#*.----...........
...........:.+=:.:*##+==+%--%---::::::...+===---===:..........=::+*=:+=*+=+++=++**+*=:--:...........
...........::..=%=======-*+-*:::::::......=--------...........-:.:+-:***==+++**+*+**#+:-............
.............=%==+=++===+%*-%::::::........=-----..........:::::=*+:=%**+*++****=*###%-:............
:...........+#+++==++=++*+++-*:::....................:::::=*%=--:=+-*#*###+**#*##*##***....==.......
--..........%++*+***=+**#-=%=--++-:::::::::::::::::-+***=-:#::::::+=###*#*#%%#*##%*#%#*...+:#.......
---........+#***+**+*##*--=%+=-:---=**+++****%****=+=::::-*-.+:...:*%%##**=--------+%%*:*=..#:......
----.......%*##+##*#%%:---+*+=:.:-.::#:::+==-:-#::#**::--=%=-+**:.:+**%#*----+**+---%%-:....#......:
-----......@####=-=#%%=:-=*%::-......#=#+:*=::::=::#+:-#=--=%@+===++-#*#+++=++=++++=#-::..:-=#+...:-
-----:%:...+%*-----*-=:--=+-==#..:%:*-----**=====--***-----=+---=-=*=-*::#*==++++*#-:::..::::*....--
------=.:=+=+%==+*#:::::=+:-=*-***=*===---*+-*--::-#*---=+*=----=-++=--:+*++*=#=----::::.....*:..---
----::+.....:-#+++#...-+:.:-==---=++-+--::*+==##*++*#=-++-.:--::::++=--===-..-+---=--::.......*::---
-----.+-....::-=**%+#-+=::.:-----:-=*:-.:.+*..-+=++*#:.-==++=:..-=.=*=----..:+----:--:......=:=::---
------::+:......:-=+*=*==:..:.::.-:..:*-..=#:..-:=-:#:...:*::*.==**+=-::.++:+=---::.::..::..=-%:----
-------..-**#-.::::-:--+=+=+-...+.+*=::...-#:.:::+=-#...::::--==--+#*-:.:++----:::....-*+:-*...-----
------:....#...::::::--+#+=+%.:%+-+-=:::::=#-:=%=*+*#::::::::=-::.-+=====--:---:.....-==#:.....-----
------:...=......:::::::---====@+-+#%%%=:-*#*--=*+=#%=-====-====+++++=---:::::::...:::-*-......-----
------...:*.....::..::.....:...*##+=*%##==+*=-::+=:#-:::::::-::-+==++::......+:*:-*=.:.........:----
-----.....*.==*.....-==:...:*:.#*%#=*###:--=+*#%**%%#********####*=-+=...++-*::..::---:.........----
----......:+*..==..=-..+.=+-.:=+*#%=+##%#####***=*==-:::::.-=+=-----+#*+*+:.:----------:.........---
--:..........:-:..::.:::..:---:.*+***+===---:::-:#-=====+=-----=**=*:.:::::-------------..........:-
:............-----------------:.+--------=*+-*%#=#*%%+--=++#*=-:::::#-.-----------------:...........
............:------------------::+-=+##%#%#%####%%%%#+-:.+##--:::+##%#:.----------------:...........
............-------------------.+######*=:#:..............:+:-###+--%##+-::--------------...........
...........:-----------------::*=%=----+*@:.................+#=--==--++*=+.--------------...........
...........:----------------::+=+**-===+#....................:+--==+**=:.:--------------:...........
...........:----------------::+###*###**-.........:--:.........:-::..::-----------------............
............------------------:..................:----:............--------------------:............
:...........:-------------------................--------...........:-------------------.............
"""
def gradient(ascii_art, start_color, end_color):

    def interpolate(start, end, factor):
        return round(start + (end - start) * factor)

    def rgb_to_ansi(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    lines = ascii_art.splitlines()
    gradient_art = ""

    total_chars = sum(len(line) for line in lines)  # Total karakter dalam gambar
    char_index = 0

    for line in lines:
        gradient_line = ""
        for char in line:
            factor = char_index / max(total_chars - 1, 1)  # Normalisasi ke rentang [0, 1]
            r = interpolate(start_color[0], end_color[0], factor)
            g = interpolate(start_color[1], end_color[1], factor)
            b = interpolate(start_color[2], end_color[2], factor)
            gradient_line += f"{rgb_to_ansi(r, g, b)}{char}"
            char_index += 1
        gradient_art += gradient_line + "\033[0m\n"  # Reset warna per baris
    return gradient_art

# Definisi warna awal dan akhir (RGB)
start_color = (255, 255, 255)  # White (RGB)
end_color = (0, 0, 255) 
sec_color = (205,133,63)
blue_color = (135,206,235)

def kobo_kanaeru():
    print(gradient(kobo, start_color, end_color))



  # Blue (RGB)

# Gambar ASCII Tokyo
def tokyo():

    tokyo = '''
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        %&&&&&&&&#((&**%&&&&&///////.&&/(.,..,......*......... ..*..//*//&&&&&&&&&&&&&&&&&&&&###&@%%@@@@@&&&
        &&&&&&%&&//#@**%%&&#&(,/*/((.##/,.. .(...  ......   .. ///,(////(&#&/####(##(/%%&&&&&%##%%%%%&&&&###
        &%&%&&@#%(//&**%%%&&&(//////*&&*****,*   ......... .  ..///*///((&&&####(###%(&&&&&&&/#%#&%%&&&&&%#%
        &@@&&&%%%&&#&(/*%#&&%////,**,&&****.,.............   .////////(((%&&(####((##(&&&&&&%%%%%%&&@&%%&@@%
        &&&@&&&%&%@@&&@&&&&&&#((/***,%&******,*,,.               //.(#(((%%%(#######%/%&&&&&&%%%@%&&@&&&&&&&
        &&@&@%&%%&&%&****&&&(//(////*%%///****,,,,.  .*   . .. .///,/(/((%%%(#(((((#%/%&%%&%%####%%%&&&#&&&%
        @@&&&&@%###@&@**%%&&&///((///%%/*****,,,..................,//(//(%%&(((#((((#/%%%%&%%###%%///#&&&&%&
        &&&&&&%@&&%&&&*#%%&&%#(***///%%/**/***,,,,,,,..........,*,..../((%%@((#/%/###/%%%%&%%%###%#@&&((&&&&
        &&&&&&&&&&%%%&&%%%%&&/%/////*(%/////****,,,,,,..@....,.***///,///&&@@(#(#%##%/%&&%%%%/(*(%(((&%%&@@@
        @&@@&&&@@@&@@&@@&&@&&%(/****/#%///(((***,,,,,...@@@%.,*****//***/##%#####%####%&&%%%#((/(%(.%&%#%&&@
        @@@@&&@@@@&@@&@@@&@&&##@***,,##*&&&&&&@@*,,,,,,,@@@@@,*********/*###(/(#(#(##/%%%%%%&(#&@%@@%%%%%%%%
        @@@@&&&@@@&@@&&@@&@@@@/@(#*&&&//%&&&%&@%,,,,,,,,@@@@@@,,,/#%*(,*/###&&(((%(/(/%%%%%%&&&@@&&@@@@@&&%&
        @&&&&&&&&&&&&&&@@&&%%@@@%&&%&&/#///(///#(//*///*@@@@@@@*//#***##*%####((,&#(((%%%%%&%@&&@@%@@&@@(&&&
        &@@@@@@&&&&@@@&&@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%&@@@@@&@@&&&&&&@@@@@@@@@@@@@@@@@@@@@&@&@@@@@@@@@@@&@&&
        &@@&@@@&&&&&@@@&@@@&@@&&@@&@&&&&%&&&&&&&&&&&%&%&%@@@###@@&&&&@@@@@@@@@@@@@@@@@@@&&&&&@@@@@@@@@@@@&@@
        @@@@&&@@@&&#%&@%&@@@@@@@&&&@&/&&&&&&&&&&&&&&@@@@@@@@&&@@&&&&&@@@@@@@@@@@@@@@@@@@@&&&&@@@@@@@@@@@@&&@
        @@@@@@@%%%%@#%%#@&@@@@@@&&&@&&&&&&&&&&&&&&&&@@&&&&&&&@@@&&&&&@@@@@@@@@@@@@@@@@@@@&&@&@@&@@@@&@@@@@@@
        &@@&&&&%%&&%####@&@@@@@@@@&@@@&&&&&&&&&&&&&&@@@@@@@@@@@@&&&&&@@@@@@@@@@@@@&@@@@@@&@@@@&&@@&@@@@@&&@@
        &&@&@&@&@@@@@@@@@@@&@&&&&&&@&&&&&&%&&&&%&&&&@@&&&&&&&@@@&&@&&@@@/@@@@@@@@&&@@@&@@@@@@@&@@@&@@&&&&&@@
        &@@@@@@@@&&@@@@@@@&@@@@@@@@@%&&&&&&&&&%%%%%#@@%%%(/*%&&@%&@&&&&@&&&&&&&&/&&&&&&&&&&&&&&@&&&&&&&&&&&&
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    '''

    # Mencetak teks dengan warna merah menggunakan escape sequence RGB
    print(gradient(tokyo, blue_color, sec_color))

# Panggil fungsi


pantun_menyindir = [
    "Kalau ada sumur di ladang,",
    "Boleh kita menumpang mandi.",
    "Kalau ada umur panjang,",
    "Boleh kita berjumpa lagi."
]

pantun_lucu = [
    "Buah mangga buah kedondong,",
    "Dimakan pagi di atas papan.",
    "Hati siapa takkan tertawa,",
    "Melihat kucing bermain sapu."
]
# Pantun function
def pantun_menu():
    print("\nSelamat datang di pembuat pantun!")
    print("Pilih jenis pantun:")
    print("1. Menyindir")
    print("2. Lucu")

    choice = input("Pilihan Anda (1/2): ").strip()
    
    if choice == "1":
        display_pantun(pantun_menyindir, "Pantun Menyindir")
    elif choice == "2":
        display_pantun(pantun_lucu, "Pantun Lucu")
    else:
        print("Pilihan tidak valid. Kembali ke menu utama.")

# Display pantun
def display_pantun(pantun_list, title):
    print(f"\n{title}:")
    for line in pantun_list:
        print(line)
        command = input("Ketik 'cakepip' untuk melanjutkan atau 'menu' untuk kembali: ").strip().lower()
        if command == "cakepip":
            continue
        elif command == "menu":
            print("Kembali ke menu utama...")
            return
        else:
            print("Input tidak dikenali. Melanjutkan...")
    print("\nPantun selesai. Kembali ke menu utama...")
