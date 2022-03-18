# Method-level-defect-prediction
## Obtaining change metrics
Steps to run the Change Distiller Script from Command Prompt on two versions of the source
code
Generating change script text files:
1. Install Java Version 8
2. Set environment variables to include the path of jdk directory
3. Download and extract zip folder containing the scripts
4. Open the folder containing the extracted scripts using the terminal
5. Run the jar file ‘ChangeScriptGenerator.jar’ using the command java -jar
ChangeScriptGenerator.jar
6. Enter the absolute paths of the version/target folder as prompted.

In the target folder, you will find text files containing the changes (Edit scripts) in the two
versions

Generating change metrics csv files:
1. Run the python file ‘ObtainChangeMetrics.py’ using the command python
ObtainChangeMetrics.py
2. Enter the absolute path of the directory containing the edit script obtained in the previous
steps.
3. Enter the absolute path of the target folder where you want the CSV files to be stored
