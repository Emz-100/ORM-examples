from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Create an SQLite database engine
engine = create_engine('sqlite:///:memory:')

# Create a Base class as a template for models
Base = declarative_base()

# Define a Task model that maps to a tasks table
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    completed = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Task(id={self.id}, title={self.title}, created_at={self.created_at}, completed={self.completed})>"

# Create the tasks table in the database
Base.metadata.create_all(engine)

# Create a session object to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create a new task
task1 = Task(title='Buy groceries', description='Milk, eggs, bread')
session.add(task1)
session.commit()

# Query all tasks
tasks = session.query(Task).all()
print("All Tasks:")
for task in tasks:
    print(task)

# Update a task's status
task1.completed = True
session.commit()

# Create another task
task2 = Task(title='Finish report', description='Due by Friday')
session.add(task2)
session.commit()

# Delete a task
session.delete(task1)
session.commit()

# Query tasks again
tasks = session.query(Task).all()
print("\nAll Tasks (after update and delete operations):")
for task in tasks:
    print(task)

# Close the session
session.close()
