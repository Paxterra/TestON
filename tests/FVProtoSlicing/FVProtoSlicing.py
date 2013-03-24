
class FVProtoSlicing :

    def __init__(self) :
        self.default = ''

    def CASE1(self,main) :

    
    
        main.step("remove flowspace by USING 'removeFlowSpace' by specifying either id or 'all'")
        main.FlowVisor.removeFlowSpace("all")
    
        main.step("Adding FlowSpace")
        main.FlowVisor.addFlowSpace("any 100 dl_type=0x806,dl_src=9e:f5:8b:78:c3:93,nw_dst=10.128.4.6 Slice:SSH=4")
        main.FlowVisor.addFlowSpace("any 100 dl_type=0x806,dl_src=d2:df:f1:53:d4:49,nw_dst=10.128.4.5 Slice:SSH=4")
        main.FlowVisor.addFlowSpace("any 100 dl_type=0x800,nw_proto=6,nw_src=10.128.4.6,tp_dst=22 Slice:SSH=4")
        main.FlowVisor.addFlowSpace("any 100 dl_type=0x800,nw_proto=6,nw_src=10.128.4.5,tp_dst=22 Slice:SSH=4")
        main.FlowVisor.addFlowSpace("any 100 dl_type=0x800,nw_proto=6,nw_src=10.128.4.6,tp_src=22 Slice:SSH=4")
        main.FlowVisor.addFlowSpace("any 100 dl_type=0x800,nw_proto=6,nw_src=10.128.4.5,tp_src=22 Slice:SSH=4")
    
        main.step("Showing the flowSpace USING 'listFlowSpace'")
        main.FlowVisor.listFlowSpace()
    
        main.step("Showing the connected devices by USING 'listDevices'")
        main.FlowVisor.listDevices()
    
        main.step("Verifying the Slice, by checking SSH is happening to the destination or not")
        main.Pax_DPVM1.execute(cmd="ssh paxterra@10.128.4.6",prompt="ssword:",timeout=10)
    
        main.Pax_DPVM1.execute(cmd="\r",prompt="\$",timeout=10)
        main.Pax_DPVM1.execute(cmd="ssh paxterra@10.128.4.6",prompt="ssword:",timeout=10)
    
        main.Pax_DPVM1.execute(cmd="0nLab_gu3st",prompt="\$",timeout=10)
        main.Pax_DPVM1.execute(cmd="\r",prompt="\$",timeout=10)
        main.Pax_DPVM1.execute(cmd="ifconfig -a",prompt="\$",timeout=10)