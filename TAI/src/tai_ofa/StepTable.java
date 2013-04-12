/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package tai_ofa;

import javafx.scene.control.Label;

/**
 *
 * @author Raghav Kashyap (raghavkashyap@paxterrasolutions.com)
 */
public class StepTable {
    public Label testStepId;
    public Label testStepName;
    public Label testStepStatus;
    
    public StepTable() {
        
    }
    public StepTable(Label stepId, Label stepName,Label status) {
        
        this.testStepId = stepId;
        this.testStepName = stepName;
        this.testStepStatus = status;
        
    }
    
  
     public Label getTestStepId() {
        return  testStepId;
    }
    public void setTestStepId(Label newStepId) {
        testStepId = newStepId;
    }
    public Label getTestStepName() {
        return  testStepName;
    }
    public void setTestCaseName(Label newStepName) {
        testStepName = newStepName;
    }
    public Label getTestStepStatus() {
        return  testStepStatus;
    }
    public void setTestCaseStatus(Label newStepStatus) {
        testStepStatus = newStepStatus;
    }
      
}
