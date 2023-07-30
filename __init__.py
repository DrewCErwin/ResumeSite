import logging
import json
import azure.functions as func
from azure.cosmosdb.table.tableservice import TableService
from azure.data.tables import TableServiceClient
from azure.data.tables import UpdateMode
from azure.cosmosdb.table.models import Entity


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')

    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
#    logging.info(req.get_json()+' was passed to the function')
#    logging.info(req.params+' was passed to the function')

    if name:
#        logging.info(name+' was passed to the function')
        my_entity = {
            "PartitionKey" : "Redirect",
            "RowKey" : name,
        }

        table_service_client = TableServiceClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=resumesitetable;AccountKey=DQbvS4yQr2HWEeL3idjoOXjkkCjEwPT9eUn3ZhFcvOzPfsQ9LKk5OonZbe28CbjFskL5qhVZZ2AyACDbpFrVXw==;TableEndpoint=https://resumesitetable.table.cosmos.azure.com:443/;")
        table_client = table_service_client.get_table_client(table_name="ResumeSiteCounter")

        created = table_client.get_entity(partition_key=my_entity["PartitionKey"], row_key=my_entity["RowKey"])
        if created["Clicks"]:
            new_clicks = int(created["Clicks"])+1
            created["Clicks"] = str(new_clicks)
            table_client.update_entity(mode=UpdateMode.REPLACE, entity=created)
            status_code=400
            return func.HttpResponse(f"{name} has been updated to {new_clicks}.")
        else:
            status_code=300
            return func.HttpResponse(f"{name} was not found on the database")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )