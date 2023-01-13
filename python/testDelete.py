#!/usr/bin/python3
import requests
import testGet
import testPut

"""
Delete pet by id
"""


def deletePetById(pet_id):
    url = 'https://petstore.swagger.io/v2/pet/' + pet_id
    headers = {'accept': 'application/json', }
    r = requests.delete(url, headers=headers)

    return r.status_code


"""
Delete pet by id validation
"""


def validateDeletePetById():

    r = testPut.putPet("dog_test_delete", "www.testDelete.com")

    if (r.status_code == 200):
        r1 = testGet.getPetById(str(r.json()['id']))

        if (r1 == 200):
            r2 = deletePetById(str(r.json()['id']))
            if (r2 == 200):
                r3 = testGet.getPetById(str(r.json()['id']))
                if (r3 == 404):
                    return True
                else:
                    return "Get API failed after delete the new pet!"
            else:
                return "Delete API failed!"

        else:
            return "Get API failed after add the new pet!"

    else:
        return "Put API failed to add the new pet"


"""
Test curl -X DELETE 
  'https://petstore.swagger.io/v2/pet/{petId}' 
"""


# Delete pet by petId
def testvalidateDeletePetById():
    assert validateDeletePetById() == True


# Delete pet by Id negative test
def testvalidateDeletePetByIdNegative():
    assert deletePetById('') == 405
    assert deletePetById('0') == 404
    assert deletePetById('not_exist') == 404








