# generate-gitlab-ci.py
import json

SERVICES = (
    "foo",
    "bar",
    "baz",
)

def make_service(name):
    return {
        "build-%s" % name: {
            "stage": "build",
            "script":[
                "echo Build %s" % name,
            ],
        },
        "test-%s" % name: {
            "stage": "test",
            "script":[
                "echo Build %s" % name,
            ],
            "needs": ["build-%s" % name]
        },
        "deploy-%s" % name: {
            "stage": "deploy",
            "script":[
                "echo Deploy %s" % name,
            ],
            "needs": ["test-%s" % name],
        }
    }

with open(".gitlab-ci.yml", "w") as f:
    pipeline = {}
    pipeline.update({
        "stages": ["build", "test", "deploy"]
    })
    for service in SERVICES:
        pipeline.update(make_service(service))
    f.write(json.dumps(pipeline))
