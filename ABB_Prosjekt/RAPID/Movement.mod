MODULE Movement
    
    PROC GoHome()
        MoveJ Home,v1000,fine,SuctionTool \WObj:=Workspace;
        ! SocketSend client \Str:="Welcome home!";
    ENDPROC    
    
    PROC MoveObject()
            TPWrite "ObjHeight: " \Num:=obj_h;
            MoveJ Offs(PickUp,0,0,-200),v1000,fine,SuctionTool\WObj:=Workspace; ! Move over object
            MoveL Offs(PickUp,0,0,-obj_h),v100,fine,SuctionTool\WObj:=Workspace; ! Move down to object
            SuctionON;
            MoveL Offs(PickUp,0,0,-200),v100,fine,SuctionTool\WObj:=Workspace; ! Move up
            TPWrite "Base height: " \Num:=z_base{index};
            
            MoveJ Offs(Delivery,0,0,-200),v1000,fine,SuctionTool\WObj:=Workspace; ! Move over base
            MoveL Offs(Delivery,0,0,-z_base{index}),v100,fine,SuctionTool\WObj:=Workspace; ! Lower object
            SuctionOFF;
            MoveL Offs(Delivery,0,0,-200),v100,fine,SuctionTool\WObj:=Workspace; ! Move up
            z_base{index} := z_base{index} + obj_h; ! Add objejct height to current base height
            prevdata := data;
            pval_x := nval_x;
            pval_y := nval_y;
            GoHome;
    ENDPROC
    
ENDMODULE