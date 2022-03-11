from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from requests.auth import HTTPBasicAuth
from .models import DP, DPExternal, DPM, DPMExternal, ImpactAreas, ImpactApplications, EDACurrentMonth, EDAPreviousMonth, EDALearnings
from .form import DPForm, DPExternalForm, DPM, DPMExternal,MOB,MOBExternal,ImpactAreaForm, ImpactApplicationForm, EDAPreviousMonthForm, EDACurrentMonthForm, EDALearningsForm


import sys
from operator import itemgetter
import requests
import json
from datetime import datetime, date, timedelta
import datetime, calendar
from collections import OrderedDict
from pytz import timezone
import time

import os
import environ
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(SECRET_KEY = str,)
environ.Env.read_env(os.path.join(BASE_DIR,'.env'))

import warnings
warnings.filterwarnings("ignore")


def index(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('qualityboard:login'))

    elif ('dialpad.com' not in request.user.email):
        print("Not A Dialpad User:", request.user)
        logout(request)
        return render(request, 'login.html', {
            "message": "Invalid User Permission !!!"
        })

    else:
        dp = DP.objects.get(id=1)
        dpexternal = DPExternal.objects.get(id=1)
        dpm = DPM.objects.get(id=1)
        dpmexternal = DPMExternal.objects.get(id=1)

        lastupdatedon = dp.LastUpdate

        dpdailyjira = [dp.One,dp.Two,dp.Three,dp.Four,dp.Five,dp.Six,dp.Seven,dp.Eight,dp.Nine,dp.Ten,dp.Eleven,dp.Twelve,dp.Thirteen,dp.Fourteen, \
                       dp.Fifteen,dp.Sixteen,dp.Seventeen,dp.Eighteen,dp.Nineteen,dp.Twenty,dp.Twentyone,dp.Twentytwo,dp.Twentythree,dp.Twentyfour, \
                       dp.Twentyfive,dp.Twentysix,dp.Twentyseven,dp.Twentyeight,dp.Twentynine,dp.Thirty,dp.Thirtyone,\
                       ]
        totaldpdailyjira = list(map(int, dpdailyjira))

        dpdailysealteam = {
            'AccountBilling': int(dp.AccountBilling), 'Analytics': int(dp.Analytics), 'BackendInfrastructure': int(dp.BackendInfrastructure), 'CallExperience': int(dp.CallExperience), 'CallingFeatures': int(dp.CallingFeatures), \
            'ContactCenter': int(dp.ContactCenter), 'CustomerAgentAssist': int(dp.CustomerAgentAssist), 'DataInsights': int(dp.DataInsights), 'DeveloperPlatform': int(dp.DeveloperPlatform), 'Devices': int(dp.Devices), 'DialpadTalk': int(dp.DialpadTalk), \
            'DigitalExperience': int(dp.DigitalExperience), 'EngineeringProductivity': int(dp.EngineeringProductivity), 'FrontendInfrastructure': int(dp.FrontendInfrastructure), 'Growth': int(dp.Growth), 'Integrations': int(dp.Integrations), \
            'Messaging': int(dp.Messaging), 'Mobile': int(dp.Mobile), 'ProductionSupport': int(dp.ProductionSupport), 'UberConference': int(dp.UberConference), 'VoiceIntelligence': int(dp.VoiceIntelligence), 'Website': int(dp.Website), \
           }
        internaltop5sealteam = dict(sorted(dpdailysealteam.items(), key = itemgetter(1), reverse = True)[:5])

        dpdailystatus = {
            'Backlog': int(dp.Backlog), 'Blocked': int(dp.Blocked), 'CodeReview': int(dp.CodeReview), 'Closed': int(dp.Closed), 'InProgress': int(dp.InProgress), \
            'NeedsTriage': int(dp.NeedsTriage), 'Open': int(dp.Open), 'ReadyforTesting': int(dp.ReadyforTesting), 'ReadyforProduction': int(dp.ReadyforProduction), 'ToDo': int(dp.ToDo),
            }
        internaltop5status = dict(sorted(dpdailystatus.items(), key=itemgetter(1), reverse=True)[:5])

        dpexternaldailyjira = [dpexternal.One, dpexternal.Two, dpexternal.Three, dpexternal.Four, dpexternal.Five, dpexternal.Six, dpexternal.Seven, dpexternal.Eight, dpexternal.Nine, dpexternal.Ten, dpexternal.Eleven,
                       dpexternal.Twelve, dpexternal.Thirteen, dpexternal.Fourteen, \
                       dpexternal.Fifteen, dpexternal.Sixteen, dpexternal.Seventeen, dpexternal.Eighteen, dpexternal.Nineteen, dpexternal.Twenty, dpexternal.Twentyone,
                       dpexternal.Twentytwo, dpexternal.Twentythree, dpexternal.Twentyfour, \
                       dpexternal.Twentyfive, dpexternal.Twentysix, dpexternal.Twentyseven, dpexternal.Twentyeight, dpexternal.Twentynine, dpexternal.Thirty, dpexternal.Thirtyone, \
                       ]
        totaldpexternaldailyjira = list(map(int, dpexternaldailyjira))
        dpexternaldailysealteam = {
            'AccountBilling': int(dpexternal.AccountBilling), 'Analytics': int(dpexternal.Analytics),'BackendInfrastructure': int(dpexternal.BackendInfrastructure), 'CallExperience': int(dpexternal.CallExperience), 'CallingFeatures': int(dpexternal.CallingFeatures), \
            'ContactCenter': int(dpexternal.ContactCenter), 'CustomerAgentAssist': int(dpexternal.CustomerAgentAssist), 'DataInsights': int(dpexternal.DataInsights), 'DeveloperPlatform': int(dpexternal.DeveloperPlatform), 'Devices': int(dpexternal.Devices), 'DialpadTalk': int(dpexternal.DialpadTalk), \
            'DigitalExperience': int(dpexternal.DigitalExperience), 'EngineeringProductivity': int(dpexternal.EngineeringProductivity), 'FrontendInfrastructure': int(dpexternal.FrontendInfrastructure), 'Growth': int(dpexternal.Growth), 'Integrations': int(dpexternal.Integrations), \
            'Messaging': int(dpexternal.Messaging), 'Mobile': int(dpexternal.Mobile), 'ProductionSupport': int(dpexternal.ProductionSupport), 'UberConference': int(dpexternal.UberConference), 'VoiceIntelligence': int(dpexternal.VoiceIntelligence), 'Website': int(dpexternal.Website), \
            }
        externaltop5sealteam = dict(sorted(dpexternaldailysealteam.items(), key=itemgetter(1), reverse=True)[:5])

        dpexternaldailystatus = {
            'Backlog': int(dpexternal.Backlog), 'Blocked': int(dpexternal.Blocked), 'CodeReview': int(dpexternal.CodeReview), 'Closed': int(dpexternal.Closed), 'InProgress': int(dpexternal.InProgress), \
            'NeedsTriage': int(dpexternal.NeedsTriage), 'Open': int(dpexternal.Open), 'ReadyforTesting': int(dpexternal.ReadyforTesting), 'ReadyforProduction': int(dpexternal.ReadyforProduction), 'ToDo': int(dpexternal.ToDo),
        }
        externaltop5status = dict(sorted(dpexternaldailystatus.items(), key=itemgetter(1), reverse=True)[:5])

        return render(request,'index.html', {
            "lastupdatedon": lastupdatedon,
            "dpdailyjira": dpdailyjira,
            "dpexternaldailyjira": dpexternaldailyjira,
            "internaltop5sealteamkeys": list(internaltop5sealteam.keys()),
            "internaltop5sealteamvalues": list(internaltop5sealteam.values()),
            "internaltop5statuskeys":list(internaltop5status.keys()),
            "internaltop5statusvalues": list(internaltop5status.values()),
            "externaltop5sealteamkeys": list(externaltop5sealteam.keys()),
            "externaltop5sealteamvalues": list(externaltop5sealteam.values()),
            "externaltop5statuskeys": list(externaltop5status.keys()),
            "externaltop5statusvalues": list(externaltop5status.values()),
            "totaldpdailyjira": sum(totaldpdailyjira),
            "totaldpexternaldailyjira": sum(totaldpexternaldailyjira),
            })



def dpm(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('qualityboard:login'))

    else:
        dpm = DPM.objects.get(id=1)
        dpmexternal = DPMExternal.objects.get(id=1)

        lastdpmupdatedon = dpm.LastUpdate
        dpmdailyjira = [dpm.One, dpm.Two, dpm.Three, dpm.Four, dpm.Five, dpm.Six, dpm.Seven, dpm.Eight, dpm.Nine, dpm.Ten, dpm.Eleven, dpm.Twelve, dpm.Thirteen, dpm.Fourteen, \
                       dpm.Fifteen, dpm.Sixteen, dpm.Seventeen, dpm.Eighteen, dpm.Nineteen, dpm.Twenty, dpm.Twentyone, dpm.Twentytwo, dpm.Twentythree, dpm.Twentyfour, \
                       dpm.Twentyfive, dpm.Twentysix, dpm.Twentyseven, dpm.Twentyeight, dpm.Twentynine, dpm.Thirty, dpm.Thirtyone, \
                       ]
        totaldpmdailyjira = list(map(int, dpmdailyjira))

        dpmdailystatus = {
            'Backlog': int(dpm.Backlog), 'Blocked': int(dpm.Blocked), 'CodeReview': int(dpm.CodeReview), 'Closed': int(dpm.Closed), 'InProgress': int(dpm.InProgress), \
            'NeedsTriage': int(dpm.NeedsTriage), 'Open': int(dpm.Open), 'ReadyforTesting': int(dpm.ReadyforTesting), 'ReadyforProduction': int(dpm.ReadyforProduction), 'ToDo': int(dpm.ToDo),
        }
        internaltop5dpmstatus = dict(sorted(dpmdailystatus.items(), key=itemgetter(1), reverse=True)[:5])

        dpmexternaldailyjira = [dpmexternal.One, dpmexternal.Two, dpmexternal.Three, dpmexternal.Four, dpmexternal.Five, dpmexternal.Six, dpmexternal.Seven, dpmexternal.Eight, dpmexternal.Nine, dpmexternal.Ten, \
                               dpmexternal.Eleven, dpmexternal.Twelve, dpmexternal.Thirteen, dpmexternal.Fourteen, dpmexternal.Fifteen, dpmexternal.Sixteen, dpmexternal.Seventeen, dpmexternal.Eighteen, \
                               dpmexternal.Nineteen, dpmexternal.Twenty, dpmexternal.Twentyone, dpmexternal.Twentytwo, dpmexternal.Twentythree, dpmexternal.Twentyfour, \
                               dpmexternal.Twentyfive, dpmexternal.Twentysix, dpmexternal.Twentyseven, dpmexternal.Twentyeight, dpmexternal.Twentynine, dpmexternal.Thirty, dpmexternal.Thirtyone, \
                               ]
        totaldpmexternaldailyjira = list(map(int, dpmexternaldailyjira))

        dpmexternaldailystatus = {
            'Backlog': int(dpmexternal.Backlog), 'Blocked': int(dpmexternal.Blocked), 'CodeReview': int(dpmexternal.CodeReview), 'Closed': int(dpmexternal.Closed), 'InProgress': int(dpmexternal.InProgress), \
            'NeedsTriage': int(dpmexternal.NeedsTriage), 'Open': int(dpmexternal.Open), 'ReadyforTesting': int(dpmexternal.ReadyforTesting), 'ReadyforProduction': int(dpmexternal.ReadyforProduction), 'ToDo': int(dpmexternal.ToDo),
        }
        externaltop5dpmstatus = dict(sorted(dpmexternaldailystatus.items(), key=itemgetter(1), reverse=True)[:5])

    return render(request,'dpm.html', {
        "lastdpmupdatedon": lastdpmupdatedon,
        "dpmdailyjira": dpmdailyjira,
        "dpmexternaldailyjira": dpmexternaldailyjira,
        "internaltop5dpmstatuskeys": list(internaltop5dpmstatus.keys()),
        "internaltop5dpmstatusvalues": list(internaltop5dpmstatus.values()),
        "externaltop5dpmstatuskeys": list(externaltop5dpmstatus.keys()),
        "externaltop5dpmstatusvalues": list(externaltop5dpmstatus.values()),
        "totaldpmdailyjira": sum(totaldpmdailyjira),
        "totaldpmexternaldailyjira": sum(totaldpmexternaldailyjira),

    })


def mob(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('qualityboard:login'))

    else:
        mob = MOB.objects.get(id=1)
        mobexternal = MOBExternal.objects.get(id=1)

        lastmobupdatedon = mob.LastUpdate
        mobdailyjira = [mob.One, mob.Two, mob.Three, mob.Four, mob.Five, mob.Six, mob.Seven, mob.Eight, mob.Nine, mob.Ten, mob.Eleven, mob.Twelve, mob.Thirteen, mob.Fourteen, \
                        mob.Fifteen, mob.Sixteen, mob.Seventeen, mob.Eighteen, mob.Nineteen, mob.Twenty, mob.Twentyone, mob.Twentytwo, mob.Twentythree, mob.Twentyfour, \
                        mob.Twentyfive, mob.Twentysix, mob.Twentyseven, mob.Twentyeight, mob.Twentynine, mob.Thirty, mob.Thirtyone, \
                        ]
        totalmobdailyjira = list(map(int, mobdailyjira))

        mobdailystatus = {
            'Backlog': int(mob.Backlog), 'Blocked': int(mob.Blocked), 'CodeReview': int(mob.CodeReview), 'Closed': int(mob.Closed), 'InProgress': int(mob.InProgress), \
            'NeedsTriage': int(mob.NeedsTriage), 'Open': int(mob.Open), 'ReadyforTesting': int(mob.ReadyforTesting), 'ReadyforProduction': int(mob.ReadyforProduction), 'ToDo': int(mob.ToDo),
        }
        internaltop5mobstatus = dict(sorted(mobdailystatus.items(), key=itemgetter(1), reverse=True)[:5])

        mobexternaldailyjira = [mobexternal.One, mobexternal.Two, mobexternal.Three, mobexternal.Four, mobexternal.Five, mobexternal.Six, mobexternal.Seven, mobexternal.Eight, mobexternal.Nine, mobexternal.Ten, \
                                mobexternal.Eleven, mobexternal.Twelve, mobexternal.Thirteen, mobexternal.Fourteen, mobexternal.Fifteen, mobexternal.Sixteen, mobexternal.Seventeen, mobexternal.Eighteen, \
                                mobexternal.Nineteen, mobexternal.Twenty, mobexternal.Twentyone, mobexternal.Twentytwo, mobexternal.Twentythree, mobexternal.Twentyfour, \
                                mobexternal.Twentyfive, mobexternal.Twentysix, mobexternal.Twentyseven, mobexternal.Twentyeight, mobexternal.Twentynine, mobexternal.Thirty, mobexternal.Thirtyone, \
                                ]
        totalmobexternaldailyjira = list(map(int, mobexternaldailyjira))

        mobexternaldailystatus = {
            'Backlog': int(mobexternal.Backlog), 'Blocked': int(mobexternal.Blocked), 'CodeReview': int(mobexternal.CodeReview), 'Closed': int(mobexternal.Closed), 'InProgress': int(mobexternal.InProgress), \
            'NeedsTriage': int(mobexternal.NeedsTriage), 'Open': int(mobexternal.Open), 'ReadyforTesting': int(mobexternal.ReadyforTesting), 'ReadyforProduction': int(mobexternal.ReadyforProduction), 'ToDo': int(mobexternal.ToDo), \
        }
        externaltop5mobstatus = dict(sorted(mobexternaldailystatus.items(), key=itemgetter(1), reverse=True)[:5])

        return render(request, 'mob.html', {
            "lastmobupdatedon": lastmobupdatedon,
            "mobdailyjira": mobdailyjira,
            "mobexternaldailyjira": mobexternaldailyjira,
            "internaltop5mobstatuskeys": list(internaltop5mobstatus.keys()),
            "internaltop5mobstatusvalues": list(internaltop5mobstatus.values()),
            "externaltop5mobstatuskeys": list(externaltop5mobstatus.keys()),
            "externaltop5mobstatusvalues": list(externaltop5mobstatus.values()),
            "totalmobdailyjira": sum(totalmobdailyjira),
            "totalmobexternaldailyjira": sum(totalmobexternaldailyjira),
        })

def eda(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('qualityboard:login'))

    else:
        month = datetime.datetime.now().strftime("%B")
        dictimpactareas = {}
        dictimpactapplication = {}
        dictedapreviousmonth = {}
        dictedacurrentmonth = {}
        dictedalaernings = {}

        countarea = 1
        while countarea <= 5:
            impactareas = ImpactAreas.objects.get(id=countarea)
            dictimpactareas[impactareas.Area] = impactareas.Number
            countarea += 1
        impactareaskeys = list(dictimpactareas.keys())
        impactareasvalues = list(dictimpactareas.values())

        countapplication = 1
        while countapplication <= 5:
            impactapplication = ImpactApplications.objects.get(id=countapplication)
            dictimpactapplication[impactapplication.Application] = impactapplication.Number
            countapplication += 1
        impactapplicationskeys = list(dictimpactapplication.keys())
        impactapplicationsvalues = list(dictimpactapplication.values())

        countprevousmonth = 1
        while countprevousmonth <= 7:
            edapreviousmonth = EDAPreviousMonth.objects.get(id=countprevousmonth)
            dictedapreviousmonth[edapreviousmonth.EDAType] = edapreviousmonth.Number
            countprevousmonth += 1
        edapreviousmonthkeys = list(dictedapreviousmonth.keys())
        edapreviousmonthvalues = list(dictedapreviousmonth.values())
        totalpreviousmonth = list(map(int, edapreviousmonthvalues))

        countcurrentmonth = 1
        while countcurrentmonth <= 7:
            edacurrentmonth = EDACurrentMonth.objects.get(id=countcurrentmonth)
            dictedacurrentmonth[edacurrentmonth.EDAType] = edacurrentmonth.Number
            countcurrentmonth += 1
        edacurrentmonthkeys = list(dictedacurrentmonth.keys())
        edacurrentmonthvalues = list(dictedacurrentmonth.values())
        totalcurrentmonth = list(map(int, edacurrentmonthvalues))

        edalearning = EDALearnings.objects.get(id=1)
        dictedalaernings["ActionItems"] = edalearning.ActionItem
        dictedalaernings["PreviousMonths"] = edalearning.PreviousMonth
        dictedalaernings["CurrentMonth"] = edalearning.CurrentMonth

        edalearningkeys = list(dictedalaernings.keys())
        edalearningvalues = list(dictedalaernings.values())

        return render(request, 'eda.html',{
            "month": month,
            "impactareaskeys": impactareaskeys,
            "impactareasvalues": impactareasvalues,
            "impactapplicationskeys": impactapplicationskeys,
            "impactapplicationsvalues": impactapplicationsvalues,
            "edapreviousmonthkeys": edapreviousmonthkeys,
            "edapreviousmonthvalues": edapreviousmonthvalues,
            "edacurrentmonthkeys": edacurrentmonthkeys,
            "edacurrentmonthvalues": edacurrentmonthvalues,
            "totalpreviousmonth": sum(totalpreviousmonth),
            "totalcurrentmonth": sum(totalcurrentmonth),
            "edalearning": edalearningvalues[0],
            "previousmonth": edalearningvalues[1],
            "currentmonth": edalearningvalues[2],            
        })


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('qualityboard:index')
        else:
            return render(request, 'login.html', {
                "message": "Incorrect Credentials !!!"
            })

    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return render(request, 'login.html', {
        "message": "Logged Out !!!"
    })



def get_custom_data(start_date,end_date,project,username,token,url):
    components = {}
    totals = {}
    status = {}
    numofissues = []
    dateofmonth = []
    startat = [0, 101, 201, 301, 401]
    error_flag = 0

    api_url=url+"?jql=created >= " + str(start_date) + " and created <= " + str(
        end_date) + " and project = " + project + " and issuetype in (Bug, Improvement, Task) and labels in (jira_escalated, EAPRequest) order by created desc&maxResults=100"

    r = requests.get(api_url, auth=HTTPBasicAuth(username, token))

    try:
        json_content = r.json()
    except ValueError:
        print("Error:", ValueError)
        error_flag = 1

    if json_content['total'] != 0:
        for i in json_content['issues']:
            if (project == 'DP'):
                jira_component = i['fields']['customfield_12136']['value']
            jira_createddate = i['fields']['created'].split('T')[0]
            jira_status = i['fields']['status']['name']

            if (project == 'DP'):
                if not jira_component in components:
                    components[jira_component] = 1
                else:
                    components[jira_component] += 1

            if not jira_createddate in totals:
                totals[jira_createddate] = 1
            else:
                totals[jira_createddate] += 1
            if not jira_status in status:
                status[jira_status] = 1
            else:
                status[jira_status] += 1

    total_jiras = json_content['total']
    iterations = int(total_jiras / 100)
    if total_jiras % 100:
        iterations = iterations + 1

    count = 1
    while count <= iterations - 1:
        api_url = url+"?jql=created >= " + str(start_date) + " and created <= " + str(
            end_date) + " and project = " + project + " and issuetype in (Bug, Improvement, Task) and labels in (jira_escalated, EAPRequest) order by created desc&startAt="+str(startat[count])+"&maxResults=100"

        r = requests.get(api_url, auth=HTTPBasicAuth(username, token))

        try:
            json_content = r.json()
        except ValueError:
            print("Error:", ValueError)
            error_flag = 1

        if json_content['total'] != 0:
            for i in json_content['issues']:
                if (project == 'DP'):
                    jira_component = i['fields']['customfield_12136']['value']
                jira_createddate = i['fields']['created'].split('T')[0]
                jira_status = i['fields']['status']['name']

                if (project == 'DP'):
                    if not jira_component in components:
                        components[jira_component] = 1
                    else:
                        components[jira_component] += 1

                if not jira_createddate in totals:
                    totals[jira_createddate] = 1
                else:
                    totals[jira_createddate] += 1
                if not jira_status in status:
                    status[jira_status] = 1
                else:
                    status[jira_status] += 1

        count += 1

    return components, totals, status, error_flag


def custom(request):
    month = datetime.datetime.now().strftime("%B")
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('qualityboard:login'))

    else:

        if request.method == 'POST':
            if request.POST['year'] != 'Year' and request.POST['month'] != 'Month' and request.POST['project'] != 'Project':
                year = int(request.POST['year'])
                month = int(request.POST['month'])
                project = request.POST['project']
                num_days = calendar.monthrange(year, month)[1]
                days = [datetime.date(year, month, day) for day in range(1, num_days + 1)]
                start_date = str(year)+"-"+str(month)+"-"+"01"
                end_date = days[-1] + timedelta(days=1)

                url = 'https://dialpad.atlassian.net/rest/api/2/search'
                username = env('DJANGO_JIRA_USER')
                token = env('DJANGO_JIRA_TOKEN')

                components, totals, status, error_flag = get_custom_data(start_date,end_date,project,username,token,url)
                
                if not bool(totals):
                    message = "No Jira Data Available. Please check the presets !!!"
                    return render(request, 'custom.html', {
                        "messages": message,
                    })
                else:
                    reversetotals = OrderedDict(reversed(list(totals.items())))
                    reversetotalsKeys = list(reversetotals.keys())
                    reversetotalsValues = list(reversetotals.values())

                    externaltop5components = dict(sorted(components.items(), key=itemgetter(1), reverse=True)[:5])
                    externaltop5status = dict(sorted(status.items(), key=itemgetter(1), reverse=True)[:5])

                    return render(request, 'custom.html', {
                        "flag": True,
                        "reversetotalsKeys": reversetotalsKeys,
                        "reversetotalsValues": reversetotalsValues,
                        "totalreversetotalsValues": sum(reversetotalsValues),
                        "externaltop5componentskeys": list(externaltop5components.keys()),
                        "externaltop5componentsvalues": list(externaltop5components.values()),
                        "externaltop5statuskeys": list(externaltop5status.keys()),
                        "externaltop5statusvalues": list(externaltop5status.values()),
                        "project": project,
                        "messages": "",
                    })
            message = "No Jira Data Available. Please check the presets !!!"
            return render(request, 'custom.html', {
                "messages": message,
            })

    return render(request, 'custom.html', {
        "messages": "",
            })



def get_dp_data(project,startdate,enddate,username,token,next_date,labels,url):
    components = {}
    totals = {}
    status = {}
    numofissues = []
    dateofmonth = []
    startat = [0, 101, 201, 301, 401]
    error_flag = 0

    if len(labels) == 0:

        api_url= url+"?jql=created >= " + str(startdate) + " and created <= " + str(
            next_date) + " and project = "+project+" and issuetype in (Bug, Improvement) and reporter in (5d1c6ad2cdf26a0d349c8e4b, 5ca66ffa1b65666cbad29e71, 5ce2a47e48f7b90dbfd62f42, 6020ffa6e6124800694a5ea1, 5c82e2bb29592211228c8ad6, 557058:53b57946-01ca-4125-9e92-b1cbb4c62182, 5ca7c177e623ae19ec5509f3, 6050684490f2880070e03fd0, 5c82e34fe6e3160b9b6fe340, 5d85053f1fcbda0da1348072, 6116df671e9ac7006816f5bc, 6020ffa77db80e006a04234c, currentUser(), 61437a3534599600714b6f9a, 5df828459a14250cb69ebf5c, 5d0a687201a78b0c4e014b76, 5df82840336e9e0cad16a003, 5ca6a83d3270b449b4fed5b2, 5c57d0a5b287111683605746, 5ff423bab66825010ea3ecb3, 5d11b4e3a3e35a0c8cd30d16, 61534c382f6aed0068476469, 5f4c1666fdc3f5003f1f5ed5, 5b33fa796b94db70b4d76a90, 5f97df2299b42e00698ce0e8) order by created desc&maxResults=100"
    else:
        api_url = url+"?jql=created >= " + str(startdate) + " and created <= " + str(
            next_date) + " and project = "+project+" and issuetype in (Bug, Improvement, Task) and labels in (jira_escalated, EAPRequest) order by created desc&maxResults=100"

    r = requests.get(api_url, auth=HTTPBasicAuth(username, token))

    try:
        json_content = r.json()
    except ValueError:
        print("Error:", ValueError)
        error_flag = 1

    if json_content['total'] != 0:
        for i in json_content['issues']:
            if (project == 'DP'):
                jira_component = i['fields']['customfield_12136']['value']
            jira_createddate = i['fields']['created'].split('T')[0]
            jira_status = i['fields']['status']['name']

            if (project == 'DP'):
                if not jira_component in components:
                    components[jira_component] = 1
                else:
                    components[jira_component] += 1

            if not jira_createddate in totals:
                totals[jira_createddate] = 1
            else:
                totals[jira_createddate] += 1
            if not jira_status in status:
                status[jira_status] = 1
            else:
                status[jira_status] += 1

    total_jiras = json_content['total']
    iterations = int(total_jiras / 100)
    if total_jiras % 100:
        iterations = iterations + 1

    count = 1

    while count <= iterations - 1:
        if len(labels) == 0:
            api_url = url+"?jql=created >= " + str(startdate) + " and created <= " + str(
                next_date) + " and project = "+project+" and issuetype in (Bug, Improvement) and reporter in (5d1c6ad2cdf26a0d349c8e4b, 5ca66ffa1b65666cbad29e71, 5ce2a47e48f7b90dbfd62f42, 6020ffa6e6124800694a5ea1, 5c82e2bb29592211228c8ad6, 557058:53b57946-01ca-4125-9e92-b1cbb4c62182, 5ca7c177e623ae19ec5509f3, 6050684490f2880070e03fd0, 5c82e34fe6e3160b9b6fe340, 5d85053f1fcbda0da1348072, 6116df671e9ac7006816f5bc, 6020ffa77db80e006a04234c, currentUser(), 61437a3534599600714b6f9a, 5df828459a14250cb69ebf5c, 5d0a687201a78b0c4e014b76, 5df82840336e9e0cad16a003, 5ca6a83d3270b449b4fed5b2, 5c57d0a5b287111683605746, 5ff423bab66825010ea3ecb3, 5d11b4e3a3e35a0c8cd30d16, 61534c382f6aed0068476469, 5f4c1666fdc3f5003f1f5ed5, 5b33fa796b94db70b4d76a90, 5f97df2299b42e00698ce0e8) order by created desc&startAt=" + str(
                startat[count]) + "&maxResults=100"
        else:
            api_url = url+"?jql=created >= " + str(startdate) + " and created <= " + str(
                next_date) + " and project = "+project+" and issuetype in (Bug, Improvement, Task) and labels in (jira_escalated, EAPRequest) order by created desc&startAt="+str(startat[count])+"&maxResults=100"

        r = requests.get(api_url, auth=HTTPBasicAuth(username, token))

        try:
            json_content = r.json()
        except ValueError:
            print("Error:", ValueError)
            error_flag = 1

        if json_content['total'] != 0:
            for i in json_content['issues']:
                if (project == 'DP'):
                    jira_component = i['fields']['customfield_12136']['value']
                jira_createddate = i['fields']['created'].split('T')[0]
                jira_status = i['fields']['status']['name']

                if (project == 'DP'):
                    if not jira_component in components:
                        components[jira_component] = 1
                    else:
                        components[jira_component] += 1

                if not jira_createddate in totals:
                    totals[jira_createddate] = 1
                else:
                    totals[jira_createddate] += 1
                if not jira_status in status:
                    status[jira_status] = 1
                else:
                    status[jira_status] += 1

        count += 1

    
    return components, totals, status, error_flag


def save_dp_data(days,components,totals,status,project):
    all_components = {
        'AccountBilling': 0,
        'Analytics': 0,
        'BackendInfrastructure': 0,
        'CallExperience': 0,
        'CallingFeatures': 0,
        'ContactCenter': 0,
        'CustomerAgentAssist': 0,
        'DataInsights': 0,
        'DeveloperPlatform': 0,
        'Devices': 0,
        'DialpadTalk': 0,
        'DigitalExperience': 0,
        'EngineeringProductivity': 0,
        'FrontendInfrastructure': 0,
        'Growth': 0,
        'Integrations': 0,
        'Messaging': 0,
        'Mobile': 0,
        'ProductionSupport': 0,
        'UberConference': 0,
        'VoiceIntelligence': 0,
        'Website': 0,
    }
    all_status = {

        'Backlog': 0,
        'Blocked': 0,
        'CodeReview': 0,
        'Closed': 0,
        'InProgress': 0,
        'NeedsTriage': 0,
        'Open': 0,
        'ReadyforTesting': 0,
        'ReadyforProduction': 0,
        'ToDo': 0,
    }
    datetotal = {}

    for i in days:
        if str(i) in totals:
            datetotal[str(i)] = totals[str(i)]
        else:
            datetotal[str(i)] = 0

    while len(datetotal) != 31:
        datetotal[len(datetotal) + 1] = 0

    if (project == 'DP') or (project == 'DPExternal'):
        for i, j in components.items():
            cleanString = str(i)
            cleanString = ''.join(e for e in cleanString if e.isalnum())
            if cleanString in all_components.keys():
                all_components[cleanString] = components[i]

    for i, j in status.items():
        cleanString = str(i)
        cleanString = ''.join(e for e in cleanString if e.isalnum())
        if cleanString in all_status.keys():
            all_status[cleanString] = status[i]

    month_jira = list(datetotal.values())
    month_component = list(all_components.values())
    month_status = list(all_status.values())

    ind_time = datetime.datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
    print("Log Jira data to database at {}".format(ind_time))

    try:
        if project == 'DP':
            jira = DP.objects.get(id=1)
        if project == 'DPExternal':
            jira = DPExternal.objects.get(id=1)
        if project == 'DPM':
            jira = DPM.objects.get(id=1)
        if project == 'DPMExternal':
            jira = DPMExternal.objects.get(id=1)
        if project == 'MOB':
            jira = MOB.objects.get(id=1)
        if project == 'MOBExternal':
            jira = MOBExternal.objects.get(id=1)

        jira.One = month_jira[0]
        jira.Two = month_jira[1]
        jira.Three = month_jira[2]
        jira.Four = month_jira[3]
        jira.Five = month_jira[4]
        jira.Six = month_jira[5]
        jira.Seven = month_jira[6]
        jira.Eight = month_jira[7]
        jira.Nine = month_jira[8]
        jira.Ten = month_jira[9]
        jira.Eleven = month_jira[10]
        jira.Twelve = month_jira[11]
        jira.Thirteen = month_jira[12]
        jira.Fourteen = month_jira[13]
        jira.Fifteen = month_jira[14]
        jira.Sixteen = month_jira[15]
        jira.Seventeen = month_jira[16]
        jira.Eighteen = month_jira[17]
        jira.Nineteen = month_jira[18]
        jira.Twenty = month_jira[19]
        jira.Twentyone = month_jira[20]
        jira.Twentytwo = month_jira[21]
        jira.Twentythree = month_jira[22]
        jira.Twentyfour = month_jira[23]
        jira.Twentyfive = month_jira[24]
        jira.Twentysix = month_jira[25]
        jira.Twentyseven = month_jira[26]
        jira.Twentyeight = month_jira[27]
        jira.Twentynine = month_jira[28]
        jira.Thirty = month_jira[29]
        jira.Thirtyone = month_jira[30]
        jira.AccountBilling = month_component[0]
        jira.Analytics = month_component[1]
        jira.BackendInfrastructure = month_component[2]
        jira.CallExperience = month_component[3]
        jira.CallingFeatures = month_component[4]
        jira.ContactCenter = month_component[5]
        jira.CustomerAgentAssist = month_component[6]
        jira.DataInsights = month_component[7]
        jira.DeveloperPlatform = month_component[8]
        jira.Devices = month_component[9]
        jira.DialpadTalk = month_component[10]
        jira.DigitalExperience = month_component[11]
        jira.EngineeringProductivity = month_component[12]
        jira.FrontendInfrastructure = month_component[13]
        jira.Growth = month_component[14]
        jira.Integrations = month_component[15]
        jira.Messaging = month_component[16]
        jira.Mobile = month_component[17]
        jira.ProductionSupport = month_component[18]
        jira.UberConference = month_component[19]
        jira.VoiceIntelligence = month_component[20]
        jira.Website = month_component[21]
        jira.Backlog = month_status[0]
        jira.Blocked = month_status[1]
        jira.CodeReview = month_status[2]
        jira.Closed = month_status[3]
        jira.InProgress = month_status[4]
        jira.NeedsTriage = month_status[5]
        jira.Open = month_status[6]
        jira.ReadyforTesting = month_status[7]
        jira.ReadyforProduction = month_status[8]
        jira.ToDo = month_status[9]
        jira.LastUpdate = ind_time

        jira.save()
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        pass

    return


def save_jira_data():
    year = date.today().year
    month = date.today().month
    num_days = calendar.monthrange(year, month)[1]
    days = [datetime.date(year, month, day) for day in range(1, num_days + 1)]
    next_date = days[-1] + timedelta(days=1)
    url = 'https://dialpad.atlassian.net/rest/api/2/search'
    username = env('DJANGO_JIRA_USER')
    token = env('DJANGO_JIRA_TOKEN')
    #print("Get Data from Jira")
    internal_dp_labels = []
    int_components, int_totals, int_status, int_error_flag = get_dp_data("DP",days[0], days[-1], username, token, next_date,internal_dp_labels,url)
    save_dp_data(days,int_components,int_totals,int_status,'DP')

    time.sleep(2)

    external_dp_labels = ['jira_escalated', 'EAPRequest']
    ext_components, ext_totals, ext_status, ext_error_flag = get_dp_data("DP", days[0], days[-1], username, token, next_date,external_dp_labels,url)
    save_dp_data(days, ext_components, ext_totals, ext_status, 'DPExternal')

    time.sleep(2)

    internal_dp_labels = []
    int_dpm_components, int_dpm_totals, int_dpm_status, int_dpm_error_flag = get_dp_data("UC", days[0], days[-1],username,token,next_date, internal_dp_labels,url)
    save_dp_data(days, int_dpm_components, int_dpm_totals, int_dpm_status, 'DPM')

    time.sleep(2)

    external_dp_labels = ['jira_escalated', 'EAPRequest']
    ext_dpm_components, ext_dpm_totals, ext_dpm_status, ext_dpm_error_flag = get_dp_data("UC", days[0], days[-1],username,token,next_date, external_dp_labels,url)
    save_dp_data(days, ext_dpm_components, ext_dpm_totals, ext_dpm_status, 'DPMExternal')

    internal_dp_labels = []
    int_mob_components, int_mob_totals, int_mob_status, int_mob_error_flag = get_dp_data("MOB", days[0], days[-1],username, token,next_date, internal_dp_labels,url)
    save_dp_data(days, int_mob_components, int_mob_totals, int_mob_status, 'MOB')

    time.sleep(2)

    external_dp_labels = ['jira_escalated', 'EAPRequest']
    ext_mob_components, ext_mob_totals, ext_mob_status, ext_mob_error_flag = get_dp_data("MOB", days[0], days[-1],username, token,next_date, external_dp_labels,url)
    save_dp_data(days, ext_mob_components, ext_mob_totals, ext_mob_status, 'MOBExternal')


    return


