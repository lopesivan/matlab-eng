/*
 * hardware.h
 *
 * Definicoes principais de registradores utilizados pelo sistema
 *
 * Felipe Bandeira, felipeband18@gmail.com
 */


#ifndef _HARDWARE_H
#define _HARDWARE_H

/*******************************************************************************
 * Funcoes de delay da arquitetura
 */
#define delay_us(a) __delay_us(a)
#define delay_ms(a) __delay_ms(a)


/*******************************************************************************
 * Frequencia externa do processador
 * Cada instrucao roda a 200ns ou 0.0000002s
 */
#define _XTAL_FREQ  20000000


/*******************************************************************************
 * Pinos utilizados pela LCD
 */
#define LCD_RS      RC7
//#define LCD_RW      RC5
#define LCD_EN      RC4
#define LCD_DATA    PORTC
#define LCD_TRIS    TRISC




#endif