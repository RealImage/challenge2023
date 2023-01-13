# Qube Cinemas Challenge 2023

Watching movies on a big screen is entertaining and provides a great experience for many of us. You are going to solve the problem to dynamically determine the ticket price for each cinema hall, based on the given criteria.

The theatre owners usually operate centrally to manage their shows and its ticket price.

They specify the ticket price of each seat in shows using price cards in the following manner (The price is in paise):

price_cards.json:

``` json
"price_cards": [
    {
        "id": "P1",
        "valid_from": "2023-01-03",
        "valid_to": "2023-03-31",
        "active": true,
        "ticket_price": 2000,
        "screens": ["S1", "S2"],
        "movies": ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10"]
    },
    {
        "id": "P2",
        "valid_from": "2023-01-03",
        "valid_to": "2023-02-28",
        "active": true,
        "ticket_price": 1800,
        "screens": ["S1", "S2", "S3"],
        "movies": ["M4", "M5"]
    },
    {
        "id": "P3",
        "valid_from": "2023-01-03",
        "valid_to": "2024-01-03",
        "active": false,
        "ticket_price": 500,
        "screens": ["S1"],
        "movies": ["M1", "M2", "M3"]
    },
    {
        "id": "P4",
        "valid_from": "2023-01-03",
        "valid_to": "2024-01-03",
        "active": false,
        "ticket_price": 2000,
        "screens": ["S3"],
        "movies": ["M11"]
    },
    {
        "id": "P5",
        "valid_from": "2023-01-03",
        "valid_to": "2023-01-31",
        "active": true,
        "ticket_price": 1500,
        "screens": ["S2"],
        "movies": ["M11"]
    }
]
```

**Explanation:**
Each price cards carry an id, validity, active status, ticket price, screens, and movies. You are going to use this price_cards.json to choose the best ticket price to create shows at the cinema hall. You will consider all these attributes to pick a ticket price for shows based on the below-given problem statements.

*NOTE*:

- Write programs in any language you want. Feel free to hold the datasets in whatever data structure you want, but try not to use external databases - as far as possible stick to your langauage without bringing in MySQL/Postgres/MongoDB/Redis/SQLite Etc.
- The data in the Readme is just an example. We've provided a json `price_cards.json` with the list of all pricecards with id, validity, active status, ticket price, screens and movies. Your logic should work for any price_card and show.
- This challenge consist of three problems. Aim to solve atleast Problem Statement 1 and 2.

## Problem Statement 1

- Given a list of shows, each show consists of show id, and screen, find the price card for each show.
- Multiple price cards can be assigned to a screen.
- While assigning a price card to a show, you may get multiple price cards.
- Find the price card for each show for a given screen where ticket price is minimum and active.
- Use the price_cards data given in `price_cards.json`. Add various price cards in `price_cards.json` to test your logic.

**Input**: A json `input.json`. Each show containing show id and screen.

**Expected Output**: A json `output.json`. Each show containing show id, screen, and selected price card.

#### Sample Scenarios (Based on above example price_cards.json)

**INPUT**:

``` json
"shows": [
    {
        "id": "SH1",
        "screen": "S1"
    },
    {
        "id": "SH2",
        "screen": "S2"
    },
    {
        "id": "SH3",
        "screen": "S3"
    },
    {
        "id": "SH4",
        "screen": "S5"
    }
]
```

**SHOW OUTPUT**:

``` json
"shows": [
    {
        "id": "SH1",
        "screen": "S1",
        "price_card": "P2"
    },
    {
        "id": "SH2",
        "screen": "S2",
        "price_card": "P5"
    },
    {
        "id": "SH3",
        "screen": "S3",
        "price_card": "P2"
    },
    {
        "id": "SH4",
        "screen": "S5",
        "price_card": ""
    }
]

```

## Problem Statement 2

Each price card specifies the **validity** they can apply to a show based on the show time in the following manner:
  
- We have provided validity details in `price_cards.json`. It has valid_from and valid_to for each price_card.
- Given a list of shows, each show consists of show id, screen, and show_time, find the price card for each show.
- While assigning a price card to a show, you may get multiple price cards.
- Find the price card for each show for a given screen where show_time meets the validity, minimum ticket price, and active.
- Use the price_cards data given in `price_cards.json`. Add various price cards in `price_cards.json` to test your logic.

**Input**: A json `input.json`. Each show containing show id, screen and show_time.

**Expected Output**: A json `output.json`. Each show containing show id, screen, show_time and selected price card.

#### Sample Scenario (Based on above examples)

**INPUT**:

``` json
"shows": [
    {
        "id": "SH1",
        "screen": "S1",
        "show_time": "2023-03-01T09:00:00Z"
    },
    {
        "id": "SH2",
        "screen": "S2",
        "show_time": "2023-02-10T09:00:00Z"
    },
    {
        "id": "SH3",
        "screen": "S3",
        "show_time": "2023-03-01T09:00:00Z"
    },
    {
        "id": "SH4",
        "screen": "S5",
        "show_time": "2023-03-01T09:00:00Z"
    }
]
```

**OUTPUT**:

``` json
"shows": [
    {
        "id": "SH1",
        "screen": "S1",
        "show_time": "2023-03-01T09:00:00Z",
        "price_card": "P1"
    },
    {
        "id": "SH2",
        "screen": "S2",
        "show_time": "2023-02-10T09:00:00Z",
        "price_card": "P5"
    },
    {
        "id": "SH3",
        "screen": "S3",
        "show_time": "2023-03-01T09:00:00Z",
        "price_card": ""
    },
    {
        "id": "SH4",
        "screen": "S5",
        "show_time": "2023-03-01T09:00:00Z",
        "price_card": ""
    }
]
```

## Problem Statement 3

Each price card specifies the **movies** they can apply to a show based on the movie selected for that show in the following manner:
  
- We have provided movie details in `price_cards.json` for each price_card.
- Given a list of shows, each show consists of show id, screen, show_time and movie, find the price card for each show.
- While assigning a price card to a show, you may get multiple price cards.
- Find the price card for each show for a given screen and movie where show_time meets the validity, minimum ticket price, and active.
- Use the price_cards data given in `price_cards.json`. Add various price cards in `price_cards.json` to test your logic.


**Input**: A json `input.json`. Each show containing show id, screen, show_time and movie.

**Expected Output**: A json `output.json`. Each show containing show id, screen, show_time, movie and selected price card.

**INPUT**:

``` json
"shows": [
    {
        "id": "SH1",
        "screen": "S1",
        "show_time": "2023-03-01T09:00:00Z",
        "movie": "M1"
    },
    {
        "id": "SH2",
        "screen": "S2",
        "show_time": "2023-02-10T09:00:00Z",
        "movie": "M2"
    },
    {
        "id": "SH2",
        "screen": "S3",
        "show_time": "2023-03-01T09:00:00Z",
        "movie": "M1"
    },
    {
        "id": "SH2",
        "screen": "S5",
        "show_time": "2023-03-01T09:00:00Z",
        "movie": "M1"
    }
]
```

**OUTPUT**:

``` json
"shows": [
    {
        "id": "SH1",
        "screen": "S1",
        "show_time": "2023-03-01T09:00:00Z",
        "movie": "M1",
        "price_card": "P1"
    },
    {
        "id": "SH2",
        "screen": "S2",
        "show_time": "2023-02-10T09:00:00Z",
        "movie": "M2",
        "price_card": "P1"
    },
    {
        "id": "SH3",
        "screen": "S2",
        "show_time": "2023-02-10T09:00:00Z",
        "movie": "M4",
        "price_card": "P2"
    },
    {
        "id": "SH4",
        "screen": "S5",
        "show_time": "2023-03-01T09:00:00Z",
        "movie": "M1",
        "price_card": ""
    }
]
```

**Note:**
To submit a solution, fork this repo and send a Pull Request on Github.
For any questions or clarifications, raise an issue on this repo and we'll answer your questions as fast as we can.
