from django.db import models

month_options = (
                ('January','January'),
                ('February','February'),
                ('March','March'),
                ('April','April'),
                ('May','May'),
                ('June','June'),
                ('July','July'),
                ('August','August'),
                ('September','September'),
                ('October','October'),
                ('November','November'),
                ('December','December'),
                )


class DP(models.Model):

    One = models.CharField(max_length=5, blank=True)
    Two = models.CharField(max_length=5, blank=True)
    Three = models.CharField(max_length=5, blank=True)
    Four = models.CharField(max_length=5, blank=True)
    Five = models.CharField(max_length=5, blank=True)
    Six = models.CharField(max_length=5, blank=True)
    Seven = models.CharField(max_length=5, blank=True)
    Eight = models.CharField(max_length=5, blank=True)
    Nine = models.CharField(max_length=5, blank=True)
    Ten = models.CharField(max_length=5, blank=True)
    Eleven = models.CharField(max_length=5, blank=True)
    Twelve = models.CharField(max_length=5, blank=True)
    Thirteen = models.CharField(max_length=5, blank=True)
    Fourteen = models.CharField(max_length=5, blank=True)
    Fifteen = models.CharField(max_length=5, blank=True)
    Sixteen = models.CharField(max_length=5, blank=True)
    Seventeen = models.CharField(max_length=5, blank=True)
    Eighteen = models.CharField(max_length=5, blank=True)
    Nineteen = models.CharField(max_length=5, blank=True)
    Twenty = models.CharField(max_length=5, blank=True)
    Twentyone = models.CharField(max_length=5, blank=True)
    Twentytwo = models.CharField(max_length=5, blank=True)
    Twentythree = models.CharField(max_length=5, blank=True)
    Twentyfour = models.CharField(max_length=5, blank=True)
    Twentyfive = models.CharField(max_length=5, blank=True)
    Twentysix = models.CharField(max_length=5, blank=True)
    Twentyseven = models.CharField(max_length=5, blank=True)
    Twentyeight = models.CharField(max_length=5, blank=True)
    Twentynine = models.CharField(max_length=5, blank=True)
    Thirty = models.CharField(max_length=5, blank=True)
    Thirtyone = models.CharField(max_length=5, blank=True)
    AccountBilling = models.CharField(max_length=5, blank=True)
    Analytics = models.CharField(max_length=5, blank=True)
    BackendInfrastructure = models.CharField(max_length=5, blank=True)
    CallExperience = models.CharField(max_length=5, blank=True)
    CallingFeatures = models.CharField(max_length=5, blank=True)
    ContactCenter = models.CharField(max_length=5, blank=True)
    CustomerAgentAssist = models.CharField(max_length=5, blank=True)
    DataInsights = models.CharField(max_length=5, blank=True)
    DeveloperPlatform = models.CharField(max_length=5, blank=True)
    Devices = models.CharField(max_length=5, blank=True)
    DialpadTalk = models.CharField(max_length=5, blank=True)
    DigitalExperience = models.CharField(max_length=5, blank=True)
    EngineeringProductivity = models.CharField(max_length=5, blank=True)
    FrontendInfrastructure = models.CharField(max_length=5, blank=True)
    Growth = models.CharField(max_length=5, blank=True)
    Integrations = models.CharField(max_length=5, blank=True)
    Messaging = models.CharField(max_length=5, blank=True)
    Mobile = models.CharField(max_length=5, blank=True)
    ProductionSupport = models.CharField(max_length=5, blank=True)
    UberConference = models.CharField(max_length=5, blank=True)
    VoiceIntelligence = models.CharField(max_length=5, blank=True)
    Website = models.CharField(max_length=5, blank=True)
    Backlog = models.CharField(max_length=20, blank=True)
    Blocked = models.CharField(max_length=20, blank=True)
    CodeReview = models.CharField(max_length=20, blank=True)
    Closed = models.CharField(max_length=20, blank=True)
    InProgress = models.CharField(max_length=20, blank=True)
    NeedsTriage = models.CharField(max_length=20, blank=True)
    Open = models.CharField(max_length=20, blank=True)
    ReadyforTesting = models.CharField(max_length=20, blank=True)
    ReadyforProduction = models.CharField(max_length=20, blank=True)
    ToDo = models.CharField(max_length=20, blank=True)
    LastUpdate = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f" {self.id}: {self.One} {self.Two} {self.Three} {self.Four} {self.Five} {self.Six} \
                  {self.Seven}: {self.Eight} {self.Nine} {self.Ten} {self.Eleven} {self.Twelve} {self.Thirteen} \
                  {self.Fourteen}: {self.Fifteen} {self.Sixteen} {self.Seventeen} {self.Eighteen} {self.Nineteen} {self.Twenty} \
                  {self.Twentyone}: {self.Twentytwo} {self.Twentythree} {self.Twentyfour} {self.Twentyfive} {self.Twentysix} {self.Twentyseven} \
                  {self.Twentyeight}: {self.Twentynine} {self.Thirty} {self.Thirtyone} {self.AccountBilling} {self.Analytics} {self.BackendInfrastructure} \
                  {self.CallExperience}: {self.CallingFeatures} {self.ContactCenter} {self.CustomerAgentAssist} {self.DataInsights} {self.DeveloperPlatform} {self.Devices} \
                  {self.DialpadTalk}: {self.DigitalExperience} {self.EngineeringProductivity} {self.FrontendInfrastructure} {self.Growth} {self.Integrations} {self.Messaging} {self.Mobile} \
                  {self.ProductionSupport} {self.UberConference} {self.VoiceIntelligence} {self.Website} {self.Backlog} {self.Blocked} {self.CodeReview} {self.Closed} \
                  {self.InProgress} {self.NeedsTriage} {self.Open} {self.ReadyforTesting} {self.ReadyforProduction} {self.ToDo} {self.LastUpdate}"



class DPExternal(models.Model):

    One = models.CharField(max_length=5, blank=True)
    Two = models.CharField(max_length=5, blank=True)
    Three = models.CharField(max_length=5, blank=True)
    Four = models.CharField(max_length=5, blank=True)
    Five = models.CharField(max_length=5, blank=True)
    Six = models.CharField(max_length=5, blank=True)
    Seven = models.CharField(max_length=5, blank=True)
    Eight = models.CharField(max_length=5, blank=True)
    Nine = models.CharField(max_length=5, blank=True)
    Ten = models.CharField(max_length=5, blank=True)
    Eleven = models.CharField(max_length=5, blank=True)
    Twelve = models.CharField(max_length=5, blank=True)
    Thirteen = models.CharField(max_length=5, blank=True)
    Fourteen = models.CharField(max_length=5, blank=True)
    Fifteen = models.CharField(max_length=5, blank=True)
    Sixteen = models.CharField(max_length=5, blank=True)
    Seventeen = models.CharField(max_length=5, blank=True)
    Eighteen = models.CharField(max_length=5, blank=True)
    Nineteen = models.CharField(max_length=5, blank=True)
    Twenty = models.CharField(max_length=5, blank=True)
    Twentyone = models.CharField(max_length=5, blank=True)
    Twentytwo = models.CharField(max_length=5, blank=True)
    Twentythree = models.CharField(max_length=5, blank=True)
    Twentyfour = models.CharField(max_length=5, blank=True)
    Twentyfive = models.CharField(max_length=5, blank=True)
    Twentysix = models.CharField(max_length=5, blank=True)
    Twentyseven = models.CharField(max_length=5, blank=True)
    Twentyeight = models.CharField(max_length=5, blank=True)
    Twentynine = models.CharField(max_length=5, blank=True)
    Thirty = models.CharField(max_length=5, blank=True)
    Thirtyone = models.CharField(max_length=5, blank=True)
    AccountBilling = models.CharField(max_length=5, blank=True)
    Analytics = models.CharField(max_length=5, blank=True)
    BackendInfrastructure = models.CharField(max_length=5, blank=True)
    CallExperience = models.CharField(max_length=5, blank=True)
    CallingFeatures = models.CharField(max_length=5, blank=True)
    ContactCenter = models.CharField(max_length=5, blank=True)
    CustomerAgentAssist = models.CharField(max_length=5, blank=True)
    DataInsights = models.CharField(max_length=5, blank=True)
    DeveloperPlatform = models.CharField(max_length=5, blank=True)
    Devices = models.CharField(max_length=5, blank=True)
    DialpadTalk = models.CharField(max_length=5, blank=True)
    DigitalExperience = models.CharField(max_length=5, blank=True)
    EngineeringProductivity = models.CharField(max_length=5, blank=True)
    FrontendInfrastructure = models.CharField(max_length=5, blank=True)
    Growth = models.CharField(max_length=5, blank=True)
    Integrations = models.CharField(max_length=5, blank=True)
    Messaging = models.CharField(max_length=5, blank=True)
    Mobile = models.CharField(max_length=5, blank=True)
    ProductionSupport = models.CharField(max_length=5, blank=True)
    UberConference = models.CharField(max_length=5, blank=True)
    VoiceIntelligence = models.CharField(max_length=5, blank=True)
    Website = models.CharField(max_length=5, blank=True)
    Backlog = models.CharField(max_length=20, blank=True)
    Blocked = models.CharField(max_length=20, blank=True)
    CodeReview = models.CharField(max_length=20, blank=True)
    Closed = models.CharField(max_length=20, blank=True)
    InProgress = models.CharField(max_length=20, blank=True)
    NeedsTriage = models.CharField(max_length=20, blank=True)
    Open = models.CharField(max_length=20, blank=True)
    ReadyforTesting = models.CharField(max_length=20, blank=True)
    ReadyforProduction = models.CharField(max_length=20, blank=True)
    ToDo = models.CharField(max_length=20, blank=True)
    LastUpdate = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f" {self.id}: {self.One} {self.Two} {self.Three} {self.Four} {self.Five} {self.Six} \
                  {self.Seven}: {self.Eight} {self.Nine} {self.Ten} {self.Eleven} {self.Twelve} {self.Thirteen} \
                  {self.Fourteen}: {self.Fifteen} {self.Sixteen} {self.Seventeen} {self.Eighteen} {self.Nineteen} {self.Twenty} \
                  {self.Twentyone}: {self.Twentytwo} {self.Twentythree} {self.Twentyfour} {self.Twentyfive} {self.Twentysix} {self.Twentyseven} \
                  {self.Twentyeight}: {self.Twentynine} {self.Thirty} {self.Thirtyone} {self.AccountBilling} {self.Analytics} {self.BackendInfrastructure} \
                  {self.CallExperience}: {self.CallingFeatures} {self.ContactCenter} {self.CustomerAgentAssist} {self.DataInsights} {self.DeveloperPlatform} {self.Devices} \
                  {self.DialpadTalk}: {self.DigitalExperience} {self.EngineeringProductivity} {self.FrontendInfrastructure} {self.Growth} {self.Integrations} {self.Messaging} {self.Mobile} \
                  {self.ProductionSupport} {self.UberConference} {self.VoiceIntelligence} {self.Website} {self.Backlog} {self.Blocked} {self.CodeReview} {self.Closed} \
                  {self.InProgress} {self.NeedsTriage} {self.Open} {self.ReadyforTesting} {self.ReadyforProduction} {self.ToDo} {self.LastUpdate}"



class DPM(models.Model):

    One = models.CharField(max_length=5, blank=True)
    Two = models.CharField(max_length=5, blank=True)
    Three = models.CharField(max_length=5, blank=True)
    Four = models.CharField(max_length=5, blank=True)
    Five = models.CharField(max_length=5, blank=True)
    Six = models.CharField(max_length=5, blank=True)
    Seven = models.CharField(max_length=5, blank=True)
    Eight = models.CharField(max_length=5, blank=True)
    Nine = models.CharField(max_length=5, blank=True)
    Ten = models.CharField(max_length=5, blank=True)
    Eleven = models.CharField(max_length=5, blank=True)
    Twelve = models.CharField(max_length=5, blank=True)
    Thirteen = models.CharField(max_length=5, blank=True)
    Fourteen = models.CharField(max_length=5, blank=True)
    Fifteen = models.CharField(max_length=5, blank=True)
    Sixteen = models.CharField(max_length=5, blank=True)
    Seventeen = models.CharField(max_length=5, blank=True)
    Eighteen = models.CharField(max_length=5, blank=True)
    Nineteen = models.CharField(max_length=5, blank=True)
    Twenty = models.CharField(max_length=5, blank=True)
    Twentyone = models.CharField(max_length=5, blank=True)
    Twentytwo = models.CharField(max_length=5, blank=True)
    Twentythree = models.CharField(max_length=5, blank=True)
    Twentyfour = models.CharField(max_length=5, blank=True)
    Twentyfive = models.CharField(max_length=5, blank=True)
    Twentysix = models.CharField(max_length=5, blank=True)
    Twentyseven = models.CharField(max_length=5, blank=True)
    Twentyeight = models.CharField(max_length=5, blank=True)
    Twentynine = models.CharField(max_length=5, blank=True)
    Thirty = models.CharField(max_length=5, blank=True)
    Thirtyone = models.CharField(max_length=5, blank=True)
    AccountBilling = models.CharField(max_length=5, blank=True)
    Analytics = models.CharField(max_length=5, blank=True)
    BackendInfrastructure = models.CharField(max_length=5, blank=True)
    CallExperience = models.CharField(max_length=5, blank=True)
    CallingFeatures = models.CharField(max_length=5, blank=True)
    ContactCenter = models.CharField(max_length=5, blank=True)
    CustomerAgentAssist = models.CharField(max_length=5, blank=True)
    DataInsights = models.CharField(max_length=5, blank=True)
    DeveloperPlatform = models.CharField(max_length=5, blank=True)
    Devices = models.CharField(max_length=5, blank=True)
    DialpadTalk = models.CharField(max_length=5, blank=True)
    DigitalExperience = models.CharField(max_length=5, blank=True)
    EngineeringProductivity = models.CharField(max_length=5, blank=True)
    FrontendInfrastructure = models.CharField(max_length=5, blank=True)
    Growth = models.CharField(max_length=5, blank=True)
    Integrations = models.CharField(max_length=5, blank=True)
    Messaging = models.CharField(max_length=5, blank=True)
    Mobile = models.CharField(max_length=5, blank=True)
    ProductionSupport = models.CharField(max_length=5, blank=True)
    UberConference = models.CharField(max_length=5, blank=True)
    VoiceIntelligence = models.CharField(max_length=5, blank=True)
    Website = models.CharField(max_length=5, blank=True)
    Backlog = models.CharField(max_length=20, blank=True)
    Blocked = models.CharField(max_length=20, blank=True)
    CodeReview = models.CharField(max_length=20, blank=True)
    Closed = models.CharField(max_length=20, blank=True)
    InProgress = models.CharField(max_length=20, blank=True)
    NeedsTriage = models.CharField(max_length=20, blank=True)
    Open = models.CharField(max_length=20, blank=True)
    ReadyforTesting = models.CharField(max_length=20, blank=True)
    ReadyforProduction = models.CharField(max_length=20, blank=True)
    ToDo = models.CharField(max_length=20, blank=True)
    LastUpdate = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f" {self.id}: {self.One} {self.Two} {self.Three} {self.Four} {self.Five} {self.Six} \
                  {self.Seven}: {self.Eight} {self.Nine} {self.Ten} {self.Eleven} {self.Twelve} {self.Thirteen} \
                  {self.Fourteen}: {self.Fifteen} {self.Sixteen} {self.Seventeen} {self.Eighteen} {self.Nineteen} {self.Twenty} \
                  {self.Twentyone}: {self.Twentytwo} {self.Twentythree} {self.Twentyfour} {self.Twentyfive} {self.Twentysix} {self.Twentyseven} \
                  {self.Twentyeight}: {self.Twentynine} {self.Thirty} {self.Thirtyone} {self.AccountBilling} {self.Analytics} {self.BackendInfrastructure} \
                  {self.CallExperience}: {self.CallingFeatures} {self.ContactCenter} {self.CustomerAgentAssist} {self.DataInsights} {self.DeveloperPlatform} {self.Devices} \
                  {self.DialpadTalk}: {self.DigitalExperience} {self.EngineeringProductivity} {self.FrontendInfrastructure} {self.Growth} {self.Integrations} {self.Messaging} {self.Mobile} \
                  {self.ProductionSupport} {self.UberConference} {self.VoiceIntelligence} {self.Website} {self.Backlog} {self.Blocked} {self.CodeReview} {self.Closed} \
                  {self.InProgress} {self.NeedsTriage} {self.Open} {self.ReadyforTesting} {self.ReadyforProduction} {self.ToDo} {self.LastUpdate}"



class DPMExternal(models.Model):

    One = models.CharField(max_length=5, blank=True)
    Two = models.CharField(max_length=5, blank=True)
    Three = models.CharField(max_length=5, blank=True)
    Four = models.CharField(max_length=5, blank=True)
    Five = models.CharField(max_length=5, blank=True)
    Six = models.CharField(max_length=5, blank=True)
    Seven = models.CharField(max_length=5, blank=True)
    Eight = models.CharField(max_length=5, blank=True)
    Nine = models.CharField(max_length=5, blank=True)
    Ten = models.CharField(max_length=5, blank=True)
    Eleven = models.CharField(max_length=5, blank=True)
    Twelve = models.CharField(max_length=5, blank=True)
    Thirteen = models.CharField(max_length=5, blank=True)
    Fourteen = models.CharField(max_length=5, blank=True)
    Fifteen = models.CharField(max_length=5, blank=True)
    Sixteen = models.CharField(max_length=5, blank=True)
    Seventeen = models.CharField(max_length=5, blank=True)
    Eighteen = models.CharField(max_length=5, blank=True)
    Nineteen = models.CharField(max_length=5, blank=True)
    Twenty = models.CharField(max_length=5, blank=True)
    Twentyone = models.CharField(max_length=5, blank=True)
    Twentytwo = models.CharField(max_length=5, blank=True)
    Twentythree = models.CharField(max_length=5, blank=True)
    Twentyfour = models.CharField(max_length=5, blank=True)
    Twentyfive = models.CharField(max_length=5, blank=True)
    Twentysix = models.CharField(max_length=5, blank=True)
    Twentyseven = models.CharField(max_length=5, blank=True)
    Twentyeight = models.CharField(max_length=5, blank=True)
    Twentynine = models.CharField(max_length=5, blank=True)
    Thirty = models.CharField(max_length=5, blank=True)
    Thirtyone = models.CharField(max_length=5, blank=True)
    AccountBilling = models.CharField(max_length=5, blank=True)
    Analytics = models.CharField(max_length=5, blank=True)
    BackendInfrastructure = models.CharField(max_length=5, blank=True)
    CallExperience = models.CharField(max_length=5, blank=True)
    CallingFeatures = models.CharField(max_length=5, blank=True)
    ContactCenter = models.CharField(max_length=5, blank=True)
    CustomerAgentAssist = models.CharField(max_length=5, blank=True)
    DataInsights = models.CharField(max_length=5, blank=True)
    DeveloperPlatform = models.CharField(max_length=5, blank=True)
    Devices = models.CharField(max_length=5, blank=True)
    DialpadTalk = models.CharField(max_length=5, blank=True)
    DigitalExperience = models.CharField(max_length=5, blank=True)
    EngineeringProductivity = models.CharField(max_length=5, blank=True)
    FrontendInfrastructure = models.CharField(max_length=5, blank=True)
    Growth = models.CharField(max_length=5, blank=True)
    Integrations = models.CharField(max_length=5, blank=True)
    Messaging = models.CharField(max_length=5, blank=True)
    Mobile = models.CharField(max_length=5, blank=True)
    ProductionSupport = models.CharField(max_length=5, blank=True)
    UberConference = models.CharField(max_length=5, blank=True)
    VoiceIntelligence = models.CharField(max_length=5, blank=True)
    Website = models.CharField(max_length=5, blank=True)
    Backlog = models.CharField(max_length=20, blank=True)
    Blocked = models.CharField(max_length=20, blank=True)
    CodeReview = models.CharField(max_length=20, blank=True)
    Closed = models.CharField(max_length=20, blank=True)
    InProgress = models.CharField(max_length=20, blank=True)
    NeedsTriage = models.CharField(max_length=20, blank=True)
    Open = models.CharField(max_length=20, blank=True)
    ReadyforTesting = models.CharField(max_length=20, blank=True)
    ReadyforProduction = models.CharField(max_length=20, blank=True)
    ToDo = models.CharField(max_length=20, blank=True)
    LastUpdate = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f" {self.id}: {self.One} {self.Two} {self.Three} {self.Four} {self.Five} {self.Six} \
                  {self.Seven}: {self.Eight} {self.Nine} {self.Ten} {self.Eleven} {self.Twelve} {self.Thirteen} \
                  {self.Fourteen}: {self.Fifteen} {self.Sixteen} {self.Seventeen} {self.Eighteen} {self.Nineteen} {self.Twenty} \
                  {self.Twentyone}: {self.Twentytwo} {self.Twentythree} {self.Twentyfour} {self.Twentyfive} {self.Twentysix} {self.Twentyseven} \
                  {self.Twentyeight}: {self.Twentynine} {self.Thirty} {self.Thirtyone} {self.AccountBilling} {self.Analytics} {self.BackendInfrastructure} \
                  {self.CallExperience}: {self.CallingFeatures} {self.ContactCenter} {self.CustomerAgentAssist} {self.DataInsights} {self.DeveloperPlatform} {self.Devices} \
                  {self.DialpadTalk}: {self.DigitalExperience} {self.EngineeringProductivity} {self.FrontendInfrastructure} {self.Growth} {self.Integrations} {self.Messaging} {self.Mobile} \
                  {self.ProductionSupport} {self.UberConference} {self.VoiceIntelligence} {self.Website} {self.Backlog} {self.Blocked} {self.CodeReview} {self.Closed} \
                  {self.InProgress} {self.NeedsTriage} {self.Open} {self.ReadyforTesting} {self.ReadyforProduction} {self.ToDo} {self.LastUpdate}"



class MOB(models.Model):

    One = models.CharField(max_length=5, blank=True)
    Two = models.CharField(max_length=5, blank=True)
    Three = models.CharField(max_length=5, blank=True)
    Four = models.CharField(max_length=5, blank=True)
    Five = models.CharField(max_length=5, blank=True)
    Six = models.CharField(max_length=5, blank=True)
    Seven = models.CharField(max_length=5, blank=True)
    Eight = models.CharField(max_length=5, blank=True)
    Nine = models.CharField(max_length=5, blank=True)
    Ten = models.CharField(max_length=5, blank=True)
    Eleven = models.CharField(max_length=5, blank=True)
    Twelve = models.CharField(max_length=5, blank=True)
    Thirteen = models.CharField(max_length=5, blank=True)
    Fourteen = models.CharField(max_length=5, blank=True)
    Fifteen = models.CharField(max_length=5, blank=True)
    Sixteen = models.CharField(max_length=5, blank=True)
    Seventeen = models.CharField(max_length=5, blank=True)
    Eighteen = models.CharField(max_length=5, blank=True)
    Nineteen = models.CharField(max_length=5, blank=True)
    Twenty = models.CharField(max_length=5, blank=True)
    Twentyone = models.CharField(max_length=5, blank=True)
    Twentytwo = models.CharField(max_length=5, blank=True)
    Twentythree = models.CharField(max_length=5, blank=True)
    Twentyfour = models.CharField(max_length=5, blank=True)
    Twentyfive = models.CharField(max_length=5, blank=True)
    Twentysix = models.CharField(max_length=5, blank=True)
    Twentyseven = models.CharField(max_length=5, blank=True)
    Twentyeight = models.CharField(max_length=5, blank=True)
    Twentynine = models.CharField(max_length=5, blank=True)
    Thirty = models.CharField(max_length=5, blank=True)
    Thirtyone = models.CharField(max_length=5, blank=True)
    AccountBilling = models.CharField(max_length=5, blank=True)
    Analytics = models.CharField(max_length=5, blank=True)
    BackendInfrastructure = models.CharField(max_length=5, blank=True)
    CallExperience = models.CharField(max_length=5, blank=True)
    CallingFeatures = models.CharField(max_length=5, blank=True)
    ContactCenter = models.CharField(max_length=5, blank=True)
    CustomerAgentAssist = models.CharField(max_length=5, blank=True)
    DataInsights = models.CharField(max_length=5, blank=True)
    DeveloperPlatform = models.CharField(max_length=5, blank=True)
    Devices = models.CharField(max_length=5, blank=True)
    DialpadTalk = models.CharField(max_length=5, blank=True)
    DigitalExperience = models.CharField(max_length=5, blank=True)
    EngineeringProductivity = models.CharField(max_length=5, blank=True)
    FrontendInfrastructure = models.CharField(max_length=5, blank=True)
    Growth = models.CharField(max_length=5, blank=True)
    Integrations = models.CharField(max_length=5, blank=True)
    Messaging = models.CharField(max_length=5, blank=True)
    Mobile = models.CharField(max_length=5, blank=True)
    ProductionSupport = models.CharField(max_length=5, blank=True)
    UberConference = models.CharField(max_length=5, blank=True)
    VoiceIntelligence = models.CharField(max_length=5, blank=True)
    Website = models.CharField(max_length=5, blank=True)
    Backlog = models.CharField(max_length=20, blank=True)
    Blocked = models.CharField(max_length=20, blank=True)
    CodeReview = models.CharField(max_length=20, blank=True)
    Closed = models.CharField(max_length=20, blank=True)
    InProgress = models.CharField(max_length=20, blank=True)
    NeedsTriage = models.CharField(max_length=20, blank=True)
    Open = models.CharField(max_length=20, blank=True)
    ReadyforTesting = models.CharField(max_length=20, blank=True)
    ReadyforProduction = models.CharField(max_length=20, blank=True)
    ToDo = models.CharField(max_length=20, blank=True)
    LastUpdate = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f" {self.id}: {self.One} {self.Two} {self.Three} {self.Four} {self.Five} {self.Six} \
                  {self.Seven}: {self.Eight} {self.Nine} {self.Ten} {self.Eleven} {self.Twelve} {self.Thirteen} \
                  {self.Fourteen}: {self.Fifteen} {self.Sixteen} {self.Seventeen} {self.Eighteen} {self.Nineteen} {self.Twenty} \
                  {self.Twentyone}: {self.Twentytwo} {self.Twentythree} {self.Twentyfour} {self.Twentyfive} {self.Twentysix} {self.Twentyseven} \
                  {self.Twentyeight}: {self.Twentynine} {self.Thirty} {self.Thirtyone} {self.AccountBilling} {self.Analytics} {self.BackendInfrastructure} \
                  {self.CallExperience}: {self.CallingFeatures} {self.ContactCenter} {self.CustomerAgentAssist} {self.DataInsights} {self.DeveloperPlatform} {self.Devices} \
                  {self.DialpadTalk}: {self.DigitalExperience} {self.EngineeringProductivity} {self.FrontendInfrastructure} {self.Growth} {self.Integrations} {self.Messaging} {self.Mobile} \
                  {self.ProductionSupport} {self.UberConference} {self.VoiceIntelligence} {self.Website} {self.Backlog} {self.Blocked} {self.CodeReview} {self.Closed} \
                  {self.InProgress} {self.NeedsTriage} {self.Open} {self.ReadyforTesting} {self.ReadyforProduction} {self.ToDo} {self.LastUpdate}"



class MOBExternal(models.Model):

    One = models.CharField(max_length=5, blank=True)
    Two = models.CharField(max_length=5, blank=True)
    Three = models.CharField(max_length=5, blank=True)
    Four = models.CharField(max_length=5, blank=True)
    Five = models.CharField(max_length=5, blank=True)
    Six = models.CharField(max_length=5, blank=True)
    Seven = models.CharField(max_length=5, blank=True)
    Eight = models.CharField(max_length=5, blank=True)
    Nine = models.CharField(max_length=5, blank=True)
    Ten = models.CharField(max_length=5, blank=True)
    Eleven = models.CharField(max_length=5, blank=True)
    Twelve = models.CharField(max_length=5, blank=True)
    Thirteen = models.CharField(max_length=5, blank=True)
    Fourteen = models.CharField(max_length=5, blank=True)
    Fifteen = models.CharField(max_length=5, blank=True)
    Sixteen = models.CharField(max_length=5, blank=True)
    Seventeen = models.CharField(max_length=5, blank=True)
    Eighteen = models.CharField(max_length=5, blank=True)
    Nineteen = models.CharField(max_length=5, blank=True)
    Twenty = models.CharField(max_length=5, blank=True)
    Twentyone = models.CharField(max_length=5, blank=True)
    Twentytwo = models.CharField(max_length=5, blank=True)
    Twentythree = models.CharField(max_length=5, blank=True)
    Twentyfour = models.CharField(max_length=5, blank=True)
    Twentyfive = models.CharField(max_length=5, blank=True)
    Twentysix = models.CharField(max_length=5, blank=True)
    Twentyseven = models.CharField(max_length=5, blank=True)
    Twentyeight = models.CharField(max_length=5, blank=True)
    Twentynine = models.CharField(max_length=5, blank=True)
    Thirty = models.CharField(max_length=5, blank=True)
    Thirtyone = models.CharField(max_length=5, blank=True)
    AccountBilling = models.CharField(max_length=5, blank=True)
    Analytics = models.CharField(max_length=5, blank=True)
    BackendInfrastructure = models.CharField(max_length=5, blank=True)
    CallExperience = models.CharField(max_length=5, blank=True)
    CallingFeatures = models.CharField(max_length=5, blank=True)
    ContactCenter = models.CharField(max_length=5, blank=True)
    CustomerAgentAssist = models.CharField(max_length=5, blank=True)
    DataInsights = models.CharField(max_length=5, blank=True)
    DeveloperPlatform = models.CharField(max_length=5, blank=True)
    Devices = models.CharField(max_length=5, blank=True)
    DialpadTalk = models.CharField(max_length=5, blank=True)
    DigitalExperience = models.CharField(max_length=5, blank=True)
    EngineeringProductivity = models.CharField(max_length=5, blank=True)
    FrontendInfrastructure = models.CharField(max_length=5, blank=True)
    Growth = models.CharField(max_length=5, blank=True)
    Integrations = models.CharField(max_length=5, blank=True)
    Messaging = models.CharField(max_length=5, blank=True)
    Mobile = models.CharField(max_length=5, blank=True)
    ProductionSupport = models.CharField(max_length=5, blank=True)
    UberConference = models.CharField(max_length=5, blank=True)
    VoiceIntelligence = models.CharField(max_length=5, blank=True)
    Website = models.CharField(max_length=5, blank=True)
    Backlog = models.CharField(max_length=20, blank=True)
    Blocked = models.CharField(max_length=20, blank=True)
    CodeReview = models.CharField(max_length=20, blank=True)
    Closed = models.CharField(max_length=20, blank=True)
    InProgress = models.CharField(max_length=20, blank=True)
    NeedsTriage = models.CharField(max_length=20, blank=True)
    Open = models.CharField(max_length=20, blank=True)
    ReadyforTesting = models.CharField(max_length=20, blank=True)
    ReadyforProduction = models.CharField(max_length=20, blank=True)
    ToDo = models.CharField(max_length=20, blank=True)
    LastUpdate = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f" {self.id}: {self.One} {self.Two} {self.Three} {self.Four} {self.Five} {self.Six} \
                  {self.Seven}: {self.Eight} {self.Nine} {self.Ten} {self.Eleven} {self.Twelve} {self.Thirteen} \
                  {self.Fourteen}: {self.Fifteen} {self.Sixteen} {self.Seventeen} {self.Eighteen} {self.Nineteen} {self.Twenty} \
                  {self.Twentyone}: {self.Twentytwo} {self.Twentythree} {self.Twentyfour} {self.Twentyfive} {self.Twentysix} {self.Twentyseven} \
                  {self.Twentyeight}: {self.Twentynine} {self.Thirty} {self.Thirtyone} {self.AccountBilling} {self.Analytics} {self.BackendInfrastructure} \
                  {self.CallExperience}: {self.CallingFeatures} {self.ContactCenter} {self.CustomerAgentAssist} {self.DataInsights} {self.DeveloperPlatform} {self.Devices} \
                  {self.DialpadTalk}: {self.DigitalExperience} {self.EngineeringProductivity} {self.FrontendInfrastructure} {self.Growth} {self.Integrations} {self.Messaging} {self.Mobile} \
                  {self.ProductionSupport} {self.UberConference} {self.VoiceIntelligence} {self.Website} {self.Backlog} {self.Blocked} {self.CodeReview} {self.Closed} \
                  {self.InProgress} {self.NeedsTriage} {self.Open} {self.ReadyforTesting} {self.ReadyforProduction} {self.ToDo} {self.LastUpdate}"


class ImpactAreas(models.Model):
    Area = models.CharField(max_length=30, blank=True)
    Number = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Area} {self.Number}:"
    
class ImpactApplications(models.Model):
    Application = models.CharField(max_length=30, blank=True)
    Number = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Application} {self.Number}:"

class EDACurrentMonth(models.Model):
    EDAType = models.CharField(max_length=30, blank=True)
    Number = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return f" {self.id}: {self.EDAType} {self.Number}:"
    
class EDAPreviousMonth(models.Model):
    EDAType = models.CharField(max_length=30, blank=True)
    Number = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return f" {self.id}: {self.EDAType} {self.Number}:"

class EDALearnings(models.Model):
    ActionItem = models.CharField(max_length=1000, blank=True)
    PreviousMonth = models.CharField(max_length=15, choices=month_options, blank=True)
    CurrentMonth = models.CharField(max_length=15, choices=month_options, blank=True)

    def __str__(self):
        return f"{self.id}: {self.ActionItem} {self.PreviousMonth} {self.CurrentMonth}"