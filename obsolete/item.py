### Udemy Section 5
# class Item(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument('price',
        # type=float,
        # required=True,
        # help="Field is either blank or unrecognised."
    # )

    # @classmethod
    # def insert(cls, item):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "INSERT INTO items VALUES (?, ?)"
        # cursor.execute(query, (item['name'], item['price']))

        # connection.commit()
        # connection.close()

    # @classmethod
    # def update(cls, item):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "UPDATE items SET price=? WHERE name=?"
        # cursor.execute(query, (item['price'], item['name']))

        # connection.commit()
        # connection.close()

    # @classmethod
    # def find_by_name(cls, name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM items WHERE name=?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()

        # if row:
            # return {'item': {'name': row[0], 'price': row[1]}}

    # @jwt_required()
    # def get(self, name):
        # try:
            # item = self.find_by_name(name)
        # except:
            # return {"message": "An error occurred while reading the item from the database."}, 500

        # if item:
            # return item, 200
        # return {'message': 'Item not found.'}, 404

    # def post(self, name):
        # try:
            # if self.find_by_name(name): # we can't do "if self.get(name)" because the 'get' method required a JWT token, so the code to find the item had been moved to 'find_by_name'
                # return {'message': "An item with name '{}' already exists.".format(name)}, 400
        # except:
            # return {"message": "An error occurred while reading the item from the database."}, 500

        # request_data = Item.parser.parse_args()

        # item = {'name': name, 'price': request_data['price']}

        # try:
            # self.insert(item)
        # except:
            # return {"message": "An error occurred while inserting the item to the database."}, 500
        # return item, 201

    # def delete(self, name):
        # try:
            # connection = sqlite3.connect('data.db')
            # cursor = connection.cursor()

            # query = "DELETE FROM items WHERE name=?"
            # cursor.execute(query, (name,))

            # connection.commit()
            # connection.close()
        # except:
            # return {"message": "An error occurred while deleting the item from the database."}, 500
        # return {'message': 'Item deleted.'}, 200

    # def put(self, name):
        # request_data = Item.parser.parse_args()

        # try:
            # item = self.find_by_name(name)
        # except:
            # return {"message": "An error occurred while reading the item from the database."}, 500
        # updated_item = {'name': name, 'price': request_data['price']}

        # if item is None:
            # try:
                # self.insert(updated_item)
            # except:
                # return {"message": "An error occurred while inserting the item to the database."}, 500
        # else:
            # try:
                # self.update(updated_item)
            # except:
                # return {"message": "An error occurred while updating the item in the database."}, 500
        # return updated_item, 200

# class Items(Resource):
    # def get(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM items"
        # result = cursor.execute(query)

        # items = []
        # for row in result:
            # items.append({'name': row[0], 'price': row[1]})

        # connection.close()

        # return {'items': items}
