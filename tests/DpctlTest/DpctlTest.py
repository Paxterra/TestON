
class DpctlTest :

    def __init__(self) :
        self.default = ''

    def CASE1(self,main) :

        main.case("DPCTL Ping Host")
        main.step("Adding flow for host2")
        main.DPCTL1.addFlow(tcpip=main.params['CASE1']['STEP1']['tcpip'], tcpport=main.params['CASE1']['STEP1']['tcpport'], inport=main.params['CASE1']['STEP1']['inport'], timeout=main.params['CASE1']['STEP1']['timeout'], action=main.params['CASE1']['STEP1']['action'])
        main.step("Adding Another Flow for Host3")
        main.DPCTL1.addFlow(tcpip=main.params['CASE1']['STEP2']['tcpip'], tcpport=main.params['CASE1']['STEP2']['tcpport'], inport=main.params['CASE1']['STEP2']['inport'], timeout=main.params['CASE1']['STEP2']['timeout'], action=main.params['CASE1']['STEP2']['action'])
        main.step("Ping From h2 to h3")
        main.Mininet1.pingHost(src=main.componentDictionary['DPCTL1']['src'], target=main.componentDictionary['DPCTL1']['target'], controller=main.componentDictionary['DPCTL1']['controller'])
        result  = main.last_result
        utilities.assert_equals(expect=main.TRUE,actual=result,onpass="Ping Successful",onfail="Ping failed")
    
    def CASE2(self,main) :

        main.case("DPCTL Show Flow")
        main.step("Adding flow for host2")
        main.DPCTL1.addFlow(tcpip=main.params['CASE2']['STEP1']['tcpip'], tcpport=main.params['CASE2']['STEP1']['tcpport'], inport=main.params['CASE2']['STEP1']['inport'], timeout=main.params['CASE2']['STEP1']['timeout'], action=main.params['CASE2']['STEP1']['action'])
        main.step("Adding Another Flow for Host3")
        main.DPCTL1.addFlow(tcpip=main.params['CASE2']['STEP2']['tcpip'], tcpport=main.params['CASE2']['STEP2']['tcpport'], inport=main.params['CASE2']['STEP2']['inport'], timeout=main.params['CASE2']['STEP2']['timeout'], action=main.params['CASE2']['STEP2']['action'])
        main.step("Execute Show Flow")
        main.DPCTL1.showFlow(tcpip=main.params['CASE2']['tcpip'], tcpport=main.params['CASE2']['tcpport'])
        result = main.last_result
        utilities.assert_equals(expect=main.TRUE,actual=result,onpass="SHOW FLOW IS EXECUTED",onfail="Show Flow Execution failed")