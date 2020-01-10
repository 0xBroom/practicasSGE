import random;

intentosTotal = 5;
intentos = 0;
numeroUser = 0;
pierde = True;
ran = random.randrange(1,21,1);

nombre = input("Como te llamas?\n");
print('Hola '+nombre+'!\n');

print("Estoy pensando en un numero del 1 al 20 Podras adivinarlo?:\n");
for i in range(intentosTotal):
    try:
        numeroUser = int(input());
        intentos = intentos + 1;

        if numeroUser != ran:
            if numeroUser < ran:
                print("Mi número es mayor, vuelvelo a intentar\n");
            elif numeroUser > ran:
                print("Mi número es menor, vuelvelo a intentar\n");
        else:
            print("¡Felicidades! has descubierto el número con ", intentos, " intentos\n");
            pierde = False;
            break;
    except:
        print("Ingresa carácteres validos");
if pierde:
    print("!Oh¡ has perdido, el número era ", ran , "\n");
