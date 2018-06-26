class Relogio:

    def __init__(self, hora=0, min=0, seg=0):
        self.hora = hora
        self.min = min
        self.seg = seg

    def ajustar_hora(self, hora, min, seg=0):
        self.hora = hora
        self.min = min
        self.seg = seg

    def __str__(self):
        return '{0:02d}:{1:02d}:{2:02d}'.format(self.hora, self.min, self.seg)

    def tick(self):
        if self.seg == 59:
            self.seg = 0
            if self.min == 59:
                self.min = 0
                if self.hora == 23:
                    self.hora = 0
                else:
                    self.hora += 1
            else:
                self.min += 1
        else:
            self.seg += 1

class Calendario:

    __meses = (31,28,31,30,31,30,31,31,30,31,30,31)

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def ajustar(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def __str__(self):
        return '{0:02d}/{1:02d}/{2:4d}'.format(self.dia, self.mes, self.ano)

    def ultimo_dia_mes(self,mes=None):
        if mes != None:
            return self.__meses[mes-1]
        else:
            return self.__meses[self.mes-1]

    def avancar(self):
        if self.dia == self.ultimo_dia_mes():
            self.dia = 1
            if self.mes == 12:
                self.mes = 1
                self.ano += 1
            else:
                self.mes += 1
        else:
            self.dia += 1

if __name__ == '__main__':

    #Exemplifica o uso do relogio
    # relogio = Relogio(23,59,58)
    # for i in range(20):
    #     print(relogio)
    #     relogio.tick()

    # Exemplifica o uso do Calendario
    calendario = Calendario(28,6,2018)
    print('ultimo_dia_mes', calendario.ultimo_dia_mes())
    for i in range(10):
        print(calendario)
        calendario.avancar()

    print('ultimo_dia_mes', calendario.ultimo_dia_mes())

    #030 Herança Múltipla - Parte 1.mp4 - 12:46