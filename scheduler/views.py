from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.template import RequestContext, Template
import simplejson as json
import reglib


def index(request):
    if request.method == 'GET':
        return render_to_response('scheduler.html')

    regclass = request.session['regclass']

    # if user chose to register a list of courses
    try:
        if not regclass.schedule:
            regclass.get_current_schedule()
        if not regclass.next_schedule:
            regclass.get_next_schedule()

        # create a dictionary of courses from the POST request
        courses = []
        # the post keys will be course1, course2....crn1, crn2....
        for i in range((len(request.POST)-1)/2): # length of post is register button + crns + courses
            course_key = "course" + str(i+1)
            crn_key = "crn" + str(i+1)
            course = request.POST[course_key]
            crn = request.POST[crn_key]
            courses.append({'course':course, 'crn':crn})

        # register
        courses_copy = courses[:] # copy this guy because he's gonna get popped to hell
        success_list = register(regclass, courses)

        # display confimation or error message if register success/fail
        # for each course
        for (course, success) in zip(courses_copy, success_list):
            if success:
                messages.success(request, "Successfully registered for " + course['course']) 
            else:
                messages.error(request, "Failed to register for " + course['course'])
        
    except:
        pass

    # get list of courses and create combinations
    try:
        classes = request.POST['classes'].split(', ')
        term_year = request.POST['term'] + request.POST['year']
        results = regclass.make_schedule(classes, term_year)
        combinations = results['combinations']
        classes_possible = results['classes_possible']
        combinations_json = json.dumps(combinations)
    except:
        return render_to_response('scheduler.html', context_instance=RequestContext(request))

    return render_to_response('scheduler.html', {
        'combinations':combinations, 
        'json':combinations_json, 
        'range':range(24), 
        'classes_possible':classes_possible},
        context_instance=RequestContext(request)
    )

def register(regclass, courses):
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
            crn_list.append(str(course_pop['crn']))
        lab_rec_pair_flag = 0

    success_list = regclass.add_classes(crn_list)
                                        
    # Ungroups lecture/lab-rec pairs in the true/false return list
    return_list = []
    for index, crn in enumerate(crn_list):
        if success_list[index]:
            return_list.append(True)
        else:
            return_list.append(False)

    return return_list
        


        
            
                


