import json
import uuid
from datetime import datetime
from typing import Optional, TypedDict, Any, Dict
from decimal import Decimal

import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("AWS-PROD-POC-DynamoTable")


class CreateProductRequest(TypedDict):
    name: str
    price: float
    category: Optional[str]
    stock: Optional[int]


class ProductItem(CreateProductRequest):
    id: str
    created_at: str
    type: str

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super().default(o)

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    try:
        body = json.loads(event.get("body", "{}"))

        product: ProductItem = {
            "id": str(uuid.uuid4()),
            "name": body["name"],
            "price": Decimal(str(body["price"])),
            "category": body.get("category", "General"),
            "stock": int(body.get("stock", 0)),
            "created_at": datetime.utcnow().isoformat(),
            "type": "product"
        }

        table.put_item(Item=product)

        return {
            "statusCode": 200,
            "body": json.dumps(
                {"message": "Product created successfully", "product": product},
                cls=DecimalEncoder
            )
        }

    except KeyError as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": f"Missing required field: {str(e)}"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
