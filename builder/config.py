import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_PATH = os.path.join(BASE_PATH, 'docs')
API_KEY = os.getenv('INPUT_API_KEY', '') or 'AIzaSyC6dzKyPLK2TsfjiWtxytUE7LQEr64QPwc'

DATA_URL = 'https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vRAwpV7A3DeMSphErTBtq4BgwayxgVLpYXF-zAP7UOwB1ogZJH4kPeYAP0DhtHzmMk-pD0RvA7pactJ/pubhtml'
