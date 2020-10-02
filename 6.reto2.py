def prestamo(informacion: dict)-> dict: 
    
    id_prestamo = informacion['id_prestamo']
    casado = informacion['casado']
    dependientes = informacion['dependientes']
    educacion = informacion['educacion']
    independiente = informacion['independiente']
    ingreso_deudor = informacion['ingreso_deudor']
    ic = ingreso_deudor/9
    ingreso_codeudor = informacion['ingreso_codeudor']
    cantidad_prestamo = informacion['cantidad_prestamo']
    plazo_prestamo = informacion['plazo_prestamo']
    historia_credito = informacion['historia_credito']
    tipo_propiedad = informacion['tipo_propiedad']

    #Rombo Inicial Aprovacion Historia 
    if historia_credito == 1: #Verdadero
             # Izquierda Rombo2
          if ingreso_codeudor > 0 and ic > cantidad_prestamo:
               return {'id_prestamo': id_prestamo, 'aprobado': True} # verdadero fin Verdadero
             # Izquierda Rombo
          elif (dependientes > 2 or dependientes == '3+') and independiente == 'Si':
              return {'id_prestamo': id_prestamo, 'aprobado': ingreso_codeudor/12 > cantidad_prestamo}

          else: 
              return {'id_prestamo': id_prestamo, 'aprobado': cantidad_prestamo < 200}
    else:
        if independiente == 'Si':
            if (casado == 'No' and dependientes <= 1):
                if ((ingreso_deudor/10 > cantidad_prestamo) or (ingreso_codeudor/10 > cantidad_prestamo)):
                     return {'id_prestamo': id_prestamo, 'aprobado': cantidad_prestamo < 180}
                else:
                    return {'id_prestamo': id_prestamo, 'aprobado': False}


            else: 
                return {'id_prestamo': id_prestamo, 'aprobado': False}


        else:
            if ((tipo_propiedad != 'Semi Urbana') and ((dependientes == '3+') or (dependientes > 2) )):
                if educacion == 'Graduado':
                    return {'id_prestamo': id_prestamo, 'aprobado': (((ingreso_deudor/11) > cantidad_prestamo) and ((ingreso_codeudor/11) > cantidad_prestamo))}
                    
                else:
                    return {'id_prestamo': id_prestamo, 'aprobado': False}

            else:
                return {'id_prestamo': id_prestamo, 'aprobado': False}



           

        

peter = {'id_prestamo':'RETOS2_001',
         'casado':'No',
         'dependientes': 4,
         'educacion': 'No Graduado',
         'independiente':'No',
         'ingreso_deudor': 120.,
         'ingreso_codeudor': 0.,
         'cantidad_prestamo': 106.,
         'plazo_prestamo': 360,
         'historia_credito': 0,
         'tipo_propiedad':'Rural'}



print(prestamo({'id_prestamo': 'RETOS2_001', 'casado': 'No', 'dependientes': 1, 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 4692, 'ingreso_codeudor': 0, 'cantidad_prestamo': 106, 'plazo_prestamo': 360, 'historia_credito': 1, 'tipo_propiedad': 'Rural'}))
print(prestamo({'id_prestamo': 'RETOS2_002', 'casado': 'No', 'dependientes': '3+', 'educacion': 'No Graduado', 'independiente': 'No', 'ingreso_deudor': 1830, 'ingreso_codeudor': 0, 'cantidad_prestamo': 100, 'plazo_prestamo': 360, 'historia_credito': 0, 'tipo_propiedad': 'Urbano'})) 
print(prestamo({'id_prestamo': 'RETOS2_003', 'casado': 'No', 'dependientes': 0, 'educacion': 'No Graduado', 'independiente': 'No', 'ingreso_deudor': 3748, 'ingreso_codeudor': 1668, 'cantidad_prestamo': 110, 'plazo_prestamo': 360, 'historia_credito': 1, 'tipo_propiedad': 'Semiurbano'}))
print(prestamo({'id_prestamo': 'RETOS2_012', 'casado': 'Si', 'dependientes': 1, 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 11500, 'ingreso_codeudor': 0, 'cantidad_prestamo': 286, 'plazo_prestamo': 360, 'historia_credito': 0, 'tipo_propiedad': 'Urbano'}))

