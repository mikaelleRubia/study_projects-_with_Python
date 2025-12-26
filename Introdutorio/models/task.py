
class Task:
    def __init__(self, id, title, description, completed=False)-> None:
        self.id = id
        self.title = title 
        self.description = description
        self.completed = completed
    
    def to_dict(self):
        return {
        "id": self.id,
        "title": self.title,
        "description": self.description,
        "completed": self.completed
        }
        


# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), nullable=False, unique=True)
#     password = db.Column(db.String(80), nullable=False)
#     cart = db.relationship('CartItem', backref='user', lazy=True)


# class  Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     description = db.Column(db.Text)

# class CartItem(db.Model):
#     __tablename__ = 'cart_item'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'),nullable=False)









# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


# @app.route('/logout', methods=["POST"])
# @login_required
# def logout():
#     logout_user()
#     return jsonify({"message":"logout com sucesso!"}),201

# @app.route('/login', methods=["POST"])
# def login():
#     data = request.json

#     user = User.query.filter_by(username=data.get("username")).first()

#     if user:
#          if data["password"] == user.password:
#             return jsonify({"message":"usuario logado com sucesso!"}),201
         
#     return jsonify({"message":"Credenciais invalidas!"}),401
             


# @app.route('/api/products/add', methods=["POST"])
# @login_required
# def add_product():
#     data = request.json
#     if 'name' in data and 'price' in data:
#         product = Product(name= data["name"], price= data["price"], description= data.get("description ", ""))
#         db.session.add(product)
#         db.session.commit()

#         return jsonify({"message":"Produto cadastrado com sucesso"}),201


# @app.route('/api/products/delete/<int:product_id>', methods=["DELETE"])
# @login_required
# def delete_product(product_id):

#     product = Product.query.get(product_id)
#     if product:
#         db.session.delete(product)
#         db.session.commit()

#         return jsonify({"message":"Produto deletado com sucesso"}),200
#     else:
#         return jsonify({"message":"Produto não encontrado"}),404
    

# @app.route('/api/products/<int:product_id>', methods=["GET"])
# def get_product_detail(product_id):

#     product = Product.query.get(product_id)
#     if product:
#         return jsonify({
#             "id": product.id,
#             "name": product.name,
#             "price": product.price,
#             "description": product.description,
#         })
#     else:
#         return jsonify({"message":"Produto não encontrado"}),404
    

# @app.route('/api/products/update/<int:product_id>', methods=["PUT"])
# @login_required
# def update_product(product_id):
#     data = request.json
#     product = Product.query.get(product_id)
#     if not product:
#         return jsonify({"message":"Produto não encontrado"}),404

#     product.name = data["name"] if 'name' in data else product.name
#     product.price = data["price"] if 'price' in data else product.price
#     product.description = data["description"] if 'description' in data else product.description

#     db.session.commit()
#     return jsonify({"message":"Produto atualizado com sucesso!"})
    

# @app.route('/api/products', methods=["GET"])
# def get_products():

#     products = Product.query.all()
#     if products:
#         prods =[]
#         for product in products:
#             prod_data = {
#                 "id": product.id,
#                 "name": product.name,
#                 "price": product.price,
#                 "description": product.description,
#             }
#             prods.append(prod_data)
#         return jsonify({"Produtos": prods})
#     else:
#         return jsonify({"message":"Produto não encontrado"}),404

# # checkout
# @app.route('/api/cart/add/<int:product_id>', methods=["POST"])
# @login_required
# def add_to_cart(product_id):
#     product = Product.query.get(product_id)

#     if product:
#         cart_item = CartItem(user_id=current_user.id, product_id=product_id)
#         db.session.add(cart_item)
#         db.session.commit()
#         return jsonify({"message": "Item adicionado com sucesso!"}), 200

#     return jsonify({"message": "Item não encontrado"}), 400
