#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

# Análise de circuitos utilizando o par diferencial TBJ
# Circuitos comuns encontrados na literatura e no mundo academico

from __future__ import division
import sys

class ct:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


modeloNPN = {
    'vbe' : 0.7,
    'bcc' : 100,
}

def conf1_resistoresBase(mNPN, VCC, VEE, RE, RC, RB):
    """Modelo simples de um amplificador diferencial
    Entrada:
        mNPN - modelo do transistor NPN
        VCC - tensão positiva da fonte simétrica [V]
        VEE - tensão negativa da fonte simétrica [V]
        RE - resistor de cauda [Ohm]
        RC - resistor do coletor [Ohm]
        RB - resistor da base [Ohm]
    Saída:
        It - corrente de cauda [A]
        Ie - corrente do emissor de cada transistor [A]
        Vout - tensão de saída, tensão coletor [V]
        Ib - corrente na base [A]
    """

    # corrente de cauda
    It = (VCC - mNPN['vbe'])/(RE+RB/(2*mNPN['bcc']))
    # corrente no emissor de cada transistor, identicos
    Ie = It/2
    # tensão no coletor do transistor Q2, lado direito
    Vout = VCC - Ie*RC
    # corrente na base
    Ib = Ie/mNPN['bcc']

    return [It, Ie, Vout, Ib]

def conf1Exemplo():
    transistor = modeloNPN
    transistor['vbe'] = 0.7
    transistor['bcc'] = 100
    vcc = 15
    vee = 15
    rc = 15e3
    rb = 33e3
    re = 15e3

    It, Ie, Vout, Ib = conf1_resistoresBase(transistor, vcc, vee, re, rc, rb)

    print 'It   [A]: ', It
    print 'Ie   [A]: ', Ie
    print 'Ib   [A]: ', Ib
    print 'Vout [V]: ', Vout

def modeloAC_ampDif(mNPN, VCC, VEE, RE, RC, RB, vin):
    It, Ie, Vout, Ib = conf1_resistoresBase(mNPN, VCC, VEE, RE, RC, RB)
    # resistência dinâmica
    re = 25e-3/Ie
    # ganho do modelo
    A = RC/(2*re)
    # corrente ie
    ie = vin/(2*re)
    # impedância de entrada
    zin = 2*mNPN['bcc']*re
    # tensão dc de saída
    vout_dc = VCC - (Ie*RC)
    # ganho final levando em consideração o ganho ac
    vout_ganho = vout_dc+vin*A

    return [It, Ie, Ib, re, A, ie, zin, vout_dc, vout_ganho]

def modeloPequenosSinaisSedra(vd, Rc, I, Vcc, Bcc):
    """Modelo para pequenos sinais vd <  2*VT.
    Este modelo pode ser encontrada na pag 459 do Sedra 4 edição.
    Entrada:
        vd - entrada diferencial
        Rc - resistor do coletor
        I - corrente de cauda
        Vcc - tensão positiva de alimentação
        Bcc - ganho cc do transistor NPN
    Saída:
        ib - corrente na base
        ic - corrente no coletor
        ie - corrente no emissor
    """
    Vt = 25e-3
    #resistência dinâmica
    re = Vt/(I/2)
    # corrente na base
    ib = vd/(2*re*(Bcc+1))
    # corrente no emissor de cada transistor, não é levado em consideração o
    # sentido da mesma
    ie = vd/(2*re)
    # corrente no coletor, levando em consideração o ganho do transistor
    alfa = Bcc/(Bcc+1)
    ic = alfa*ie
    vc  =ic*Rc

    return [re, ib, ie, alfa, ic, vc]

def modeloPequenosSinaisSedraResistoresEmissor(vd, Rc, I, Vcc, Bcc):
    re, ib, ie, alfa, ic, vc = modeloPequenosSinaisSedra(vc, Rc, I, Vcc, Bcc)

def zonaTeste():
    print ct.BOLD+ct.PURPLE+'Entrando na zona de teste'+ct.END


    transistor = modeloNPN
    transistor['vbe'] = 0.7
    transistor['bcc'] = 100
    vcc = 15
    vee = 15
    rc = 15e3
    rb = 33e3
    re = 15e3

    It, Ie, Vout, Ib = conf1_resistoresBase(transistor, vcc, vee, re, rc, rb)
    print '-'*10
    print ct.BOLD+'Modelo repouso, Malvino'+ct.BOLD
    print ct.BOLD+'Entrada,'+ct.END
    print 'Vcc   [V]:', vcc
    print 'Vee   [V]:', vee
    print 'Rc [ohms]:', rc
    print 'Rb [ohms]:', rb
    print 'Re [ohms]:', re
    print ct.BOLD+'Saída,'+ct.END
    print ' It   [A]:', It
    print ' Ie   [A]:', Ie
    print ' Ib   [A]:', Ib
    print ' Vout [V]:', Vout

################################################################################

    vd = 1e-3
    Rc = 1e3
    I = 5e-3
    Vcc = 10
    Bcc = 100
    re, ib, ie, alfa, ic, vc = modeloPequenosSinaisSedra(vd, Rc, I, Vcc, Bcc)
    print '-'*10
    print ct.BOLD+'Modelo para pequenos sinais, Sedra'+ct.BOLD
    print ct.BOLD+'Entrada,'+ct.END
    print ' vd    [V]:', vd
    print ' Rc [ohms]:', Rc
    print ' I     [A]:', I
    print ' Vcc   [V]:', Vcc
    print ' Bcc      :', Bcc
    print ct.BOLD+'Saída,'+ct.END
    print ' re [ohms]:', re
    print ' ie    [A]:', ie
    print ' ib    [A]:', ib
    print ' ic    [A]:', ic
    print ' vc    [V]:', vc
    print ' vo    [V]:', vc*2
    print ' alfa     :', alfa

    return 0

if __name__ == '__main__':
    print ct.BOLD+'Amplificador diferencial'+ct.END
    print

    zonaTeste()

    sys.exit(0)

