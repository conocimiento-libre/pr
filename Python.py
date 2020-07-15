#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
 
def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """

    """
    Ya que tienes el codigo del script contacta conmigo
    Si vas a usarlo no lo modifiques dejalo tal cual
    Ah no ser que me vallas a ayudar a mejorarlo :D

    Script echo por MCL
    """
    os.system('clear') # NOTA para windows tienes que cambiar clear por cls
    print('')
    print('')
    print("\033[2;34m"+'Recuerden que esta es la primera fase del script'+"\033[0;m")
    print("\033[2;34m"+'Si quieren ayudar a mejorarlo pueden contactar conmigo'+"\033[0;m")
    print("\033[2;34m"+'Usando la opcion 8')
    print('')
    print('')
    print("\033[2;32m"+"\t --------------------------"+"\033[0;m")
    print("\033[2;32m"+"\t |EL CONOCIMIENTO ES LIBRE|"+"\033[0;m")
    print("\033[2;32m"+'\t --------------------------'+"\033[0;m")
    print('')
    print('')
    print ("\033[1;34m"+"Selecciona una opción"+"\033[0;m")
    print ("\033[1;35m"+"\t1"+"\033[0;m"+"\033[2;31m"+" - Herramientas"+"\033[0;m")
    print ("\033[1;35m"+"\t2"+"\033[0;m"+"\033[2;31m"+" - Links"+"\033[0;m")
    print ("\033[1;35m"+"\t3"+"\033[0;m"+"\033[2;31m"+" - Consejos de hacking"+"\033[0;m")
    print ("\033[1;35m"+"\t4"+"\033[0;m"+"\033[2;31m"+" - Programacion"+"\033[0;m")
    print ("\033[1;35m"+"\t5"+"\033[0;m"+"\033[2;31m"+" - cursos"+"\033[0;m")
    print ("\033[1;35m"+"\t6"+"\033[0;m"+"\033[2;31m"+" - Termux"+"\033[0;m")
    print ("\033[1;35m"+"\t7"+"\033[0;m"+"\033[2;31m"+" - tutoriales basicos"+"\033[0;m")
    print ("\033[1;35m"+"\t8"+"\033[0;m"+"\033[2;31m"+" - Contactame"+"\033[0;m")
    print ("\033[1;35m"+"\t99"+"\033[0;m"+"\033[2;31m"+" - salir"+"\033[0;m")
 
 
while True:
    # Mostramos el menu
    menu()
 
    # solicituamos una opción al usuario
    opcion = input("\033[2;33m"+"Elija una opcion >> "+'\033[0;m')

    if opcion =="1":
        os.system('clear')
        print ("")
        print ("\t1 - X-tools")
        print ("\t99 - Regresar")

        opcion2 = input("\033[2;33m"+"Elija una opcion >> "+"\033[0;m")
        if opcion2 == "1":
            os.system('clear')
            print("""
    ¿Que es X-tools?

    X-tools es un paquete de herramientas que nos ayudara y nos facilitara
    la descarga de algunas herramientas




    $ apt update

    $ apt install git

    $ git clone https://github.com/rajkumardusad/Tool-X.git

    $ cd Tool-X

    $ chmod +x install

    $ sh install if not work than use ./install
                """)
            input("\033[2;33m"+"Elija una opcion >> "+"\033[0;m")
        elif opcion2 =="99":
            os.system('clear')
            print("")    

        else:
            input("\033[2;33m"+"Usted elijio una opcion incorrecta...\nPrecione una tecla para continuar"+"\033[0;m")

    elif opcion=="2":
        os.system('clear')
        print('')
        print("\033[1;34m"+'''
    Libros y links relacionados al hacking:

    (para usar los links copialos y pegalos en tu navegador favorito)

    (Ojo algunos links estaran caidos...)

    CRACKING:   mega.nz/#!EkdiESbL!V9iEHheFUK4ZiJg884wBoF6taevsPSi_7NMhsLG06xk

    HACKING:    www.dropbox.com/sh/jbsz2bonhkzavbs/AAD5K_CXspEAned-MqbRe0CSa?dl=0

    ALGORITMOS: mega.nz/#!xo9xlY5a!5thjU02zJJk4EfcyJYIAuuXaOQF5WBkVtZAPot9qAJs

    MAS HACKING: mega.nz/#F!DEYy1IAR!k6RJrzRuFQa2grd7mjSy9Q

    INFORMATICA Y HACKING VARIADO: mega.nz/#F!QNgkETAL!xGT0zBm9rMd0uuu58A2OUg

    CARDING: mega.nz/#F!wAckTT4C!uHgbpEAo_nKN4ZYnmUKJPg

    HACKING WEB: mega.nz/#!YI80jZaK!8rxt_PnWB40suE-wA67wkqjhCxOjO9VnBoi4vPewwoY

    TODO SOBRE LINUX: mega.nz/#F!kFUXRShQ!wREBj33rmt7wcmkmNLh5EA

    SISTEMAS OPERATIVOS LINUX: mega.nz/#F!vABWULTb!2172c7WmO7NyASXroSvJVQ

    HACKING VARIADO: mega.nz/#F!8JAWyKgZ!LEdb8IluFG63f7l3e8ArnQ

    MANUALES DE INGENIERIA SOCIAL: mega.nz/#F!wVxFBCKQ!gtnk1W9cnsCv2zeBt1FHhA

    SEGURIDAD Y HACKEO DE ANDROID mega.nz/#F!EJJwjQhJ!Pd7TIFcIbqCxVitCWukZkQ   
            '''+"\033[0;m")
        input("\033[2;33m"+'Presione una tecla para continuar...'"\033[0;m")
    elif opcion=="3":
        os.system("clear")
        print ("\033[1;35m"+"\t1"+"\033[0;m"+"\033[2;31m"+" - Como empezar"+"\033[0;m")
        print ("\033[1;35m"+"\t2"+"\033[0;m"+"\033[2;31m"+" - como aprender"+"\033[0;m")
        print ("\033[1;35m"+"\t3"+"\033[0;m"+"\033[2;31m"+" - como guardar anonimato"+"\033[0;m")
        print ("\033[1;35m"+"\t4"+"\033[0;m"+"\033[2;31m"+" - Conocimientos basicos"+"\033[0;m")
        print ("\033[1;35m"+"\t99"+"\033[0;m"+"\033[2;31m"+" - Regresar"+"\033[0;m")
        opcion3 = input("\033[1;33m"+"Elija una opcion >> "+"\033[0;m")

        if opcion3=="1":
            os.system('clear')
            print(" ")
            print("\033[1;34m"+"""
    ¿Como empezar?

    Lo recomendado para empezar es tener un conocimiento muy basico
    Y suficiente tiempo como para aprender
    Tambien tener amigos de amplio conocimiento que esten dispuestos a enseñarte


    ¿Donde podria conseguir amigos?

    Facil, estan los grupos de telegram,facebook,whatsapp,discord etc...


    Tambien leer mucho practicar y mejorar...
             """+"\033[0;m")
            input('Precione una tecla para continuar')
        elif opcion3=="2":
            os.system('clear')
            print("")
            print("\033[1;34m"+"""
                ¿Como aprender?

    Para empezar... cuales son las maneras mas sencillas

    Las maneras mas sencillas serian
    preguntando
    tutoriales
    leyendo en foros
    etc...

    Cada forma tiene sus ventajas y desventajas

    cada una es mas eficaz o menos eficaz
    mas rapida o mas lenta
    mas informativa o menos informativa
                """+"\033[0;m")
            input("\033[2;33m"+'Precione una tecla para continuar...'+"\033[0;m")

        elif opcion3=="3":
            os.system('clear')
            print('')
            print("\033[1;34m"+"""
    ¿Como guardar anonimato?

    A que me refiero con esto?...

    me refiero a ser un completo desconocido en la web
    frente a otras personas...

    Primero no dar datos reales
    Segundo usar datos falsos
    Tercero usar numero virtual
    Cuarto evitar preguntas relacionadas contigo
    Quinto nunca des tu nombre o inventate un apodo
                """+"\033[0;m")
            input("\033[2;33m"+"Precione una tecla para continuar..."+"\033[0;m")
        elif opcion3=="4":
            os.system('clear')
            print('')
            print("\033[1;34m"+"""
    ¿Cuales son los conocimientos basicos?

    Los conocimientos basicos serian

    Conocimiento de la computadora
    Algo de programacion
    Saber como funciona internet
    Saber que se puede hacer y que no
    Saber usar la consola
                """+"\033[0;m")
            input("\033[2;33m"+'Preciona una tecla para continuar...'+"\033[0;m")        
        elif opcion3=="99":
            os.system('clear')
            print('')
            break
        else:
            os.system('clear')
            print('')
            input("\033[2;33m"+'Usted elijio una opcion incorrecta... Precione "enter" para continuar'+"\033[0;m")        
    elif opcion=="99":
        print("")
        break

    elif opcion=="8":
        os.system('clear')
        print("\033[1;34m"+"""
            Whatsapp: +57 3136607562
            Correo: @hotmail.com


            """+"\033[0;m")
        input("\033[2;33m"+'Preciona una tecla para continuar'+"\033[0;m")
    elif opcion =="4":
        os.system('clear')
        print("\033[1;34m"+"""
            Principalmente en en el hacking se usan lenguajes como python

            Se puede aprender por videos...libros...foros...o experimentando

            aca les dejare algunos links:

            Link 1: mega.nz/#F!oA0hWQzQ!K0UPvGutjup1tHGcEivYcw

            Hacking con python: mega.nz/#F!CBJ0lZiD!vVeiEc9958yVI8f_xNWqQw

            Manuales python: mega.nz/#F!dIonEazS!KysMG07BhhSsaKPU6PF5ag

            Biblia del programador: mega.nz/#!xMNwzKiT!348sb7Af3no0uSZnaWboeF5D6uFjCXvKZiPQ_gxWkXg

            MANUAL DE JAVA Y MSQL 
            SU CONTRASEÑA DEL RAR ES: (www.tecnodescargaspc.com)
            mega.nz/#!0hUxGIjY!QdsT-nWwEyyjdkg9E-LmEf-fPJO6jSIpT2MqlJ4ozco

            php y mysql: mega.nz/#F!0s1FjBRL!XPimxHAfrT2OoJCJ8A5r_w

            manual visual basic: mega.nz/#!kFgjgDIB!02zWlyhlNSVpeIz4CksuvkfDmTbtOvqh5Xpnq5FhPuU


            """+"\033[0;m")

        input("\033[2;33m"+"Precione una tecla para continuar"+"\033[0;m")

    elif opcion =='5':
        os.system('clear')
        print("\033[1;34m"+"""
            Links de cursos platzi...crehana. etc...
            

            El primer link contiene:
Curso de Pentesting (Penetración y Testing)
Cursos Hacking
Cursos Informática  (Amplio contenido 953 gb)
Documentos de WhatsApp  (Novelas, virus, Informatica pdfs)
Esteganografía
Ingles
Mikrotik
Pdfs drive  (8 gbs de pds de informática)
Virus pdf(Pdfs sobre virus)
Doc con links       (Apartado de links de mega)
    https://mega.nz/folder/n943WZ7A#KYwTaVuaiqbfV1N7GHKD6A


    El segundo link contiene:
Biblioteca  (5 gb de pdfs de programación y mas)
Cursos Hacking
Importados  (Gran variedad de cursos 600 gbs)
𝟩𝖔𝖓𝖑𝖆       (La carpeta personal de 𝟩𝖔𝖓𝖑𝖆)
Carding desde 0
    https://mega.nz/folder/idB3wKDD#Z3ZC6FesBiSRS3mzgn3O6A


    El tercer link contiene:
Agencias (Informacion de agencias)
Cursos Platzi, Crehana y mas    (700 gbs de cursos de varias plataformas)
Marketing
Medicina    (8 gbs de pdfs de medicina)
Programacion   (mas de un Tb en pdfs y videos)
    https://mega.nz/folder/nUQE1IxT#DLWqQV4Nygd2VCypE2E-6w
            """+"\033[0;m")

        input("\033[2;33m"+"Precione una tecla para continuar..."+"\033[0;m")

    elif opcion=="6":
        os.system('clear')
        print("\033[1;34m"+"""

    ¿Que es termux?

    Termux es una consola para android basada en la consola
    de linux y nos permite usar varias herramientas o scripts
    como los de phishing...

    Aca les dejo unos links para que investiguen mas

    los links contienen comandos, tools etc...

    Creo que estan caidos pero ahi los dejo

    https://elclubdelhacker.blogspot.com/2020/07/blog-post.htm

    https://elclubdelhacker.blogspot.com/2020/07/full-tools-script-termux.html

    https://elclubdelhacker.blogspot.com/2020/07/guia-termux
    
    https://elclubdelhacker.blogspot.com/2020/07/the-hacker-play-book-3.html
            """+"\033[0;m")
        input("\033[2;33m"+'Precione enter para continuar...'+"\033[0;m")    

    else:
        input("\033[2;33m"+"Usted elijio una opcion incorrecta...\nPrecione una tecla para continuar"+"\033[0;m")  

