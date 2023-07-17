import os
import core
from datetime import date
global diccCi
diccCi = {"data":[]}

isRun = True
# def loadInfo():
#     if core.checkFile("citas.json") == True:
#         global diccCi
#         diccCi = core.loadFile("citas.json")
#     else:
#         diccCi = core.saveInfo("citas.json",diccCi)
# loadInfo()

def menu():
    try:
        isRun = True
        horas =["8am-9am","9am-10am","10am-11am","11am-12m","2pm-3pm","3pm-4pm","4pm-5pm"]
        mes = [{"enero":31},{"febrero":28},{"marzo":31},{"abril":30},{"mayo":31},{"junio":30},{"julio":31},{"agosto":31},{"septiembre":30},{"octubre":31},{"noviembre":30},{"diciembre":31}]
        year= date.today().year

        while isRun:
            os.system("clear")
            print("+",'-'*29,'+')
            print("|{:^8}{}{:^8}|".format('','GESTIONAR CITAS',''))
            print("1.Agregar cita")
            print("2.Buscar cita")
            print("3.Modificar cita")
            print("4.Cancelar cita")
            print("5.Salir del programa")
            op = int(input("Seleccione una opcion: "))
            if op == 1:
                diccCi = core.loadFile("citas.json")
                horS = ''
                mon = ''
                horBol = True
                os.system("clear")
                nomP = input("Ingrese el nombre del paciente: ")
                os.system("clear")
                print("+",'-'*29,'+')
                print("|{:^8}{}{:^8}|".format('','SELECCION MES',''))
                for i,item in enumerate(mes):
                    for j,k in enumerate(item.keys()):
                        print(i+1,".",k)
                fecP = int(input("Seleccione el mes de la cita: "))
                for i,item in enumerate(mes):
                    if (fecP-1 == i):
                        for j,k in enumerate(item.items()):
                            mon = k
                            horBol = True
                        break
                    else:
                        horBol = False
                        horS = "Mes no registrado"
                if horBol == True:
                    dia = int(input("Ingrese la fecha del dia, ejemplo(01,08,12,31): "))
                    if dia > k[1]:
                        horBol = False
                        horS = "Dia fuera de rango de los dias del mes"
                    if horBol:
                        if dia>0 and dia<10:
                            dia = f"0{dia}"
                        if fecP>0 and fecP<10:
                            fecP = f"0{fecP}"
                        dateC =  f"{year}-{fecP}-{dia}"
                        if(str(date.today()) <= dateC):
                            os.system("clear")
                            for i,item in enumerate(horas):
                                print(i+1,".",item)
                            horC = int(input("Seleccione la hora de la cita: "))
                            for i,item in enumerate(horas):
                                if horC-1 == i:
                                    horS = item
                                    horBol = True
                                    break
                                else: 
                                    horBol = False
                                    horS = "Hora no registrada"
                            if horBol:
                                os.system("clear")
                                movC = input("Motivo de la consulta: ")
                                cont = 0
                                if len(diccCi["data"]) >=1:
                                    cont = diccCi["data"][-1]["codigo cita"]+1
                                else:
                                    cont=1
                                data = {
                                    "codigo cita":cont,
                                    "nombre paciente":nomP,
                                    "fecha cita":dateC,
                                    "hora cita":horS,
                                    "motivo consulta":movC
                                }
                                diccCi["data"].append(data)
                                core.saveInfo("citas.json",data)
                            else:
                                print(horS)
                                input("Enter para continuar....")
                        else:
                            print(f"Fecha ingresada invalida, debe ser fecha a futuro no fecha pasada:{dateC}\n fecha actual: {str(date.today())}")
                            input("Enter para continuar....")
                    else:
                        print(horS)
                        input("Enter para continuar....")
                else:
                    print(horS)
                    input("Enter para continuar....")
            elif op == 2:
                diccCi = core.loadFile("citas.json")
                pa = []
                if(len(diccCi["data"]) == 0):
                    os.system("clear")
                    print("No hay citas disponibles para mostrar...")
                    input("Enter para continuar....")
                else:           
                    os.system("clear")
                    print("+",'-'*29,'+')
                    print("|{:^8}{}{:^8}|".format('','BUSQUEDA CITA',''))
                    print("1.Consultar cita por nombre de paciente: ")
                    print("2.Consultar cita por fecha: ")
                    opc = int(input("Seleccion un opcion: "))
                    if(opc == 1):
                        os.system("clear")
                        nomP = input("Ingrese el nombre del paciente: ")
                        for i,item in enumerate(diccCi["data"]):
                            nom = item["nombre paciente"]
                            if nom.lower() == nomP.lower():
                                pa.append(item)
                        print("+",'-'*60,'+')
                        print("|{:^25}{}{:^20}|".format('','CITAS DISPONIBLES',''))
                        print("+",'-'*60,'+')
                        print("|{:^8}|{:^10}|{:^10}|{:^10}|{:^20}|".format("Codigo","Nombre","Fecha","Hora","Motivo Consulta"))
                        if len(pa) == 0:
                            print("No se encontraron pacientes con ese nombre")
                        else:
                            for i,item in enumerate(pa):
                                print("+",'-'*60,'+')
                                print("|{:^8}|{:^10}|{:^10}|{:^10}|{:^20}|".format(item["codigo cita"],item["nombre paciente"],item["fecha cita"],item["hora cita"],item["motivo consulta"]))
                        print("+",'-'*60,'+')
                        input("Enter para continuar....")
                    elif opc == 2:
                        os.system("clear")
                        feP = input("Ingrese la fecha de la cita a buscar con el formato(AAAA-MM-DD) ejemplo(2023-02-01): ")
                        if str(date.today()) > feP:
                            print(f"Fecha ingresada invalida, debe ser una fecha futura, fecha ingresada: {feP}\n fecha actual: {str(date.today())}")
                            input("Enter para continuar....")
                        else:
                            for i,item in enumerate(diccCi["data"]):
                                if item["fecha cita"] == feP:
                                    pa.append(item)
                            print("+",'-'*60,'+')
                            print("|{:^25}{}{:^20}|".format('','CITAS DISPONIBLES',''))
                            print("+",'-'*60,'+')
                            print("|{:^8}|{:^10}|{:^10}|{:^10}|{:^20}|".format("Codigo","Nombre","Fecha","Hora","Motivo Consulta"))
                            if len(pa) == 0:
                                print("No se encontraron pacientes con esa fecha")
                                print("+",'-'*60,'+')
                                input(":")
                            for i,item in enumerate(pa):
                                print("+",'-'*60,'+')
                                print("|{:^8}|{:^10}|{:^10}|{:^10}|{:^20}|".format(item["codigo cita"],item["nombre paciente"],item["fecha cita"],item["hora cita"],item["motivo consulta"]))
                            print("+",'-'*60,'+')
                            input("Enter para continuar")    
            elif op == 3:
                new = ''
                diccCi = core.loadFile("citas.json")
                res = ''
                mon = ''
                editInfo = {}
                bol = False
                if(len(diccCi["data"]) == 0):
                    os.system("clear")
                    print("No hay citas disponibles para mostrar...")
                    input("Enter para continuar....")
                else:
                    os.system("clear")
                    print("+",'-'*29,'+')
                    print("|{:^8}{}{:^8}|".format('','MODIFICAR CITA',''))
                    print("Solo podra modificar la fecha y hora")
                    print("+",'-'*29,'+')
                    cod = int(input("Ingrese el codigo de la cita: "))
                    for i,item in enumerate(diccCi["data"]):
                        if cod == item["codigo cita"]:
                            editInfo = item
                            bol = True
                            break
                        else:
                            bol = False
                    if bol:
                        os.system("clear")
                        print("+",'-'*29,'+')
                        print("|{:^8}{}{:^8}|".format('','SELECCION NUEVO MES',''))
                        for i,item in enumerate(mes):
                            for j,k in enumerate(item.keys()):
                                print(i+1,".",k)
                        fecP = int(input("Seleccione el nuevo mes para Reagendar la cita: "))
                        for i,item in enumerate(mes):
                            if (fecP-1 == i):
                                for j,k in enumerate(item.items()):
                                    bol = True
                                break
                            else:
                                bol = False
                                res = "Mes no registrado"
                        if bol == True:
                            dia = int(input("Ingrese la fecha del dia, ejemplo(01,08,12,31): "))
                            if dia > k[1]:
                                bol = False
                                res = "Dia fuera de rango de los dias del mes"
                            if bol:
                                if dia>0 and dia<10:
                                    dia = f"0{dia}"
                                if fecP>0 and fecP<10:
                                    fecP = f"0{fecP}"
                                newDateC =  f"{year}-{fecP}-{dia}"
                                if(str(date.today()) <= newDateC):
                                    os.system("clear")
                                    for i,item in enumerate(horas):
                                        print(i+1,".",item)
                                    horC = int(input("Seleccione la hora de la cita: "))
                                    for i,item in enumerate(horas):
                                        if horC-1 == i:
                                            res = item
                                            bol = True
                                            break
                                        else: 
                                            horBol = False
                                            res = "Hora no registrada"

                                    for i,item in enumerate(diccCi["data"]):
                                        if item["codigo cita"] == cod:    
                                            diccCi["data"][i]["fecha cita"] = newDateC
                                            diccCi["data"][i]["hora cita"] = res
                                            core.editFile("citas.json",diccCi)
                                            bol = True
                                            break
                                        else:
                                            bol = False
                                    if bol:
                                        os.system("clear")
                                        print("Se actualizo satisfactoriamente: ")
                                        input("Enter para continuar ")
                                    else:
                                        print("No se actualizo: ")
                                        input("Enter para continuar....")
                                else: 
                                    os.system("clear")
                                    print("Fecha invalida, la fecha no puede ser de meses anteriores")
                                    input("Enter para continuar....")
                        else:
                            print("Mes no registrado")
                            input("Enter para continuar....")        
                    else:
                        os.system("clear")
                        print("Cita no registrada")
                        input("Enter para continuar....")
            elif op == 4:
                diccCi = core.loadFile("citas.json")
                bol = False
                if(len(diccCi["data"]) == 0):
                    os.system("clear")
                    print("No hay citas disponibles para mostrar...")
                    input("Enter para continuar....")
                else:
                    os.system("clear")
                    print("+",'-'*38,'+')
                    print("|{:^15}{}{:^12}|".format('','CANCELAR CITA',''))
                    codC = int(input("Ingrese el codigo de la cita a eliminar: "))
                    for i,item in enumerate(diccCi["data"]):
                        if codC == item["codigo cita"]:
                            print("|{:^8}|{:^10}|{:^10}|{:^10}|{:^20}|".format("Codigo","Nombre","Fecha","Hora","Motivo Consulta"))
                            print("+",'-'*60,'+')
                            print("|{:^8}|{:^10}|{:^10}|{:^10}|{:^20}|".format(item["codigo cita"],item["nombre paciente"],item["fecha cita"],item["hora cita"],item["motivo consulta"]))
                            print("+",'-'*60,'+')
                            opci = int(input("Seguro de eliminar la cita: 1(SI) 2(NO)"))
                            if opci == 1:
                                diccCi["data"].pop(i)
                                core.editFile("citas.json",diccCi)
                                bol = True
                                break
                            elif opci == 2:
                                pass
                            else:
                                print("Valor invalido")
                                input("Enter para continuar...")
                                break
                        else: 
                            os.system("clear")
                            print("cita no encontrada")
                            bol = False
                    if bol:
                        print("Se eliminó satisfactoriamente: ")
                        input("Enter para continuar...")
                    else: 
                        print("No se eliminó: ")
                        input("Enter para continuar...")
            elif op == 5:
                os.system("clear")
                print("Gracias por usar el programa, hasta luego...")
                input("Enter para continuar....")
                isRun = False
            else:
                print("Opcion no valida")
                input("Enter para continuar....")
                menu()
    except ValueError: 
        print("VALOR INGRESADO INVALIDO")
        input("Enter para continuar....")
        menu()
menu()