import mercado_libre_data
import pytest


@pytest.mark.parametrize("uri,expected_result",[

    ("mongodb://root:pass@localhost:27019","MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True, authsource='admin')")
]
)

def test_connection(uri,expected_result):
    uri = "mongodb://root:pass@localhost:27017/?authSource=admin"
    """
    GIVEN a Product model
    WHEN a new Prodcut is added 
    THEN check the product_name, price, and url fields are defined correctly
    """
    assert str(mercado_libre_data.connect_mongo(uri)) == expected_result

