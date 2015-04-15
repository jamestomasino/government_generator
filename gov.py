#!/usr/local/bin/python

import cmd
import json
import random

class Government(cmd.Cmd):
    """Simple government type generator."""

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "=>> "
        self.intro = "Government Type Generator. Type 'help' for commands."
        self.json_data = open('gov.json')
        self.data = json.load(self.json_data)
        self.gov = self.data["government"];
        self.GOV_LIST = [ x["name"] for x in self.gov]
        self.TEMP_TYPE = []

        self.active_list = 'rand'
        self.active_type = 'rand' # not yet being used to limit rand

    # List methods & helpers
    def do_list(self, gov_list):
        """list [gov_list]
        Choose a government type list to use for generation."""
        if gov_list:
            print "gov_list chosen:", gov_list
            if gov_list.lower() in (list_item.lower() for list_item in self.GOV_LIST):
                self.active_list = gov_list.lower()
                self.do_rand(self)
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
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.GOV_LIST if s.lower().startswith(mline.lower())]

    def do_rand(self, arg):
        """rand
        Generate a random government"""
        if self.active_list == "rand":
            pick_list = random.choice(self.gov)
        else:
            print "using stored active list"
            pick_list = next((x for x in self.gov if x["name"].lower() == self.active_list.lower()), None)

        if pick_list != None:
            list_name = pick_list["name"]
            list_options = pick_list["option"]
            list_option = random.choice(list_options)
            type_option = random.choice(list_option["option"])
            print "##", list_name
            print "\n###", list_option["name"]
            if list_option["desc"]:
                print "\n", list_option["desc"]
            print "\n####", type_option["name"]
            if type_option["desc"]:
                print "\n", type_option["desc"]

    def help_rand(self):
        print '\n'.join([ '',
                          'rand',
                          '-- Generate a random government',
                          ''
                          ])


    def do_hist(self, args):
        """Print a list of commands that have been entered"""
        print self._hist

    def do_exit(self, args):
        """Exits from the console"""
        return -1

    ## Command definitions to support Cmd object functionality ##
    def do_EOF(self, args):
        """Exit on system end of file character"""
        return self.do_exit(args)

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_shell(self, args):
        """Do not allow shell commands"""
        pass

    def preloop(self):
        """Initialization before prompting user for commands.
           Despite the claims in the Cmd documentaion, Cmd.preloop() is not a stub.
        """
        cmd.Cmd.preloop(self)   ## sets up command completion
        self._hist    = []      ## No history yet
        self._locals  = {}      ## Initialize execution namespace for user
        self._globals = {}

    def precmd(self, line):
        """ This method is called after the line has been input but before
            it has been interpreted. If you want to modifdy the input line
            before execution (for example, variable substitution) do it here.
        """
        self._hist += [ line.strip() ]
        return line

    def postloop(self):
        """Take care of any unfinished business.
           Despite the claims in the Cmd documentaion, Cmd.postloop() is not a stub.
        """
        cmd.Cmd.postloop(self)   ## Clean up command completion
        print "Exiting..."

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        Government().onecmd(' '.join(sys.argv[1:]))
    else:
        Government().cmdloop()
