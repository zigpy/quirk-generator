import json


def prepare_input(file: str) -> dict:
    diagnostics_data = json.loads(file)

    if (
        diagnostics_data.get("data") is None
        and diagnostics_data.get("node_descriptor") is None
    ):
        raise ValueError(
            "Invalid input. Please provide a device signature or diagnostics file."
        )

    # if we only get a signature, wrap in "data" and "signature" keys
    if diagnostics_data.get("data") is None and diagnostics_data.get("node_descriptor"):
        diagnostics_data = {"data": {"signature": diagnostics_data}}
        # add model and manufacturer from signature to data
        diagnostics_data["data"]["model"] = diagnostics_data["data"]["signature"][
            "model"
        ]
        diagnostics_data["data"]["manufacturer"] = diagnostics_data["data"][
            "signature"
        ]["manufacturer"]

    return diagnostics_data
