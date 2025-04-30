![Platforms](https://img.shields.io/badge/platform-windows%20%7C%20osx%20%7C%20linux-lightgray.svg)
[![License](http://img.shields.io/:license-mit-blue.svg)](http://opensource.org/licenses/MIT)

**Fusion API:** 
[![Fusion API](https://img.shields.io/badge/Fusion%20API-blue)](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-86F49F01-14E4-44A4-9403-D13836F39BF4)
## Purpose
**ModelHierarchyAddIn** is used to retrieve the model hierarchy of a Fusion Design via the Fusion API and display the results in the **TEXT COMMANDS** window within Fusion 360.

## Platform & Technologies
- Fusion API  
- Visual Studio Code for debugging  
- Python programming language  

## Installation of Fusion 360 Add-ins

### I. Windows

1. Follow the instructions specific to the add-in or script to download the ZIP file.
2. Unzip to any convenient location.
3. Rename the top-level folder to match the name of the add-in (e.g., remove “-master” if present).
4. Copy the folder to:  
   `%AppData%\Autodesk\Autodesk Fusion 360\API\AddIns`  
   (Usually located at: `C:\Users\<YourUsername>\AppData\Autodesk\Autodesk Fusion 360\API\AddIns`)
5. You should now see the add-in folder (e.g., `Project-Archiver`) in the AddIns directory.

![image](https://github.com/user-attachments/assets/aacbb2c5-ee75-4d3b-9e09-1092380cf49e)

---

### II. MacOS – Fusion 360 Downloaded from Autodesk Website

1. Follow the instructions specific to the add-in or script to download the ZIP file.
2. Unzip to any convenient location.
3. Rename the top-level folder to match the name of the add-in.
4. Copy the folder to:  
   `~/Library/Application Support/Autodesk/Autodesk Fusion 360/API/AddIns`  
   *(click [here](https://www.macworld.com/article/222209/how-to-view-the-library-folder-in-mavericks.html) for reference)*
5. You should now see the add-in folder (e.g., `Project-Archiver`) in the AddIns directory.

![image](https://github.com/user-attachments/assets/8332d4dd-dcda-4797-994b-7d11ffa810a8)

---

### III. MacOS – Fusion 360 Downloaded from Mac App Store

1. Follow the instructions specific to the add-in or script to download the ZIP file.
2. Unzip to any convenient location.
3. Rename the top-level folder to match the name of the add-in.
4. Copy the folder to:  
   `~/Library/Containers/com.autodesk.mas.fusion360/Data/Library/Application Support/Autodesk/Autodesk Fusion 360/API/AddIns`  
   *(click [here](https://www.macworld.com/article/222209/how-to-view-the-library-folder-in-mavericks.html) for reference)*
5. You should now see the add-in folder (e.g., `OctoFusion`) in the AddIns directory.

![image](https://github.com/user-attachments/assets/a2a0520b-5691-4d29-80ec-b550340d3481)

---

## Starting the Add-In Inside Fusion 360

1. Launch Fusion 360.
2. Go to the **UTILITIES** tab and open **Scripts and Add-Ins**.
3. Navigate to the **Add-Ins** tab.
4. Select **ModelHierarchyAddIn** from the list.
5. Click on **Edit**.
6. Launch **Visual Studio Code**.
7. Start debugging by selecting **Run > Start Debugging** or press `F5`.
8. Upon successful execution, results will appear in the **TEXT COMMANDS** panel.

![image](https://github.com/user-attachments/assets/fc80ceeb-2d10-4b3b-885b-b0ede7726583)

---

## Output Overview

### Example Model Hierarchy Output:
```
Joints Demo Block

├── 98541A445_External Retaining Ring
├── 98541A445_External Retaining Ring
├── Base Plate
├── Slider
├── Rigid
├── Dual Pin Slot
├── Pin Slot
├── Ball
├── Revolute
├── Cylindrical
├── Planar
└── Planar + Tangency
```
![image](https://github.com/user-attachments/assets/128f7334-60c3-4ff6-b229-eb3360e5bcd8)

# 📄 License

This sample is licensed under the terms of the [MIT License](http://opensource.org/licenses/MIT). Please see the [LICENSE](LICENSE) file for full details.


---

# ✍️ Written by

Chandra shekar G [chandra.shekar.gopal@autodesk.com](chandra.shekar.gopal@autodesk.com), [Autodesk Partner Development](http://aps.autodesk.com)

---
Please refer to this page for more details: [Fusion API Docs](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-86F49F01-14E4-44A4-9403-D13836F39BF4) 

 
