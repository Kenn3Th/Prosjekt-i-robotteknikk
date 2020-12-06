MODULE Communication
    PROC Transmission()
        SocketCreate server;
        SocketBind server, "192.168.12.97", 2222;
        SocketListen server;
        SocketAccept server, client, \ClientAddress:=Client_IP, \Time:=120;
        
        TPWrite "Client_IP:" + Client_IP; ! Write client IP address to FlexPendant
        
        WHILE data <> "EXIT" OR data <> "exit" DO
            WaitTime 1;
            SocketSend client \Str:="Feed me!"; ! Send "Ready to start" to client
            TPWrite "Waiting for instructions";
            
            SocketReceive client \Str:=data;
            fig := StrPart(data, 1, 3); ! Retrieve figure type from string
            val_x := StrPart(data, 5, 3); ! Retrieve figure x-position from string
            val_y := StrPart(data, 9, 3); ! Retrieve figure y-positon from string
            ok := StrToVal(val_x, nval_x); ! Convert x-position to numeric value
            ok := StrToVal(val_y, nval_y); ! Convert y-position to numeric value
            IF data <> prevdata THEN
                IF nval_x <> pval_x THEN
                    IF nval_y <> pval_y THEN
                       TPWrite data; ! Write received data to FlexPendant
                        len := StrLen(data); ! Determine string length
                        IF data = "Home" THEN
                            GoHome;
                        ELSEIF data = "" THEN
                            SocketSend client \Str:="Feed me!";
                        ELSE
                            ! Write position to FlexPendant
                            TPWrite "Position x: " \Num:=nval_x;
                            TPWrite "Position y: " \Num:=nval_y;
                            IF fig = "CRC" THEN ! What to do when figure is a circle
                                index := 1;
                                obj_h := h_crc;
                                Delivery := Offs(Base1,0,0,0);
                                PickUp := Offs(Origo, nval_x,nval_y, 0); ! Position of object from string
                                MoveObject;
                            ELSEIF fig = "TRI" THEN ! What to do when figure is a triangle
                                index := 2;
                                obj_h := h_tri;
                                Delivery := Offs(Base2,0,0,0);
                                PickUp := Offs(Origo, nval_x,nval_y, 0); ! Position of object from string
                                MoveObject;
                            ELSEIF fig = "SQR" THEN  ! What to do when figure is a square
                                index := 3;
                                obj_h := h_sqr;
                                Delivery := Offs(Base3,0,0,0);
                                PickUp := Offs(Origo, nval_x,nval_y, -0); ! Position of object from string
                                MoveObject;
                            ELSEIF fig = "HEX" THEN ! What to do when figure is a hexagon
                                index := 4;
                                obj_h := h_hex;
                                Delivery := Offs(Base4,0,0,0);
                                PickUp := Offs(Origo, nval_x,nval_y, 0); ! Position of object from string
                                MoveObject;
                            ELSE
                                SocketSend client \Str:="Feed me!";
                            ENDIF
                        ENDIF 
                    ENDIF
                ENDIF
            ELSE
                WaitTime 0.5;
                SocketSend client \Str:="Feed me!"; 
            ENDIF
            ! SocketSend client \Str:=msg; ! Send answer after received command
        ENDWHILE
        
        SocketClose server;
        SocketClose client;
        
        ERROR
            IF ERRNO = ERR_SOCK_TIMEOUT THEN
                IF retry_no < 10 THEN
                    WaitTime 1;
                    retry_no := retry_no + 1;
                    RETRY;
                ELSE
                    retry_no := 0;
                    RAISE;
                ENDIF
            ELSEIF ERRNO = ERR_SOCK_CLOSED THEN
                server_recover;
                RETRY;
            ELSE
                ! No error recovery handling
            ENDIF 
    ENDPROC
ENDMODULE