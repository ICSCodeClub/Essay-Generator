# Essay-Generator
Generates essays based on a seed paragraph to mitigate laborious work using python simple-gpt2
It respects quotes and has a generally logical flow.

## Downloading the Trained Model
You can download the pretrained model from my onedrive here:
<link pending>

Place it in <code>models/____</code>
Make sure it's called <code>'run1'</code> unless you edited the code to reflect a different file name

## Running the program
First, install the requirements by running <code>'pip3 install -r requirements.txt'</code> (yes, this project does require python3)
Make sure you have a generated neural net downloaded (see <b>Downloading the Trained Model</b>)
Then, run either <code>'essay.py'</code> or <code>'essay-respect-quotes.py'</code> in command prompt or powershell to both generate and print the essay to the command line!
<i>You may need to run it multiple times to get a perfect or even useable result. Mix and match!</i>

## Training your own model
I finetuned my model on 40mb of freely available essays on the internet. 
I won't share them due to possible copyright conflicts, but you can finetune your own model quite easily!
First, fill up <code>datasets/MyEssays.txt</code> with essays following the format proveded. Then, simply run 'net-train.py'

For initial training, I personally recommend 4000 steps, especially with as much data as I had.
Additionally, running <code>'net-train.py'</code> takes a <b>lot</b> of computing power. Using a jupiter notebook, as described in <a href="https://github.com/minimaxir/gpt-2-simple">the gpt2-simple repository</a> is recommended

## Finetuning on your own essays
Finetuning is similar and also a surefire way to keep your essays uniquely yours!
First, download the model as described in <b>Downloading the Trained Model</b> to get a starting point
Then, much like training the model, fill in <code>datasets/MyEssays.txt</code> and run <code>'net-train.py'</code>
Again, I'd recommend the jupiter notebook to train the network.
