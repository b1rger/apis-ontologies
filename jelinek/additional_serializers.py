from dataclasses import dataclass
from apis_ontology.models import *
from apis_core.apis_relations.models import *
from apis_core.apis_metainfo.models import *

@dataclass
class AdditionalSerializer:
    url: str # For now, it is recommended to prefix the url with 'additional'
    name: str # unique name for django
    path_structure: dict # see example structure
    viewset = None # will be programmatically generated

additional_serializers_list = [
    AdditionalSerializer( # Keep this example one for now
        url="addtional/example_serializer",
        name="some_example_serializer",
        path_structure={
            F1_Work: [
                F1_Work.id,
                F1_Work.name,
                F1_Work.idno,
                {
                    F1_Work.triple_set_from_subj: [
                        {
                            Triple.prop: [
                                Property.name_forward,
                                Property.name_reverse,
                            ]
                        },
                        {
                            Triple.obj: [
                                F3_Manifestation_Product_Type.name,
                                F3_Manifestation_Product_Type.bibl_id,
                                {
                                    F3_Manifestation_Product_Type.triple_set_from_obj: [
                                        {
                                            Triple.prop: [
                                                Property.name_forward,
                                                Property.name_reverse,
                                            ]
                                        },
                                        {
                                            Triple.subj: [
                                                F10_Person.name
                                            ],
                                        }
                                    ]
                                }
                            ]
                        },
                    ]
                }
            ]
        }
    ),
]