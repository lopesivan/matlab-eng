#include <stdio.h>
#include <pic.h>

void sys_init(void) {
    // Oscilador interno para 4MHz
    while (!OSCSTATbits.HFIOFR) {
    }
    OSCCON = 0x6A;
}

void interrupt isr(void) {
    if (INTCONbits.IOCIF) {
        if (IOCAFbits.IOCAF1) {
            
        }
        // limpa a flag do pino RX e a flag de interrupcao por mudanca de estado
        IOCAFbits.IOCAF1 = 0;
        INTCONbits.IOCIF = 0;
    } else {
        while (1) {
            // GAME OVER, erro no sistema.
            // Algo nao foi configurado ou tratado corretamente
        }
    }
}

int main(void) {
    sys_init();

    //INTCONbits.GIE = 1;

    printf("I");
    
    while(1){
        
    }
    return 0;
}
