# Important [Notes - Tasks]  Documantation:
## Models:

> 1-You should differ between what is applied to the database[need to make new migration]- and what applay to the admin site only[no need to migrate].

2-When building a generic model, don't make it interact with you main models or apps directly [store_cutom]
3- Foreginkey is translated to Foreginkey_id in the database 

3-1 Ex: Product has a Foreginkey field-> customer, it will be customer_id when dealing with this field in the database level, when ORM try to search for it 

## DBMS:
1-the DBMS we use is mysql
2- DataGrip: workstation to make it easy to interact with mysql
3- Full Picture: DataGrip->mysql->database

## APIs:
1- Is there a difference between RESTful[Representaional State Transfer] APIs and REST Framework?constrains and rules - the real implementation
2- what is the Charastictis for RESTful? Data Representaiona[JSON] - HTTP Methods - use URL to resource locator
3- What is JSON? JavaScript Object Notation?it is how we represent object in java inside curly brackts 
4- in Http methods: what is the difference between PUT and PATCH? Put udate all - Patch update specific fields

## REST Framework:
1- what happens when we decorate django view with api_view from rest Framework? - in the term of requeset object - 
2- What is browsable api page?
3- Is is better to use 404? or use constant?
4- I API model is the same of Data object Model? N
5- API is the interface of our application, the remote control buttons, object model is the inside implement of our application as it can be changed or updated
6- API endpoint [remote buttons] difficult to be changedm but the entire process can be
7- we have 4 ways to serialize a relationship: [primary key - String - Nested Object - Hyperlink]


## Building endpoint:
##serialize-> GET:
Serializers are used to validate the data in Django rest framework.
IMPORTANT: we call the jsno--> pyload,
serializer fields is what we want to recieve with what names, and it is not the same as our model, they are totally different in usage  
Stps to build an API:
- Create the serializer
-Create the as_view
-Register a route
1- Create the serializer with the fields you want to return to the customer
2- Take care of fields that didn't belong to the queryset that you will serializer.
3- if fields did not belong to the queryset, the serializer will search for a defination to it inside the serializer class 
3.1 - this field may be a column from a method or ........
4. what .as_view() do? it tell djago to treat this class as function



## Build with viewsets:
1- get pyload : begin with this
2- post pyload: exclude what you don't want from the fields by setting read only = true


## Routers:
1- Router registration only for viewsets as it have multiple methods inside it, so it need something like handler to handle hte URLs
2- we aer using rest Framework router [simpleRouter - DefaulRouter] to handle it
3 -Nested Router:
3.1 Register the parent router
3.2 




## Design and implement a shoping cart API:
1- What is the operations? <pre> 
[ <b>Methods:</b> , <b>URL: </b> ,<b>Request: </b>: , <b>Response</b>: ]
</pre>

  Cart:
    - Create a cart [method:Post , URL:carts/ , requeset:{} , response:cart object ] 
    - Get a cart   [method:GET , URL:carts/:id , requeset:{} , response:cart object ]
    - Delete a cart [method:Delete , URL:carts/:id , requeset:{} , response:{} ]

  items:
    - Add items to the cart - [method:Post , URL:carts/:id/items , requeset:{product_id, quantity} , response:item ]
    - Update the quantity of items [method:Patch , URL:carts/:id/items/:id , requeset:{quantity} , response:quantity ]
    - Remove items from the cart Delete [method:Delete , URL:carts/:id/items/:id , requeset:{} , response: ]

