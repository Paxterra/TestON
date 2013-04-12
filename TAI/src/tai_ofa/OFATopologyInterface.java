/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package tai_ofa;

import javafx.scene.control.Label;
import javafx.scene.control.TextField;

/**
 *
 * @author Raghav Kashyap (raghavkashyap@paxterrasolutions.com)
 */
public class OFATopologyInterface {
    public Label interFaceNumber; 
    private TextField deviceName;
    private  TextField deviceType;
     

    
    public OFATopologyInterface(Label emailtext,TextField deviceNameText,TextField deviceTypeText){
            this.deviceName = deviceNameText;
            this.deviceType = deviceTypeText;
            this.interFaceNumber = emailtext;
    }
     
        public TextField getDeviceName() {
            return deviceName;
        }
        public void setDeviceName(TextField fName) {
            deviceName = fName;
        }
        
        public TextField getDeviceType() {
            return deviceType;
        }
        public void setDeviceType(TextField fName) {
            deviceType = fName;
        }
        
        public Label getInterFaceNumber() {
            return interFaceNumber;
        }
        public void setInterFaceNumber(Label fName) {
            interFaceNumber = fName;
        }
}

    

