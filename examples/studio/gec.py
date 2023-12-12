from ai21 import AI21Client

client = AI21Client()
response = client.gec.create(text="jazzz is a great stile of music")

print("---------------------")
print(response.corrections[0].suggestion)
print(response.corrections[0].start_index)
print(response.corrections[0].end_index)
print(response.corrections[0].original_text)
print(response.corrections[0].correction_type)
