MODULE Pneumatics
    PROC SuctionON()
        Set DO10_1; ! Activate suction pneumatics
        Set DO10_8; ! Activate visible signal
        SocketSend client \Str:="Successfull grip!";
    ENDPROC
    PROC SuctionOFF()
        Reset DO10_1; ! Deactivate suction pneumatics
        Reset DO10_8; ! Dectivate visible signal
        SocketSend client \Str:="Successfull ungrip!";
    ENDPROC
ENDMODULE