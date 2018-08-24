# kudos-badges
Kudos badges and creative assets for Gitcoin

## Naming schema

For consistency, name all images with all lowercase letters and underscores between each word.  For example,

- level_up.svg
- night_owl.svg

## kudos.yaml file

This file contains the information about each of the kudos artifacts.  When adding a new Kudos, please add a corresponding record to the file.

## init_kudos.py

This python script reads the **images** directory and creates a kudos.yaml file.  It uses the filename to create the `name`, the `image` field.  The rest of the fields are sample defaults.

You only need to run this script if the kudos.yaml file doesn't already exist.

