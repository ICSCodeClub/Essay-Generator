import warnings
warnings.simplefilter("ignore")

import gpt_2_simple as gpt2
import os
import requests
import sys

model_name = "355M" #124M is also acceptable
if not os.path.isdir(os.path.join("models", model_name)):
	print(f"Downloading {model_name} model...")
	gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/
    

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout



sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

divider = '===================='


def generate(prefix='', start=True):
        text = ''
        if start:
                prefix = str(divider)+'\n'+str(prefix)
        with HiddenPrints():
                
                text = gpt2.generate(sess,
                      temperature=0.65,
                      length=100,
                      prefix=str(prefix),
                      sample_delim=divider,
                      return_as_list=True,
                      )[0]
        
        text = text[len(prefix):]
        if len(text) <= 1 or abs(len(text) - text.count('=')) <= 1:
                return ''
        while text.lstrip()[0] == '=':
                text = text[1:]
                if len(text) == 0:
                        return ''
        
        if text.rfind(divider) > len(prefix)-1:
                text = text[:text.rfind(divider)]
        text = text[0:text.rfind('.')+1]
        return text.lstrip()

if __name__ == "__main__":
        print(generate(prefix='What is reality?'))
