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

