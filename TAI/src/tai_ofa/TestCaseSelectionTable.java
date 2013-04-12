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
public class TestCaseSelectionTable {
    
    public CheckBox testCaseIdCheck;
    public Label testCaseId;
    public Label testCaseName;
    public TestCaseSelectionTable() {
        
    }
    public TestCaseSelectionTable(CheckBox idCheck, Label caseId, Label caseName) {
        this.testCaseIdCheck = idCheck;
        this.testCaseId = caseId;
        this.testCaseName = caseName;
    }
    
    public CheckBox getTestCaseCheckBox() {
        return  testCaseIdCheck;
    }
    public void setTestCaseCheckBox(CheckBox newCheck) {
        testCaseIdCheck = newCheck;
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
}
