# Media Framing in News NLP Project
Media framing in news on Israel-Palestine conflict in 2023

This analysis is performed for the final project of Empirical Methods course of Master 2 in Economie du Développement Durable of Univesité de Paris 1 Panthéon-Sorbonne in collaboration with Elif Çanga.

### Content Warning: Sensitive Material
The content analyzed in this repository may contain historically and culturally sensitive terms as well as references to violent themes, consequences of warfare, death and human suffering. Reader discretion is advised. The information provided may be distressing or triggering to some individuals. Proceeding further acknowledges your understanding and acceptance of encountering such sensitive subject matter.

## Research Question
The purpose of this analysis is to show how two different countries / two media from different countries cover the war in news, how the reality of war can be reflected in the media in different ways, by using the NLP technique in the context of the Israel-Palestinian conflict. The fact that this issue is linked to international relations and politics has caused most countries in the world to position themselves. In this regard, we conducted a media framing analysis by examining the news of the Qatari media Al-Jazeera and the British media BBC, in which we detected differences in their political statements.

## Why This Question?

As far as the ongoing conflict between Israel and Palestine since 1948 is concerned, the issue has always got substantial international media attention. However, with the tension escalating following 7 October attacks, an equivalent battle started to be fought over gaining legitimacy. Hence,  the language and discourses in the news coverage became more important than ever. 
A study held by the [Glasgow Media Group in 2011](https://www.glasgowmediagroup.org/downloads/17-war-and-conflict), documented the language used by journalists for Israelis and Palestinians reviewing the BBC's news broadcasts. They found that while terms such as “brutal murder”, “mass murder”, and “massacre” were used to describe the deaths of Israelis, Palestinians were linked with "terrorism".
On the other hand, as a global media giant from Qatar, a country with an explicit Pro-Palestinian position with Qatar openly condemning "genocide" in Gaza, Al-Jazeera reported that 2023 was the deadliest year for Palestinians since the 1948 Nakba, while BBC News [has recently been criticized](https://thewire.in/media/dead-versus-killed-a-closer-look-at-the-media-bias-in-reporting-israel-palestine-conflict) for a biased language against Palestine, such as an allegedly deliberate use of the word “dead” for those killed in Gaza whereas the word “killed” for those who lost lives in Israel.

Taking into account all these controversies and the powerful impacts of media framing found in the previous literature, this study aims to portray how the current conflict is conveyed objectively from different perspectives through language usage in media news.

## Organization of this Repository:
In this repository you will find:
- _Web Scraping_ folder showing our code for scraping and storing the news from 7 October to 31 December 2023 on this issue from BBC and Aljazeera news websites
- media_framing_in_news.ipynb for our analyses and visualizations
- _data_ folder containing the cleaned version of our main data all_news.json, a subset of the data (df_death.json) which we used for media framing in reporting of fatalities, and a labeled version of that subset by the algorithm we trained (df_death_pred.json)
- _Model_ folder where you can find the notebook for our sentence classification algorithm which we trained on AI-generated data to predict whether a sentence (given that it makes reference to deaths) reports Palestinian fatalities or Israeli fatalities
- NLP_project-Elif&Yagmur.pdf file where you can see our poster for the course.