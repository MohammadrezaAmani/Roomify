# Roomify

**reservation system via Django for [realtyna](https://realtyna.com/) task**

### Task

As a listing owner, I want a system for making and tracking reservations that can be handled by third-party services.

* The system can be used by multiple listings.
* The system provides REST API endpoints:
-> To make reservations
-> To check if a number of rooms are available at a certain time
* A reservation is for a name (any string) and for a certain amount of time
* The listing owner can get an overview over the booked rooms as an HTML or TEXT report


Limitations:

* Authentication / Authorization is not in the scope of this task
* No localization needed

___
### description

this project contains all of needed apis and endpoints 


### how to use
after installing python and `virtualenv` create a virtual environment using `virtualenv venv` and activate it


```bash
source venv/bin/activate
```

after that just install the requirements via 

```bash
pip install requirements.txt
```

and run django project:

```bash
python3 manage.py runserver
```

### APIs
you can find this list at [postman collection](hhi) and swagger ui

```json
{
    "swagger": "2.0",
    "info": {
        "title": "Reservation API",
        "description": "API endpoints for realtynas task",
        "contact": {
            "email": "more.amani@yahoo.com"
        },
        "version": "v1"
    },
    "host": "127.0.0.1:8000",
    "schemes": [
        "http"
    ],
    "basePath": "/",
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json"
    ],
    "securityDefinitions": {
        "Basic": {
            "type": "basic"
        }
    },
    "security": [
        {
            "Basic": []
        }
    ],
    "paths": {
        "/listings/": {
            "get": {
                "operationId": "listings_list",
                "description": "",
                "parameters": [],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/Listing"
                            }
                        }
                    }
                },
                "tags": [
                    "listings"
                ]
            },
            "post": {
                "operationId": "listings_create",
                "description": "",
                "parameters": [
                    {
                        "name": "data",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/Listing"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/Listing"
                        }
                    }
                },
                "tags": [
                    "listings"
                ]
            },
            "parameters": []
        },
        "/listings/rooms/": {
            "get": {
                "operationId": "listings_rooms_list",
                "description": "",
                "parameters": [],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/Room"
                            }
                        }
                    }
                },
                "tags": [
                    "listings"
                ]
            },
            "post": {
                "operationId": "listings_rooms_create",
                "description": "",
                "parameters": [
                    {
                        "name": "data",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/Room"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/Room"
                        }
                    }
                },
                "tags": [
                    "listings"
                ]
            },
            "parameters": []
        },
        "/listings/rooms/filter/": {
            "get": {
                "operationId": "listings_rooms_filter_list",
                "description": "",
                "parameters": [],
                "responses": {
                    "200": {
                        "description": ""
                    }
                },
                "tags": [
                    "listings"
                ]
            },
            "parameters": []
        },
        "/listings/rooms/{id}/": {
            "get": {
                "operationId": "listings_rooms_read",
                "description": "",
                "parameters": [],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/Room"
                        }
                    }
                },
                "tags": [
                    "listings"
                ]
            },
            "put": {
                "operationId": "listings_rooms_update",
                "description": "",
                "parameters": [
                    {
                        "name": "data",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/Room"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/Room"
                        }
                    }
                },
                "tags": [
                    "listings"
                ]
            },
            "patch": {
                "operationId": "listings_rooms_partial_update",
                "description": "",
                "parameters": [
                    {
                        "name": "data",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/Room"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/Room"
                        }
                    }
                },
                "tags": [
                    "listings"
                ]
            },
            "delete": {
                "operationId": "listings_rooms_delete",
                "description": "",
                "parameters": [],
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "listings"
                ]
            },
            "parameters": [
                {
                    "name": "id",
                    "in": "path",
                    "description": "A unique integer value identifying this room.",
                    "required": true,
                    "type": "integer"
                }
            ]
        },
        "/listings/{id}/": {
            "get": {
                "operationId": "listings_read",
                "description": "",
                "parameters": [],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/Listing"
                        }
                    }
                },
                "tags": [
                    "listings"
                ]
            },
            "put": {
                "operationId": "listings_update",
                "description": "",
                "parameters": [
                    {
                        "name": "data",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/Listing"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/Listing"
                        }
                    }
                },
                "tags": [
                    "listings"
                ]
            },
            "patch": {
                "operationId": "listings_partial_update",
                "description": "",
                "parameters": [
                    {
                        "name": "data",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/Listing"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/Listing"
                        }
                    }
                },
                "tags": [
                    "listings"
                ]
            },
            "delete": {
                "operationId": "listings_delete",
                "description": "",
                "parameters": [],
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "listings"
                ]
            },
            "parameters": [
                {
                    "name": "id",
                    "in": "path",
                    "description": "A unique integer value identifying this listing.",
                    "required": true,
                    "type": "integer"
                }
            ]
        },
        "/reports/listings/{listing_id}/report/": {
            "get": {
                "operationId": "reports_listings_report_list",
                "description": "",
                "parameters": [
                    {
                        "name": "search",
                        "in": "query",
                        "description": "A search term.",
                        "required": false,
                        "type": "string"
                    }
                ],
                "responses": {
                    "200": {
                        "description": ""
                    }
                },
                "tags": [
                    "reports"
                ]
            },
            "parameters": [
                {
                    "name": "listing_id",
                    "in": "path",
                    "required": true,
                    "type": "string"
                }
            ]
        },
        "/reservations/": {
            "get": {
                "operationId": "reservations_list",
                "description": "",
                "parameters": [],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/Reservation"
                            }
                        }
                    }
                },
                "tags": [
                    "reservations"
                ]
            },
            "post": {
                "operationId": "reservations_create",
                "description": "",
                "parameters": [
                    {
                        "name": "data",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/Reservation"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/Reservation"
                        }
                    }
                },
                "tags": [
                    "reservations"
                ]
            },
            "parameters": []
        },
        "/reservations/filter/": {
            "get": {
                "operationId": "reservations_filter_list",
                "description": "",
                "parameters": [],
                "responses": {
                    "200": {
                        "description": ""
                    }
                },
                "tags": [
                    "reservations"
                ]
            },
            "parameters": []
        },
        "/reservations/{id}/": {
            "get": {
                "operationId": "reservations_read",
                "description": "",
                "parameters": [],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/Reservation"
                        }
                    }
                },
                "tags": [
                    "reservations"
                ]
            },
            "put": {
                "operationId": "reservations_update",
                "description": "",
                "parameters": [
                    {
                        "name": "data",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/Reservation"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/Reservation"
                        }
                    }
                },
                "tags": [
                    "reservations"
                ]
            },
            "patch": {
                "operationId": "reservations_partial_update",
                "description": "",
                "parameters": [
                    {
                        "name": "data",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/Reservation"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/Reservation"
                        }
                    }
                },
                "tags": [
                    "reservations"
                ]
            },
            "delete": {
                "operationId": "reservations_delete",
                "description": "",
                "parameters": [],
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "reservations"
                ]
            },
            "parameters": [
                {
                    "name": "id",
                    "in": "path",
                    "description": "A unique integer value identifying this reservation.",
                    "required": true,
                    "type": "integer"
                }
            ]
        }
    },
    "definitions": {
        "Listing": {
            "required": [
                "name",
                "owner"
            ],
            "type": "object",
            "properties": {
                "id": {
                    "title": "Id",
                    "type": "integer",
                    "readOnly": true
                },
                "name": {
                    "title": "Name",
                    "type": "string",
                    "maxLength": 100,
                    "minLength": 1
                },
                "slug": {
                    "title": "Slug",
                    "type": "string",
                    "maxLength": 100,
                    "minLength": 1
                },
                "address": {
                    "title": "Address",
                    "type": "string",
                    "maxLength": 255,
                    "x-nullable": true
                },
                "description": {
                    "title": "Description",
                    "type": "string",
                    "x-nullable": true
                },
                "owner": {
                    "title": "Owner",
                    "type": "string",
                    "maxLength": 100,
                    "minLength": 1
                }
            }
        },
        "Room": {
            "required": [
                "listing"
            ],
            "type": "object",
            "properties": {
                "id": {
                    "title": "Id",
                    "type": "integer",
                    "readOnly": true
                },
                "listing": {
                    "title": "Listing",
                    "type": "integer"
                },
                "name": {
                    "title": "Name",
                    "type": "string",
                    "maxLength": 100,
                    "minLength": 1
                },
                "slug": {
                    "title": "Slug",
                    "type": "string",
                    "maxLength": 100,
                    "x-nullable": true
                },
                "description": {
                    "title": "Description",
                    "type": "string",
                    "x-nullable": true
                },
                "price": {
                    "title": "Price",
                    "type": "integer"
                }
            }
        },
        "Reservation": {
            "required": [
                "room",
                "start_date",
                "end_date",
                "guest_name",
                "guest_email",
                "guest_phone"
            ],
            "type": "object",
            "properties": {
                "id": {
                    "title": "Id",
                    "type": "integer",
                    "readOnly": true
                },
                "room": {
                    "title": "Room",
                    "type": "integer"
                },
                "start_date": {
                    "title": "Start date",
                    "type": "string",
                    "format": "date"
                },
                "end_date": {
                    "title": "End date",
                    "type": "string",
                    "format": "date"
                },
                "guest_name": {
                    "title": "Guest name",
                    "type": "string",
                    "maxLength": 100,
                    "minLength": 1
                },
                "guest_email": {
                    "title": "Guest email",
                    "type": "string",
                    "maxLength": 100,
                    "minLength": 1
                },
                "guest_phone": {
                    "title": "Guest phone",
                    "type": "string",
                    "maxLength": 100,
                    "minLength": 1
                }
            }
        }
    }
}
```
