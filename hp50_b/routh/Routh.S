RPL 
( C:\Documents and Settings\andrea\Desktop\hp\Miei\Controlli\Routh.S, part of the Routh.HPP project, created by <> on 02/10/2002 )

INCLUDE Routh.H

EXTERNAL DoMsgBox
EXTERNAL MsgBoxMenu
EXTERNAL grobAlertIcon

DEFINE kcRightShift     FORTYTWO

DEFINE kpNoShift        ONE
DEFINE kpLeftShift      THREE
DEFINE kpRightShift     THREE

DEFINE kcUpArrow        TEN
DEFINE kcLeftArrow      FOURTEEN
DEFINE kcDownArrow      FIFTEEN
DEFINE kcRightArrow     SIXTEEN
DEFINE kcOn             FORTYSEVEN

DEFINE startx    	FIVE
DEFINE starty   	TWELVE

DEFINE lungsub   	1GETLAM
DEFINE lung      	2GETLAM
DEFINE gradopol  	3GETLAM
DEFINE Msg	 	4GETLAM

DEFINE !lungsub  	1PUTLAM
DEFINE !lung     	2PUTLAM
DEFINE !gradopol 	3PUTLAM
DEFINE !Msg	 	4PUTLAM

DEFINE Flag		TEN

ASSEMBLE
  CON(1)        8
RPL
xNAME Routh
::
	CK1&Dispatch
	FIVE
    		Main
;

ASSEMBLE
  CON(1)        8
RPL
*** Main Program *****
NULLNAME Main
::
	
	Flag ClrUserFlag
	
	Dividi ( {1 2 3} -> {1 3 } {2} lung )
	
	ROT
	DUPLENCOMP
	DUPDUP
	"" 4UNROLL
	4NULLLAM{}
	BIND
	
	UNROT
	DUP
	
	!lung
	
	PopMetaVStack DROP lung #1- FLASHPTR #>Z >HCOMP #1 PushMetaVStack&Drop
	
	#1- ONE_DO
	
		Msg DISPROW1
		lung INDEX@#- !gradopol ( lunghezza della lista - indice=gradopol )
	
	      	lungsub ( INDEX@ #- #1+)
		CompletaZeri ( lista nmzrozeri -> lista+nmrozeri )
		
		gradopol UNROT
		ControllaZeri
	
		DUP gradopol #1- FLASHPTR #>Z >HCOMP PopMetaVStack #1+ PushMetaVStack&Drop
	
	 	ApplicaRouth ( lista1 lista2 -> lista1 lista2 lista3 )
	        Msg "" &$ !Msg
	[LOOP]
	
	DUP ZINT 0 >TCOMP ZINT 0 >HCOMP
	lung #1+UNROLL
	
	NULL{}
	lung #1+_ONE_DO
		SWAPONE NTHCOMPDROP >TCOMP
	[LOOP]
	
	ControllaStabilita
	
	SWAP
	
	PopMetaVStack
	#1+
	NULL{}
	SWAP
	#1+_ONE_DO
		SWAP >TCOMP
	[LOOP]
	
	FLASHPTR LIST2MATRIX
	TRUE SWAP
	FLASHPTR EQW3GROBmini DROPSWAPDROP
	DUPGROBDIM
	#4-
	THREE ONE 4ROLL 4ROLL SWAP
	SUBGROB
	DUPGROBDIM DROPONE
	MAKEGROB INVGROB
	
	ONE lung MAKEGROB INVGROB !lung
	Flag TestUserFlag
	ITE TWELVE FIVE ( La prima riga può essere o di 1 carattere o di 3, quindi le coordinate sono 5 o 12 )
	ONE
	GROB+#
	
	ClrDA1IsStat RECLAIMDISP TURNMENUOFF
	
	DUPGROBDIM SWAP startx #+ #10+
	4ROLL DUP GROBDIMw DUP #83 #< ITE :: #83 SWAP#- #2/ ; startx
	UNROT
	XYGROBDISP  ( Visualizza il messaggio di stabilità)
	
	DUP #83 #< ITE :: #83 SWAP#- #2/ ; startx
	starty ROT XYGROBDISP
	
	BINT26 BINT2
	"ROUTH'S TABLE"
	$>GROB XYGROBDISP
	
	ABND
	GestioneScroll
	
;
*** End Main ****

( Controllo della Stabilità del Sistema)
( {First Column} -> "Stable for ..." or "Not Stable" or "Stable")
NULLNAME ControllaStabilita
::
	ZERO ZERO NULL{}
	{ NULLLAM NULLLAM NULLLAM } BIND
	
	DUPLENCOMP
	#1+_ONE_DO
		DUPINDEX@ NTHCOMPDROP FLASHPTR LVARext NULLCOMP?
		ITE
		:: CRUNCH %0  %> DUP ?SKIP :: 2GETLAM #1+ 2PUTLAM ; DROP ;
		:: ZINT 0 x> NULL{} SWAP >TCOMP 1GETLAM SWAP >TCOMP 1PUTLAM ; ( caso elemento algebrico)
	
	[LOOP]
	
	LENCOMP 3PUTLAM
	
	( non ci sono componenti algebrici)
	1GETLAM LENCOMP #0=case :: 2GETLAM #0= case :: "The System is Stable" $>grob ;
				    2GETLAM ZERO #> 2GETLAM 3GETLAM #= ANDcase :: "The System is Stable" $>grob ;
				    2GETLAM ZERO #> 2GETLAM 3GETLAM #< ANDcase :: "The System is Not Stable" $>grob ;
				 ;
	
	1GETLAM LENCOMP #0 #>case ::
	( sono presenti componenti algebrici, ma anche variazioni di segno, non stabile)
				    2GETLAM #0 #> 3GETLAM 1GETLAM LENCOMP #- 2GETLAM #< ANDcase :: "The System is Not Stable" $>grob ;
	( sono presenti componenti algebrici, senza variazioni di segno-tutti negativi- , stabile per)
				    2GETLAM #0 #> 3GETLAM 1GETLAM LENCOMP #- 2GETLAM #= ANDcase :: 1GETLAM "The System is Stable for" ToGrob ;
	( sono presenti componenti algebrici, senza variazioni di segno, stabile per)
				    2GETLAM #0= case :: 1GETLAM "The System is Stable for" ToGrob ;
				   ;
	ABND
;

NULLNAME ToGrob
::
	$>grob DUPGROBDIM
	4ROLL
	FLASHPTR LIST2MATRIX
	FLASHPTR EQW3GROBmini
	DROPSWAPDROP
	DUPGROBDIM
	#4-
	THREE ONE 4ROLL 4ROLLSWAP
	SUBGROB
	DUPGROBDIM
	DUP 5ROLL DUPROT #< ?SKIP SWAPDROP
	SWAP4ROLL #+
	SWAP MAKEGROB
	ROT ZERO ZERO TRUE 5UNROLL GROB+#
	
	DUP GROBDIMw
	ROTDUP GROBDIMw
	ROTSWAP
	#-#2/
	EIGHT ( altezza della scritta + spazio)
	TRUE 5UNROLL GROB+#

;

( Divide la lista in due, coefficienti  dispari sulla prima coefficienti pari sulla seconda)
( Inserisce la lista dei coefficenti dispari in VS)
( {1 2 3} -> {1 3 } {2} lung )
( VS:  -> {GROB1 GROB3 }  )
NULLNAME Dividi
::
	DUPLENCOMP
	NULL{}
	SWAP #1+_ONE_DO
		SWAP DUPINDEX@ NTHCOMPDROP ROTSWAP >TCOMP
	BINT2
	[+LOOP]
	
	SWAP
	DUPLENCOMP
	NULL{}
	SWAP #1+ TWO [DO]
		SWAPDUP INDEX@ NTHCOMPDROP ROTSWAP >TCOMP
	#2
	[+LOOP]
	
	ROT
	
	ListRtoZ
	
	DUPONE  PushMetaVStack&Drop
	SWAP  ListRtoZ ROT LENCOMP
;

( Trasforma una lista di reali in ZINT)
( { %1 %2 %3 %4} -> {ZINT1 ZINT2 ZINT3 ZINT4 })
NULLNAME ListRtoZ
::
	INNERDUP
	#1+_ONE_DO
		INDEX@ #1+ROLL DUPTYPEREAL? IT :: DUP %FP %0= IT FLASHPTR R>Z ;
	SWAPLOOP
	reversym
	{}N
	;
	
NULLNAME CompletaZeri
::
	
	2DUPSWAP LENCOMP SWAP #<
	NOTcaseDROP
	::
		SWAP
		DUPLENCOMP
		ROTSWAP #-
		#1+_ONE_DO
			ZINT 0 >TCOMP
		[LOOP]
	;

;

* Moltiplicazione di coefficenti secondo il criterio di Routh
( lista1 lista2 -> lista1 lista2 lista3 )
NULLNAME ApplicaRouth
::
	
	DUPLENCOMP #1+ NULL{}
	TWO ROTSWAP
	[DO]
		ROTDUP CARCOMP x->Q
		4ROLL DUPINDEX@ NTHCOMPDROP
		FLASHPTR QPI
		ROT x*
		
		SWAPDUP CARCOMP x->Q	
		4ROLL DUPINDEX@ NTHCOMPDROP FLASHPTR QPI
		ROTSWAP x*
		
		4ROLL x-
		
		ROT DUP CARCOMP FLASHPTR QPI
		ROTSWAP x/ xEVAL
		
		4ROLLSWAP >TCOMP
	[LOOP]

;


( Conta il numero di zeri iniziali di una lista, richiama Trasla o Deriva a seconda del caso)
NULLNAME ControllaZeri
::

	DUPLENCOMP
	ZEROSWAP
	 #1+_ONE_DO
		SWAP DUPINDEX@ NTHCOMPDROP
		DUP%0= SWAP ZINT 0 EQUALOR
		ITE SWAP#1+ :: INDEX@ ISTOPSTO SWAP ;	
	[LOOP]
	
	
	DUP #0= case :: DROP ROTDROP ;
	DUPZERO #> ROT DUPLENCOMP 4ROLL DUPROT #< 4ROLL ANDcase :: Trasla Flag SetUserFlag ;
	DUPZERO #> ROT DUPLENCOMP 4ROLL DUPROT #= 4ROLL ANDcase :: Deriva Flag SetUserFlag ;
;

NULLNAME Trasla
::
	DUP#1+ ROT DUPLENCOMP
	SWAPDUP 4ROLL 4ROLL SUBCOMP ROT
	DUP ROTSWAP
	#1+_ONE_DO
			ZINT 0
			>TCOMP
	[LOOP]
	SWAP
	ZINT -1
	SWAPDUP
	FLASHPTR #>Z
	ROTSWAP
	x^
	ROTSWAP
	x*
	
	ListRtoZ 	
	
	ROTSWAP
	DUPLENCOMP
	NULL{}
	SWAP
	#1+_ONE_DO
		SWAPDUP INDEX@ NTHCOMPDROP
		4ROLL DUP INDEX@ NTHCOMPDROP
		ROT x+
		4ROLL SWAP >TCOMP
	[LOOP]
	
	(  gradopol prev count	newlista'' newlista' newlista )
	
	6ROLL #1- UNCOERCE DUP % .2 %+ SWAP % .1 %+
	4ROLLSWAP >HCOMP 4ROLLROT >HCOMP SWAP
	PopMetaVStack #2+ PushMetaVStack&Drop
	
	SWAPDROP
;


NULLNAME Deriva
::
	DROP
	ROT DUP#1-
	UNCOERCE
	%.1 %+ ROTSWAP >HCOMP
	PopMetaVStack #1+ PushMetaVStack&Drop
	
	FLASHPTR #>Z SWAP
	DUPLENCOMP
	#1+
	NULL{}
	SWAP
	ONE_DO
		SWAP
		DUPINDEX@
		NTHCOMPDROP
		4ROLL
		DUPROT
		x*
		4ROLLSWAP
		>TCOMP
		SWAP ZINT 2 FLASHPTR QSub ( Sottrae 2 -ZINT- al grado polinomio)
		UNROT
	[LOOP]
	ROTDROP			
;

NULLNAME GestioneScroll
::
	FALSE		
	NULLLAM BIND	
	' NOP			
	' ::			
	kpNoShift #=casedrop
	    ::
		kcUpArrow    ?CaseKeyDef SCROLLUP
		kcLeftArrow  ?CaseKeyDef SCROLLLEFT
		kcDownArrow  ?CaseKeyDef SCROLLDOWN
		kcRightArrow ?CaseKeyDef SCROLLRIGHT
		kcOn	     ?CaseKeyDef :: TakeOver TRUE 1PUTLAM ;
	
		kcRightShift	#=casedrpfls DROP 'DoBadKeyT
	    ;
	kpLeftShift #=casedrop
	    ::
		kcUpArrow    ?CaseKeyDef  JUMPTOP
		kcLeftArrow  ?CaseKeyDef  JUMPLEFT
		kcDownArrow  ?CaseKeyDef  JUMPBOT
		kcRightArrow ?CaseKeyDef  JUMPRIGHT
		
		kcRightShift #=casedrpfls DROP 'DoBadKeyT
	    ;
		2DROP 'DoBadKeyT
	;
	TrueTrue		
	NULL{}		
	ONEFALSE		
	' 1GETLAM		
	' ERRJMP		
	ParOuterLoop
	ABND
;


NULLNAME Cfg
::
	
	# 531
	XEQSETLIB
;

NULLNAME Help
::
	  BINT9
	  #=casedrop
	  ::
	    DROPTRUE
	    BINT9
	  ;
	  BINT10
	  #=casedrop
	  ::
	ROMPTR>#
	SWAPDROP
	"           - Routh -\0a\0aBuild routh's tables\0a\0aIN : Coefficents List { 1 2 3 }\0aOUT: Routh's Table"  ViewStrObject
	  ;
;

xNAME About
::
	FALSE "           - Routh -\0a\0aBy Andrea Baccin\0a\0afor comments/bugs:\0a\0abaccin.andrea@libero.it"  ViewStrObject DROP
;

