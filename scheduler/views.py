from  django.shortcuts import render_to_response
from django.http import Http404
import simplejson as json
from django.http import HttpResponseRedirect
import reglib

def index(request):
    if request.method == 'GET':
        return render_to_response('scheduler/index.html')

    # if user chose to register a list of courses
    try:
        # create a dictionary of courses from the POST request
        courses = []
        # the post keys will be course1, course2....crn1, crn2....
        for i in range((len(request.POST)-1)/2): # length of post is register button + crns + courses
            course_key = "course" + str(i+1)
            crn_key = "crn" + str(i+1)
            course = request.POST[course_key]
            crn = request.POST[crn_key]
            courses.append({'course':course, 'crn':crn})

        register(courses)
        return render_to_response('scheduler/index.html')
    except:
        pass
        
    # get list of courses and create combinations
    regclass = request.session['regclass']
    try:
        classes = request.POST['classes'].split(', ')
        term_year = request.POST['term'] + request.POST['year']
        results = regclass.make_schedule(classes, term_year)
        combinations = results['combinations']
        classes_possible = results['classes_possible']
        combinations_json = json.dumps(combinations)
    except:
        return render_to_response('scheduler/index.html')

    return render_to_response('scheduler/index.html', {'combinations':combinations, 'json':combinations_json, 'range':range(24), 'classes_possible':classes_possible})

def register(courses):
    """ register for all courses in a combination at once 
    @parameters courses is a list of course dictionaries with crn and course title 
    puts the crns in an appropriate list (with lecture/lab-rec logic) and hands it to add_class """

    # makes a list of crns. lecture/lab-rec pairs are a list within that list and normal lectuers are simply within the list.
    # algorithm pops a course, checks if any other course is in the list of courses to add. if there is, that must be its linked lecture/lab-rec. else, it is just a normal course and add it to the crn list.
    crn_list = []
    lab_rec_pair_flag = 0
    while len(courses) is not 0:
        course_pop = courses.pop()
        for course in courses:
            if not lab_rec_pair_flag:
                if course_pop['course'] == course['course']:
                    lab_rec_pair_flag = 1
                    crn_list.append([ course_pop['crn'], course['crn'] ])
                    courses.remove( {'course': course['course'], 'crn': course['crn']} )
        if not lab_rec_pair_flag:
            crn_list.append(course_pop['crn'])
        lab_rec_pair_flag = 0

    regclass = request.session['regclass']
    regclass.add_classes(crn_list)

        
            
                


