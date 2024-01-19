"""Locate existing quirks that may match a device diagnostic file from ZHA."""

from typing import List

import zhaquirks
import zigpy.quirks as zq


def locate_quirk_matches(diagnostics_data: dict) -> List[str]:
    zhaquirks.setup()

    ALL_QUIRK_CLASSES = []
    for manufacturer in zq._DEVICE_REGISTRY._registry.values():
        for model_quirk_list in manufacturer.values():
            for quirk in model_quirk_list:
                if quirk in ALL_QUIRK_CLASSES:
                    continue
                ALL_QUIRK_CLASSES.append(quirk)

    del quirk, model_quirk_list, manufacturer

    possible_matches = []

    signature = diagnostics_data.get("data").get("signature")

    for quirk in ALL_QUIRK_CLASSES:
        sig_ep_ids = {int(id) for id in signature.get("endpoints").keys()}
        quirk_ep_ids = {int(id) for id in quirk.signature.get("endpoints").keys()}

        # XXX: this was `not sig_ep_ids.issubset(quirk_ep_ids)` before,
        # but that breaks with having more endpoints in the quirk than in the signature
        # we're comparing to, and we likely want to stay strict for now
        # regarding the endpoint ids matching?
        if sig_ep_ids != quirk_ep_ids:
            continue

        quirk_match = True
        for quirk_endpoint_id, quirk_endpoint in quirk.signature.get(
            "endpoints"
        ).items():
            endpoint = signature.get("endpoints").get(str(quirk_endpoint_id))
            if int(quirk_endpoint.get("device_type")) != int(
                endpoint.get("device_type"), base=16
            ):
                quirk_match = False
                break
            if quirk_endpoint.get("profile_id") != int(
                endpoint.get("profile_id"), base=16
            ):
                quirk_match = False
                break
            endpoint_input_clusters = {
                int(cluster_id, base=16)
                for cluster_id in endpoint.get("input_clusters")
            }
            endpoint_output_clusters = {
                int(cluster_id, base=16)
                for cluster_id in endpoint.get("output_clusters")
            }
            quirk_input_clusters = {
                int(cluster_id) for cluster_id in quirk_endpoint.get("input_clusters")
            }
            quirk_output_clusters = {
                int(cluster_id) for cluster_id in quirk_endpoint.get("output_clusters")
            }

            if not endpoint_input_clusters.issubset(
                quirk_input_clusters
            ) or not endpoint_output_clusters.issubset(quirk_output_clusters):
                quirk_match = False
                break

        if quirk_match:
            possible_matches.append(f"{quirk.__module__}.{quirk.__name__}")
            break

    return possible_matches
