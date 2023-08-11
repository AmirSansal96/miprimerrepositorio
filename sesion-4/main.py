def calculadora():
    print("Hola bienvenido a la calculadora")
    op=input("Que operacion quieres ejecutar?(suma/resta)")
    if op == "suma":
        primer_numero = int(input("dame tu primer numero"))
        segundo_numero = int(input("dame tu segundo numero"))
        print(f"tu numero es: {primer_numero + segundo_numero}")
    elif op == "resta":
        primer_numero = int(input("dame tu primer numero"))
        segundo_numero = int(input("dame tu segundo numero"))
        print(f"tu numero es: {primer_numero - segundo_numero}")
       
