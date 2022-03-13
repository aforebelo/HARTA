# HARTA - Epicardial Fat Segmentation and Quantification Software
HARTA is software developed in the context of a master thesis project.
- Rebelo, A. F. O. (2021). Semi-automatic approach for epicardial fat segmentation and quantification on non-contrast cardiac CT. Dissertation submitted in partial fulfillment of the requirements for the degree of Master of Science in Biomedical Engineering, NOVA University of Lisbon, NOVA Scholl of Science and Technology. Retrieved from: [coming soon]

This application comes as an answer to the time-consuming task of manually segmenting epicardial fat on CT images. The proposed algorithm uses exclusively basic image operations, so no training steps are required. This software must be seen as a prototype that can be upgraded and optimized with the community's suggestions.

Feel free to contact me! Here is my email: afo.rebelo@campus.fct.unl.pt.

![All text](https://github.com/aforebelo/HARTA/blob/main/Screenshots/5_Semiautomatic_result.png)

## Getting Started
To use HARTA, follow the next steps:
1. Install Python 3.8.3
2. Access to the environment variables of Windows
3. Open the directory of Python
4. Copy the Python folder path (e.g., C:\Python38\) and the folder Scripts path (e.g., C:\Python38\Scripts\)
5. Download and extract the zip file of this repository
6. Open the terminal in the folder
7. Run the following lines

```pip install -r requirements.txt```

```python3 harta.py```

8. Enjoy HARTA!

## Input files
HARTA only accepts cardiac CT datasets in DICOM format (.dcm). Although it runs on contrast-enhanced images, HARTA is optimized for segmenting non-contrast images.
If you do not own any cardiac CT in DICOM format, you can use the public [Visual Lab - Cardiac Fat Database](https://visual.ic.uff.br/en/cardio/ctfat/).

## Version
1.0.0

## License
HARTA follows [CC-BY-NC-4.0 license](https://github.com/aforebelo/HARTA/blob/main/LICENSE), being freely available for academic purpose or individual research, however it is restricted for commercial use.

## Authors
Ana Filipa Rebelo
 
## Acknowledgments 
This project was supervised by:
- Prof. Dr. José Manuel Fonseca, Associate Professor in the Departement of  Electrical Engineering in NOVA Scholl of Science and Technology of NOVA University of Lisbon.

With great insights from:
- Doctor António Miguel Ferreira, Cardiologist in Hospital Santa Cruz of Western Lisbon Hospital Center.
