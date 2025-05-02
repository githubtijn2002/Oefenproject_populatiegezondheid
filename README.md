Youth Healthcare Data Analysis Project
English Summary
This project analyzes youth healthcare services across municipalities in the Haaglanden region of the Netherlands. It leverages data from the Dutch Central Bureau of Statistics (CBS) to explore relationships between youth wellbeing survey responses, demographic factors, and the costs associated with youth care services.

Key Features
Data Acquisition: Automated retrieval of multiple youth care datasets from the CBS Open Data API
Data Processing: Comprehensive ETL pipeline that cleans, transforms, and merges data from different sources
Statistical Analysis: Normalization of age brackets, household types, and referral sources to enable cross-municipal comparison
Machine Learning: Linear regression model to identify factors most strongly correlated with youth care costs
Visualization: Creation of pie charts to illustrate the distribution of youth care services across age groups, household types, and referral sources
Technical Components
Uses cbsodata for accessing the Dutch Central Statistics Bureau API
Implements custom pagination for handling large datasets
Includes data normalization routines for both row-wise and column-wise scaling
Employs scikit-learn for regression modeling
Creates visualizations with matplotlib
Usage
The project is structured as a Jupyter Notebook, allowing for interactive exploration of the data and modification of analysis parameters. It provides insights into which factors may contribute to higher youth care costs, though it acknowledges the limited sample size and emphasizes that correlations should not be interpreted as causation.

Disclaimer:
This project is just for fun and practice. This model is not up to production level standard, nor is the data cleaning as thorough as I would prefer to do in a more serious setting.
It still generates some insightful findings (Stress seems to be the strongest predictor of youthcare presence), but the model is obviously limited in it's real-life applications.
What could be done given more time and budget?
-Read into the domain of jeugdzorg and everything it entails -> domain knowledge is key to understanding your data and building a solid model
-Involving more municipality specific data (income, job sectors, etc.) to better understand how those factors might influence the costs of jeugdzorg
-Seek anonymized individual-level data instead of aggregated statistics for more granular analysis
-Better missing data handling -> instead of instantly dropping, look at what is salvagable and if perhaps a predictive model can potentially fill in the gaps
-Look not only at the cost, but also at the discrepency between predicted cost and actual cost in the different municipalities

Jeugdzorg Data Analyse Project
Nederlandse Samenvatting
Dit project analyseert jeugdzorgdiensten in gemeenten binnen de regio Haaglanden. Het maakt gebruik van gegevens van het Centraal Bureau voor de Statistiek (CBS) om verbanden te onderzoeken tussen antwoorden op welzijnsenquêtes onder jongeren, demografische factoren en de kosten van jeugdzorg.

Belangrijkste Functionaliteiten
Gegevensverwerving: Geautomatiseerd ophalen van meerdere jeugdzorgdatasets via de CBS Open Data API
Gegevensverwerking: Uitgebreide ETL-pipeline die gegevens uit verschillende bronnen opschoont, transformeert en samenvoegt
Statistische Analyse: Normalisatie van leeftijdsgroepen, huishoudtypen en verwijzers om vergelijking tussen gemeenten mogelijk te maken
Machine Learning: Lineair regressiemodel om factoren te identificeren die het sterkst correleren met jeugdzorgkosten
Visualisatie: Creatie van cirkeldiagrammen om de verdeling van jeugdzorg over leeftijdsgroepen, huishoudtypen en verwijzers te illustreren
Technische Componenten
Gebruikt cbsodata voor toegang tot de CBS API
Implementeert aangepaste paginering voor het verwerken van grote datasets
Bevat routines voor gegevensnormalisatie voor zowel rij- als kolomgewijze schaling
Past scikit-learn toe voor regressiemodellering
Maakt visualisaties met matplotlib
Gebruik
Het project is opgezet als een Jupyter Notebook, wat interactieve verkenning van de gegevens en aanpassing van analyseparameters mogelijk maakt. Het biedt inzichten in welke factoren kunnen bijdragen aan hogere jeugdzorgkosten, maar erkent de beperkte steekproefomvang en benadrukt dat correlaties niet als causale verbanden moeten worden geïnterpreteerd.

Disclaimer:
Dit project is om te oefenen. Het model is niet van productie-niveau kwaliteit, en de data cleaning is ook niet zo grondig uitgevoerd als in een serieuzere setting gedaan zou worden.
Een aantal interessante inzichten duiken op (stress lijkt de sterkste voorspeller van jeugdzorggebruik te zijn), maar het model is uiteraard beperkt in zijn toepasbaarheid in de echte wereld.
Wat zou kunnen worden gedaan met meer budget en tijd?
-Verdieping in het domein van jeugdzorg en alles wat daarbij komt kijken -> domeinkennis is cruciaal voor het begrijpen van je data en het bouwen van een degelijk model
-Meer gemeente-specifieke data erbij betrekken (inkomen, werksectoren, etc.) om beter te begrijpen hoe deze factoren de kosten van jeugdzorg beïnvloeden
-Anonieme data op individueel niveau zoeken in plaats van geaggregeerde statistieken, voor meer gedetailleerde analyses
-Beter omgaan met missende datapunten i.p.v. deze meteen te verwijderen -> kijken wat er te redden valt en of een voorspellend model wellicht de gaten kan opvullen
-Niet alleen kijken naar de gerealiseerde kosten, maar ook de discrepantie tussen gerealiseerde kosten en voorspelde kosten.
