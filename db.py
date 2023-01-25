from sqlmodel import create_engine, Session

engine = create_engine(
    "sqlite:///db/carsharing.db",
    connect_args={"check_same_thread": False}, #Needed for SQlite and FastAPI
    echo=True #Log generated SQL - Not for prod
)

def get_session():
    with Session(engine) as session:
        yield session #The with session will be closed as soon as the get_session execution is finished. This wraps everything inside the tiwh block. If anything goes wrong, it will revert the entire operation.
