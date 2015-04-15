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
    GOV_LIST = [ x["name"] for x in gov]

    active_list = 'rand'
    active_type = 'rand'


    # List methods & helpers
    def do_list(self, gov_list):
        """list [gov_list]
        Choose a government type list to use for generation."""
        if gov_list:
            print "gov_list chosen:", gov_list
            if gov_list.lower() in (list_item.lower() for list_item in self.GOV_LIST):
                active_list = gov_list.lower()
            else:
                print "That list type is invalid. Please try again."
        else:
            print "No list chosen. Please try again."

    def help_list(self):
        print '\n'.join([ '',
                          'list [gov_list]',
                          '-- Choose a government type list to use for generation.',
                          ''
                          ])

    def complete_list(self, text, line, begidx, endidx):
        if not text:
            completions = self.GOV_LIST[:]
        else:
            completions = [ f
                            for f in self.GOV_LIST
                            if f.lower().startswith(text.lower())
                            ]
        return completions


    def do_type(self, gov_type):
        """type [gov_type]
        Choose a type of government list to use."""
        if gov_type:
            print "gov_type chosen:", gov_type
        else:
            print "No type chosen. Please try again."

    def help_type(self):
        print '\n'.join([ '',
                          'type [gov_type]',
                          '-- Choose a type of government to use from the active list',
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
