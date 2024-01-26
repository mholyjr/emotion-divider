import os
from openai import OpenAI


class OpenAIController:
    def call_openai_api(self, prompt):
        client = OpenAI()
        completion = client.chat.completions.create(
          model="gpt-4",
          messages=[
            {"role": "system", "content": "Jsi expert na analýzu textu. Věty, které dostaneš, rozděl do dvou hlavních skupin – pozitivní a negativní – a poté je znovu rozděl do tří podskupin podle podobnosti jejich významu. Následně vypočítej procentuální zastoupení každé podskupiny v její nadřazené skupině. Procenta musí dávat dohromady 100%.\n\nStruktura bude:\n- Pozitivní\n-- přímá pozitivní hodnocení\n-- zábavnost a zaujetí\n-- obecný zájem\n- Negativní\n-- přímá negativní hodnocení\n-- nuda a nezaujetí\n-- nejasnost a relativní hodnocení\n\nOdpověď vždy vrátíš v json formátu:\n{\n\"totalNumberOfMessages\": [celkový počet zadaných vět pro analýzu],\n\"positive\": [\n{group: \"direct positive reviews\", percentage: [procentuální zastoupení v přímých a pozitivních hodnocení pozitivních emocích], emotions: [seznam vět patřících do této skupiny]},\n{group: \"fun and engagement\", percentage: [procentuální zastoupení zábavnost a zaujetí v pozitivních emocích]},\n{group: \"general interest\", percentage: [procentuální zastoupení obecný zájem v pozitivních emocích], emotions: [seznam vět patřících do této skupiny]}\n],\n\"negative\": [\n{group: \"direct negative reviews\", percentage: [procentuální zastoupení přímá negativní hodnocení v negativních emocích], emotions: [seznam vět patřících do této skupiny]},\n{group: \"boring and disinterested\", percentage: [procentuální zastoupení nuda a nezaujetí v negativních emocích], emotions: [seznam vět patřících do této skupiny]},\n{group: \"ambiguity and relative assessment\", percentage: [procentuální zastoupení nejasnost a relativní hodnocení v negativních emocích], emotions: [seznam vět patřících do této skupiny]}\n]\n}"},
            {"role": "user", "content": prompt}
          ],
          temperature=0.5,
          max_tokens=2000,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )

        return completion.choices[0].message