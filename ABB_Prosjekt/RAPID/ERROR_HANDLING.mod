MODULE ERROR_HANDLING
    PROC server_recover()
        SocketClose server;
        SocketClose client;
        SocketCreate server;
        SocketBind server, "192.168.12.97", 2222;
        SocketListen server;
        SocketAccept server, client, \ClientAddress:=Client_IP, \Time:=120;
            
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
                CurrentRobTarget := CRobT();
                SuctionOFF;
                MoveL Offs(CurrentRobTarget,0,0,-50),v50,fine,SuctionTool\WObj:=Workspace;
                GoHome;
                server_recover;
                RETRY;
            ELSE
                ! No error recovery handling
            ENDIF 
    ENDPROC
ENDMODULE