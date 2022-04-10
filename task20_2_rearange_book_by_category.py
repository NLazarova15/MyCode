import json

def rearange_books_by_category(books_json):
	"""rearange_books_by_category.
		Returns JSON with following structure:
			{
				"Beginner":[
					{
						"title":
						"author":
						"url"
					}
				],
				"Intermediate":[
					{
						"title":
						"author":
						"url"
					}
				],
			}
	"""
	
	rearanged_books = {}

	for book in books_json['books']:
		category = book['level']
		book_data = {
			"title": book['title'],
			"author":book['author'],
			"url":book['url']
		}

		if category in rearanged_books.keys():
			rearanged_books[category].append(book_data)
		else:
			rearanged_books[category] = [book_data]

	return rearanged_books


def main():
	json_file = "pythonbooks.revolunet.com.issues.json"
	
	#read json data from file
	with open(json_file) as f:
			json_data = json.load(f)

	rearanged_books = rearange_books_by_category(json_data)

	# print json data:
	print(json.dumps(rearanged_books,indent=4,sort_keys=True))

	# create a new, filtered JSON-file rearanged_books_by_category.json:
	output_file='rearanged_books_by_category.json'
	
	with open(output_file, mode='w') as file:
		json.dump(rearanged_books, file)   

		
main()