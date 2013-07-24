/* GERADOR DE PULSO PARA SISTEMAS DE ATERRAMENTO
 * Felipe Bandeira da Silva, Graduando Engenharia Elétrica 2013.2
 *
 * Gerador de pulso para o sistema de aterramento
 *
 * OBS:
 * - tentativa inicial de compatibilidade com o hadware desenvolvido pela UFC, 24/07/2013
 *
 * Softwares utilizados:
 * - MPLABX V.185
 * - XC8 V1.20
 *
 * Microcontrolador utilizado:
 * - PIC16F1503
 */
#include <xc.h>

#pragma config BOREN = ON, FOSC = INTOSC
#pragma config MCLRE = OFF, WDTE = OFF, CP = ON, PWRTE = ON

#define _XTAL_FREQ  16000000

#define alimentaBancoCapacitores()  {LATC0 = 1;}
#define desligaBancoCapacitores()   {LATC0 = 0;}
#define liberaPulsoAterramento()    {LATC1 = 1;}
#define desligaPulsoAterramento()   {LATC1 = 0;}

#define ligaLed()       {LATC2 = 1;}
#define desligaLed()    {LATC2 = 0;}
#define mudaEstadoLed() {LATC2 = LATC2;}

#define botao1Pressionado() (RA4 == 0)

void configuraPortas(void) {
    // garantido que todo mundo esteja desligado
    PORTA = 0;
    PORTC = 0;


    /* Entrada e Saída para o usuário
     * - botão de acionamento do gerador de pulso
     */
    ANSELA = 0; // PORTA para entrada e saida digital
    TRISA4 = 1; // botão para o acionamento do gerador
    TRISC2 = 0; // led de aviso


    /* Controle da potência
     * - ligação com o banco de capacitores
     * - ligação com o mosfet do pulso do aterramento
     */    
    TRISC0 = 0; // acionamento do mosfet de carrega os capacitores
    TRISC1 = 0; // acionamento do mosfet de gera o impulso para o aterramento
}

void configuraClock(void) {
    while (!OSCSTATbits.HFIOFR) {
    }
    //OSCCON = 0x6A;
    OSCCONbits.IRCF = 0b1111;
}

void configuraTimer(){
//    TMR0 = 0;
//    TMR0CS = 0; // a fonte para o timer 0 é o clock interno
//    OPTION_REGbits.PS = 0;
//    TMR0IE = 1; // habilita o timer 0

    T2CONbits.T2CKPS = 0;
    T2CONbits.T2OUTPS = 0b1111;
    T2CONbits.TMR2ON = 1;

    PR2 = 0;
    TMR2IE = 1;
    
    PEIE = 1;
}

void interrupt isr(void){
    while(1){
        //GAMEOVER
    }
}

void geraPulso(void){
    alimentaBancoCapacitores();
    __delay_ms(100);
    desligaBancoCapacitores();
    __delay_us(10);

    
    liberaPulsoAterramento();
    __delay_ms(10);
    desligaPulsoAterramento();

    __delay_ms(1);
}

void geraTremPulso(char quantidade){
    char i;
    for(i = 0; i < quantidade; i++){
        geraPulso();
    }
}

int main(void) {
    configuraClock();
    configuraPortas();
    //configuraTimer();

    ligaLed();

    while (1) {
        if(botao1Pressionado()){
            //geraPulso();
            geraTremPulso(4);
            __delay_ms(100);
            while(botao1Pressionado());
        }
    }

    desligaLed();
}
