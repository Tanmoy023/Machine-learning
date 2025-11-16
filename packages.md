# Virtual Environment (in windows)
sudo apt install python3-venv
python -m venv myenv # To create a virtual environment
myenv/Scripts/activate # To activate this virtual environment

# install jupyter notebook
pip install jupyter

# open jupyter notebook
jupyter notebook

# Install numpy
pip install numpy

# Install pandas
pip install pandas
pip install openpyxl // to read .xlsx and export DataFrame into .xlsx file

# install matplotlib
pip install matplotlib

# install seaborn
pip install seaborn

# install scikit Learn
pip install scikit-learn

# upgrade all python libraryes
pip install --upgradelibrary-name

# delete Virtual environment(ubuntu)
deactivate
rm -rf myenv


python -m venv myenv
myenv/Scripts/activate
pip install jupyter
pip install numpy
pip install pandas
pip install openpyxl
pip install matplotlib
pip install seaborn
pip install scikit-learn