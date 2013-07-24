opt subtitle "Microchip Technology Omniscient Code Generator (Lite mode) build 52243"

opt pagewidth 120

	opt lm

	processor	16F1503
clrc	macro
	bcf	3,0
	endm
clrz	macro
	bcf	3,2
	endm
setc	macro
	bsf	3,0
	endm
setz	macro
	bsf	3,2
	endm
skipc	macro
	btfss	3,0
	endm
skipz	macro
	btfss	3,2
	endm
skipnc	macro
	btfsc	3,0
	endm
skipnz	macro
	btfsc	3,2
	endm
indf	equ	0
indf0	equ	0
indf1	equ	1
pc	equ	2
pcl	equ	2
status	equ	3
fsr0l	equ	4
fsr0h	equ	5
fsr1l	equ	6
fsr1h	equ	7
bsr	equ	8
wreg	equ	9
intcon	equ	11
c	equ	1
z	equ	0
pclath	equ	10
# 46 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
INDF0 equ 00h ;# 
# 65 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
INDF1 equ 01h ;# 
# 84 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PCL equ 02h ;# 
# 103 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
STATUS equ 03h ;# 
# 166 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
FSR0L equ 04h ;# 
# 185 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
FSR0H equ 05h ;# 
# 207 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
FSR1L equ 06h ;# 
# 226 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
FSR1H equ 07h ;# 
# 245 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
BSR equ 08h ;# 
# 296 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
WREG equ 09h ;# 
# 315 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PCLATH equ 0Ah ;# 
# 334 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
INTCON equ 0Bh ;# 
# 411 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PORTA equ 0Ch ;# 
# 460 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PORTC equ 0Eh ;# 
# 509 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PIR1 equ 011h ;# 
# 554 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PIR2 equ 012h ;# 
# 593 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PIR3 equ 013h ;# 
# 618 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
TMR0 equ 015h ;# 
# 637 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
TMR1 equ 016h ;# 
# 643 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
TMR1L equ 016h ;# 
# 662 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
TMR1H equ 017h ;# 
# 681 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
T1CON equ 018h ;# 
# 752 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
T1GCON equ 019h ;# 
# 821 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
TMR2 equ 01Ah ;# 
# 840 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PR2 equ 01Bh ;# 
# 859 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
T2CON equ 01Ch ;# 
# 929 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
TRISA equ 08Ch ;# 
# 978 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
TRISC equ 08Eh ;# 
# 1027 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PIE1 equ 091h ;# 
# 1072 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PIE2 equ 092h ;# 
# 1111 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PIE3 equ 093h ;# 
# 1136 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
OPTION_REG equ 095h ;# 
# 1218 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PCON equ 096h ;# 
# 1274 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
WDTCON equ 097h ;# 
# 1332 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
OSCCON equ 099h ;# 
# 1397 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
OSCSTAT equ 09Ah ;# 
# 1429 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
ADRES equ 09Bh ;# 
# 1435 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
ADRESL equ 09Bh ;# 
# 1454 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
ADRESH equ 09Ch ;# 
# 1473 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
ADCON0 equ 09Dh ;# 
# 1552 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
ADCON1 equ 09Eh ;# 
# 1598 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
ADCON2 equ 09Fh ;# 
# 1645 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
LATA equ 010Ch ;# 
# 1689 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
LATC equ 010Eh ;# 
# 1738 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CM1CON0 equ 0111h ;# 
# 1794 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CM1CON1 equ 0112h ;# 
# 1865 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CM2CON0 equ 0113h ;# 
# 1921 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CM2CON1 equ 0114h ;# 
# 1992 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CMOUT equ 0115h ;# 
# 2017 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
BORCON equ 0116h ;# 
# 2049 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
FVRCON equ 0117h ;# 
# 2124 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
DACCON0 equ 0118h ;# 
# 2164 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
DACCON1 equ 0119h ;# 
# 2215 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
APFCON equ 011Dh ;# 
# 2259 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
ANSELA equ 018Ch ;# 
# 2305 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
ANSELC equ 018Eh ;# 
# 2350 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PMADR equ 0191h ;# 
# 2356 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PMADRL equ 0191h ;# 
# 2375 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PMADRH equ 0192h ;# 
# 2394 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PMDAT equ 0193h ;# 
# 2400 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PMDATL equ 0193h ;# 
# 2419 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PMDATH equ 0194h ;# 
# 2438 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PMCON1 equ 0195h ;# 
# 2493 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PMCON2 equ 0196h ;# 
# 2512 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
VREGCON equ 0197h ;# 
# 2532 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
WPUA equ 020Ch ;# 
# 2589 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
SSP1BUF equ 0211h ;# 
# 2594 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
SSPBUF equ 0211h ;# 
# 2626 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
SSP1ADD equ 0212h ;# 
# 2631 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
SSPADD equ 0212h ;# 
# 2663 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
SSP1MSK equ 0213h ;# 
# 2668 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
SSPMSK equ 0213h ;# 
# 2700 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
SSP1STAT equ 0214h ;# 
# 2705 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
SSPSTAT equ 0214h ;# 
# 2821 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
SSP1CON1 equ 0215h ;# 
# 2826 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
SSPCON equ 0215h ;# 
# 2830 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
SSPCON1 equ 0215h ;# 
# 3024 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
SSP1CON2 equ 0216h ;# 
# 3029 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
SSPCON2 equ 0216h ;# 
# 3145 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
SSP1CON3 equ 0217h ;# 
# 3150 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
SSPCON3 equ 0217h ;# 
# 3266 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
IOCAP equ 0391h ;# 
# 3323 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
IOCAN equ 0392h ;# 
# 3380 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
IOCAF equ 0393h ;# 
# 3439 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
NCO1ACC equ 0498h ;# 
# 3445 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
NCO1ACCL equ 0498h ;# 
# 3514 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
NCO1ACCH equ 0499h ;# 
# 3583 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
NCO1ACCU equ 049Ah ;# 
# 3628 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
NCO1INC equ 049Bh ;# 
# 3634 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
NCO1INCL equ 049Bh ;# 
# 3703 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
NCO1INCH equ 049Ch ;# 
# 3772 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
NCO1CON equ 049Eh ;# 
# 3816 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
NCO1CLK equ 049Fh ;# 
# 3875 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PWM1DCL equ 0611h ;# 
# 3910 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PWM1DCH equ 0612h ;# 
# 3979 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PWM1CON equ 0613h ;# 
# 3984 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PWM1CON0 equ 0613h ;# 
# 4054 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PWM2DCL equ 0614h ;# 
# 4089 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PWM2DCH equ 0615h ;# 
# 4158 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PWM2CON equ 0616h ;# 
# 4163 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PWM2CON0 equ 0616h ;# 
# 4233 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PWM3DCL equ 0617h ;# 
# 4268 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PWM3DCH equ 0618h ;# 
# 4337 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PWM3CON equ 0619h ;# 
# 4342 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PWM3CON0 equ 0619h ;# 
# 4412 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PWM4DCL equ 061Ah ;# 
# 4447 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PWM4DCH equ 061Bh ;# 
# 4516 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PWM4CON equ 061Ch ;# 
# 4521 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PWM4CON0 equ 061Ch ;# 
# 4591 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CWG1DBR equ 0691h ;# 
# 4648 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CWG1DBF equ 0692h ;# 
# 4705 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CWG1CON0 equ 0693h ;# 
# 4763 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CWG1CON1 equ 0694h ;# 
# 4839 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CWG1CON2 equ 0695h ;# 
# 4889 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CLCDATA equ 0F0Fh ;# 
# 4914 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CLC1CON equ 0F10h ;# 
# 5033 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CLC1POL equ 0F11h ;# 
# 5110 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CLC1SEL0 equ 0F12h ;# 
# 5214 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CLC1SEL1 equ 0F13h ;# 
# 5318 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CLC1GLS0 equ 0F14h ;# 
# 5429 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CLC1GLS1 equ 0F15h ;# 
# 5540 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CLC1GLS2 equ 0F16h ;# 
# 5651 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CLC1GLS3 equ 0F17h ;# 
# 5762 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CLC2CON equ 0F18h ;# 
# 5881 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CLC2POL equ 0F19h ;# 
# 5958 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CLC2SEL0 equ 0F1Ah ;# 
# 6062 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CLC2SEL1 equ 0F1Bh ;# 
# 6166 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CLC2GLS0 equ 0F1Ch ;# 
# 6277 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CLC2GLS1 equ 0F1Dh ;# 
# 6388 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CLC2GLS2 equ 0F1Eh ;# 
# 6499 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
CLC2GLS3 equ 0F1Fh ;# 
# 6610 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
BSR_ICDSHAD equ 0FE3h ;# 
# 6629 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
STATUS_SHAD equ 0FE4h ;# 
# 6660 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
WREG_SHAD equ 0FE5h ;# 
# 6679 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
BSR_SHAD equ 0FE6h ;# 
# 6698 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
PCLATH_SHAD equ 0FE7h ;# 
# 6717 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
FSR0L_SHAD equ 0FE8h ;# 
# 6736 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
FSR0H_SHAD equ 0FE9h ;# 
# 6755 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
FSR1L_SHAD equ 0FEAh ;# 
# 6774 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
FSR1H_SHAD equ 0FEBh ;# 
# 6793 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
STKPTR equ 0FEDh ;# 
# 6812 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
TOSL equ 0FEEh ;# 
# 6831 "C:\Program Files (x86)\Microchip\xc8\v1.20\include\pic16f1503.h"
TOSH equ 0FEFh ;# 
	FNROOT	_main
psect	maintext,global,class=CODE,delta=2,merge=1,split=1
global __pmaintext
__pmaintext:	;psect for function _main
; #config settings
	file	"Debug.as"
	line	#
psect cinit,class=CODE,delta=2
global start_initialization
start_initialization:

global __initialization
__initialization:
psect cinit,class=CODE,delta=2,merge=1
global end_of_initialization,__end_of__initialization

;End of C runtime variable initialization code

end_of_initialization:
__end_of__initialization:movlb 0
ljmp _main	;jump to C main() function
psect	cstackCOMMON,class=COMMON,space=1,noexec
global __pcstackCOMMON
__pcstackCOMMON:
?_main:	; 0 bytes @ 0x0
??_main:	; 0 bytes @ 0x0
;!
;!Data Sizes:
;!    Strings     0
;!    Constant    0
;!    Data        0
;!    BSS         0
;!    Persistent  0
;!    Stack       0
;!
;!Auto Spaces:
;!    Space          Size  Autos    Used
;!    COMMON           14      0       0
;!    BANK0            80      0       0
;!    BANK1            32      0       0

;!
;!Pointer List with Targets:
;!
;!    None.


;!
;!Critical Paths under _main in COMMON
;!
;!    None.
;!
;!Critical Paths under _main in BANK0
;!
;!    None.
;!
;!Critical Paths under _main in BANK1
;!
;!    None.

;;
;;Main: autosize = 0, tempsize = 0, incstack = 0, save=0
;;

;!
;!Call Graph Tables:
;!
;! ---------------------------------------------------------------------------------
;! (Depth) Function   	        Calls       Base Space   Used Autos Params    Refs
;! ---------------------------------------------------------------------------------
;! (0) _main                                                 0     0      0       0
;! ---------------------------------------------------------------------------------
;! Estimated maximum stack depth 0
;! ---------------------------------------------------------------------------------
;!
;! Call Graph Graphs:
;!
;! _main (ROOT)
;!

;! Address spaces:

;!Name               Size   Autos  Total    Cost      Usage
;!BIGRAM              70      0       0       0        0.0%
;!NULL                 0      0       0       0        0.0%
;!CODE                 0      0       0       0        0.0%
;!BITCOMMON            E      0       0       1        0.0%
;!BITSFR0              0      0       0       1        0.0%
;!SFR0                 0      0       0       1        0.0%
;!COMMON               E      0       0       2        0.0%
;!BITSFR1              0      0       0       2        0.0%
;!SFR1                 0      0       0       2        0.0%
;!BITSFR2              0      0       0       3        0.0%
;!SFR2                 0      0       0       3        0.0%
;!STACK                0      0       0       3        0.0%
;!BITSFR3              0      0       0       4        0.0%
;!SFR3                 0      0       0       4        0.0%
;!ABS                  0      0       0       4        0.0%
;!BITBANK0            50      0       0       5        0.0%
;!BITSFR4              0      0       0       5        0.0%
;!SFR4                 0      0       0       5        0.0%
;!BANK0               50      0       0       6        0.0%
;!BITSFR5              0      0       0       6        0.0%
;!SFR5                 0      0       0       6        0.0%
;!BITBANK1            20      0       0       7        0.0%
;!BITSFR6              0      0       0       7        0.0%
;!SFR6                 0      0       0       7        0.0%
;!BANK1               20      0       0       8        0.0%
;!BITSFR7              0      0       0       8        0.0%
;!SFR7                 0      0       0       8        0.0%
;!BITSFR8              0      0       0       9        0.0%
;!SFR8                 0      0       0       9        0.0%
;!DATA                 0      0       0       9        0.0%
;!BITSFR9              0      0       0      10        0.0%
;!SFR9                 0      0       0      10        0.0%
;!BITSFR10             0      0       0      11        0.0%
;!SFR10                0      0       0      11        0.0%
;!BITSFR11             0      0       0      12        0.0%
;!SFR11                0      0       0      12        0.0%
;!BITSFR12             0      0       0      13        0.0%
;!SFR12                0      0       0      13        0.0%
;!BITSFR13             0      0       0      14        0.0%
;!SFR13                0      0       0      14        0.0%
;!BITSFR14             0      0       0      15        0.0%
;!SFR14                0      0       0      15        0.0%
;!BITSFR15             0      0       0      16        0.0%
;!SFR15                0      0       0      16        0.0%
;!BITSFR16             0      0       0      17        0.0%
;!SFR16                0      0       0      17        0.0%
;!BITSFR17             0      0       0      18        0.0%
;!SFR17                0      0       0      18        0.0%
;!BITSFR18             0      0       0      19        0.0%
;!SFR18                0      0       0      19        0.0%
;!BITSFR19             0      0       0      20        0.0%
;!SFR19                0      0       0      20        0.0%
;!BITSFR20             0      0       0      21        0.0%
;!SFR20                0      0       0      21        0.0%
;!BITSFR21             0      0       0      22        0.0%
;!SFR21                0      0       0      22        0.0%
;!BITSFR22             0      0       0      23        0.0%
;!SFR22                0      0       0      23        0.0%
;!BITSFR23             0      0       0      24        0.0%
;!SFR23                0      0       0      24        0.0%
;!BITSFR24             0      0       0      25        0.0%
;!SFR24                0      0       0      25        0.0%
;!BITSFR25             0      0       0      26        0.0%
;!SFR25                0      0       0      26        0.0%
;!BITSFR26             0      0       0      27        0.0%
;!SFR26                0      0       0      27        0.0%
;!BITSFR27             0      0       0      28        0.0%
;!SFR27                0      0       0      28        0.0%
;!BITSFR28             0      0       0      29        0.0%
;!SFR28                0      0       0      29        0.0%
;!BITSFR29             0      0       0      30        0.0%
;!SFR29                0      0       0      30        0.0%
;!BITSFR30             0      0       0      31        0.0%
;!SFR30                0      0       0      31        0.0%
;!BITSFR31             0      0       0      32        0.0%
;!SFR31                0      0       0      32        0.0%

	global	_main

;; *************** function _main *****************
;; Defined at:
;;		line 11 in file "../main.c"
;; Parameters:    Size  Location     Type
;;		None
;; Auto vars:     Size  Location     Type
;;		None
;; Return value:  Size  Location     Type
;;		None               void
;; Registers used:
;;		None
;; Tracked objects:
;;		On entry : 17F/0
;;		On exit  : 0/0
;;		Unchanged: 0/0
;; Data sizes:     COMMON   BANK0   BANK1
;;      Params:         0       0       0
;;      Locals:         0       0       0
;;      Temps:          0       0       0
;;      Totals:         0       0       0
;;Total ram usage:        0 bytes
;; This function calls:
;;		Nothing
;; This function is called by:
;;		Startup code after reset
;; This function uses a non-reentrant model
;;
psect	maintext
psect	maintext
	file	"../main.c"
	line	11
	global	__size_of_main
	__size_of_main	equ	__end_of_main-_main
	
_main:	
;incstack = 0
	opt	stack 16
; Regs used in _main: []
	line	13
	
l3:	
	line	14
	
l4:	
	line	13
	goto	l3
	
l5:	
	line	15
	
l6:	
	global	start
	ljmp	start
	opt stack 0
GLOBAL	__end_of_main
	__end_of_main:
	signat	_main,88
	global	btemp
	btemp set 07Eh

	DABS	1,126,2	;btemp
	global	wtemp0
	wtemp0 set btemp
	end
