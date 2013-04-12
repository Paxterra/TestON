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
public class TestSelectStepTable {
    public Label testStepId;
    public Label testStepName;
    public Label testStepStatus;
    
    public TestSelectStepTable() {
        
    }
    public TestSelectStepTable(Label stepId, Label stepName) {
        
        this.testStepId = stepId;
        this.testStepName = stepName;
        
        
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
    public void setTestStepName(Label newStepName) {
        testStepName = newStepName;
   }
      
}
