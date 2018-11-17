curriculum = {
    "name": "John",
    "last_name": "Smith",
    "age": 37,
    "email": "john.smith@example.com",
    "education": [
        {
            "instituion": "Super High School",
            "completed": True,
            "degree": "Bachillerado en Educación Media",
            "year_of_completion": 2002
        },
        {
            "instituion": "University of California in Berkeley",
            "completed": True,
            "degree": "Bachellor Degree Applied Mathematics",
            "year_of_completion": 2006
        },
        {
            "instituion": "Harvard University",
            "completed": True,
            "degree": "Master of Science in Data Science",
            "year_of_completion": 2009
        }
    ],
    "experience": [
        {
            "company": "GladOS Research Lab",
            "position": "Staff Data Analyst",
            "started": 2007,
            "finished": 2008,
            "actual_job": False,
            "description": "Part of the staff working in diverse revenue leakage tasks"
        },
        {
            "company": "Troogle Inc.",
            "position": "Junior Social Data Analyst",
            "started": 2010,
            "finished": 2013,
            "actual_job": False,
            "description": "Designed algorithms to analyze people's social media and sell them stuff they don't need"
        },
        {
            "company": "Tramazon Corporation",
            "position": "Senior Evil Algorithm Designer",
            "started": 2014,
            "finished": 2018,
            "actual_job": False,
            "description": "Lead the team of Automated Manipulation Algorithms Research Group"
        },
                {
            "company": "Profe en GreenCore",
            "position": "Senior Torturador de Estudiantes",
            "started": 2018,
            "actual_job": True,
            "description": "Atormenta estudiantes con tarea de Python"
        }
    ]
}


class Experiencia(object):

    def __init__(self, company, position, started, finished, description, actual_job=False):
        self.__company = company
        self.__actual_job = actual_job
        self.__position = position
        self.__started = started
        self.__finished = finished
        self.__description = description

    def as_dictionary(self):
        return {
            "company": self.__company,
            "actual_job": self.__actual_job,
            "position": self.__position,
            "started": self.__started,
            "finished": self.__finished,
            "description": self.__description
        }

    def calculate_experience(self, actual_year):
        if self.__actual_job:
            return self.__calculate_experience_when_actual_job(actual_year)
        else:
            return self.__calculate_experience_when_not_actual_job()

    def __calculate_experience_when_not_actual_job(self):
        return self.__finished - self.__started

    def __calculate_experience_when_actual_job(self, actual_year):
        return actual_year - self.__started


experiencia = Experiencia(
    company="La Compania",
    actual_job=False,
    position="Contador",
    started=2014,
    finished=2017,
    description="Esta es una descripcion del trabajo"
)
print(experiencia.as_dictionary())
print(experiencia.calculate_experience(2018))
