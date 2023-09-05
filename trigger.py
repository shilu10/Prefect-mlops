import subprocess
import os 

#print(os.environ)
#os.environ["account_id"]

result = subprocess.call('curl --location --request POST "$PREFECT_API_URL/deployments/$DEPLOYMENT_ID/create_flow_run" --header "Content-Type: application/json" --header "Authorization: Bearer $PREFECT_API_KEY" --header "X-PREFECT-API-VERSION: 0.8.4" --data-raw "{}"', shell=True)
print(result)
