/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package tai_ofa;

import javafx.scene.control.Label;

/**
 *
 * @author Raghav Kashyap (raghavkashyap@paxterrasolutions.com)
	
 *   TestON is free software: you can redistribute it and/or modify
 *   it under the terms of the GNU General Public License as published by
 *   the Free Software Foundation, either version 2 of the License, or
 *   (at your option) any later version.

 *   TestON is distributed in the hope that it will be useful,
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *   GNU General Public License for more details.


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
