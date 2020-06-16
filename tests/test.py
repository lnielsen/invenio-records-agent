
obj = RecordController.create(data, ctx=....)


class RDMRecord(PIDVersionedRecord):
    pass

class RDMDraft(PIDVersionedRecord):
    pass

# 1) Create a record without all the fuss


obj.mint('doi','')


obj = RecordDatastore.create(data, context=)




DepositAP


obj = RDMDraft.create(...)
obj.publish()

RDMRecord.restore(

)


RecordMediator.invoelRestoreAction()


RecordState()

RecordDirector.create(
    id=None,

)

#
# State
#
class TombstoneState:
    pid =
    record =
    bucket =

class RecordState:
    pid =
    record =
    bucket =

class DraftState:
    pid =
    record =que
    bucket =

class SearchResultState:
    hits =
    params =


class QueryInterpreter:
    def __init__(**kwargs):
        self.params = **kwargs

    def apply(s):
        return s.search(Q('query_string', 'q'))


class RDMRecord(Record):
    __table__ = 'rdmrecords_metadata'



class RDMRecordAgent(RecordAgent):
    record_class = RDMRecord
    search_class = RecordSearch
    resolver = PIDResolver
    query_interpreter = QueryInterpreter(
        parser=ESParser,
        sort_options={},
        aggregations={},
    )
    permission_policy = MyPermissionPolicy
    commands = {
        'publish': PublishCommand(
            SpamCheckCommand(),
            RunRecord()
            Noftify()
            PackageSIPCommand(async_=true),
        ),
        'restore': RestoreCommand,
        'new-version': NewVersionCommand,
    }
    schemas = [
        'v1': schema
    ]


#
#
#

from invenio_rdm_records import RDMRecordAgent

#
# Retrieve a record
#

r = RDMRecordAgent.get('abcde-12345', identity=g.identity)
    # resolve pid, tombstone page,
    # check permission against what?
    # retrieve record
r.revision_id
r.updated
r.record
r.id
r.pids
r.tombstone
r.versions

#
# Searching
#

# Getting a search class.
s = RDMRecordAgent.create_search(versions=True, identity=my_identity)
    # Make a new Elasticsearch DSL with the right filters.
    # Apply permission policy from invenio-records-permissions
s = s.query(Q('query_string', query='+created:[2020-06-11 TO 2020-06-12] +owners:>104000')).sort('owners')
q.apply(s)

# Querying
res_state = RDMRecordAgent.query(
    q='+created:[2020-06-11 TO 2020-06-12] +owners:>104000',
    from_idx=0,
    to_idx=500,
    sort=['-created','authors.full_name'],
    filters={},
    aggregations=False,
    search_params={
        identity=my_id,
        versions=True,
    }
)

#
# Create
#
draftstate = RDMRecordMediator.create(
    # id='avfg7a-876dfs',
    owners=[],
    acls=dict(
        readers=dict(
            users=[1, 434, 234, 22525],
            roles=[2,3,4],
            systemroles=[14,3],
        ),
        curators=dict(
            users=[1,],
            roles=[2,3,4],
            systemroles=[14,3],
        ),
        admins=dict(
            users=[1, 434, 234, 22525],
            roles=[2,3,4],
            systemroles=[14,3],
        ),
    ),
    metadata_version='v1',
    metadata=dict(
        resource_type=dict(type='text', subtype='article'),
        title='Test',
        description='This is an awesome description of a record.',
        publication_date='2020-02-23',
        creators=[
            dict(family_name='Nielsen', given_names='Lars Holm', identifers=dict(orcid='8152-4323-3424-4342'), type='personal',
                 affiliations=[dict(name='CERN', identifiers=dict(ror='8152-4323-3424-4342')])
        ]
    ),
    with_bucket=True,
    with_files=False,
    expires=utcnow()+timedelta(days=300)
    identity=my_identity,
)

draftstate.id
draftstate.pids
draftstate.revision_id
draftstate.record
draftstate.fork
draftstate.acls
draftstate.bucket
draftstate.files.add()

#
# Update
#
draftstate = RDMDraftsAgent.update(
    '12345-12345',
    acls={},
    metadata={},
    revision_id=...
    force=True,
    identity=my_identity
)

#
# Publish
#
RDMDraftsAgent.publish()

recordstate = RDMDraftsAgent.run(
    'publish',
    '12345-12345',
    identity=my_id,
    mint_pids=True
)

#
# Delete
#

# Discard
recordstate = RDMDraftsAgent.delete(
    '12345-12345',
    identity=my_id,
    register_doi
)

# Delete
recordstate = RDMDraftsAgent.run(
    'delete',
    '12345-12345',
    identity=my_id,
    tombstone=
    files=
)


#
# New version
#

draftstate = RDMRecordAgent.new_version('12345-12345')

drafts =  RDMDraftsAgent.drafts()




# Use cases:,
# - search
# - get a record
# - create a record/draft
# - delete a record
# - restore a record
# - edit a record
# - discard an edit (draft)
# -


# - actions: publish, restore
#


class MultiCommand:
    def __init__(self, state, commands):
        self.commands = commands
        self.state = state

    def run(self):
        for c in self.commands:
            state = c.run(state)


MultiCommand(
    spam_command
)

(-)RecordAdapter +
+ RecordAgent
- RecordAPI +
- RecordArchitect
RecordAssistant
+ RecordBroker +
- RecordBuilder
- RecordCompiler
RecordController +
RecordCoordinator
- RecordCreator
- RecordDirector
- RecordEngineer
- RecordFacade
- RecordHandler
- RecordHelper +
- RecordMaker
- RecordMediator
+ RecordModerator
- RecordProducer
+ RecordStrategy
- RecordSupervisor
- RecordSystem +
- RecordWorker
RecordWorkflow +

