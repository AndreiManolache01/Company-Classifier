# Company-Classifier
Proiectul pe are l-am facut este un clasificator pentru companiile din csv, prin care se foloseste e descrierea companiei,taguri,nisa. Fisierul "ml_insurance_challenge.csv" prezinta lista de companii cu subcategorii, iar "insurance_taxonomy.xlsx" prezinta lista etichetelor. 
Codul pe care l-am facut va atribui o eticheta sau mai multe, fiecarei companii in functie de subcategoriile din primul fisier. 
Pentru a putea compara textul companiilor, am folosit vectori numerici atat pentru textele companiilor cat si pentru tichete. Cu ajutorul acestora, am ajutat la valorificarea cuvintelor relevante. Ulterior, am calculat similaritatea folosindu-ma de 1 cand sunt identice si 0 cand nu seamana deloc, apoi am clasificat companiile are depasesc un prag de 0,2 al similaritatii.
