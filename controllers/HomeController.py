from flask import render_template
from models.instructor import instructor
from models.student import student
from models.course import course
from models.studentscourses import studentscourses
from models.eventlist import eventlist
import json

class HomeController():

    @staticmethod
    def view_page(request):
        # i  = instructor.query.filter_by(mail='admin@example.com').first()

        alli = instructor.query.all()
        return render_template('instructor.html', alli=alli)
    @staticmethod
    def listCourse(request):
        a = course.query.filter_by(iid=12)
        return render_template('instructor.html', alli=a)

    @staticmethod
    def coursesTakenByStudent(request):
        a = studentscourses.query.filter_by(sid=12)
        return render_template('instructor.html', alli=a)

    @staticmethod
    def getEvents(request):
        a = eventlist.query.all()
        print type(a)
        return render_template('instructor.html', alli=a)

    @staticmethod
    def listEvents(request):
        a = eventlist.query.all()

        listOfEvents=[]
        for i in a:
            listOfEvents.append(i.jsonEvents())
        return json.dumps(listOfEvents)
        # return json.dumps(listOfEvents)
