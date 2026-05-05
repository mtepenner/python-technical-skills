# database_basics.py
# Example: ORM implementation for Telemetry Data Reconstruction using SQLAlchemy

from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

# Define the database schema as a Python class
class TelemetryData(Base):
    __tablename__ = 'telemetry'
    id = Column(Integer, primary_key=True)
    aircraft_type = Column(String, nullable=False) # e.g., MD-11 or Boeing 737
    altitude = Column(Float)
    velocity = Column(Float)

def main():
    # Setup an in-memory SQLite database for testing
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # INSERT: Create a new record
    new_data = TelemetryData(aircraft_type="MD-11", altitude=35000.5, velocity=520.0)
    session.add(new_data)
    session.commit() # Save changes

    # SELECT: Query the record back
    record = session.query(TelemetryData).filter_by(aircraft_type="MD-11").first()
    if record:
        print(f"Retrieved Telemetry: {record.aircraft_type} cruising at {record.altitude}ft")

if __name__ == "__main__":
    main()
