# Quirk Generator for [`zha-quirks`](https://github.com/zigpy/zha-device-handlers)

This is a tool to generate stub quirks for a specific devices using their device signature or a diagnostics file.

Note: This tool will not generate a full quirk that magically makes your device work. It will only generate a stub quirk that you can use as a base for your own quirk.

The base for the quirk generator was made by [@dmulcahey](https://github.com/dmulcahey).

## Installation

```console
$ pip install git+https://github.com/zigpy/quirk-generator.git
```

Note: It's planned to add this to PyPi in the future for easier installation.

## Usage

### Generate stub quirk

If you want to start writing a quirk for a device, you can use the `generate-quirk` command to generate a stub quirk for that device.

To generate a quirk from a device signature or a diagnostics file, run:
```console
$ quirk-generator generate-quirk sample_files/diagnostics.json
```

If you want to save the generated quirk to a file, you can use the `--output` option:
```console
$ quirk-generator generate-quirk sample_files/diagnostics.json --output my_quirk.py
```

### Search for matches in existing quirks

If you have a device signature or a diagnostics file and want to know if existing quirks would already match that file if the manufacturer and model was ignored, you can use the `locate-matches` command.

To search for possible matches for existing quirks, run:
```console
$ quirk-generator locate-matches sample_files/signature.json
```
