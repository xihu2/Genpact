#!/usr/bin/python3
import pytest
import requests

"""
Add new pet to the store
"""


def postPet(pet_name, photoUrls):
    url = 'https://petstore.swagger.io/v2/pet'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json', }
    payload = '{"name": "' + pet_name + '", "photoUrls": ["' + photoUrls + '"]}'
    r = requests.post(url, headers=headers, data=payload)

    return r


"""
Post new pet with required payload, Get API return the new posted pet
"""


def validatePostPet(pet_name, photoUrls):
    r = postPet(pet_name, photoUrls)
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
Post pet without name in payload
"""


def postPetWithoutName(photoUrls):
    url = 'https://petstore.swagger.io/v2/pet'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json', }
    payload = '{"photoUrls": ["' + photoUrls + '"]}'
    r = requests.post(url, headers=headers, data=payload)

    return r.status_code


"""
Post pet without photoUrls in payload
"""


def postPetWithoutPhotoUrls(pet_name):
    url = 'https://petstore.swagger.io/v2/pet'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json', }
    payload = '{"name": "' + pet_name + '"}'
    r = requests.post(url, headers=headers, data=payload)

    return r.status_code


"""
Post pet without payload
"""


def postPetWithoutPayload():
    url = 'https://petstore.swagger.io/v2/pet'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json', }
    r = requests.post(url, headers=headers)

    return r.status_code


"""
Post pet without Header
"""


def postPetWithoutHeader(pet_name, photoUrls):
    url = 'https://petstore.swagger.io/v2/pet'
    payload = '{"name": "' + pet_name + '", "photoUrls": ["' + photoUrls + '"]}'
    r = requests.post(url, data=payload)

    return r.status_code


"""
Post pet with not existing payload
"""


def postPetWithWrongKey(pet_name, photoUrls):
    url = 'https://petstore.swagger.io/v2/pet'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json', }
    payload = '{"pet_Name": "' + pet_name + '", "photoUrls": ["' + photoUrls + '"]}'
    r = requests.post(url, headers=headers, data=payload)

    return r.status_code


"""
Upload pet image
"""


def postPetImage(petId):
    url = 'https://petstore.swagger.io/v2/pet/' + petId + '/uploadImage'
    headers = {'accept': 'application/json', }
    f = open('test-image.jpg', 'rb')
    file = {'file': f, 'Content-Type': 'image/jpeg'}
    r = requests.post(url, headers=headers, files=file)

    return r.status_code


"""
Test curl -d '{"name":"dog1", "photoUrls": ["https://www.test.com"]}' 
	-H "accept: application/json, Content-Type: application/json" -X POST https://petstore.swagger.io/v2/pet
"""


# Post pet with name & photoUrls
# currently the Post pet API doesn't have error check for required name and photoUrls fields
@pytest.mark.parametrize("pet_name, photoUrls, expected",
                         [("dog_1234", "https://www.nationalgeographic.com/animals/mammals/facts/domestic-dog", 200),
                          ("", "http://www.dogphoto.com", 400), ("dog_name", "", 400), ("", "", 400)])
def testPostPet(pet_name, photoUrls, expected):
    assert postPet(pet_name, photoUrls).status_code == expected


# Post pet with required payload, Get API return the posted pet
# currently Get pet API is not working correctly which cause this test case failed
def testvalidatePostPet():
    assert validatePostPet("dog_12345", "https://www.nationalgeographic.com/animals/mammals/facts/domestic-dog") == True


# Post pet without photoUrls in payload
# currently Post pet API doesn't have error check for required photoUrls field
def testpostPetWithoutPhotoUrls():
    assert postPetWithoutPhotoUrls('dog_12345') == 400


# Post pet without name in payload
# currently Post pet API doesn't have error check for required name field
def testpostPetWithoutName():
    assert postPetWithoutName('https://www.nationalgeographic.com/animals/mammals/facts/domestic-dog') == 400


# Post pet without Header
def testpostPetWithoutHeader():
    assert postPetWithoutHeader('dog_12345', 'https://www.nationalgeographic.com/animals/mammals/facts/domestic-dog') == 415


# Post pet without payload
def testpostPetWithoutPayload():
    assert postPetWithoutPayload() == 405


# Post pet with not existing payload
# currently Post pet API doesn't have error check for wrong input parameter
def testpostPetWithWrongKey():
    assert postPetWithWrongKey('dog_12345', 'https://www.nationalgeographic.com/animals/mammals/facts/domestic-dog') == 400


# Post pet image
def testpostPetImage():
    assert postPetImage('9223372036854626000') == 200
    assert postPetImage('') == 404