# From Data to Translation: Leveraging AI for Efficient and Accurate Translation of Scientific Reports 

# Phase 1: Data Gathering and Transformation

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

## Future Work Phases

Following the completion of the data gathering and cleaning phase, a number of finetuned translation models were trained. The subsequent steps included choosing a selection of models to finetune, performing the finetuning, creating test cases to evaluate results, and tweaking hyperparameters to optimise translation performance improvements.

After finetuning the models, a rules-based translation layer was added. Using a list of preferred translations for locations, species, acronyms, and scientific terms, the quality of these scientific translations was further improved.

To evaluate the performance of different models, with and without different rules-based translation layers, a survey was created to evaluate random samplings from different schemas, as well as the corresponding published translations. This survey was randomised with model information hidden to create a blind survey, reducing bias when rating or ranking translation quality results.

Using survey data and analytical calculations to evaluate translation quality, as well as similarity to previously published translations, the final model and rules-based layer will be selected (in-progress).

After a translation model is chosen and finalised, the model will be deployed for internal use by select CSAS staff within DFO (in-progress).

### Links to Repositories for All Phases:

- **Phase 1**: Data Gathering and Transformation (complete)
- **Phase 2**: [AI Translation Fine-Tuning](https://github.com/KevinCarr42/Translation-Fine-Tuning) (complete)
- **Phase 3**: [Rule-Based Preferential Translations](https://github.com/KevinCarr42/rule-based-translation) (complete)
- **Phase 4**: [AI Translation Quality Survey App](https://github.com/KevinCarr42/translation-quality-survey-app) (complete)
- **Phase 5**: [Final AI Translation Model and Translation Quality Evaluation](https://github.com/KevinCarr42/CSAS-Translations) (in-progress)
- **Phase 6**: Deploy the Final Model (in-progress)
