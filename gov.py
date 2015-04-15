#!/usr/local/bin/python

import cmd
import json

class Government(cmd.Cmd):
    """Simple government type generator."""

    prompt = 'gov> '
    intro = "Government Type Generator. Type 'help' for commands."

    json_data = open('gov.json')
    data = json.load(json_data)
    gov = data["government"];
    TYPES = [ x["name"] for x in gov]

    def do_type(self, gov_type):
        """type [gov_type]
        Choose a type of government list to use."""
        if gov_type:
            print "gov_type chosen:", gov_type
        else:
            print 'no gov_type chosen'

    def help_type(self):
        print '\n'.join([ '',
                          'type [gov_type]',
                          '-- Choose a type of government list to use',
                          ''
                          ])

    def do_rand(self, gov_type):
        """rand [gov_type]
        Generate a random government from the type chosen, or random if blank"""
        if gov_type:
            print "gov_type chosen:", gov_type
        else:
            print 'no gov_type chosen'

    def help_rand(self):
        print '\n'.join([ '',
                          'rand [gov_type]',
                          '-- Generate a random government from the type chosen, or random if blank',
                          ''
                          ])

    def complete_rand(self, text, line, begidx, endidx):
        if not text:
            completions = self.TYPES[:]
        else:
            completions = [ f
                            for f in self.TYPES
                            if f.startswith(text)
                            ]
        return completions

    def do_exit(self, line):
        "Exit"
        return True

    def do_EOF(self, line):
        "Exit"
        return True

    def postloop(self):
        print "\n"

if __name__ == '__main__':
    Government().cmdloop()
