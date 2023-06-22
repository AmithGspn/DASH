from pprint import pprint

import pytest

# Constants
SWITCH_ID = 5

commands = [
    {
        "name": "route_entry_1",
        "op": "create",
        "type": "SAI_OBJECT_TYPE_ROUTE_ENTRY",
        "key": {
            "switch_id": "$SWITCH_ID",
            "vr_id": "10",
            "destination": "221.1.0.0/24"
        },
        "attributes": [
            "SAI_ROUTE_ENTRY_ATTR_NEXT_HOP_ID",
            "0"
        ]
    },
    {
        "name": "route_entry_2",
        "op": "create",
        "type": "SAI_OBJECT_TYPE_ROUTE_ENTRY",
        "key": {
            "switch_id": "$SWITCH_ID",
            "vr_id": "10",
            "destination": "221.2.0.0/24",
        },
        "attributes": [
            "SAI_ROUTE_ENTRY_ATTR_NEXT_HOP_ID", 
            "1"
        ]
    }
]

class TestSaiVnetRoutingEntry:
    def test_vnet_nhop_routing_create(self, dpu):
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_vnet_nhop_routing_remove(self, dpu):
        results = [*dpu.process_commands(commands, cleanup=True)]
        print("\n======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
