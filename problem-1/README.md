

*Problem 1*

Sedbit log 20780909, Neptune orbit.

I have been a prisoner on an ancient spacecraft for 6 weeks.

Luckily I was able to wire my way out of my cell.  I can sneak out every couple days to raid the ship for supplies.  Something great happened the other day:  I figured out where the security post is.  

I was able to sneak in when Tim the security guard is asleep and get access to the ancient linux computer controlling the cameras and also to how the 8 airlocks open and close.

I know airlock 5 leads to the hanger bay where my ship is stashed.

That's the door I need to open.

That's also the door I need to watch because Tim will come back in through that door.

Here's my plan:

I have to wait for him to leave his post.

Run a series of programs in the security post.

Rush down and hide near airlock 5.  There's a spacesuit closet where I can get a suit and hide.

Wait for Tim to come back inside.

A minute later my programs will put the cameras near airlock 5 on a loop and open the locked airlock door so I can escape.  

I have three programs.

The first program runs the other two every minute.  (Linux can do this for me.)

The second program reads a file and looks through the contents and if it sees the information that tells it that airlock 5 is open, it prints out the escape sequence 8AR7W98.  There's a text file on the system that contains characters.  Each character is ascii encoded.  8-bits.  Each bit is a 0 or 1.  0 means the door is shut.  1 means the door is open.  The fifth bit is from the right... so 00010000 would be the fifth door open.  10000000 is the 8th door open.  11111111 is all eight doors open.  I found a printable ascii table in my archives.


32	040	20	00100000	 	&#32;	 	Space
33	041	21	00100001	!	&#33;	 	Exclamation mark
34	042	22	00100010	"	&#34;	&quot;	Double quotes (or speech marks)
35	043	23	00100011	#	&#35;	 	Number
36	044	24	00100100	$	&#36;	 	Dollar
37	045	25	00100101	%	&#37;	 	Per cent sign
38	046	26	00100110	&	&#38;	&amp;	Ampersand
39	047	27	00100111	'	&#39;	 	Single quote
40	050	28	00101000	(	&#40;	 	Open parenthesis (or open bracket)
41	051	29	00101001	)	&#41;	 	Close parenthesis (or close bracket)
42	052	2A	00101010	*	&#42;	 	Asterisk
43	053	2B	00101011	+	&#43;	 	Plus
44	054	2C	00101100	,	&#44;	 	Comma
45	055	2D	00101101	-	&#45;	 	Hyphen
46	056	2E	00101110	.	&#46;	 	Period, dot or full stop
47	057	2F	00101111	/	&#47;	 	Slash or divide
48	060	30	00110000	0	&#48;	 	Zero
49	061	31	00110001	1	&#49;	 	One
50	062	32	00110010	2	&#50;	 	Two
51	063	33	00110011	3	&#51;	 	Three
52	064	34	00110100	4	&#52;	 	Four
53	065	35	00110101	5	&#53;	 	Five
54	066	36	00110110	6	&#54;	 	Six
55	067	37	00110111	7	&#55;	 	Seven
56	070	38	00111000	8	&#56;	 	Eight
57	071	39	00111001	9	&#57;	 	Nine
58	072	3A	00111010	:	&#58;	 	Colon
59	073	3B	00111011	;	&#59;	 	Semicolon
60	074	3C	00111100	<	&#60;	&lt;	Less than (or open angled bracket)
61	075	3D	00111101	=	&#61;	 	Equals
62	076	3E	00111110	>	&#62;	&gt;	Greater than (or close angled bracket)
63	077	3F	00111111	?	&#63;	 	Question mark
64	100	40	01000000	@	&#64;	 	At symbol
65	101	41	01000001	A	&#65;	 	Uppercase A
66	102	42	01000010	B	&#66;	 	Uppercase B
67	103	43	01000011	C	&#67;	 	Uppercase C
68	104	44	01000100	D	&#68;	 	Uppercase D
69	105	45	01000101	E	&#69;	 	Uppercase E
70	106	46	01000110	F	&#70;	 	Uppercase F
71	107	47	01000111	G	&#71;	 	Uppercase G
72	110	48	01001000	H	&#72;	 	Uppercase H
73	111	49	01001001	I	&#73;	 	Uppercase I
74	112	4A	01001010	J	&#74;	 	Uppercase J
75	113	4B	01001011	K	&#75;	 	Uppercase K
76	114	4C	01001100	L	&#76;	 	Uppercase L
77	115	4D	01001101	M	&#77;	 	Uppercase M
78	116	4E	01001110	N	&#78;	 	Uppercase N
79	117	4F	01001111	O	&#79;	 	Uppercase O
80	120	50	01010000	P	&#80;	 	Uppercase P
81	121	51	01010001	Q	&#81;	 	Uppercase Q
82	122	52	01010010	R	&#82;	 	Uppercase R
83	123	53	01010011	S	&#83;	 	Uppercase S
84	124	54	01010100	T	&#84;	 	Uppercase T
85	125	55	01010101	U	&#85;	 	Uppercase U
86	126	56	01010110	V	&#86;	 	Uppercase V
87	127	57	01010111	W	&#87;	 	Uppercase W
88	130	58	01011000	X	&#88;	 	Uppercase X
89	131	59	01011001	Y	&#89;	 	Uppercase Y
90	132	5A	01011010	Z	&#90;	 	Uppercase Z
91	133	5B	01011011	[	&#91;	 	Opening bracket
92	134	5C	01011100	\	&#92;	 	Backslash
93	135	5D	01011101	]	&#93;	 	Closing bracket
94	136	5E	01011110	^	&#94;	 	Caret - circumflex
95	137	5F	01011111	_	&#95;	 	Underscore
96	140	60	01100000	`	&#96;	 	Grave accent
97	141	61	01100001	a	&#97;	 	Lowercase a
98	142	62	01100010	b	&#98;	 	Lowercase b
99	143	63	01100011	c	&#99;	 	Lowercase c
100	144	64	01100100	d	&#100;	 	Lowercase d
101	145	65	01100101	e	&#101;	 	Lowercase e
102	146	66	01100110	f	&#102;	 	Lowercase f
103	147	67	01100111	g	&#103;	 	Lowercase g
104	150	68	01101000	h	&#104;	 	Lowercase h
105	151	69	01101001	i	&#105;	 	Lowercase i
106	152	6A	01101010	j	&#106;	 	Lowercase j
107	153	6B	01101011	k	&#107;	 	Lowercase k
108	154	6C	01101100	l	&#108;	 	Lowercase l
109	155	6D	01101101	m	&#109;	 	Lowercase m
110	156	6E	01101110	n	&#110;	 	Lowercase n
111	157	6F	01101111	o	&#111;	 	Lowercase o
112	160	70	01110000	p	&#112;	 	Lowercase p
113	161	71	01110001	q	&#113;	 	Lowercase q
114	162	72	01110010	r	&#114;	 	Lowercase r
115	163	73	01110011	s	&#115;	 	Lowercase s
116	164	74	01110100	t	&#116;	 	Lowercase t
117	165	75	01110101	u	&#117;	 	Lowercase u
118	166	76	01110110	v	&#118;	 	Lowercase v
119	167	77	01110111	w	&#119;	 	Lowercase w
120	170	78	01111000	x	&#120;	 	Lowercase x
121	171	79	01111001	y	&#121;	 	Lowercase y
122	172	7A	01111010	z	&#122;	 	Lowercase z
123	173	7B	01111011	{	&#123;	 	Opening brace
124	174	7C	01111100	|	&#124;	 	Vertical bar
125	175	7D	01111101	}	&#125;	 	Closing brace
126	176	7E	01111110	~	&#126;	 	Equivalency sign - tilde
127	177	7F	01111111		&#127;	 	Delete



It looks like there are several characters that could mean the 5th bit is on.  So I'll need to watch for one of those and if I see it, print out the escape sequence.

The third program is listening to the second program and when it sees the escape sequence, it will send me a notification near airlock 5 that the door just opened.  Then a minute later, it will turn the camera loop on and open the door.  (I've cobbled this together with old shell commands.)

I've just got to code this second program if I want to escape.

Sedbit out.

Directions

You will be writing the second program Sedbit needs.

The computer running the security system is a very old computer scavenged from the 2020s.  

It's capable of running any code you can run today on a current computer.

Here's what your program needs to do:

- reads a text file

- go through all the text data in the file and look to see if the fifth bit is set.

- if it's set, output the escape sequence.  (Think print statement or console out or whatever's appropriate to your code.)

Have fun! 

Hopefully Sedbit will escape.  This part is up to you!

matt







