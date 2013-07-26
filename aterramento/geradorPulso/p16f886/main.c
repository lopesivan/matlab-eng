#include <xc.h>
#include "lcd.h"

#define _XTAL_FREQ  20000000

#define alimentaBancoCapacitores()  {RB4 = 1;}
#define desligaBancoCapacitores()   {RB4 = 0;}
#define liberaPulsoAterramento()    {RB5 = 1;}
#define desligaPulsoAterramento()   {RB5 = 0;}

#define ligaLed()       
#define desligaLed()    
#define mudaEstadoLed() 

#define botaoPulso() (RA0 == 0)
#define botaoTrem() (RA1 == 0)

void interrupt isr(void) {
    while (1) {
        //GAMEOVER
    }
}

void geraPulso(void) {
    alimentaBancoCapacitores();
    __delay_ms(100);
    desligaBancoCapacitores();
    __delay_us(10);


    liberaPulsoAterramento();
    __delay_ms(10);
    desligaPulsoAterramento();

    __delay_ms(1);
}

void geraTremPulso(char quantidade) {
    char i;
    for (i = 0; i < quantidade; i++) {
        geraPulso();
    }
}

void configuraPortas(void) {
    // garantido que todo mundo esteja desligado
    PORTB = 0;

    /* Entrada e Saída para o usuário
     * - botão de acionamento do gerador de pulso
     */
    ANSEL = 0; // PORTA para entrada e saida digital
    TRISA0 = 1; // botão para a geração de um pulso unico
    TRISA1 = 1; // botão para o trem de pulso
    //TRISC2 = 0; // led de aviso


    /* Controle da potência
     * - ligação com o banco de capacitores
     * - ligação com o mosfet do pulso do aterramento
     */
    ANSELH = 0;
    TRISB4 = 0; // acionamento do mosfet de carrega os capacitores
    TRISB5 = 0; // acionamento do mosfet de gera o impulso para o aterramento
}

void msgInicial(void) {
    lcd_string((char *) "Gerador de Pulso", LCD_LINHA1);
    lcd_string((char *) "LAMOTRIZ - UFC", LCD_LINHA2);
    lcd_string((char *) "25/07/2013", LCD_LINHA3);
    lcd_string((char *) "", LCD_LINHA4);
}

int main(void) {
    lcd_init();
    configuraPortas();
    msgInicial();

    while (1) {
        if(botaoPulso()){

            lcd_clear();
            lcd_string((char *) "gerando pulso", LCD_LINHA1);

            geraPulso();
            __delay_ms(100);

            lcd_string((char *) "pulso gerado", LCD_LINHA2);
            while(botaoPulso());


        }

        if(botaoTrem()){

            lcd_clear();
            lcd_string((char *) "gerando trem", LCD_LINHA1);

            geraTremPulso(4);
            __delay_ms(100);

            lcd_string((char *) "trem gerado", LCD_LINHA2);
            while(botaoTrem());
        }


    }

}

