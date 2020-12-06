MODULE FlytteBokser
    
    CONST robtarget Start := [[0,0,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    VAR robtarget posisjon;
    
    VAR num heights{4} := [24,48,72,96];
    
    PERS wobjdata WO1;
    PERS wobjdata WO2;
    
    PROC flyttboks(num prosedyre)
        WO1 := woListe{prosedyre};
        WO2 := woListe{prosedyre+1};
        
        posisjon := Offs(Start,0,0,-120);
        FOR indeks FROM 1 TO 4 DO
            MoveL Offs(posisjon, 0, 0, 0),v500,fine,sugeKopp\WObj:=WO1;
            MoveL Offs(posisjon, 0, 0, heights{indeks}),v100,fine,sugeKopp\WObj:=WO1;
            Set DO10_1;
            MoveL Offs(posisjon, 0, 0, 0),v100,fine,sugeKopp\WObj:=WO1;
            MoveL Offs(posisjon, 0, 0, 0),v100,fine,sugeKopp\WObj:=WO2;
            MoveL Offs(posisjon, 0, 0, heights{5-indeks}),v100,fine,sugeKopp\WObj:=WO2;
            Reset DO10_1;
            MoveL Offs(posisjon, 0, 0, -24),v100,fine,sugeKopp\WObj:=WO2;
        ENDFOR
    ENDPROC
ENDMODULE