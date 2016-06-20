#BEGIN_HEADER
#END_HEADER


class HelloService3:
    '''
    Module Name:
    HelloService3

    Module Description:
    A KBase module: HelloService3
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = "2aa5811787422c5d5726fafd62a5454b0e791c1e"
    
    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        #END_CONSTRUCTOR
        pass
    

    def do_something(self, ctx):
        """
        Insert your typespec information here.
        :returns: instance of String
        """
        # ctx is the context object
        # return variables are: s
        #BEGIN do_something
        s = 'doing something'
        print('I am doing something.')
        #END do_something

        # At some point might do deeper type checking...
        if not isinstance(s, basestring):
            raise ValueError('Method do_something return value ' +
                             's is not type basestring as required.')
        # return the results
        return [s]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION, 
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
