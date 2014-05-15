
class Odl :

    def __init__(self) :
        self.default = ''

    def CASE1(self,main) :

        main.case("ping to host")
        main.step("ping to host h2 from h1")
        result = main.Mininet1.pingHost(SRC=main.params['CASE1']['src'],TARGET=main.params['CASE1']['target'])
        utilities.assert_equals(expect=main.TRUE,actual=result,onpass="Ping to host successful",onfail="Ping host not successful")
    
        result = main.Mininet1.dump()
        utilities.assert_equals(expect=main.TRUE,actual=result,onpass="Getting dump results",onfail="Not getting dump results")
    
        result = main.Mininet1.net()
        utilities.assert_equals(expect=main.TRUE,actual=result,onpass="Getting net configuration",onfail="Not getting net configuration")
    
        result = main.Mininet1.intfs()
        utilities.assert_equals(expect=main.TRUE,actual=result,onpass="Getting intfs results",onfail="Not getting intfs results")
    
    def CASE2(self,main) :

        main.case("Get list of containers")
        main.step("Getting list of containers")
        result = main.ODL1.get(URL=main.params['CASE2']['get_url'])
        utilities.assert_equals(expect=200,actual=result,onpass="Getting containers list",onfail="Not getting any containers list")
    
    def CASE3(self,main) :

        main.case("Create a container")
        main.step("Creating a new container")
        result = main.ODL1.put(URL=main.params['CASE3']['put_url'],BODY=main.params['CASE3']['put_body'])
        utilities.assert_equals(expect=201,actual=result,onpass="Container getting added",onfail="Container not added")
    
    def CASE4(self,main) :

        main.case("Get container flows")
        main.step("Getting container flows")
        result  = main.ODL1.get(main.params['CASE4']['get_url'])
        utilities.assert_equals(expect=200,actual=result,onpass="Container flows getting",onfail="Container flows not getting")
    
    def CASE5(self,main) :

        main.case("Get topology")
        main.step("Getting topology ")
        result  = main.ODL1.get(main.params['CASE5']['get_url'])
        utilities.assert_equals(expect=200,actual=result,onpass="Topology getting successfully",onfail="Topology not getting successfully")
    
    def CASE6(self,main) :

        main.case("Get list of subnets")
        main.step("Getting list of Subnets")
        result  = main.ODL1.get(main.params['CASE6']['get_url'])
        utilities.assert_equals(expect=200,actual=result,onpass="Getting list of subnets",onfail="Not getting list of subnets")
    
    def CASE7(self,main) :

        main.case("Get list of hosts")
        main.step("Getting list of hosts from topology")
        result  = main.ODL1.get(main.params['CASE7']['get_url'])
        utilities.assert_equals(expect=200,actual=result,onpass="Getting list of hosts",onfail="Not getting list of hosts")
    
    def CASE8(self,main) :

        main.case("Add subnet to the controller")
        main.step("Adding subnet to the controller")
        result = main.ODL1.put(URL=main.params['CASE8']['put_url'],BODY=main.params['CASE8']['put_body'])
        utilities.assert_equals(expect=201,actual=result,onpass="Subnet is added successfully",onfail="Subnet not added")
    
    def CASE9(self,main) :

        main.case("Get list of connections")
        main.step("Getting list of connections")
        result  = main.ODL1.get(main.params['CASE9']['get_url'])
        utilities.assert_equals(expect=200,actual=result,onpass="Getting list of connections",onfail="Connections are not getting")
    
    def CASE10(self,main) :

        main.case("Get list of nodes")
        main.step("Getting list of nodes")
        result  = main.ODL1.get(main.params['CASE10']['get_url'])
        utilities.assert_equals(expect=200,actual=result,onpass="Getting list of nodes",onfail="Not getting list of nodes")
    
    def CASE11(self,main) :

        main.case("Add user link")
        main.step("Adding userlink to the topology")
        result = main.ODL1.put(URL=main.params['CASE11']['put_url'],BODY=main.params['CASE11']['put_body'])
        utilities.assert_equals(expect=200,actual=result,onpass="Use link added successfully",onfail="User link not added")
    
    def CASE12(self,main) :

        main.case("Get flow statistics")
        main.step("Getting flow Statistics from topology")
        result  = main.ODL1.get(main.params['CASE12']['get_url'])
        utilities.assert_equals(expect=200,actual=result,onpass="Getting all flow statistics",onfail="Not getting flow statistics")
    
    def CASE13(self,main) :

        main.case("Get port statistics")
        main.step("Getting port statistics from topology")
        result  = main.ODL1.get(main.params['CASE13']['get_url'])
        utilities.assert_equals(expect=200,actual=result,onpass="Getting all port statistics",onfail="Not getting port statistics")
    
    def CASE14(self,main) :

        main.case("Get table statistics")
        main.step("Getting default table Statistics")
        result  = main.ODL1.get(main.params['CASE14']['get_url'])
        utilities.assert_equals(expect=200,actual=result,onpass="Getting all Table statistics",onfail="Not getting table statistics")
    
    def CASE15(self,main) :

        main.case("Adding Flows")
        main.step("Adding flow1 to reach host1")
        result = main.ODL1.put(URL=main.params['CASE15']['put_url'],BODY=main.params['CASE15']['put_body'])
        utilities.assert_equals(expect=201,actual=result,onpass="Adding flow is sucessfull",onfail="Adding flow is not sucessfull")
    
    def CASE16(self,main) :

        main.case("Get flow stats")
        main.step("Getting  flow stats")
        result  = main.ODL1.get(main.params['CASE16']['get_url'])
        utilities.assert_equals(expect=200,actual=result,onpass="Getting flow stats sucessfully",onfail="Not getting flow stats sucessfully")
    
    def CASE17(self,main) :

        main.case("Get flow stats")
        main.step("Getting  flow stats")
        result  = main.ODL1.get(main.params['CASE17']['get_url'])
        utilities.assert_equals(expect=200,actual=result,onpass="Getting flow stats sucessfully",onfail="Not getting flow stats sucessfully")
    def CASE18(self,main) :

        main.case("Add static route")
        main.step("Adding static route ")
        result = main.ODL1.put(URL=main.params['CASE18']['put_url'],BODY=main.params['CASE18']['put_body'])
        utilities.assert_equals(expect=201,actual=result,onpass="static route added successfully",onfail="static route not added")
    
    def CASE19(self,main) :

        main.case("Get static route")
        main.step("Getting static route")
        result  = main.ODL1.get(main.params['CASE19']['get_url'])
        utilities.assert_equals(expect=200,actual=result,onpass="Getting static route",onfail="Not getting static route")
    
    def CASE20(self,main) :

        main.case("Remove static route")
        main.step("Removing static route")
        result = main.ODL1.delete(main.params['CASE20']['delete_url'])
        utilities.assert_equals(expect=204,actual=result,onpass="User link removed",onfail="User link not removed")
    
    def CASE21(self,main) :

        main.case("Add flowspec to cont1")
        main.step("Adding flowspec to cont1 ")
        result = main.ODL1.put(URL=main.params['CASE21']['put_url'],BODY=main.params['CASE21']['put_body'])
        utilities.assert_equals(expect=201,actual=result,onpass="flowsppec added successfully",onfail="flowspecs not added")
    
    def CASE22(self,main) :

        main.case("Get flowspecs")
        main.step("Getting flowspecs on cont1")
        result  = main.ODL1.get(main.params['CASE22']['get_url'])
        utilities.assert_equals(expect=200,actual=result,onpass="Getting flowspecs ",onfail="Not getting flowspecs")
    
    def CASE23(self,main) :

        main.case("Get node connectors list")
        main.step("Getting list of NodeConnectors")
        result = main.ODL1.get(URL=main.params['CASE23']['get_url'])
        utilities.assert_equals(expect=200,actual=result,onpass="Got list of nodeconnectors",onfail="Not getting list of nodeconnectors")
    
    def CASE24(self,main) :

        main.case("Add property description")
        main.step("Adding property description to the switch")
        result = main.ODL1.put(URL=main.params['CASE24']['put_url'],BODY=main.params['CASE24']['put_body'])
        utilities.assert_equals(expect=201,actual=result,onpass="Property Description added",onfail="Property description not added")
    
    def CASE25(self,main) :

        main.case("Add static host")
        main.step("Adding static host")
        result = main.ODL1.put(URL=main.params['CASE25']['put_url'],BODY=main.params['CASE25']['put_body'])
        utilities.assert_equals(expect=201,actual=result,onpass="static host added successfully",onfail="static host not added")
    
    def CASE26(self,main) :

        main.case("Add bandwidth ")
        main.step("Adding bandwidth to swith")
        result  = main.ODL1.put(URL=main.params['CASE26']['put_url'],BODY=main.params['CASE26']['put_body'])
        utilities.assert_equals(expect=201,actual=result,onpass="Bandwidth added successfully",onfail="Bandwidth not added ")
    
    def CASE27(self,main) :

        main.case("Get Static Host")
        main.step("Getting Static Host")
        result  = main.ODL1.get(main.params['CASE27']['get_url'])
        utilities.assert_equals(expect=200,actual=result,onpass="Getting Static Host",onfail="Not getting Static Host")
    
    def CASE28(self,main) :

        main.case("Delete bandwidth ")
        main.step("Deleting bandwidth from swith")
        result  = main.ODL1.delete(main.params['CASE28']['delete_url'])
        utilities.assert_equals(expect=204,actual=result,onpass="Bandwidth deleted successfully",onfail="Bandwidth not deleted")
    
    def CASE29(self,main) :

        main.case("Remove user_link")
        main.step("Removing userlink")
        result = main.ODL1.delete(main.params['CASE29']['delete_url'])
        utilities.assert_equals(expect=204,actual=result,onpass="User link removed",onfail="User link not removed")
    
    def CASE30(self,main) :

        main.case("Removing flow")
        main.step("Removing flow to reach host1")
        result = main.ODL1.delete(main.params['CASE30']['delete_url'])
        utilities.assert_equals(expect=204,actual=result,onpass="Flow Removed sucessfully",onfail="Unable to remove flow")
    
    def CASE31(self,main) :

        main.case("Delete node property")
        main.step("Removing Node property from topology")
        result  = main.ODL1.delete(main.params['CASE31']['delete_url'])
        utilities.assert_equals(expect=204,actual=result,onpass="Node property deleted successfully",onfail="Node property not deleted ")
    
    def CASE32(self,main) :

        main.case("Remove Static Host")
        main.step("Removing Static Host")
        result = main.ODL1.delete(main.params['CASE32']['delete_url'])
        utilities.assert_equals(expect=204,actual=result,onpass="Static Host removed successfully",onfail="Static Host not removed")
    
    def CASE33(self,main) :

        main.case("Remove existing containers")
        main.step("Removing container")
        result = main.ODL1.delete(main.params['CASE33']['delete_url'])
        utilities.assert_equals(expect=204,actual=result,onpass="Container removed successfully",onfail="Container not removed")
    
