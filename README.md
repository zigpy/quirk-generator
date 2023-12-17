# Quirk Generator for [`zha-quirks`](https://github.com/zigpy/zha-device-handlers)

This is a tool to generate stub quirks for a specific devices using their device signature or a diagnostics file.

Note: This tool will not generate a full quirk that magically makes your device work. It will only generate a stub quirk that you can use as a base for your own quirk.

The base for the quirk generator was made by [@dmulcahey](https://github.com/dmulcahey).

### Note

This tool is still work-in-progress. If you have any issues or suggestions, please open an issue.

## Installation

Make sure you have Python 3.10 or newer installed.

### Virtual environment

If you want to install `quirk-generator` in a virtual environment, you can execute these commands before installing the package. Otherwise, skip to the "Install" section below.
```console
python -m venv venv
source venv/bin/activate
```

### Install

```console
pip install git+https://github.com/zigpy/quirk-generator.git
```

Note: It's planned to add this to PyPi in the future for easier installation and updating.

### Updating

Also note that [`zha-quirks`](https://github.com/zigpy/zha-device-handlers) should be updated regularly to make sure `quirk-generator` can match against the latest quirks. To just upgrade `zha-quirks`, use:
```console
pip install zha-quirks --upgrade
```
To force a full re-installation of `quirk-generator` and all its dependencies, use:
```console
pip install git+https://github.com/zigpy/quirk-generator.git --force-reinstall
```

## Usage

### Generate stub quirk

If you want to start writing a quirk for a device, you can use the `generate-quirk` command to generate a stub quirk for that device.

To generate a quirk from a device signature or a diagnostics file, run:
```console
quirk-generator generate-quirk sample_files/diagnostics.json
```

If you want to save the generated quirk to a file, you can use the `--output` option:
```console
quirk-generator generate-quirk sample_files/diagnostics.json --output my_quirk.py
```

### Search for matches in existing quirks

If you have a device signature or a diagnostics file and want to know if existing quirks would already match that file if the manufacturer and model was ignored, you can use the `locate-matches` command.

To search for possible matches for existing quirks, run:
```console
quirk-generator locate-matches sample_files/signature.json
```
