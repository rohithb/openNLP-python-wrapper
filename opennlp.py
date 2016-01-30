import pexpect


class OpenNLP():
    def __init__(self, path, tool, model):
        '''
            Initializes OpenNLP
            :params
                path: Absolute path to the opennlp folder
                tool:OpenNLP tool (Eg: ChunkerME, TokenizerME)
                model: model file name
        '''
        opennlp = path + '/bin/opennlp'
        model_path = path + '/models/' + model
        cmd = '%s %s %s' % (opennlp, tool, model_path)

        # Spawn the chunker process
        self.process = pexpect.spawn(cmd)
        self.process.setecho(False)
        self.process.expect('done')
        self.process.expect('\r\n')

    def parse(self, text):
        # clear any pending output
        try:
            self.process.read_nonblocking(2048, 0)
        except:
            pass

        self.process.sendline(text)
        self.process.waitnoecho()  # remove this if not working
        timeout = 5 + len(text) / 20.0

        self.process.expect('\r\n', timeout)
        results = self.process.before
        # Remove this if block if required.
        # This is added to address invalid input format for ChunkerME
        if b'Invalid' in results:
            try:
                self.process.readline()
            except:
                pass
            return False
        return results
