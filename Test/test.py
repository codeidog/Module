from SubModule.submodule import default
import pytest
import requests
from main import *
from SubModule import *
from requests import Response
import json

def default_test(response):    
    assert 'version' in response.keys()
    assert 'name' in response.keys()


def test_module():        
    response = json.loads(index())
    default_test(response= response)

def test_submodule():
    response = json.loads(index())
    default_test(response= response)

    

