class SpirentTest :

    def __init__(self) :
        self.default = ''

    def CASE1(self,main) :

        main.case("Basic Spirent test")
        main.step("Check if handle is created")
        main.log.info("Handle created successfully")
    
        main.case("Creating a Project")
        main.step("Checking the creation of project")
        project = main.Stc1.create('project1')
    
        main.step("Get Project attributes")
        projectAtt = main.Stc1.get(project ,'name')
    
    
    
        main.step("Creating ports under the Project")
        port1 = main.Stc1.create('port',under=project)
        port2 = main.Stc1.create('port',under=project)
    
        main.step("Configuring the Port locations")
        chassisAddress = '10.254.1.102'
        slot = '1'
        p1 = '1'
        p2 = '2'
        main.Stc1.config(port1, location="//%s/%s/%s" % (chassisAddress, slot,p1))
        main.Stc1.config(port2, location="//%s/%s/%s" % (chassisAddress, slot,p2))
    
        main.step("Creating streamBlock on port1")
        streamBlock = main.Stc1.create('streamBlock',under=port1)
        generator = main.Stc1.get(port1,'children-generator')
        analyzer = main.Stc1.get(port2,'children-Analyzer')
    
    
        main.step("Attaching Ports...")
        main.Stc1.perform('AttachPorts', portList = [port1 , port2], autoConnect='TRUE')
        main.Stc1.apply ()
    
        main.case("Subscribe the ports ports from Project")
        main.step("Call Subscribe...")
        port1GeneratorResult    = main.Stc1.subscribe(Parent=project,ResultParent=port1,ConfigType='Generator',resulttype='GeneratorPortResults',filenameprefix="Generator_port1_counter/%s" % port1 ,Interval=2)
        port2AnalyzerResult = main.Stc1.subscribe(Parent=project,ResultParent=port2,ConfigType='Analyzer',resulttype='AnalyzerPortResults',filenameprefix="Analyzer_port2_counter/%s" % port2)
    
        main.step("Starting traffic")
        main.Stc1.perform('AnalyzerStart', analyzerList = 'analyzer')
    
    
        main.step("Start Analyzer")
        main.log.info("# wait for analyzer to start")
        main.Stc1.sleep(numberSecondsInteger=1)
        main.Stc1.perform('GeneratorStart', generatorList = 'generator')
    
        main.step("Sleep 5 seconds...")
        main.log.info("# generate traffic for 5 seconds")
        main.Stc1.sleep(numberSecondsInteger=5)
    
        main.step("Stopping Traffic...")
        main.log.info("stop generator")
        main.Stc1.perform('GeneratorStop', generatorList = 'generator')
        main.log.info("Stop analyzer")
        main.Stc1.perform('AnalyzerStop', analyzerList = 'analyzer')
    
        main.step("Call Unsubscribe...")
        main.Stc1.unsubscribe(port2AnalyzerResult)
        main.Stc1.unsubscribe(port1GeneratorResult)
    
        main.step("Call Disconnect...")
        main.Stc1.disconnect(chassisAddress)
        main.Stc1.delete(project)
