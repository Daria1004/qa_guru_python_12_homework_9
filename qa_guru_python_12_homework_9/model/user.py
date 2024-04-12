import enum


class Gender(enum.Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Subject(enum.Enum):
    computer = "Computer Science"


class Hobby(enum.Enum):
    sports = "Sports"
    reading = "Reading"
    music = "Music"


class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile: str
    year: str
    month: str
    day: str
    subjects: Subject
    hobbies: Hobby
    picture: str
    current_address: str
    state: str
    city: str

    def __init__(self, first_name, last_name, email, gender, mobile, year, month, day, subjects, hobbies, picture, current_address, state, city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.mobile = mobile
        self.year = year
        self.month = month
        self.day = day
        self.subjects = subjects
        self.hobbies = hobbies
        self.picture = picture
        self.current_address = current_address
        self.state = state
        self.city = city


test_user = User(
    'Ivan',
    'Durian',
    'ID@gmail.com',
    Gender.other,
    '1234512345',
    '1900', 'May', '10',
    Subject.computer,
    Hobby.music,
    'clover.jpg',
    'Thailand, Phuket',
    'Haryana',
    'Panipat'
)
