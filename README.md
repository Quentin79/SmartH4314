# SmartH4314

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
