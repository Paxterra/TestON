/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package tai_ofa;

import javafx.scene.control.Label;

/**
 *
 * @author Raghav Kashyap raghavkashyap@paxterrasolutions.com
 */

public class FinalSummaryTable {
    public Label summaryItem;
    public Label information;
    
    public FinalSummaryTable() {
        
    }
    public FinalSummaryTable(Label summaryItem, Label information) {
        
        this.summaryItem = summaryItem;
        this.information = information;
        
    }
    
  
     public Label getSummaryItem() {
        return  summaryItem;
    }
    public void setSummaryItem(Label newSummaryItem) {
        summaryItem = newSummaryItem;
    }
    public Label getInformation() {
        return  information;
    }
    public void setInformation(Label newInformation) {
        information = newInformation;
    }
    
}

