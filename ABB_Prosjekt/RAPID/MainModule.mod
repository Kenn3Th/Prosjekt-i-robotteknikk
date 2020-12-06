MODULE MainModule
        
    ! Target constants
    CONST robtarget Home:=[[100,-100,-200],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Base1:=[[-50,-100,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Base2:=[[-50,0,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Base3:=[[-50,100,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Base4:=[[-50,200,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Origo:=[[0,0,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    ! Target variables
    VAR robtarget CurrentRobTarget;
    VAR robtarget PickUp;
    VAR robtarget Delivery;

    VAR num retry_no := 0;
    VAR socketdev server;
    VAR socketdev client;
    VAR string Client_IP;
    VAR string data := "";
    VAR string prevdata := "";
    VAR string msg := "Operation conducted!";
    VAR num len := 0;
    VAR string fig := "";
    VAR string val_x := "";
    VAR string val_y := "";
    VAR bool ok;
    VAR num nval_x := 0;
    VAR num nval_y := 0;
    VAR num pval_x := 0;
    VAR num pval_y := 0;
    
    ! Object constants
    CONST num h_crc := 24;
    CONST num h_tri := 20;
    CONST num h_sqr := 15;
    CONST num h_hex := 10;
    ! Object variables
    VAR num obj_h := 0;
    
    ! Stack variables
    VAR num index := 0;
    VAR num z_base{4} := [h_crc,h_tri,h_sqr,h_hex];
    
    
    PROC main()
        WHILE TRUE DO
            GoHome;
            Transmission;
        ENDWHILE 
    ENDPROC
ENDMODULE