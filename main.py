import os
import tarfile
import urllib.request
import pandas as pd

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


def fetch_housing_data(housing_url, housing_path):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

def load_housing_data(housing_path):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

if __name__ == "__main__" :
    #fetch_housing_data(HOUSING_URL, HOUSING_PATH)
    housing = load_housing_data(HOUSING_PATH)

    #print("housing.head() ->" + "\n", housing.head())
    #print("housing.info() ->" + "\n", housing.info())
    #print("housing.value_counts() ->" + "\n", housing.value_counts())
    print("housing.describe() ->" + "\n", housing.describe())