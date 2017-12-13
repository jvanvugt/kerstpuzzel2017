map1 = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
       "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
       "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
       "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
       "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
       "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
       "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
       "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
       "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
       "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
       "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
       "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
       "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
       "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
       "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
       "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
	   
map2 = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
       "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
       "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"O",
       "UGU":"C", "UGC":"C", "UGA":"U", "UGG":"W",
       "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
       "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
       "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
       "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
       "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
       "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
       "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
       "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
       "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
       "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
       "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
       "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
	   
map3 = {"UUU":"phe", "UUC":"phe", "UUA":"leu", "UUG":"leu",
       "UCU":"ser", "UCC":"ser", "UCA":"ser", "UCG":"ser",
       "UAU":"tyr", "UAC":"tyr", "UAA":"STOP", "UAG":"pyl",
       "UGU":"cys", "UGC":"cys", "UGA":"sec", "UGG":"trp",
       "CUU":"leu", "CUC":"leu", "CUA":"leu", "CUG":"leu",
       "CCU":"pro", "CCC":"pro", "CCA":"pro", "CCG":"pro",
       "CAU":"his", "CAC":"his", "CAA":"gln", "CAG":"gln",
       "CGU":"arg", "CGC":"arg", "CGA":"arg", "CGG":"arg",
       "AUU":"ile", "AUC":"ile", "AUA":"ile", "AUG":"met",
       "ACU":"thr", "ACC":"thr", "ACA":"thr", "ACG":"thr",
       "AAU":"asn", "AAC":"asn", "AAA":"lys", "AAG":"lys",
       "AGU":"ser", "AGC":"ser", "AGA":"arg", "AGG":"arg",
       "GUU":"val", "GUC":"val", "GUA":"val", "GUG":"val",
       "GCU":"ala", "GCC":"ala", "GCA":"ala", "GCG":"ala",
       "GAU":"asp", "GAC":"asp", "GAA":"glu", "GAG":"glu",
       "GGU":"gly", "GGC":"gly", "GGA":"gly", "GGG":"gly",}
	   
input1= "UGGAGCGGGAGUUGAGGAUAGGGAUUAGGUAGGAGGG"
input2 = input1[::-1]
input3 = "UGGAGCGGGAGUUGAGGAAGGGAUUAGGUAGGAGGG"
input4 = "UGGAGCGGAGUUGAGGAUAGGGAUUAGUAGGAGGG"
input5 = input3[::-1]
input6 = input4[::-1]
for x in range (0, 3):
	endstring= ""
	i=x
	while i < len(input6):
		codon= input6[i:i+3]
		if len(codon)>2:
			endstring = endstring + map2[codon]
		i = i+3
	print(endstring)
