# From Data to Translation: Leveraging AI for Efficient and Accurate Translation of Technical Scientific Reports 

## Description

The Canadian Science Advisory Secretariat (CSAS) publishes hundreds of scientific documents each year, most of which require translation from English to French under the Official Languages Act. This project involves fine-tuning an AI translation model using ~10,000 existing CSAS translations. This could improve consistency, accuracy, and significantly reduce translation costs and timelines, ensuring faster delivery of scientific recommendations to Canadians. 

Current translations are costly and time-consuming, with AI models often missing scientific nuance, often leading to heavy manual edits. By leveraging our large corpus of verified translations, we can train a model to handle context-specific language far better than generic AI solutions. Implementation involves data preparation, model training, and validation against existing translations and standard AI tools. 

While human review will remain essential, this approach would streamline workflows and offer a valuable tool for the Translation Bureau and other Science-Based Departments and Agencies (SBDAs).

## Relevant Departments or Agencies

As CSAS is unique to Fisheries and Oceans Canada (DFO), initial work will be handled internally, with input from the Translation Bureau as needed. If successful, this proof of concept could be expanded to support other departments requiring high-quality, context-aware scientific translations.

## Initial Insights

1. Many older documents do not include translated data

![{0F606E09-271C-4F4C-9289-6702DA28234E}](https://github.com/user-attachments/assets/fd66e5e5-8ae0-4b1b-8b71-ce6be773f702)

2. Many documents contain only translations for abstracts and title pages

![{D84497E7-2E97-4BCE-9670-1BF9462337FE}](https://github.com/user-attachments/assets/19f0a7ac-d805-40f8-b342-cf58a30dfc89)

3. Similarity between linked text fragments are maximised in longer documents with full translations, but which include minimal figures and graphs

![{D5591EE4-F9E5-4219-BE4E-D328230F9E13}](https://github.com/user-attachments/assets/26ba8307-b9a2-4d5f-a3a0-b5d71e0bc915)

4. Correlating French and English text fragments is non-trivial and required an advanced search algorithm

![image](https://github.com/user-attachments/assets/d918a9c9-2c00-41e3-88b9-e382f740033f)

## Future Work (in-progress)

Now that training data has be compiled and cleaned, it is possible to finetune an LLM translation model. The next steps include choosing a model to finetune, performing the finetuning, creating test cases to evaluate results, and tweaking hyperparameters to optimise the translation performance improvements.


