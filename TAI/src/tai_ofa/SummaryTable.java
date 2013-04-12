/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package tai_ofa;

import javafx.scene.control.CheckBox;
import javafx.scene.control.Label;

/**
 *
 * @author Raghav Kashyap (raghavkashyap@paxterrasolutions.com)
 */
public class SummaryTable {
    public Label testCaseId;
    public Label testCaseName;
    public Label testCaseStatus;
    public Label testCaseStartTime;
    public Label testCaseEndTime;
    public SummaryTable() {
        
    }
    public SummaryTable(Label caseId, Label caseName,Label status,Label startTime, Label endTime) {
        
        this.testCaseId = caseId;
        this.testCaseName = caseName;
        this.testCaseStatus = status;
        this.testCaseStartTime =startTime;
        this.testCaseEndTime = endTime;
    }
    
  
     public Label getTestCaseId() {
        return  testCaseId;
    }
    public void setTestCaseId(Label newCaseId) {
        testCaseId = newCaseId;
    }
    public Label getTestCaseName() {
        return  testCaseName;
    }
    public void setTestCaseName(Label newCaseName) {
        testCaseName = newCaseName;
    }
    public Label getTestCaseStatus() {
        return  testCaseStatus;
    }
    public void setTestCaseStatus(Label newCaseStatus) {
        testCaseStatus = newCaseStatus;
    }
    
    public Label getTestCaseStartTime() {
        return  testCaseStartTime;
    }
    public void setTestCaseStartTime(Label newCaseStartTime) {
        testCaseStartTime = newCaseStartTime;
    }
    public Label getTestCaseEndTime() {
        return  testCaseEndTime;
    }
    public void setTestCaseEndTime(Label newCaseEndTime) {
        testCaseEndTime = newCaseEndTime;
    }
   
    
}
