# Getting started

Lanternfish collects log files and ships them to a sink.

## Install

Download the installer for your platform from the releases page. Lanternfish runs on Linux
(x86-64 and ARM), macOS and Windows (x86-64).

## Create a configuration

Run `lanternfish init` to write a starter `lantern.yaml` in the current folder, then add the
paths you want to collect under `inputs`.

## Start shipping

Run `lanternfish run`. To check what is being collected, see the [CLI reference](cli-reference.md).
