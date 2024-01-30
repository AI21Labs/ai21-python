from ai21 import AI21Client

file_path = "<file_path>"

client = AI21Client()
client.dataset.create(file_path=file_path, dataset_name="my_new_ds_name")
result = client.dataset.list()
print(result)
first_ds_id = result[0].id
result = client.dataset.get(first_ds_id)
print(result)
