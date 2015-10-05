--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.9
-- Dumped by pg_dump version 9.3.9
-- Started on 2015-10-02 21:02:13 CEST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 173 (class 3079 OID 11799)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 1999 (class 0 OID 0)
-- Dependencies: 173
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 172 (class 1259 OID 16475)
-- Name: books; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE books (
    book_id integer NOT NULL,
    title character varying
);


ALTER TABLE public.books OWNER TO postgres;

--
-- TOC entry 171 (class 1259 OID 16468)
-- Name: ratings; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ratings (
    user_id integer NOT NULL,
    rated_at timestamp without time zone DEFAULT now(),
    rat_book_01 integer,
    rat_book_02 integer,
    rat_book_03 integer,
    rat_book_04 integer,
    rat_book_05 integer,
    rat_book_06 integer,
    rat_book_07 integer,
    rat_book_08 integer,
    rat_book_09 integer,
    rat_book_10 integer,
    rat_book_11 integer,
    rat_book_12 integer,
    rat_book_13 integer,
    rat_book_14 integer,
    rat_book_15 integer
);


ALTER TABLE public.ratings OWNER TO postgres;

--
-- TOC entry 170 (class 1259 OID 16466)
-- Name: ratings_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ratings_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ratings_user_id_seq OWNER TO postgres;

--
-- TOC entry 2000 (class 0 OID 0)
-- Dependencies: 170
-- Name: ratings_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ratings_user_id_seq OWNED BY ratings.user_id;


--
-- TOC entry 1876 (class 2604 OID 16471)
-- Name: user_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ratings ALTER COLUMN user_id SET DEFAULT nextval('ratings_user_id_seq'::regclass);


--
-- TOC entry 1991 (class 0 OID 16475)
-- Dependencies: 172
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY books (book_id, title) FROM stdin;
1	A Study In Scarlet
2	The Sign of the Four
3	The Adventures of Sherlock Holmes
4	Memoirs of Sherlock Holmes
5	The Return of Sherlock Holmes
6	The Hound of the Baskervilles
7	The Valley of Fear
8	The Adventure of Wisteria Lodge
9	The Adventure of the Cardboard Box
10	The Adventure of the Red Circle
11	The Adventure of the Bruce-Partington Plans
12	The Adventure of the Dying Detective
13	The Disappearance of Lady Frances Carfax
14	The Adventure of the Devil's Foot
15	His Last Bow
\.


--
-- TOC entry 1990 (class 0 OID 16468)
-- Dependencies: 171
-- Data for Name: ratings; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ratings (user_id, rated_at, rat_book_01, rat_book_02, rat_book_03, rat_book_04, rat_book_05, rat_book_06, rat_book_07, rat_book_08, rat_book_09, rat_book_10, rat_book_11, rat_book_12, rat_book_13, rat_book_14, rat_book_15) FROM stdin;
1	2015-08-31 14:25:35.610547	0	1	1	0	0	0	0	0	0	0	-1	1	1	0	0
2	2015-08-31 14:25:35.836636	1	1	-1	0	0	1	0	0	-1	1	0	0	0	1	0
3	2015-08-31 14:25:35.845055	1	1	0	0	0	-1	1	0	0	0	0	1	0	0	0
4	2015-08-31 14:25:35.85759	0	0	0	0	1	1	0	1	1	0	-1	0	1	0	0
5	2015-08-31 14:25:35.868627	1	0	1	0	0	1	0	0	1	0	0	0	1	0	0
6	2015-08-31 14:25:35.879813	0	-1	-1	0	1	1	0	-1	0	0	0	0	0	1	0
7	2015-08-31 14:25:35.891174	1	0	-1	0	0	-1	-1	0	1	0	0	0	0	0	-1
8	2015-08-31 14:25:35.902125	0	0	0	0	0	0	1	1	0	0	-1	1	1	0	0
9	2015-08-31 14:25:35.913359	0	0	0	0	0	0	1	1	0	0	0	0	0	0	-1
10	2015-08-31 14:25:35.924392	-1	0	1	1	0	0	1	1	1	0	0	0	1	0	0
11	2015-08-31 14:25:35.935508	1	0	1	1	-1	0	0	0	0	0	0	0	0	0	0
12	2015-08-31 14:25:35.946499	1	0	0	1	0	-1	0	0	0	0	1	0	1	0	0
13	2015-08-31 14:25:35.957907	0	0	1	1	0	0	0	1	0	0	-1	0	1	0	1
14	2015-08-31 14:25:35.968316	0	1	0	1	0	-1	1	0	1	1	0	0	0	0	-1
15	2015-08-31 14:25:35.97794	0	0	-1	0	0	0	1	0	0	0	0	1	0	1	0
16	2015-08-31 14:25:35.989401	1	0	0	-1	0	1	0	0	1	0	1	-1	1	0	1
17	2015-08-31 14:25:36.000408	1	1	0	0	0	1	0	-1	0	0	0	-1	0	1	0
18	2015-08-31 14:25:36.011554	0	-1	0	0	0	0	-1	0	1	0	0	0	0	0	1
19	2015-08-31 14:25:36.022437	0	-1	1	0	0	1	0	0	1	0	0	0	-1	0	0
20	2015-08-31 14:25:36.033567	0	-1	0	1	1	0	-1	1	0	0	1	1	1	0	0
21	2015-08-31 14:25:36.044654	1	0	0	0	0	0	0	-1	-1	-1	0	0	1	1	0
22	2015-08-31 14:25:36.056902	0	0	1	0	0	0	0	0	1	0	0	0	0	1	0
23	2015-08-31 14:25:36.068495	1	1	-1	0	1	0	0	0	-1	-1	1	0	1	-1	0
24	2015-08-31 14:25:36.079605	0	1	0	0	1	1	1	-1	0	0	1	0	0	1	0
25	2015-08-31 14:25:36.090918	-1	0	0	0	0	-1	0	1	0	0	1	1	-1	0	0
26	2015-08-31 14:25:36.101666	0	0	-1	-1	-1	0	0	0	0	0	0	0	0	0	-1
27	2015-08-31 14:25:36.112332	1	1	0	0	1	-1	1	1	1	0	0	0	1	0	0
28	2015-08-31 14:25:36.123118	0	1	1	1	0	0	0	-1	0	1	-1	-1	0	-1	0
29	2015-08-31 14:25:36.135307	1	0	0	0	0	0	0	0	1	0	-1	-1	0	0	-1
30	2015-08-31 14:25:36.147087	0	1	0	0	0	0	0	-1	1	0	0	0	1	0	1
31	2015-08-31 14:25:36.157368	0	0	1	1	1	0	1	0	-1	0	0	-1	0	0	0
32	2015-08-31 14:25:36.168167	1	0	0	0	0	0	1	0	1	0	1	0	1	0	0
33	2015-08-31 14:25:36.179414	0	1	1	-1	0	-1	0	0	1	0	0	0	0	1	1
34	2015-08-31 14:25:36.190633	-1	1	0	0	0	1	0	0	0	0	1	0	0	0	1
35	2015-08-31 14:25:36.201772	0	0	0	0	0	0	0	-1	0	0	-1	-1	1	-1	-1
36	2015-08-31 14:25:36.212837	0	0	0	0	1	0	1	0	-1	0	-1	0	0	0	0
37	2015-08-31 14:25:36.224087	0	1	1	0	0	0	0	1	-1	0	0	0	0	0	1
38	2015-08-31 14:25:36.233834	0	1	0	0	0	1	0	1	0	0	1	0	1	0	0
39	2015-08-31 14:25:36.244533	0	0	1	0	-1	0	1	-1	1	0	0	1	0	1	0
40	2015-08-31 14:25:36.255716	1	0	0	0	1	0	0	1	1	0	0	0	0	-1	0
41	2015-08-31 14:25:36.26799	0	0	0	0	0	1	0	0	-1	0	0	0	0	0	1
42	2015-08-31 14:25:36.277881	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1
43	2015-08-31 14:25:36.28906	0	1	0	0	0	0	1	0	0	0	0	0	0	0	1
44	2015-08-31 14:25:36.30007	1	1	1	0	0	0	0	1	-1	0	0	0	0	0	0
45	2015-08-31 14:25:36.311204	0	0	-1	-1	0	1	-1	1	0	1	0	1	1	0	1
46	2015-08-31 14:25:36.322311	0	0	0	0	1	0	0	1	0	0	-1	0	0	0	0
47	2015-08-31 14:25:36.333271	0	0	0	0	-1	0	0	0	-1	0	0	1	0	0	0
48	2015-08-31 14:25:36.344378	-1	0	-1	1	0	0	1	-1	0	0	0	0	0	1	0
49	2015-08-31 14:25:36.355552	-1	1	0	1	0	0	1	1	1	-1	-1	0	0	1	-1
50	2015-08-31 14:25:36.366677	0	1	0	1	1	-1	0	0	-1	1	0	0	0	0	0
51	2015-08-31 14:25:36.377576	0	1	0	-1	1	1	0	1	0	0	-1	-1	0	0	0
52	2015-08-31 14:25:36.388935	0	-1	1	0	0	0	-1	-1	0	0	1	0	0	1	0
53	2015-08-31 14:25:36.400018	0	0	0	0	0	0	0	0	0	1	0	1	1	1	0
54	2015-08-31 14:25:36.411111	0	0	0	0	1	0	1	0	0	0	0	0	0	1	0
55	2015-08-31 14:25:36.422147	1	0	1	-1	0	-1	1	0	-1	1	1	0	1	0	0
56	2015-08-31 14:25:36.434765	0	1	0	-1	0	0	0	0	1	0	1	0	0	1	1
57	2015-08-31 14:25:36.444342	0	0	1	0	1	0	1	0	1	1	0	1	1	1	1
58	2015-08-31 14:25:36.455452	0	1	0	1	0	1	0	0	0	0	1	0	1	0	0
59	2015-08-31 14:25:36.466559	0	-1	-1	0	0	-1	0	1	0	-1	-1	-1	0	1	0
60	2015-08-31 14:25:36.477723	0	0	1	0	0	1	0	1	1	-1	0	0	1	1	1
61	2015-08-31 14:25:36.488724	0	0	1	0	1	0	1	0	0	0	1	0	0	0	0
62	2015-08-31 14:25:36.499664	1	0	0	0	0	1	0	1	0	0	-1	1	1	1	0
63	2015-08-31 14:25:36.510985	-1	0	1	0	0	0	1	0	0	1	0	0	1	0	0
64	2015-08-31 14:25:36.522076	0	-1	1	0	0	0	-1	0	0	0	-1	0	1	0	0
65	2015-08-31 14:25:36.533412	1	0	1	0	0	0	0	-1	1	1	1	0	0	1	1
66	2015-08-31 14:25:36.544204	1	0	0	1	0	0	0	1	0	0	0	0	0	0	0
67	2015-08-31 14:25:36.555366	1	0	0	0	1	0	-1	0	0	0	1	1	-1	0	1
68	2015-08-31 14:25:36.566389	1	1	0	0	0	0	0	1	0	0	0	0	0	1	0
69	2015-08-31 14:25:36.577553	0	0	0	1	1	0	0	1	0	0	1	0	0	0	-1
70	2015-08-31 14:25:36.588626	0	1	0	1	0	0	0	0	0	1	0	0	0	1	0
71	2015-08-31 14:25:36.599738	0	-1	1	0	1	1	0	0	0	-1	1	1	1	1	-1
72	2015-08-31 14:25:36.610792	1	0	1	1	-1	1	-1	0	0	0	0	-1	0	0	0
73	2015-08-31 14:25:36.621896	0	1	0	1	0	0	0	0	1	0	0	0	0	0	-1
74	2015-08-31 14:25:36.633019	-1	0	0	1	0	1	0	0	1	0	0	0	0	0	0
75	2015-08-31 14:25:36.644084	0	1	-1	1	0	-1	0	1	0	0	1	1	0	0	1
76	2015-08-31 14:25:36.655186	0	0	1	-1	0	1	0	0	0	0	0	1	0	0	0
77	2015-08-31 14:25:36.666306	0	0	1	0	1	0	0	0	0	1	1	0	1	-1	0
78	2015-08-31 14:25:36.67739	0	0	1	0	1	0	0	1	1	-1	1	0	0	1	0
79	2015-08-31 14:25:36.688461	0	0	0	0	0	0	0	0	0	0	0	1	0	1	0
80	2015-08-31 14:25:36.699555	1	1	0	1	1	1	0	0	0	1	1	0	0	1	-1
81	2015-08-31 14:25:36.71066	-1	0	1	0	1	-1	1	0	0	1	0	0	0	1	0
82	2015-08-31 14:25:36.722022	0	0	0	0	1	0	0	0	0	0	1	1	1	0	-1
83	2015-08-31 14:25:36.732644	1	1	0	0	1	0	1	0	1	0	0	0	0	0	0
84	2015-08-31 14:25:36.743901	0	0	0	1	0	-1	1	1	1	0	0	-1	0	0	0
85	2015-08-31 14:25:36.754808	0	0	0	1	-1	1	0	0	1	0	0	0	0	1	1
86	2015-08-31 14:25:36.766465	0	-1	0	0	0	0	0	-1	0	0	0	0	0	0	0
87	2015-08-31 14:25:36.777068	0	0	0	1	0	0	0	1	0	1	0	1	-1	0	0
88	2015-08-31 14:25:36.78818	0	0	0	0	-1	0	0	1	1	1	0	0	1	1	0
89	2015-08-31 14:25:36.799277	0	0	1	1	0	0	1	0	0	0	0	0	0	1	0
90	2015-08-31 14:25:36.810294	0	-1	0	0	0	1	0	0	0	1	1	1	0	1	0
91	2015-08-31 14:25:36.821439	1	-1	0	0	1	0	0	0	1	1	0	0	0	1	-1
92	2015-08-31 14:25:36.832568	0	1	0	0	0	0	0	1	1	1	0	0	0	0	0
93	2015-08-31 14:25:36.843629	0	0	0	1	0	0	-1	0	0	1	0	0	1	0	0
94	2015-08-31 14:25:36.854771	0	0	0	0	1	0	0	0	0	1	0	-1	1	0	-1
95	2015-08-31 14:25:36.865813	0	0	0	0	0	0	0	-1	0	0	0	0	0	0	0
96	2015-08-31 14:25:36.877117	1	0	0	0	0	1	1	-1	0	0	0	0	1	0	-1
97	2015-08-31 14:25:36.888151	1	1	1	1	1	0	0	-1	1	-1	0	1	1	0	1
98	2015-08-31 14:25:36.899307	0	0	1	1	1	1	0	0	0	0	0	0	0	0	0
99	2015-08-31 14:25:36.910408	0	0	1	0	1	-1	0	0	0	1	0	1	1	0	1
100	2015-08-31 14:25:36.921473	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
\.


--
-- TOC entry 2001 (class 0 OID 0)
-- Dependencies: 170
-- Name: ratings_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ratings_user_id_seq', 135, true);


--
-- TOC entry 1881 (class 2606 OID 16482)
-- Name: books_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY books
    ADD CONSTRAINT books_pkey PRIMARY KEY (book_id);


--
-- TOC entry 1879 (class 2606 OID 16474)
-- Name: ratings_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ratings
    ADD CONSTRAINT ratings_pkey PRIMARY KEY (user_id);


--
-- TOC entry 1998 (class 0 OID 0)
-- Dependencies: 5
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2015-10-02 21:02:17 CEST

--
-- PostgreSQL database dump complete
--

