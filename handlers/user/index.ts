import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, PutCommand } from "@aws-sdk/lib-dynamodb";
import { APIGatewayProxyEvent, APIGatewayProxyResult } from "aws-lambda";
import { v4 } from "uuid";

const client = new DynamoDBClient();
const docClient = DynamoDBDocumentClient.from(client);

type CreateUserRequest = {
    name: string;
    email: string;
    age?: number;
    location?: string;
}

type UserItem = CreateUserRequest & {
    id: string;
    created_at: string;
    type: string;
}

export const handler = async (event: APIGatewayProxyEvent): Promise<APIGatewayProxyResult> => {
    if (!event.body) {
        return {
        statusCode: 400,
        body: JSON.stringify({ message: "Missing request body" }),
        };
    }

    const body = JSON.parse(event.body);
    if (!body.name || !body.email) {
        return {
            statusCode: 400,
            body: JSON.stringify({ message: "Missing required fields" }),
        };
    }

    const requestBody: CreateUserRequest = {
        name: body.name,
        email: body.email,
        age: body.age,
        location: body.location,
    };

    const user: UserItem = {
        id: v4(),
        ...requestBody,
        type: "user",
        created_at: new Date().toISOString(),
    };

    const tableName = "AWS-PROD-POC-DynamoTable";

    const command = new PutCommand({
        TableName: tableName,
        Item: user
    });

    const res = await docClient.send(command);

    return { statusCode: 200, body: JSON.stringify({ message: res }) };
}