#!/usr/bin/python3
import pytest
import requests
import testGet

"""
Add new pet to the store
"""


def putPet(pet_name, photoUrls):
    url = 'https://petstore.swagger.io/v2/pet'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json', }
    payload = '{"name": "' + pet_name + '", "photoUrls": ["' + photoUrls + '"]}'
    r = requests.put(url, headers=headers, data=payload)

    return r


"""
Put new pet with required payload, Get API return the new posted pet
"""


def validatePutPet(pet_name, photoUrls):
    r = putPet(pet_name, photoUrls)
    if r.status_code == 200:

        url = 'https://petstore.swagger.io/v2/pet' + str(r.json()['id'])
        headers = {'accept': 'application/json', }
        r1 = requests.get(url, headers=headers)

        if (r1.status_code == 200):
            data = r1.json()
            if (len(data) > 0):
                for i in range(len(data)):
                    if data[i]['name'] == pet_name:
                        return True

            return False

        else:
            return "Get API failed!"
    else:
        return "Post API failed!"


"""
Put pet without name in payload
"""


def putPetWithoutName(photoUrls):
    url = 'https://petstore.swagger.io/v2/pet'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json', }
    payload = '{"photoUrls": ["' + photoUrls + '"]}'
    r = requests.put(url, headers=headers, data=payload)

    return r.status_code


"""
Put pet without photoUrls in payload
"""


def putPetWithoutPhotoUrls(pet_name):
    url = 'https://petstore.swagger.io/v2/pet'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json', }
    payload = '{"name": "' + pet_name + '"}'
    r = requests.put(url, headers=headers, data=payload)

    return r.status_code


"""
Put pet without payload
"""


def putPetWithoutPayload():
    url = 'https://petstore.swagger.io/v2/pet'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json', }
    r = requests.put(url, headers=headers)

    return r.status_code


"""
Put pet without Header
"""


def putPetWithoutHeader(pet_name, photoUrls):
    url = 'https://petstore.swagger.io/v2/pet'
    payload = '{"name": "' + pet_name + '", "photoUrls": ["' + photoUrls + '"]}'
    r = requests.put(url, data=payload)

    return r.status_code


"""
Put pet with not existing payload
"""


def putPetWithWrongKey(pet_name, photoUrls):
    url = 'https://petstore.swagger.io/v2/pet'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json', }
    payload = '{"pet_Name": "' + pet_name + '", "photoUrls": ["' + photoUrls + '"]}'
    r = requests.put(url, headers=headers, data=payload)

    return r.status_code


"""
Test curl -d '{"name":"dog1", "photoUrls": ["https://www.test.com"]}' 
	-H "accept: application/json, Content-Type: application/json" -X PUT https://petstore.swagger.io/v2/pet
"""


# Put pet with name & photoUrls
# currently the Put pet API doesn't have error check for required name and photoUrls fields
@pytest.mark.parametrize("pet_name, photoUrls, expected",
                         [("dog_1234", "https://www.nationalgeographic.com/animals/mammals/facts/domestic-dog", 200),
                          ("", "http://www.dogphoto.com", 400), ("dog_name", "", 400), ("", "", 400)])
def testPutPet(pet_name, photoUrls, expected):
    assert putPet(pet_name, photoUrls).status_code == expected


# Post pet with required payload, Get API return the posted pet
# currently Get pet API is not working correctly which cause this test case failed
def testvalidatePutPet():
    assert validatePutPet("dog_12345", "https://www.nationalgeographic.com/animals/mammals/facts/domestic-dog") == True


# Post pet without photoUrls in payload
# currently Post pet API doesn't have error check for required photoUrls field
def testputPetWithoutPhotoUrls():
    assert putPetWithoutPhotoUrls('dog_12345') == 400


# Post pet without name in payload
# currently Post pet API doesn't have error check for required name field
def testputPetWithoutName():
    assert putPetWithoutName('https://www.nationalgeographic.com/animals/mammals/facts/domestic-dog') == 400


# Post pet without Header
def testputPetWithoutHeader():
    assert putPetWithoutHeader('dog_12345', 'https://www.nationalgeographic.com/animals/mammals/facts/domestic-dog') == 415


# Post pet without payload
def testputPetWithoutPayload():
    assert putPetWithoutPayload() == 405


# Post pet with not existing payload
# currently Post pet API doesn't have error check for wrong input parameter
def testputPetWithWrongKey():
    assert putPetWithWrongKey('dog_12345', 'https://www.nationalgeographic.com/animals/mammals/facts/domestic-dog') == 400



