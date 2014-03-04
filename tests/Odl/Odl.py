class Odl :

    def __init__(self) :
        self.default = ''

    def CASE1(self,main) :

        main.case("Get list of containers")
        main.step("Getting list of containers")
        result = main.ODL1.list_containers()
        utilities.assert_equals(expect=200,actual=result,onpass="getting containers list",onfail="not getting any containers list")
    def CASE2(self,main) :

        main.case("remove existing containers")
        main.step("removing container")
        result = main.ODL1.remove_container(CONTAINER='cont1')
        utilities.assert_equals(expect=204,actual=result,onpass="container removed successfully",onfail="container not removed")
    def CASE3(self,main) :

        main.case("create a container")
        main.step("creating a new container")
        result = main.ODL1.create_container(CONTAINER='cont1',INPUT={"container" : "cont1","nodeConnectors" : ["OF|1@OF|00:00:00:00:00:00:00:01","OF|2@OF|00:00:00:00:00:00:00:02"],"staticVlan" : "10"})
        utilities.assert_equals(expect=201,actual=result,onpass="container getting added",onfail="container not added")
    
    def CASE4(self,main) :

        main.case("get container flows")
        main.step("getting container flows")
        result  = main.ODL1.flow_stats(CONTAINER='cont1')
        utilities.assert_equals(expect=200,actual=result,onpass="container flows getting",onfail="container flows not getting")
