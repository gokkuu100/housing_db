import os
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, House, Agent, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
CORS(app)
migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

class HousesResource(Resource):
    def get(self):
        houses = House.query.all()
        house_list = []
        for house in houses:
            house_data = {
                'id': house.id,
                'title': house.title,
                'description': house.description,
                'price': house.price,
                'bedrooms': house.bedrooms,
                'bathrooms': house.bathrooms,
                'city': house.city,
                'agent_id': house.agent_id,
                'image_paths': house.image_paths,
                'size': house.size,
                "county": house.county
            }
            house_list.append(house_data)
        return jsonify(house_list), 200

    def post(self):
        data = request.get_json()

        title = data.get('title')
        description = data.get('description')
        price = data.get('price')
        bedrooms = data.get('bedrooms')
        bathrooms = data.get('bathrooms')
        city = data.get('city')
        image_paths = data.get('image_paths')
        agent_id = data.get('agent_id')
        size = data.get('size')
        county = data.get('county')

        new_house = House(
            title=title,
            description=description,
            price=price,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            city=city,
            agent_id=agent_id,
            image_paths=image_paths,
            size=size,
            county=county
        )

        db.session.add(new_house)
        db.session.commit()

        house_data = {
            'id': new_house.id,
            'title': new_house.title,
            'description': new_house.description,
            'price': new_house.price,
            'bedrooms': new_house.bedrooms,
            'bathrooms': new_house.bathrooms,
            'city': new_house.city,
            'agent_id': new_house.agent_id,
            'image_paths': new_house.image_paths,
            'size': new_house.size,
            "county": new_house.county
        }

        return jsonify(house_data), 201

api.add_resource(HousesResource, '/houses')

class HouseByIDResource(Resource):
    def get(self, id):
        house = House.query.filter_by(id=id).first()

        if not house:
            return jsonify({"error": "House not found"}), 404

        house_data = {
            'id': house.id,
            'title': house.title,
            'description': house.description,
            'price': house.price,
            'bedrooms': house.bedrooms,
            'bathrooms': house.bathrooms,
            'city': house.city,
            'agent_id': house.agent_id,
            'image_paths': house.image_paths,
            'size': house.size,
            "county": house.county
        }
        return jsonify(house_data), 200

    def patch(self, id):
        house = House.query.filter_by(id=id).first()

        if not house:
            return jsonify({"error": "House not found"}), 404

        data = request.get_json()

        house.title = data.get('title', house.title)
        house.description = data.get('description', house.description)
        house.price = data.get('price', house.price)
        house.bedrooms = data.get('bedrooms', house.bedrooms)
        house.bathrooms = data.get('bathrooms', house.bathrooms)
        house.city = data.get('city', house.city)
        house.agent_id = data.get('agent_id', house.agent_id)
        house.image_paths = data.get('image_paths', house.image_paths)
        house.size = data.get('size', house.size)
        house.county = data.get('county', house.county)

        db.session.commit()
        return jsonify({"message": "House updated successfully"}), 200

    def delete(self, id):
        house = House.query.filter_by(id=id).first()

        if not house:
            return jsonify({"error": "House not found"}), 404

        db.session.delete(house)
        db.session.commit()
        return jsonify({"message": "House deleted successfully"}), 200

api.add_resource(HouseByIDResource, '/houses/<int:id>')

class AgentsResource(Resource):
    def get(self):
        all_agents = Agent.query.all()
        agent_list = []
        for agent in all_agents:
            agent_data = {
                'id': agent.id,
                'name': agent.name,
                'email': agent.email,
                'phonebook': agent.phonebook
            }
            agent_list.append(agent_data)
        return jsonify(agent_list), 200

api.add_resource(AgentsResource, '/agents')

class AgentByIDResource(Resource):
    def get(self, agent_id):
        agent = Agent.query.get(agent_id)

        if agent is None:
            return jsonify({"error": "Agent not found"}), 404

        response_data = {
            'id': agent.id,
            'name': agent.name,
            'email': agent.email,
            'phonebook': agent.phonebook,
        }

        return jsonify(response_data), 200

api.add_resource(AgentByIDResource, '/agents/<int:agent_id>')

class UsersResource(Resource):
    def get(self):
        all_users = User.query.all()
        user_list = []
        for user in all_users:
            user_data = {
                'id': user.id,
                'name': user.name,
                'phonebook': user.phonebook
            }
            user_list.append(user_data)
        return jsonify(user_list), 200

api.add_resource(UsersResource, '/users')

class UserByIDResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)

        if user is None:
            return jsonify({"error": "User not found"}), 404

        response_data = {
            'id': user.id,
            'name': user.name,
            'phonebook': user.phonebook
        }

        return jsonify(response_data), 200

api.add_resource(UserByIDResource, '/users/<int:user_id>')

if __name__ == "__main__":
    app.run(port=5555)
