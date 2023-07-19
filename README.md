# similarity_search
*Simple similarity search grpc service*
 
To install this project from the repository:

>git clone https://github.com/RGBsrs/similarity_search.git

Install packages:
> pip install grpcio

> pip install grpc-tools

go to directory
> cd similarity_search

run Docker-Compose to start service and it's database.
>docker-compose build

>docker-compose up

Than, after all containers is up.
>cd similarity

Start client without additional parameters to fill db and make tests
>python similarity_search_client.py 

Also similarity_search_client.py can be executed with additional parameters

-a , --add to add new description to database
> python similarity_search_client.py -a test

> python similarity_search_client.py -a 'test string'

-q , --query to create new search and retrieve search id
> python similarity_search_client.py -q test

> python similarity_search_client.py -q 'test string'


-s , --search_id to get results by search id
> python similarity_search_client.py {search_id}





