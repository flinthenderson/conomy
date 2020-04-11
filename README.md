# conomy
A simple spending tracker app on django with rest api

После деплоймента взаимодействие с сервисом можно производить через браузер либо платформу вроде Postman

**It's Not a Bug, It's a Feature!!!**
1.Некоторые id передаются через slug некоторые через POST. 
Сделато только для демонстрации разнообразности кода.
Легко может быть изменено.
2.В отличии от CRUD для кошельков, транзакции нельзя редактировать как и было запрошено в задании. 
Сделано в целях безопасности в том числе. К тому же, когда удаляется кошелек транзакции остаются, 
возможно в будущих версиях нужно будет добавить перенос транзакций из одного кошелька в другой

**Примеры использоавния**
**Просматривать список своих кошельков**
GET http://127.0.0.1:8000/api/account/listwallets
`{
    "wallets": [
        {
            "id": 3,
            "name": "Groceries",
            "description": "Wallet for everyday stuff",
            "balance": 34990
        },
        {
            "id": 4,
            "name": "Business Wallet",
            "description": "Running business of company",
            "balance": 14787100
        },
        {
            "id": 6,
            "name": "internet spendings",
            "description": "for internet purchases",
            "balance": 0
        },
        {
            "id": 7,
            "name": "A wallet for my dogs food",
            "description": "My dogs wallet",
            "balance": 450
        }
    ]
}`

**Просматривать список своих транзакций в рамках одного кошелька**
GET http://127.0.0.1:8000/api/account/get_wallet_by_id/3
`{
    "wallet": {
        "id": 3,
        "name": "Groceries",
        "description": "Wallet for everyday stuff",
        "balance": 34990
    },
    "transactions": [
        {
            "id": 1,
            "wallet": 3,
            "volume": -60,
            "description": "Bought pepsicola"
        },
        {
            "id": 2,
            "wallet": 3,
            "volume": 35000,
            "description": "Salary"
        },
        {
            "id": 5,
            "wallet": 3,
            "volume": 50,
            "description": "sold my mug"
        }
    ]
}`

**Создать кошелек.**
POST http://127.0.0.1:8000/api/account/addwallet
{
    "wallets": {
        "id": 8,
        "name": "Wishlist",
        "description": "My whims",
        "balance": 0
    }
}

**Редактировать кошелек**
PUT http://127.0.0.1:8000/api/account/updatewallet/8
{
    "wallet": {
        "id": 8,
        "name": "Wishlist",
        "description": "Or just wishes",
        "balance": 0
    }
}

**Удалять кошелек**
DELETE http://127.0.0.1:8000/api/account/deletewallet/6
``

**Просматривать список своих транзакций(общий, всех кошельков сразу)**
GET http://127.0.0.1:8000/api/account/listalltransactions
`{
    "transactions": [
        {
            "id": 1,
            "wallet": 3,
            "volume": -60,
            "description": "Bought pepsicola"
        },
        {
            "id": 2,
            "wallet": 3,
            "volume": 35000,
            "description": "Salary"
        },
        {
            "id": 3,
            "wallet": 4,
            "volume": 15000000,
            "description": "IPO round"
        },
        {
            "id": 4,
            "wallet": 4,
            "volume": -30000,
            "description": "Renting office"
        },
        {
            "id": 5,
            "wallet": 3,
            "volume": 50,
            "description": "sold my mug"
        },
        {
            "id": 7,
            "wallet": 4,
            "volume": -182900,
            "description": "acquire equipment"
        },
        {
            "id": 8,
            "wallet": 7,
            "volume": 450,
            "description": "he found it on a street"
        }
    ]
}`

**Cоздавать транзакции в рамках кошелька**

POST http://127.0.0.1:8000/api/account/addtransactiontowallet
description = Tax cuts
id = 4 (This is id of wallet not transaction)
volume = 250000

`{
    "transaction": {
        "id": 9,
        "wallet": 4,
        "volume": 250000,
        "description": "Tax cuts"
    }
}`

**И удалять транзакции в рамках кошелька**
DELETE http://127.0.0.1:8000/api/account/deletetransaction
id = 7
` `

  
