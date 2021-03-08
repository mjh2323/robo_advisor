## Robo Advisor App
This application allows users to obtain real-time price data for stock's of their choice, as well as purchasing recommendations. 

## SETUP 

To get started, please obtain an Alphantage API Key (https://www.alphavantage.co/support/#api-key).

Afterwards, create a new file in this respository called ".env", and update the contents of the "env." file to show your API key: 
    ALPHANTAGE_API_KEY="xyz123"
We will create a .env file within our repository. This will secure your API key.
```py
ALPHANTAGE_API_KEY="xyz123"
```

You'll need to setup a virtual environment with conda. (Including the python version specifies we would like to use python 3.8) 
```py
conda create -n stocks-env python=3.8
conda activate stocks-env
```

Next, we have to install the necessary packages. To do this: 
```py
pip install -r requirements.txt
```

## USAGE

Run the reccomendsation script -->
```py
python app/robo_advisor.py
```


