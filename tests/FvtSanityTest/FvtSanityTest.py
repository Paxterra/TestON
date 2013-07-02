
class FvtSanityTest :

    def __init__(self) :
        self.default = ''

    def CASE1(self,main) :

    
        main.case("Checking FVT Sanity Test")
        main.step("Checking FVT Sanity Test")
    
        listed = main.FlowVisor1.listDevices()
        utilities.assert_equals(expect=main.TRUE,actual=listed,onpass="Listed Devices connected to the flowvisor",onfail="No Devices connected to flowvisor")
    
        main.step(" Configuring VLANS")
        vlan_setup   = main.HPSwitch1.setup_vlan(vlan_id='2', vlan_name="OF_DP")
        utilities.assert_equals(expect=main.TRUE,actual=vlan_setup,onpass="Configured VLAN successfully ",onfail="Failed to configure VLAN")
    
        untagged = main.HPSwitch1.vlan_untagged(vlan_id='2', untagging='a5-a24,b1-b24')
        utilities.assert_equals(expect=main.TRUE,actual=untagged,onpass="VLAN untagging done Successfully",onfail="Failed to untag VLAN")
    
    
        main.step(" Configuring Controller")
        controller_added = main.HPSwitch1.add_openflow_controller(controller_id='3', controller_ip='10.128.4.3', interface_vlan_id='1')
        utilities.assert_equals(expect=main.TRUE,actual=controller_added,onpass="OpenFlow Controller Added Successfully",onfail="Failed to Configure OpenFlow controller")
    
    
        main.step(" Configuring Openflow Instance")
        instance_created = main.HPSwitch1.create_openflow_instance(instance_name="InstanceTesting2",controller_id='3', member_vlan_id='2')
        utilities.assert_equals(expect=main.TRUE,actual=instance_created,onpass="OpenFlow Instance Added Successfully",onfail="Failed to Configure OpenFlow Instance")
    
    
        main.step(" Enable Openflow")
        paired = main.HPSwitch1.pair_vlan_with_openflow_instance(vlan_id='1')
        utilities.assert_equals(expect=main.TRUE,actual=paired,onpass="OpenFlow Instance Paired with VLAN",onfail="Failed to Paired Openflow instance with VLAN")
    
        paired = main.HPSwitch1.pair_vlan_with_openflow_instance(vlan_id='2')
        utilities.assert_equals(expect=main.TRUE,actual=paired,onpass="OpenFlow Instance Paired with VLAN",onfail="Failed to Paired Openflow instance with VLAN")
    
        enabled = main.HPSwitch1.openflow_enable()
        utilities.assert_equals(expect=main.TRUE,actual=enabled,onpass="OpenFlow enabled successfully",onfail="Failed to enable Openflow")
    
    
        main.step("Showing Controllers and Vlans")
        list_controllers = main.HPSwitch1.show('openflow controllers')
        utilities.assert_equals(expect=main.TRUE,actual=list_controllers,onpass="Openflow controllers listed",onfail="Failed to list controllers")
    
        list_vlans = main.HPSwitch1.show('vlans')
        utilities.assert_equals(expect=main.TRUE,actual=list_vlans,onpass="VLANS listed",onfail="Failed to list LANS")
    
    
        main.step(" Tearing up the configurations")
        removed_vlan = main.HPSwitch1.remove_vlan('2')
        utilities.assert_equals(expect=main.TRUE,actual=removed_vlan,onpass="VLAN removed successfully",onfail="Failed to remove VLAN")
    
        removed_controller = main.HPSwitch1.remove_controller('3')
        utilities.assert_equals(expect=main.TRUE,actual=removed_controller,onpass="Controller removed successfully",onfail="Failed to remove Controller")
    
        removed_instance = main.HPSwitch1.remove_openflow_instance('InstanceTesting2')
        utilities.assert_equals(expect=main.TRUE,actual=removed_instance,onpass="Instance removed successfully",onfail="Failed to remove Instance")