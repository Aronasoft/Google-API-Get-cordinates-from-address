from mapbox import Geocoder
from dotenv import load_dotenv 
import pandas as pd

load_dotenv()

geocoder = Geocoder()

latLong = []
longt = []
PropAddress = []
def load_dataset():
    """Load data from CSV."""
    citiDF = pd.read_csv('Desktop/data/data_new_1.csv').head(12493)
    
    return citiDF


def geocode_address(address):
    """Geocode street address into lat/long."""
   
     
    response = geocoder.forward(address) 
    #print(response.json());
    #exit();
    
    latitude = str(response.json()['features'][0]['center'][1])
    longitude = str(response.json()['features'][0]['center'][0])

    coords = str(response.json()['features'][0]['center'])
    coords = coords.replace(']', '')
    coords = coords.replace('[', '')
    print(coords)



    PropAddress.append(address)
    latLong.append(latitude)
    longt.append(longitude)

    
    df = pd.DataFrame(data={"PROPERTYNAME":PropAddress, "longitude":longt, "latLong": latLong})	
    df.to_csv("Desktop/data/data_new_append.csv", sep=',',index=False)
     
    #return coords


def geocode_dataframe(row):
    """Geocode start and end address."""
      
    propAddress = str(row['PROPERTY_NAME'])+ "," +str(row['PROPERTY_STREET'])+","+ str(row['PROPERTY_CITY'])+","+str(row['PROPERTY_STATE'])
     
    print(propAddress);
    citiDF['start_station_latlong'] = geocode_address(propAddress)
     
    
     

citiDF = load_dataset()
citiDF.apply(geocode_dataframe, axis=1)

