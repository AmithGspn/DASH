#include <core.p4>
#include "dash_headers.p4"
#include "dash_metadata.p4"

control underlay(
      inout headers_t hdr
    , inout metadata_t meta
#ifdef TARGET_BMV2_V1MODEL
    , inout standard_metadata_t standard_metadata
#endif // TARGET_BMV2_V1MODEL
    ) 
{
    // #ifdef UNDERLAY
    #ifdef TARGET_BMV2_V1MODEL
        action set_nhop(bit<9> next_hop_id) {
            standard_metadata.egress_spec = next_hop_id;
        }

        action def_act() {
            standard_metadata.egress_spec = standard_metadata.ingress_port;
        }

        @name("route|route")
        // @Sai[skipHeaderGen=true]
        table underlay_routing {
            key = {
                meta.dst_ip_addr : lpm @name("meta.dst_ip_addr:destination");
            }

            actions = {
                set_nhop;
                @defaultonly def_act;
            }
        }
    // #endif // UNDERLAY
    #endif // TARGET_BMV2_V1MODEL

    apply {
#ifdef TARGET_BMV2_V1MODEL
        underlay_routing.apply();
#endif // TARGET_BMV2_V1MODEL
    }
}
