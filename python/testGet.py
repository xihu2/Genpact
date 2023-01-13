#!/usr/bin/python3
import requests

"""
Get pet by id
"""


def getPetById(pet_id):
    url = 'https://petstore.swagger.io/v2/pet/' + pet_id
    headers = {'accept': 'application/json', }
    r = requests.get(url, headers=headers)

    return r.status_code


"""
Get pet by id return all the expected records
"""


def validateGetPetById(pet_id):
    url = 'https://petstore.swagger.io/v2/pet/' + pet_id
    headers = {'accept': 'application/json', }
    r = requests.get(url, headers=headers)

    if (r.status_code == 200):
        data = r.json()
        total = len(data)

        for i in range(total):
            if pet_id not in data[i]['id']:
                return False

        return True

    else:
        return "Get API failed!"


"""
Get pets by status
"""


def getPetByStatus(status):
    url = 'https://petstore.swagger.io/v2/pet/findByStatus'
    headers = {'accept': 'application/json', }
    params = (('status', status),)
    r = requests.get(url, headers=headers, params=params)

    return r.status_code


"""
Get pet by status return all the expected records
"""


def validateGetPetByStatus(status):
    url = 'https://petstore.swagger.io/v2/pet/findByStatus'
    headers = {'accept': 'application/json', }
    params = (('status', status),)
    r = requests.get(url, headers=headers, params=params)

    if (r.status_code == 200):
        data = r.json()
        total = len(data)

        for i in range(total):
            if status not in data[i]['status']:
                return False

        return True

    else:
        return "Get API failed!"


"""
Get pet with status without parameter
"""


def getPetByStatusWithoutParam():
    url = 'https://petstore.swagger.io/v2/pet/findByStatus'
    headers = {'accept': 'application/json', }

    r = requests.get(url, headers=headers)

    return r.status_code


"""
Test curl -X GET 
  'https://petstore.swagger.io/v2/pet/{petId}' 
  'https://petstore.swagger.io/v2/pet/findByStatus?status={status}'
"""


# Get pet by petId
# Currently Get pet by Id API is not working correctly. Get pet by Id is not returning the existing pet
def testvalidateGetPetById():
    assert getPetById('9223372036854626000') == 200
    assert validateGetPetById('9223372036854626000')
    assert validateGetPetById('12222')


# Get pet by petId negative test
def testvalidateGetPetByIdNegative():
    assert getPetById('') == 405
    assert getPetById('a') == 404


# Get pet with status return all the expected records
def testvalidateGetPetByStatus():
    assert getPetByStatus("available") == 200
    assert validateGetPetByStatus('available')
    assert validateGetPetByStatus('pending')
    assert validateGetPetByStatus('sold')


# Get pet with status negative test
# Currently following error checks are not working for Get pet by status API
def testvalidateGetPetByStatusNegative():
    assert getPetByStatusWithoutParam() == 400
    assert getPetByStatus("bad") == 400






