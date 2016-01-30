
# openNLP-pywrapper
A python wrapper for OpenNLP

## Example Usage

```
import opennlp

# The model file should be inside `models` folder.
instance = opennlp.OpenNLP("/home/user/apache-opennlp-1.6.0", "ChunkerME", "en-chunker.bin")

instance.parse('A_DT sale_NN is_VBZ the_DT exchange_NN of_IN a_DT commodity_NN or_CC money_NN as_IN the_DT price_NN of_IN a_DT good_JJ or_CC a_DT service._NN')

```
