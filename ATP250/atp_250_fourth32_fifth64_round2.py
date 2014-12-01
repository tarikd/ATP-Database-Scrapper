# coding: utf-8

from bs4 import BeautifulSoup
import requests
import sys
import os
import shutil
import argparse

sys.setrecursionlimit(30000)


tournamentList = ['301', '338', '505', '5053', '316', '423', '341', '1720', '6003', '339', '891', '451', '5012', '2276', '533', '424', '506', '496', '499', '360', '717', '468', '308', '306', '500', '741', '440', '315', '321', '419', '314', '439', '773', '438', '429', '568', '375', '337', '3348', '311']

#ATP 250 P1
#tournamentList = ['301', '338', '505', '5053', '316', '423', '341', '1720', '6003']
#ATP 250 P2
#tournamentList = ['339', '891', '451', '5012', '2276', '533', '424', '506', '496', '499']
#ATP 250 P3
#tournamentList = ['360', '717', '468', '308', '306', '500', '741', '440', '315', '321', '419']
#ATP 250 P4
#tournamentList = ['314', '439', '773', '438', '429', '568', '375', '337', '3348', '311']


atp_weeks_list = ['17.02.2014', '10.02.2014', '03.02.2014', '27.01.2014', '13.01.2014', '06.01.2014', '30.12.2013', '23.12.2013', '16.12.2013', '09.12.2013', '02.12.2013', '25.11.2013', '18.11.2013', '11.11.2013', '04.11.2013', '28.10.2013', '21.10.2013', '14.10.2013', '07.10.2013', '30.09.2013', '23.09.2013', '16.09.2013', '09.09.2013', '26.08.2013', '19.08.2013', '12.08.2013', '05.08.2013', '29.07.2013', '22.07.2013', '15.07.2013', '08.07.2013', '24.06.2013', '17.06.2013', '10.06.2013', '27.05.2013', '20.05.2013', '13.05.2013', '06.05.2013', '29.04.2013', '22.04.2013', '15.04.2013', '08.04.2013', '01.04.2013', '18.03.2013', '04.03.2013', '25.02.2013', '18.02.2013', '11.02.2013', '04.02.2013', '28.01.2013', '14.01.2013', '07.01.2013', '31.12.2012', '24.12.2012', '17.12.2012', '10.12.2012', '03.12.2012', '26.11.2012', '19.11.2012', '12.11.2012', '05.11.2012', '29.10.2012', '22.10.2012', '15.10.2012', '08.10.2012', '01.10.2012', '24.09.2012', '17.09.2012', '10.09.2012', '27.08.2012', '20.08.2012', '13.08.2012', '06.08.2012', '30.07.2012', '23.07.2012', '16.07.2012', '09.07.2012', '25.06.2012', '18.06.2012', '11.06.2012', '28.05.2012', '21.05.2012', '14.05.2012', '07.05.2012', '30.04.2012', '23.04.2012', '16.04.2012', '09.04.2012', '02.04.2012', '19.03.2012', '05.03.2012', '27.02.2012', '20.02.2012', '13.02.2012', '06.02.2012', '30.01.2012', '16.01.2012', '09.01.2012', '02.01.2012', '26.12.2011', '19.12.2011', '12.12.2011', '05.12.2011', '28.11.2011', '21.11.2011', '14.11.2011', '07.11.2011', '31.10.2011', '24.10.2011', '17.10.2011', '10.10.2011', '03.10.2011', '26.09.2011', '19.09.2011', '12.09.2011', '29.08.2011', '22.08.2011', '15.08.2011', '08.08.2011', '01.08.2011', '25.07.2011', '18.07.2011', '11.07.2011', '04.07.2011', '20.06.2011', '13.06.2011', '06.06.2011', '23.05.2011', '16.05.2011', '09.05.2011', '02.05.2011', '25.04.2011', '18.04.2011', '11.04.2011', '04.04.2011', '21.03.2011', '07.03.2011', '28.02.2011', '21.02.2011', '14.02.2011', '07.02.2011', '31.01.2011', '17.01.2011', '10.01.2011', '03.01.2011', '27.12.2010', '20.12.2010', '13.12.2010', '06.12.2010', '29.11.2010', '22.11.2010', '15.11.2010', '08.11.2010', '01.11.2010', '25.10.2010', '18.10.2010', '11.10.2010', '04.10.2010', '27.09.2010', '20.09.2010', '13.09.2010', '06.09.2010', '30.08.2010', '23.08.2010', '16.08.2010', '09.08.2010', '02.08.2010', '26.07.2010', '19.07.2010', '12.07.2010', '05.07.2010', '28.06.2010', '21.06.2010', '14.06.2010', '07.06.2010', '31.05.2010', '24.05.2010', '17.05.2010', '10.05.2010', '03.05.2010', '26.04.2010', '19.04.2010', '12.04.2010', '05.04.2010', '29.03.2010', '22.03.2010', '15.03.2010', '08.03.2010', '01.03.2010', '22.02.2010', '15.02.2010', '08.02.2010', '01.02.2010', '25.01.2010', '18.01.2010', '11.01.2010', '04.01.2010', '28.12.2009', '21.12.2009', '14.12.2009', '07.12.2009', '30.11.2009', '23.11.2009', '16.11.2009', '09.11.2009', '02.11.2009', '26.10.2009', '19.10.2009', '12.10.2009', '05.10.2009', '28.09.2009', '21.09.2009', '14.09.2009', '07.09.2009', '31.08.2009', '24.08.2009', '17.08.2009', '10.08.2009', '03.08.2009', '27.07.2009', '20.07.2009', '13.07.2009', '06.07.2009', '29.06.2009', '22.06.2009', '15.06.2009', '08.06.2009', '01.06.2009', '25.05.2009', '18.05.2009', '11.05.2009', '04.05.2009', '27.04.2009', '20.04.2009', '13.04.2009', '06.04.2009', '30.03.2009', '23.03.2009', '16.03.2009', '09.03.2009', '02.03.2009', '23.02.2009', '16.02.2009', '09.02.2009', '02.02.2009', '26.01.2009', '19.01.2009', '12.01.2009', '05.01.2009', '29.12.2008', '22.12.2008', '15.12.2008', '08.12.2008', '01.12.2008', '24.11.2008', '17.11.2008', '10.11.2008', '03.11.2008', '27.10.2008', '20.10.2008', '13.10.2008', '06.10.2008', '29.09.2008', '22.09.2008', '15.09.2008', '08.09.2008', '01.09.2008', '25.08.2008', '18.08.2008', '11.08.2008', '04.08.2008', '28.07.2008', '21.07.2008', '14.07.2008', '07.07.2008', '30.06.2008', '23.06.2008', '16.06.2008', '09.06.2008', '02.06.2008', '26.05.2008', '19.05.2008', '12.05.2008', '05.05.2008', '28.04.2008', '21.04.2008', '14.04.2008', '07.04.2008', '31.03.2008', '24.03.2008', '17.03.2008', '10.03.2008', '03.03.2008', '25.02.2008', '18.02.2008', '11.02.2008', '04.02.2008', '28.01.2008', '21.01.2008', '14.01.2008', '07.01.2008', '31.12.2007', '24.12.2007', '17.12.2007', '10.12.2007', '03.12.2007', '26.11.2007', '19.11.2007', '12.11.2007', '05.11.2007', '29.10.2007', '22.10.2007', '15.10.2007', '08.10.2007', '01.10.2007', '24.09.2007', '17.09.2007', '10.09.2007', '03.09.2007', '27.08.2007', '20.08.2007', '13.08.2007', '06.08.2007', '30.07.2007', '23.07.2007', '16.07.2007', '09.07.2007', '02.07.2007', '25.06.2007', '18.06.2007', '11.06.2007', '04.06.2007', '28.05.2007', '21.05.2007', '14.05.2007', '07.05.2007', '30.04.2007', '23.04.2007', '16.04.2007', '09.04.2007', '02.04.2007', '26.03.2007', '19.03.2007', '12.03.2007', '05.03.2007', '26.02.2007', '19.02.2007', '12.02.2007', '05.02.2007', '29.01.2007', '22.01.2007', '15.01.2007', '08.01.2007', '01.01.2007', '25.12.2006', '18.12.2006', '11.12.2006', '04.12.2006', '27.11.2006', '20.11.2006', '13.11.2006', '06.11.2006', '30.10.2006', '23.10.2006', '16.10.2006', '09.10.2006', '02.10.2006', '25.09.2006', '18.09.2006', '11.09.2006', '04.09.2006', '28.08.2006', '21.08.2006', '14.08.2006', '07.08.2006', '31.07.2006', '24.07.2006', '17.07.2006', '10.07.2006', '03.07.2006', '26.06.2006', '19.06.2006', '12.06.2006', '05.06.2006', '29.05.2006', '22.05.2006', '15.05.2006', '08.05.2006', '01.05.2006', '24.04.2006', '17.04.2006', '10.04.2006', '03.04.2006', '27.03.2006', '20.03.2006', '13.03.2006', '06.03.2006', '27.02.2006', '20.02.2006', '13.02.2006', '06.02.2006', '30.01.2006', '23.01.2006', '16.01.2006', '09.01.2006', '02.01.2006', '26.12.2005', '19.12.2005', '12.12.2005', '05.12.2005', '28.11.2005', '21.11.2005', '14.11.2005', '07.11.2005', '31.10.2005', '24.10.2005', '17.10.2005', '10.10.2005', '03.10.2005', '26.09.2005', '19.09.2005', '12.09.2005', '05.09.2005', '29.08.2005', '22.08.2005', '15.08.2005', '08.08.2005', '01.08.2005', '25.07.2005', '18.07.2005', '11.07.2005', '04.07.2005', '27.06.2005', '20.06.2005', '13.06.2005', '06.06.2005', '30.05.2005', '23.05.2005', '16.05.2005', '09.05.2005', '02.05.2005', '25.04.2005', '18.04.2005', '11.04.2005', '04.04.2005', '28.03.2005', '21.03.2005', '14.03.2005', '07.03.2005', '28.02.2005', '21.02.2005', '14.02.2005', '07.02.2005', '31.01.2005', '24.01.2005', '17.01.2005', '10.01.2005', '03.01.2005', '27.12.2004', '20.12.2004', '13.12.2004', '06.12.2004', '29.11.2004', '22.11.2004', '15.11.2004', '08.11.2004', '01.11.2004', '25.10.2004', '18.10.2004', '11.10.2004', '04.10.2004', '27.09.2004', '20.09.2004', '13.09.2004', '06.09.2004', '30.08.2004', '23.08.2004', '16.08.2004', '09.08.2004', '02.08.2004', '26.07.2004', '19.07.2004', '12.07.2004', '05.07.2004', '28.06.2004', '21.06.2004', '14.06.2004', '07.06.2004', '31.05.2004', '24.05.2004', '17.05.2004', '10.05.2004', '03.05.2004', '26.04.2004', '19.04.2004', '12.04.2004', '05.04.2004', '29.03.2004', '22.03.2004', '15.03.2004', '08.03.2004', '01.03.2004', '23.02.2004', '16.02.2004', '09.02.2004', '02.02.2004', '26.01.2004', '19.01.2004', '12.01.2004', '05.01.2004', '29.12.2003', '22.12.2003', '15.12.2003', '08.12.2003', '01.12.2003', '24.11.2003', '17.11.2003', '10.11.2003', '03.11.2003', '27.10.2003', '20.10.2003', '13.10.2003', '06.10.2003', '29.09.2003', '22.09.2003', '15.09.2003', '08.09.2003', '01.09.2003', '25.08.2003', '18.08.2003', '11.08.2003', '04.08.2003', '28.07.2003', '21.07.2003', '14.07.2003', '07.07.2003', '30.06.2003', '23.06.2003', '16.06.2003', '09.06.2003', '02.06.2003', '26.05.2003', '19.05.2003', '12.05.2003', '05.05.2003', '28.04.2003', '21.04.2003', '14.04.2003', '07.04.2003', '31.03.2003', '24.03.2003', '17.03.2003', '10.03.2003', '03.03.2003', '24.02.2003', '17.02.2003', '10.02.2003', '03.02.2003', '27.01.2003', '20.01.2003', '13.01.2003', '06.01.2003', '30.12.2002', '23.12.2002', '16.12.2002', '09.12.2002', '02.12.2002', '25.11.2002', '18.11.2002', '11.11.2002', '04.11.2002', '28.10.2002', '21.10.2002', '14.10.2002', '07.10.2002', '30.09.2002', '23.09.2002', '16.09.2002', '09.09.2002', '02.09.2002', '26.08.2002', '19.08.2002', '12.08.2002', '05.08.2002', '29.07.2002', '22.07.2002', '15.07.2002', '08.07.2002', '01.07.2002', '24.06.2002', '17.06.2002', '10.06.2002', '03.06.2002', '27.05.2002', '20.05.2002', '13.05.2002', '06.05.2002', '29.04.2002', '22.04.2002', '15.04.2002', '08.04.2002', '01.04.2002', '25.03.2002', '18.03.2002', '11.03.2002', '04.03.2002', '25.02.2002', '18.02.2002', '11.02.2002', '04.02.2002', '28.01.2002', '21.01.2002', '14.01.2002', '07.01.2002', '31.12.2001', '24.12.2001', '17.12.2001', '10.12.2001', '03.12.2001', '26.11.2001', '19.11.2001', '12.11.2001', '05.11.2001', '29.10.2001', '22.10.2001', '15.10.2001', '08.10.2001', '01.10.2001', '24.09.2001', '17.09.2001', '10.09.2001', '03.09.2001', '27.08.2001', '20.08.2001', '13.08.2001', '06.08.2001', '30.07.2001', '23.07.2001', '16.07.2001', '09.07.2001', '02.07.2001', '25.06.2001', '18.06.2001', '11.06.2001', '04.06.2001', '28.05.2001', '21.05.2001', '14.05.2001', '07.05.2001', '30.04.2001', '23.04.2001', '16.04.2001', '09.04.2001', '02.04.2001', '26.03.2001', '19.03.2001', '12.03.2001', '05.03.2001', '26.02.2001', '19.02.2001', '12.02.2001', '05.02.2001', '29.01.2001', '22.01.2001', '15.01.2001', '08.01.2001', '01.01.2001', '25.12.2000', '18.12.2000', '11.12.2000', '04.12.2000', '27.11.2000', '20.11.2000', '13.11.2000', '06.11.2000', '30.10.2000', '23.10.2000', '16.10.2000', '09.10.2000', '02.10.2000', '25.09.2000', '18.09.2000', '11.09.2000', '04.09.2000', '28.08.2000', '21.08.2000', '14.08.2000', '07.08.2000', '31.07.2000', '24.07.2000', '17.07.2000', '10.07.2000', '03.07.2000', '26.06.2000', '19.06.2000', '12.06.2000', '05.06.2000', '29.05.2000', '22.05.2000', '15.05.2000', '08.05.2000', '01.05.2000', '24.04.2000', '17.04.2000', '10.04.2000', '03.04.2000', '27.03.2000', '20.03.2000', '13.03.2000', '06.03.2000', '28.02.2000', '21.02.2000', '14.02.2000', '07.02.2000', '31.01.2000', '24.01.2000', '17.01.2000', '10.01.2000', '27.12.1999', '20.12.1999', '13.12.1999', '06.12.1999', '29.11.1999', '22.11.1999', '15.11.1999', '08.11.1999', '01.11.1999', '25.10.1999', '18.10.1999', '11.10.1999', '04.10.1999', '27.09.1999', '20.09.1999', '13.09.1999', '06.09.1999', '30.08.1999', '23.08.1999', '16.08.1999', '09.08.1999', '02.08.1999', '26.07.1999', '19.07.1999', '12.07.1999', '05.07.1999', '28.06.1999', '21.06.1999', '14.06.1999', '07.06.1999', '31.05.1999', '24.05.1999', '17.05.1999', '10.05.1999', '03.05.1999', '26.04.1999', '19.04.1999', '12.04.1999', '05.04.1999', '29.03.1999', '22.03.1999', '15.03.1999', '08.03.1999', '01.03.1999', '22.02.1999', '15.02.1999', '08.02.1999', '01.02.1999', '25.01.1999', '18.01.1999', '11.01.1999', '04.01.1999', '28.12.1998', '21.12.1998', '14.12.1998', '07.12.1998', '30.11.1998', '23.11.1998', '16.11.1998', '09.11.1998', '02.11.1998', '26.10.1998', '19.10.1998', '12.10.1998', '05.10.1998', '28.09.1998', '21.09.1998', '14.09.1998', '07.09.1998', '31.08.1998', '24.08.1998', '17.08.1998', '10.08.1998', '03.08.1998', '27.07.1998', '20.07.1998', '13.07.1998', '06.07.1998', '29.06.1998', '22.06.1998', '15.06.1998', '08.06.1998', '01.06.1998', '25.05.1998', '18.05.1998', '11.05.1998', '04.05.1998', '27.04.1998', '20.04.1998', '13.04.1998', '06.04.1998', '30.03.1998', '23.03.1998', '16.03.1998', '09.03.1998', '02.03.1998', '23.02.1998', '16.02.1998', '09.02.1998', '02.02.1998', '26.01.1998', '19.01.1998', '12.01.1998', '05.01.1998', '29.12.1997', '22.12.1997', '15.12.1997', '08.12.1997', '01.12.1997', '24.11.1997', '17.11.1997', '10.11.1997', '03.11.1997', '27.10.1997', '20.10.1997', '13.10.1997', '06.10.1997', '29.09.1997', '22.09.1997', '15.09.1997', '08.09.1997', '01.09.1997', '25.08.1997', '18.08.1997', '11.08.1997', '04.08.1997', '28.07.1997', '21.07.1997', '14.07.1997', '07.07.1997', '30.06.1997', '23.06.1997', '16.06.1997', '09.06.1997', '02.06.1997', '26.05.1997', '19.05.1997', '12.05.1997', '05.05.1997', '28.04.1997', '21.04.1997', '14.04.1997', '07.04.1997', '31.03.1997', '24.03.1997', '17.03.1997', '10.03.1997', '03.03.1997', '24.02.1997', '17.02.1997', '10.02.1997', '03.02.1997', '27.01.1997', '20.01.1997', '13.01.1997', '06.01.1997', '30.12.1996', '23.12.1996', '16.12.1996', '09.12.1996', '02.12.1996', '25.11.1996', '18.11.1996', '11.11.1996', '04.11.1996', '28.10.1996', '21.10.1996', '14.10.1996', '07.10.1996', '30.09.1996', '23.09.1996', '16.09.1996', '09.09.1996', '02.09.1996', '26.08.1996', '19.08.1996', '12.08.1996', '05.08.1996', '29.07.1996', '22.07.1996', '15.07.1996', '08.07.1996', '01.07.1996', '24.06.1996', '17.06.1996', '10.06.1996', '03.06.1996', '27.05.1996', '20.05.1996', '13.05.1996', '06.05.1996', '29.04.1996', '22.04.1996', '15.04.1996', '08.04.1996', '01.04.1996', '25.03.1996', '18.03.1996', '11.03.1996', '04.03.1996', '26.02.1996', '19.02.1996', '12.02.1996', '05.02.1996', '29.01.1996', '22.01.1996', '15.01.1996', '08.01.1996', '01.01.1996', '25.12.1995', '18.12.1995']


#########################################################################################################################

#if tournamentId

#########################################################################################################################

# Fonction qui renvoie le html parsé
def make_soup(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    return soup

# Fonction qui récupère le nom du tournoi
def get_tournament_title(soup):
    try:
        title = soup.find("a", "tournamentTitle").string.encode('utf-8')
        return title
    except AttributeError:
        try:
            title = soup.find("span", "tournamentTitle")
            clean_title = title.find("strong").string
            return clean_title
        except AttributeError:
            return None

# Fonction qui récupère le lieu du tournoi
def get_tournament_location(soup):
    location = soup.find("p", "tournamentSubTitle").string.split(" -")[0]
    return location

# Fonction qui récupère la date de début et de fin du tournoi
def get_tournament_date(soup):
    try:
        date = soup.find("p", "tournamentSubTitle").string.split("- ")[1]
        debut = date.split("-")[0].encode('utf-8')
        fin = date.split("-")[1].encode('utf-8')
        return debut, fin
    except AttributeError:
        no = 2
        return no

# Fonction qui récupère le type de surface
def get_tournament_surface(soup):
    inlineWrapper = soup.find("span", "inlineWrapper")
    surface = inlineWrapper.findAll("p")[1]
    surface = str(surface).split(">")[3]
    surface = surface.split("<")[0]
    return surface

# Fonction qui récupère la dotation du tournoi
def get_tournament_prizemoney(soup):
    inlineWrapper = soup.find("span", "inlineWrapper")
    prizemoney = inlineWrapper.findAll("p")[2]
    prizemoney = str(prizemoney).split(">")[3]
    prizemoney = prizemoney.split("<")[0]
    return prizemoney

# Fonction qui récupère la taille du tournoi
def get_tournament_draw(soup):
    try:
        inlineWrapper = soup.find("span", "inlineWrapper")
        draw = inlineWrapper.findAll("p")[0]
        draw = str(draw).split(">")[3]
        draw = draw.split("<")[0]
        return int(draw)
    except AttributeError:
        no = 2
        return no

################################################################################################################

# # Fonction qui récupère le nom des joueurs dans le classement parsé et les renvoies dans une liste
# def get_players_name(soup): #, soup3):
#     html = str(soup.findAll("td", "first"))
#     #html3 = str(soup3.findAll("td", "first"))
#     soup = BeautifulSoup(html, "html.parser")
#     #soup3 = BeautifulSoup(html3, "html.parser")
#     list_players_name = []
#     for rank in soup.findAll("a"):
#         list_players_name.append(rank.string.encode('utf-8'))
#     # for rank in soup3.findAll("a"):
#     #     list_players_name.append(rank.string.encode('utf-8'))
#     # return list_players_name

# # Fonction qui produit un dictionaire dont la clé est le nom du joueur et la valeur son classement, elle renvoie le classement du joueur
# def get_player_specific_rank(soup, player): # soup3):
#     dico = {}
#     dico.clear()
#     i = 0
#     rank = 1
#     while i < len(get_players_name(soup)):
#         name = get_players_name(soup)[i].replace("\xc2\xa0", " ")
#         dico.update({name : rank})
#         i+=1
#         rank+=1
#     return dico[player]


def get_player_specific_rank(soup, player): #, soup3):
    try:
        html = str(soup.findAll("td", "first"))
        #html3 = str(soup3.findAll("td", "first"))
        soup = BeautifulSoup(html, "html.parser")
        #soup3 = BeautifulSoup(html3, "html.parser")
        list_players_name = []
        dico = {}
        dico.clear()
        i = 1
        for rank in soup.findAll("a"):
            name = rank.string.encode('utf-8').replace("\xc2\xa0", " ")
            dico.update({name : i})
            i+=1

        rank = dico[player]
        return rank
    except KeyError:
        rank = "X"
        print "Le joueur n'est pas dans le top 100."
        return rank


def get_player_specific_nation(soup, player): #, soup3):
    try:
        html = str(soup.findAll("td", "first"))
        #html3 = str(soup3.findAll("td", "first"))
        soup = BeautifulSoup(html, "html.parser")
        #soup3 = BeautifulSoup(html3, "html.parser")

        liste = []
        for nat in soup:
            liste.append(nat)

        liste_country = []
        i = 3
        while i < len(liste):
            country = str(liste[i]).split("</a>\xc2\xa0(")[1].split(")")[0]
            liste_country.append(country)
            i+=2

        list_players_name = []
        dico = {}
        dico.clear()
        i = 0
        for rank in soup.findAll("a"):
            name = rank.string.encode('utf-8').replace("\xc2\xa0", " ")
            dico.update({name : liste_country[i]})
            i+=1

        nation = dico[player]
        return nation
    except KeyError:
        nation = "X"
        print "Le joueur n'est pas dans le top 100, impossible d'avoir sa nationalité."
        return nation


#################################################################################################################

# Parfois la date de publication du classement ne coincide pas avec la date de début du tournoi, on test alors différentes dates avec une amplitude de 4 jours
# Dès qu'une date coïncide, on la renvoi et on l'utilise pour former l'URL du classement que l'on veut parsé (car il est le plus proche de la date du tournoi)
def get_closest_tournament_date(soup):
    date1 = str(int(get_tournament_date(soup)[0].split(".")[0])+1)+"."+get_tournament_date(soup)[0].split(".", 1)[1]
    date2 = str(int(get_tournament_date(soup)[0].split(".")[0])+2)+"."+get_tournament_date(soup)[0].split(".", 1)[1]
    date3 = str(int(get_tournament_date(soup)[0].split(".")[0])+3)+"."+get_tournament_date(soup)[0].split(".", 1)[1]
    date4 = str(int(get_tournament_date(soup)[0].split(".")[0])+4)+"."+get_tournament_date(soup)[0].split(".", 1)[1]
    if get_tournament_date(soup)[0] in atp_weeks_list:
        return get_tournament_date(soup)[0]
    elif date1 in atp_weeks_list:
        return date1
    elif date2 in atp_weeks_list:
        return date2
    elif date3 in atp_weeks_list:
        return date3
    elif date4 in atp_weeks_list:
        return date4

######################################################################################################

# Fonction qui récupère le nom des deux finalistes si c'est un grand chelem
# Sinon elle renvoie une liste contenant pour seul élément le gagnant du tournoi
def get_player_name_third_round_winner32(soup):
    colonne4 = soup.find("td", "col_4")
    playerWrap = colonne4.findAll("div", "playerWrap")
    list_winner_third_round = []
    for name in playerWrap:
        list_winner_third_round.append(name.a.string)
    return list_winner_third_round

def get_player_name_fourth_round_winner64(soup):
    colonne5 = soup.find("td", "col_5")
    playerWrap = colonne5.findAll("div", "playerWrap")
    list_winner_fourth_round = []
    for name in playerWrap:
        list_winner_fourth_round.append(name.a.string)
    return list_winner_fourth_round

######################################################################################################

# def get_fifth_round_winner(soup):
#     colonne5 = soup.find("td", "col_5")

#     player = colonne5.find("div", "playerWrap")
#     score = colonne5.find("div", "scores")

#     return player.a.string, score.a.string

def get_fourth_round_winner32(soup):
    colonne5 = soup.find("td", "col_5")
    player = colonne5.findAll("div", "playerWrap")
    scores = colonne5.findAll("div", "scores")

    list_name_winner_fourth_round = []
    list_score_winner_fourth_round = []

    for name in player:
        list_name_winner_fourth_round.append(name.a.string)
    for score in scores:
        list_score_winner_fourth_round.append(score.a.string)

    return list_score_winner_fourth_round, list_name_winner_fourth_round

def get_fifth_round_winner64(soup):
    colonne6 = soup.find("td", "col_6")
    player = colonne6.findAll("div", "playerWrap")
    scores = colonne6.findAll("div", "scores")

    list_name_winner_fifth_round = []
    list_score_winner_fifth_round = []

    for name in player:
        list_name_winner_fifth_round.append(name.a.string)
    for score in scores:
        list_score_winner_fifth_round.append(score.a.string)

    return list_score_winner_fifth_round, list_name_winner_fifth_round

######################################################################################################

# URL de base pour construire l'url permettant de récupérer les draws des tournois
BASE_URL_NAME = "http://www.atpworldtour.com/Share/Event-Draws.aspx?e="

# Boucle qui parcours toutes la liste des tournois de tennis qui existent
l = 0
while l < len(tournamentList):

    tournamentId = tournamentList[l] # On récupére l'identifiant d'un tournoi spécifique pour construire l'URL

    print tournamentId

    # On construit une liste d'URL spécifique à un tournoi pour la période s'étendant de 1996 à 2014
    tournamentYear_urls = [BASE_URL_NAME + str(tournamentId) + "&y=" + str(year) for year in range(1996,2014)]

    ######################################################################################################
    tournamentYear_urls_clean = []
    for tournamentYear_url in tournamentYear_urls:
        soup = make_soup(tournamentYear_url)
        if get_tournament_title(soup) != None:
            tournamentYear_urls_clean.append(tournamentYear_url)


    ######################################################################################################
    print tournamentYear_urls_clean
    # On parse cette page arbitrairement choisie
    soup = make_soup(tournamentYear_urls_clean[len(tournamentYear_urls_clean)-1])

    ######################################################################################################

    # On vérifie que le dossier du tournoi existe, sinon on le crée
    # if not os.path.exists(get_tournament_title(soup)):
    #     os.makedirs(get_tournament_title(soup))

    ######################################################################################################

    tournamentYear_urls32 = []
    tournamentYear_urls64 = []
    for tournamentYear_url in tournamentYear_urls_clean:
        soup = make_soup(tournamentYear_url)
        if get_tournament_draw(soup) == 32:
            tournamentYear_urls32.append(tournamentYear_url)
        elif get_tournament_draw(soup) == 64:
            tournamentYear_urls64.append(tournamentYear_url)
    
    print tournamentYear_urls
    print "32"
    print tournamentYear_urls32
    print "64"
    print tournamentYear_urls64

    r32 = 0
    while r32 < len(tournamentYear_urls32):
        mon_fichier = open("atp250_1996_2013", "a")

        ######################################################################################################
        # On parse cette page arbitrairement choisie
        soup = make_soup(tournamentYear_urls32[len(tournamentYear_urls32)-1])

        ######################################################################################################

        # On écrit au début du fichier le nom du tournoi, le lieu où se déroule le tournoi et le type de surface
        name_tournament = get_tournament_title(soup)
        tournament_location = get_tournament_location(soup)
        surface = str(get_tournament_surface(soup))

        # on écrit la légende de nos colonnes
        # mon_fichier.write('{ANNEE:<15} {PRIZEMONEY:<15} {TOUR:<15} {RANK1:<5} {JOUEUR1:<25} {NATION1:<10} {RANK2:<5} {JOUEUR2:<25} {NATION2:<10} {GAGNANT:<25} {SCORE}'.format(
        #     ANNEE="ANNEE",
        #     PRIZEMONEY="PRIZEMONEY",
        #     TOUR="TOUR",
        #     RANK1="RANK1",
        #     JOUEUR1="JOUEUR1",
        #     NATION1="NATION1",
        #     RANK2="RANK2",
        #     JOUEUR2="JOUEUR2",
        #     NATION2="NATION2",
        #     GAGNANT="GAGNANT",
        #     SCORE="SCORE"))
        # mon_fichier.write("\n\n")

        # On traite un même tournoi de 1996 à 2014 en utilisant notre liste d'URL
        tournamentYear = 1996
        for tournamentYear_url in tournamentYear_urls32:

            # On parse la page spécifique à un tournoi et un année précise
            soup = make_soup(tournamentYear_url)


            third_round_winner = get_player_name_third_round_winner32(soup)
            size = get_fourth_round_winner32(soup)
            winner, score = get_fourth_round_winner32(soup)
            draw = get_tournament_draw(soup)
            round_name = "Fourth Round"
            file_name = "_Fourth_Round"

            if get_tournament_date(soup) != 2 or get_tournament_draw(soup) != 2:

                ############################################
                # On construit une url menant au classement atp qui coïncide le plus avec le tournoi (100premiers)
                URL2 = "http://www.atpworldtour.com/Rankings/Singles.aspx?d=" + str(get_closest_tournament_date(soup))
                
                # # On construit une url menant au classement atp qui coïncide le plus avec le tournoi (101 - 200)
                # URL3 = "http://www.atpworldtour.com/Rankings/Singles.aspx?d=" + get_closest_tournament_date(soup) + "&r=101"

                print URL2

                # On parse la page spécifique au classement qui coïncide le plus avec le tournoi (1 - 100)
                soup2 = make_soup(URL2)

                # # On parse la page spécifique au classement qui coïncide le plus avec le tournoi (101 - 200)
                # soup3 = make_soup(URL3)

                ############################################

                i = 0
                j = 0

                # Le nombre de gagnant étant égale au nombre de match jouer, on boucle sur ce nombre qui sera le nombre de lignes produites
                while i < len(size):
                    player1 = third_round_winner[j]
                    player2 = third_round_winner[j+1]
                    nation1 = get_player_specific_nation(soup2, player1)
                    nation2 = get_player_specific_nation(soup2, player2)
                    #winner, score = get_fourth_round_winner32(soup)
                    prize = get_tournament_prizemoney(soup)
                    rank1 = get_player_specific_rank(soup2, player1)
                    rank2 = get_player_specific_rank(soup2, player2)
                    mon_fichier.write('{Tournament};{Draw};{Location};{Surface};{tournamentYear};{Prize};{Round};{Rank1};{Player1};{Nation1};{Rank2};{Player2};{Nation2};{Gagnant};{Score}'.format(
                        Tournament=name_tournament,
                        Location=tournament_location,
                        Surface=surface,
                        Draw=draw,
                        tournamentYear=get_tournament_date(soup)[0],
                        Prize=prize, 
                        Round=round_name,
                        Rank1=rank1,
                        Player1=player1,
                        Nation1=nation1,
                        Rank2=rank2,
                        Player2=player2,
                        Nation2=nation2,
                        Gagnant=winner[i], 
                        Score=score[i]))
                    mon_fichier.write("\n")        
                    i+=1
                    j+=2
                tournamentYear+=1
                r32+=1

            else:
                tournamentYear+=1
                r32+=1

        # # On vérifie si le fichier existe, si c'est le cas on le supprime
        # myfile = get_tournament_title(soup)+"/"+get_tournament_title(soup)+file_name

        # if os.path.isfile(myfile):
        #     os.remove(myfile)

        # # On déplace le fichier produit dans le dossier du tournoi
        # shutil.move(get_tournament_title(soup)+file_name, get_tournament_title(soup)+"/")


    ######################################################################################################

    r64 = 0
    while r64 < len(tournamentYear_urls64):
        mon_fichier = open("atp250_1996_2013", "a")

        ######################################################################################################
        # On parse cette page arbitrairement choisie
        soup = make_soup(tournamentYear_urls64[len(tournamentYear_urls64)-1])

        ######################################################################################################

        # On écrit au début du fichier le nom du tournoi, le lieu où se déroule le tournoi et le type de surface
        name_tournament = get_tournament_title(soup)
        tournament_location = get_tournament_location(soup)
        surface = str(get_tournament_surface(soup))

        # on écrit la légende de nos colonnes
        # mon_fichier.write('{ANNEE:<15} {PRIZEMONEY:<15} {TOUR:<15} {RANK1:<5} {JOUEUR1:<25} {NATION1:<10} {RANK2:<5} {JOUEUR2:<25} {NATION2:<10} {GAGNANT:<25} {SCORE}'.format(
        #     ANNEE="ANNEE",
        #     PRIZEMONEY="PRIZEMONEY",
        #     TOUR="TOUR",
        #     RANK1="RANK1",
        #     JOUEUR1="JOUEUR1",
        #     NATION1="NATION1",
        #     RANK2="RANK2",
        #     JOUEUR2="JOUEUR2",
        #     NATION2="NATION2",
        #     GAGNANT="GAGNANT",
        #     SCORE="SCORE"))
        # mon_fichier.write("\n\n")

        # On traite un même tournoi de 1996 à 2014 en utilisant notre liste d'URL
        tournamentYear = 1996
        for tournamentYear_url in tournamentYear_urls64:

            # On parse la page spécifique à un tournoi et un année précise
            soup = make_soup(tournamentYear_url)


            fourth_round_winner = get_player_name_fourth_round_winner64(soup)
            size = get_fifth_round_winner64(soup)
            winner, score = get_fifth_round_winner64(soup)
            draw = get_tournament_draw(soup)
            round_name = "Fifth Round"
            file_name = "_Fifth_Round64"

            if get_tournament_date(soup) != 2:

                ############################################
                # On construit une url menant au classement atp qui coïncide le plus avec le tournoi (100premiers)
                URL2 = "http://www.atpworldtour.com/Rankings/Singles.aspx?d=" + str(get_closest_tournament_date(soup))
                
                # # On construit une url menant au classement atp qui coïncide le plus avec le tournoi (101 - 200)
                # URL3 = "http://www.atpworldtour.com/Rankings/Singles.aspx?d=" + get_closest_tournament_date(soup) + "&r=101"

                print URL2

                # On parse la page spécifique au classement qui coïncide le plus avec le tournoi (1 - 100)
                soup2 = make_soup(URL2)

                # # On parse la page spécifique au classement qui coïncide le plus avec le tournoi (101 - 200)
                # soup3 = make_soup(URL3)

                ############################################

                i = 0
                j = 0

                # Le nombre de gagnant étant égale au nombre de match jouer, on boucle sur ce nombre qui sera le nombre de lignes produites
                while i < len(size):
                    player1 = fourth_round_winner[j]
                    player2 = fourth_round_winner[j+1]
                    nation1 = get_player_specific_nation(soup2, player1)
                    nation2 = get_player_specific_nation(soup2, player2)
                    #winner, score = get_fourth_round_winner32(soup)
                    prize = get_tournament_prizemoney(soup)
                    rank1 = get_player_specific_rank(soup2, player1)
                    rank2 = get_player_specific_rank(soup2, player2)
                    mon_fichier.write('{Tournament};{Draw};{Location};{Surface};{tournamentYear};{Prize};{Round};{Rank1};{Player1};{Nation1};{Rank2};{Player2};{Nation2};{Gagnant};{Score}'.format(
                        Tournament=name_tournament,
                        Location=tournament_location,
                        Surface=surface,
                        Draw=draw,
                        tournamentYear=get_tournament_date(soup)[0],
                        Prize=prize, 
                        Round=round_name,
                        Rank1=rank1,
                        Player1=player1,
                        Nation1=nation1,
                        Rank2=rank2,
                        Player2=player2,
                        Nation2=nation2,
                        Gagnant=winner[i], 
                        Score=score[i]))
                    mon_fichier.write("\n")        
                    i+=1
                    j+=2
                tournamentYear+=1
                r64+=1

            else:
                tournamentYear+=1
                r64+=1

        #####################################################################################################

        # On vérifie si le fichier existe, si c'est le cas on le supprime
        # myfile = get_tournament_title(soup)+"/"+get_tournament_title(soup)+file_name

        # if os.path.isfile(myfile):
        #     os.remove(myfile)

        # # On déplace le fichier produit dans le dossier du tournoi
        # shutil.move(get_tournament_title(soup)+file_name, get_tournament_title(soup)+"/")


    l+=1