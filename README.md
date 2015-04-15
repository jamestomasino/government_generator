# Government Generator

This is a very simple python script that will randomly select a type of government from [this list found on Wikipedia](https://en.m.wikipedia.org/wiki/Government#Forms_of_government_by_associated_attributes).

## Options

You can run the program in interactive mode by typing:

    $ gov.py

You can also run commands directly via CLI:

    $ gov.py rand

Or:

    $ gov.py list <list_type>

In either interactive mode or CLI, `rand` will chose a random government type and output it to stdout with some basic [Markdown formatting](https://daringfireball.net/projects/markdown/syntax).

If you use the `list` command, you can limit the random output to one of the list types. For a complete list of these, launch interactive mode, type `rand list <TAB>` and the auto-complete will display a list.

## Help

Help is available inside the script by typing either:

    $ gov.py help

Or, in interactive mode:

	=>> help
