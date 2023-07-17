**Description of PR**\
This PR represents a partial implementation of the issue mentioned in the main repository [Sonic-net#236](https://github.com/sonic-net/DASH/issues/236). The focus of this PR is on introducing the implementation of SAI-Thrift call for "route_entry." It is unable to support the underlay bmv2 tests, which are presently marked as "skipped" for bmv2. However, it serves as a foundational step for future implementations, which aim to comprehensively cover the entire underlay scenario. This PR lays the groundwork for further advancements in addressing the broader scope of the issue at hand.

**What is the motivation for this PR?**\


**Functionality**\
The current implementation defaults to an "echo" behavior, where the packet is reflected back on the same port it arrived. However, this behavior has been modified by incorporating a routing table. As a result, when there is no match in the routing table, the packet continues to be reflected on the same port. On the other hand, when a route is matched in the routing table, the packet is directed to a different port as specified by the matching route.

**Main Changes**
- Add Underlay routing table P4 logic for routing the packets based on match.
- Add VNET API for testing the functionality.
- Add the following test cases
    - Routing Unidirectional (Send packet from one port and receive the packet on other port upon route match)
    - Routing Bidirectional (Send packets from both ports of bmv2 switch and receive the packets on other ports upon route match)

**Diagram**
![image](images/dash-underlay-changes.svg)