# from random import randint
# from faker import Faker
# from app import app, db, House, Agent, User

# fake = Faker()

# def create_fake_houses(num_houses=5):
#     houses = []
#     for i in range(num_houses):
#         house = House(
#             title=fake.catch_phrase(),
#             size=randint(1000, 5000),
#             price=randint(100000, 1000000),
#             description=fake.paragraph(),
#             city=fake.city(),
#             county=fake.state(),
#             bedrooms=randint(1, 5),
#             bathrooms=randint(1, 3),
#             image_paths=fake.image_url(),
#             agent_id=randint(1, 5)  
#         )
#         houses.append(house)
#     return houses

# def create_fake_agents(num_agents=5):
#     agents = []
#     for i in range(num_agents):
#         agent = Agent(
#             name=fake.name(),
#             email=fake.email(),
#             phonebook=fake.phone_number()
#         )
#         agents.append(agent)
#     return agents

# def create_fake_users(num_users=5):
#     users = []
#     for i in range(num_users):
#         user = User(
#             name=fake.name(),
#             phonebook=fake.phone_number()
#         )
#         users.append(user)
#     return users

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
        
#         fake_houses = create_fake_houses()
#         db.session.add_all(fake_houses)
        
#         fake_agents = create_fake_agents()
#         db.session.add_all(fake_agents)
        
#         fake_users = create_fake_users()
#         db.session.add_all(fake_users)
        
#         db.session.commit()
#         print("Database seeded successfully!")

from app import db, House, Agent, User, app

app.app_context().push()

house1 = House(
    title="Roracio House",
    size=2000,
    price=4500000,
    description="Middle Family House",
    city="Kilimani",
    county="Nairobi",
    bedrooms=3,
    bathrooms=2,
    # image_paths=["https://langatalinkrealestate.com/wp-content/uploads/2023/07/KAR222S-1.jpg", "https://langatalinkrealestate.com/wp-content/uploads/2023/07/KAR222S-3.jpg", "https://langatalinkrealestate.com/wp-content/uploads/2023/07/KAR222S-1-2.jpg", "https://langatalinkrealestate.com/wp-content/uploads/2023/07/KAR222S-2.jpg", "https://langatalinkrealestate.com/wp-content/uploads/2023/07/KAR222S-4.jpg"],
    image_paths="https://langatalinkrealestate.com/wp-content/uploads/2023/07/KAR222S-1.jpg",
    agent_id=1
)

house2 = House(
    title="Osoro&Family House",
    size=3000,
    price=4500000,
    description="House of memories, located on a serene environment",
    city="Upperhill",
    county="Nairobi",
    bedrooms=4,
    bathrooms=2,
    # image_paths=["https://langatalinkrealestate.com/wp-content/uploads/2023/03/KAR302S-1-1.jpg", "https://langatalinkrealestate.com/wp-content/uploads/2023/03/KAR302S-2.jpg", "https://langatalinkrealestate.com/wp-content/uploads/2023/03/KAR302S-4.jpg", "https://langatalinkrealestate.com/wp-content/uploads/2023/03/KAR302S-5.jpg", "https://langatalinkrealestate.com/wp-content/uploads/2023/03/KAR302S-7.jpg"],
    image_paths="https://langatalinkrealestate.com/wp-content/uploads/2023/03/KAR302S-1-1.jpg",
    agent_id=2
)

agent1 = Agent(
    name="Faith Kaburu",
    email="faithkaburu@gmail.com",
    phonebook="0789126352"
)

agent2 = Agent(
    name="Emmanual Peter",
    email="emmanuelpeter@gmail.com",
    phonebook="0796325841"
)

user1 = User(
    name="Prince Hope",
    phonebook="0796564749"
)

user2 = User(
    name="Sumeya Mohammed",
    phonebook="0786235641"
)

db.session.add_all([house1, house2, agent1, agent2, user1, user2])
db.session.commit()

print("Data added to the database successfully!")

