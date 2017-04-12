# SmartH4314

## Deploy the architecture
If it's the first time, just run ./CreateServers.sh
It removes existing servers with the same name and it runs and starts all servers.

You can stop all the server with ./StopServers.sh.
And starts all with ./StartServers.sh

### Configure postGres Client pgadmin
- You can browse on http://127.0.0.1:5050 to go to the pgadmin UI.

- Then add a postgre server with "add New server".

- Add the IP@ of the postgres client and validate.

- Add fuzzystrsearch extension by right click>Create on "extension" item of the menu.

## Engine REST Api Reference
Engine responds to the following endpoint (using POST or GET) :

IP:5000/engine

### request :
{ 
"tokens" :
	[
		{"facebook" : <valeur>},
		{"twitter" : <valeur>}
	]
} 

### responds
{
	"status" : <err_code>,
	"recommandations" :
		[
			{TO DEFINE}
		]
}
