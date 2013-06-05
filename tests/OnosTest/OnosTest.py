
class OnosTest :

    def __init__(self) :
        self.default = ''

    def CASE1(self,main) :

        main.case("Testing the ONOS sanity")
        main.step("Testing the ONOS sanity")
    
        main.Zookeeper1.status()
        main.Cassandra1.status ()
        main.ONOS1.status()
    
        Response = main.ONOSRESTAPI1.curlRequest()
        main.log.info("***************************************")
        main.log.info(Response)
        main.log.info("***************************************")
    
        main.ONOS1.stop()
        main.Cassandra1.stop()
        main.Zookeeper1.stop()