from django import forms
from .models import DP,DPExternal,DPM,DPMExternal,MOB,MOBExternal,ImpactAreas,ImpactApplications,EDACurrentMonth,EDAPreviousMonth,EDALearnings

class DPForm(forms.ModelForm):
    class Meta:
        model: DP
        fields: ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen',\
                 'Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen','Twenty','Twentyone','Twentytwo',\
                 'Twentythree','Twentyfour','Twentyfive','Twentysix','Twentyseven','Twentyeight','Twentynine','Thirty',\
                 'Thirtyone','AccountBilling','Analytics','BackendInfrastructure','CallExperience','CallingFeatures',\
                 'ContactCenter','CustomerAgentAssist','DataInsights','DeveloperPlatform','Devices','DialpadTalk',\
                 'DigitalExperience','EngineeringProductivity','FrontendInfrastructure','Growth','Integrations',\
                 'Messaging','Mobile','ProductionSupport','UberConference','VoiceIntelligence','Website', \
                 'Backlog','Blocked','CodeReview','Closed','InProgress','NeedsTriage','Open','ReadyforTesting',\
                 'ReadyforProduction','ToDo', 'LastUpdate']

class DPExternalForm(forms.ModelForm):
    class Meta:
        model: DPExternal
        fields: ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen',\
                 'Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen','Twenty','Twentyone','Twentytwo',\
                 'Twentythree','Twentyfour','Twentyfive','Twentysix','Twentyseven','Twentyeight','Twentynine','Thirty',\
                 'Thirtyone','AccountBilling','Analytics','BackendInfrastructure','CallExperience','CallingFeatures',\
                 'ContactCenter','CustomerAgentAssist','DataInsights','DeveloperPlatform','Devices','DialpadTalk',\
                 'DigitalExperience','EngineeringProductivity','FrontendInfrastructure','Growth','Integrations',\
                 'Messaging','Mobile','ProductionSupport','UberConference','VoiceIntelligence','Website', \
                 'Backlog','Blocked','CodeReview','Closed','InProgress','NeedsTriage','Open','ReadyforTesting',\
                 'ReadyforProduction','ToDo' , 'LastUpdate']

class DPMForm(forms.ModelForm):
    class Meta:
        model: DPM
        fields: ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen',\
                 'Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen','Twenty','Twentyone','Twentytwo',\
                 'Twentythree','Twentyfour','Twentyfive','Twentysix','Twentyseven','Twentyeight','Twentynine','Thirty',\
                 'Thirtyone','AccountBilling','Analytics','BackendInfrastructure','CallExperience','CallingFeatures',\
                 'ContactCenter','CustomerAgentAssist','DataInsights','DeveloperPlatform','Devices','DialpadTalk',\
                 'DigitalExperience','EngineeringProductivity','FrontendInfrastructure','Growth','Integrations',\
                 'Messaging','Mobile','ProductionSupport','UberConference','VoiceIntelligence','Website', \
                 'Backlog','Blocked','CodeReview','Closed','InProgress','NeedsTriage','Open','ReadyforTesting',\
                 'ReadyforProduction','ToDo', 'LastUpdate']

class DPMExternalForm(forms.ModelForm):
    class Meta:
        model: DPMExternal
        fields: ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen',\
                 'Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen','Twenty','Twentyone','Twentytwo',\
                 'Twentythree','Twentyfour','Twentyfive','Twentysix','Twentyseven','Twentyeight','Twentynine','Thirty',\
                 'Thirtyone','AccountBilling','Analytics','BackendInfrastructure','CallExperience','CallingFeatures',\
                 'ContactCenter','CustomerAgentAssist','DataInsights','DeveloperPlatform','Devices','DialpadTalk',\
                 'DigitalExperience','EngineeringProductivity','FrontendInfrastructure','Growth','Integrations',\
                 'Messaging','Mobile','ProductionSupport','UberConference','VoiceIntelligence','Website', \
                 'Backlog','Blocked','CodeReview','Closed','InProgress','NeedsTriage','Open','ReadyforTesting',\
                 'ReadyforProduction','ToDo', 'LastUpdate']

class MOBForm(forms.ModelForm):
    class Meta:
        model: MOB
        fields: ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen',\
                 'Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen','Twenty','Twentyone','Twentytwo',\
                 'Twentythree','Twentyfour','Twentyfive','Twentysix','Twentyseven','Twentyeight','Twentynine','Thirty',\
                 'Thirtyone','AccountBilling','Analytics','BackendInfrastructure','CallExperience','CallingFeatures',\
                 'ContactCenter','CustomerAgentAssist','DataInsights','DeveloperPlatform','Devices','DialpadTalk',\
                 'DigitalExperience','EngineeringProductivity','FrontendInfrastructure','Growth','Integrations',\
                 'Messaging','Mobile','ProductionSupport','UberConference','VoiceIntelligence','Website', \
                 'Backlog','Blocked','CodeReview','Closed','InProgress','NeedsTriage','Open','ReadyforTesting',\
                 'ReadyforProduction','ToDo', 'LastUpdate']

class MOBExternalForm(forms.ModelForm):
    class Meta:
        model: MOBExternal
        fields: ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen',\
                 'Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen','Twenty','Twentyone','Twentytwo',\
                 'Twentythree','Twentyfour','Twentyfive','Twentysix','Twentyseven','Twentyeight','Twentynine','Thirty',\
                 'Thirtyone','AccountBilling','Analytics','BackendInfrastructure','CallExperience','CallingFeatures',\
                 'ContactCenter','CustomerAgentAssist','DataInsights','DeveloperPlatform','Devices','DialpadTalk',\
                 'DigitalExperience','EngineeringProductivity','FrontendInfrastructure','Growth','Integrations',\
                 'Messaging','Mobile','ProductionSupport','UberConference','VoiceIntelligence','Website', \
                 'Backlog','Blocked','CodeReview','Closed','InProgress','NeedsTriage','Open','ReadyforTesting',\
                 'ReadyforProduction','ToDo', 'LastUpdate']

class ImpactAreaForm(forms.ModelForm):
    class Meta:
        model: ImpactAreas
        fields: ['Area','Number']
        
class ImpactApplicationForm(forms.ModelForm):
    class Meta:
        model: ImpactApplications
        fields: ['Application','Number']
        
class EDACurrentMonthForm(forms.ModelForm):
    class Meta:
        model: EDACurrentMonth
        fields: ['EDAType','Number']
        
class EDAPreviousMonthForm(forms.ModelForm):
    class Meta:
        model: EDAPreviousMonth
        fields: ['EDAType','Number']
        
class EDALearningsForm(forms.ModelForm):
    class Meta:
        model: EDALearnings
        fields: ['ActionItem','PreviousMonth','CurrentMonth']
