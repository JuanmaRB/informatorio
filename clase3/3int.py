registeredUser = ('juanma')
registeredPW = ('asd')

i=0
while i<3:

      usuario=input("ingrese su nombre de usuario: ")
      clave=input("ingrese su clave: ")
      i=i +1

      if str(usuario)==registeredUser:

            print("USUARIO CORRECTO")

            if str(clave)==registeredPW:

                  print("Bienvenido ", usuario)

                  break

            else:

                  print("CLAVE INCORRECTA")

                  if    i==3:

                        print("INTENTOS AGOTADOS")

                        break

      else:

            print("USUARIO INCORRECTO")

            if    i==3:

                  print("INTENTOS AGOTADOS")