from flask import Flask, jsonify    

app = Flask(__name__)


courses = [{'name': "Python Programming Certification",
            'course_id': "0",
            'Description': "Python Programming certification helps you learn"
                           "Python in the structured learning path with innovative"
                           "Out of the box projets matching the industry standards",
            'price': "Visit Edureka.co to know more"},
           {'name': "Data science with python certification",
            'course_id': "1",
            'Description': "Data science with python helps you master the data science"
                           "Life cycle processes in a structure learning path",
            'Price': "Visit Edureka.co to know more"},
           {'name': "AI and Machine Learning Certification",
            'course_id': "2",
            'Description': "AI and ML certification will help you master AI/ML with "
                           "top notch projects like speechrecognition, chatbots, etc.",
            'Price': "Visit Edureka.co to know more"},
           {'name': "Python Spark certification",
            'course_id': "3",
            'Description': "ySpark Certifcation Training is designed to provide you the knowledge and skillset "
                           "that are required to become a successful spark developer using python"
                           "you for the cloudera Hadoop and Spark Developer Certification Exam",
            'Price': "Visit Edureka.co to know more"},
           {'name': "Natural Language Processing with Python Certification",
           'course_id': "4",
            'Description': "Natural Language Processing with Python course will take you through essentials "
                           "of text processing all the way up to classifying texts using machine Learning",
            'Price': "visit edureka.co to know more"}
           ]


@app.route('/')
def index():
    return "Welcome to the course API"


@app.route("/courses", methods=['GET'])
def get():
    return jsonify({'Courses': courses})


@app.route("/courses/<int:course_id>", methods=['GET'])
def get_course(course_id):
    return jsonify({'course': courses[course_id]})


@app.route("/courses", methods=['POST'])
def create():
    course = {'name': "Python Programming Certification",
            'course_id': "5",
            'Description': "Python Programming certification helps you learn"
                           "Python in the structured learning path with innovative"
                           "Out of the box projets matching the industry standards",
            'price': "Visit Edureka.co to know more"}
    courses.append(course)
    return jsonify({'Created': course})


@app.route("/courses/<int:course_id>", methods=['PUT'])
def course_update(course_id):
    courses[course_id]['Description'] = "QRSTUVWXYZ"
    return jsonify({'course':courses[course_id]})


@app.route("/courses/<int:course_id>", methods=['DELETE'])
def delete(course_id):
    courses.remove(courses[course_id])
    return jsonify({'result': True})


if __name__ == "__main__":
    app.run(debug=True)
