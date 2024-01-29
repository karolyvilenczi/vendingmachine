from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder

from app import ep_app
from busapp.epserver.ep_routes.r_products import crud_service_product
from busapp.services.models.product import Product, ProductWoID

import pytest

client = TestClient(ep_app)

# @pytest.fixture
# def test_user_w_id():
#     return User(id=1, name="Buyer1", role="buyer")


# @pytest.mark.order(1)
# def test_create_user(test_user_w_id):
#     response = client.post("/users/", json=jsonable_encoder(test_user_w_id))
       
#     resp_dict = response.json()
#     test_dict = test_user_w_id.model_dump()
    
    
#     # 1st we test if we get a 200 resp from the E/P and if the resp is valid
#     assert response.status_code == 200
#     assert resp_dict == test_dict, "OK"       
#     # 2nd if it was saved in the 'DB', but db contains User objects, the resp_dict has to be converted to one 1st
#     assert test_dict in crud_service_user.get_database_in_dict()

# @pytest.mark.order(2)
# def test_read_user(test_user_w_id):
#     response = client.get(f"/users/{test_user_w_id.id}")
    
#     assert response.status_code == 200
#     assert response.json() == test_user_w_id.model_dump()

# @pytest.mark.order(3)
# def test_get_all_users():       
#     response = client.get("/users/")

#     assert response.status_code == 200
#     assert response.json() == crud_service_user.get_database_in_dict()

# @pytest.mark.order(4)
# def test_update_user(test_user_w_id):
#     # the original test user at id 1 is a buyer
#     update_data = {"name": "UpdatedUser", "role": "seller"}

#     response = client.put(f"/users/{test_user_w_id.id}", json=update_data)
#     # add the new id to the test dict
#     update_data["id"] = test_user_w_id.id
    
#     assert response.status_code == 200
    
#     updated_user = response.json()
#     assert updated_user["name"] == update_data["name"]
#     assert updated_user["role"] == update_data["role"]
#     assert updated_user in crud_service_user.get_database_in_dict()

# @pytest.mark.order(5)
# def test_delete_user(test_user_w_id):
#     response = client.delete(f"/users/{test_user_w_id.id}")
#     expected_data = {"name": "UpdatedUser", "role": "seller", "id": test_user_w_id.id}
#     assert response.status_code == 200
    
#     assert response.json() == expected_data
#     assert test_user_w_id not in crud_service_user.get_database_in_dict()