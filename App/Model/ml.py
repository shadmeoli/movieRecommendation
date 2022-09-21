{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c93e10c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# recommendation model\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import json\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "cefe87f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from API import detailed_results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "3e5683fc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'imdbID': 'tt9850370',\n",
       " 'tmdbID': '610643',\n",
       " 'imdbRating': 65,\n",
       " 'imdbVoteCount': 1565,\n",
       " 'tmdbRating': 71,\n",
       " 'backdropPath': '/pYziM5SEmptPW0LdNhWvjzR2zD1.jpg',\n",
       " 'backdropURLs': {'1280': 'https://image.tmdb.org/t/p/w1280/pYziM5SEmptPW0LdNhWvjzR2zD1.jpg',\n",
       "  '300': 'https://image.tmdb.org/t/p/w300/pYziM5SEmptPW0LdNhWvjzR2zD1.jpg',\n",
       "  '780': 'https://image.tmdb.org/t/p/w780/pYziM5SEmptPW0LdNhWvjzR2zD1.jpg',\n",
       "  'original': 'https://image.tmdb.org/t/p/original/pYziM5SEmptPW0LdNhWvjzR2zD1.jpg'},\n",
       " 'originalTitle': '#AnneFrank. Parallel Stories',\n",
       " 'genres': [18, 36],\n",
       " 'countries': ['IT'],\n",
       " 'year': 2019,\n",
       " 'runtime': 92,\n",
       " 'cast': ['Helen Mirren', 'Anne Frank', 'Martina Gatti', 'Arianna Szorenyi'],\n",
       " 'significants': ['Sabina Fedeli', 'Anna Migotto'],\n",
       " 'title': '#AnneFrank. Parallel Stories',\n",
       " 'overview': \"One single Anne Frank moves us more than the countless others who suffered just as she did but whose faces have remained in the shadows-Primo Levi. The Oscar®-winning Helen Mirren will introduce audiences to Anne Frank's story through the words in her diary. The set will be her room in the secret refuge in Amsterdam, reconstructed in every detail by set designers from the Piccolo Theatre in Milan. Anne Frank this year would have been 90 years old. Anne's story is intertwined with that of five Holocaust survivors, teenage girls just like her, with the same ideals, the same desire to live: Arianna Szörenyi, Sarah Lichtsztejn-Montard, Helga Weiss and sisters Andra and Tatiana Bucci. Their testimonies alternate with those of their children and grandchildren.\",\n",
       " 'tagline': '',\n",
       " 'video': 'FzT7-NfkxLA',\n",
       " 'posterPath': '/hkC4yNDFmW1yQuQhtZydMeRuaAb.jpg',\n",
       " 'posterURLs': {'154': 'https://image.tmdb.org/t/p/w154/hkC4yNDFmW1yQuQhtZydMeRuaAb.jpg',\n",
       "  '185': 'https://image.tmdb.org/t/p/w185/hkC4yNDFmW1yQuQhtZydMeRuaAb.jpg',\n",
       "  '342': 'https://image.tmdb.org/t/p/w342/hkC4yNDFmW1yQuQhtZydMeRuaAb.jpg',\n",
       "  '500': 'https://image.tmdb.org/t/p/w500/hkC4yNDFmW1yQuQhtZydMeRuaAb.jpg',\n",
       "  '780': 'https://image.tmdb.org/t/p/w780/hkC4yNDFmW1yQuQhtZydMeRuaAb.jpg',\n",
       "  '92': 'https://image.tmdb.org/t/p/w92/hkC4yNDFmW1yQuQhtZydMeRuaAb.jpg',\n",
       "  'original': 'https://image.tmdb.org/t/p/original/hkC4yNDFmW1yQuQhtZydMeRuaAb.jpg'},\n",
       " 'age': 10,\n",
       " 'streamingInfo': {'netflix': {'us': {'link': 'https://www.netflix.com/title/81264660/',\n",
       "    'added': 1600283847,\n",
       "    'leaving': 0}}},\n",
       " 'originalLanguage': 'en'}"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d = detailed_results()[0]\n",
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "a71a988f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def essentials():\n",
    "    det = {}\n",
    "    det[\"title\"] = d[\"title\"]\n",
    "    det[\"overview\"] = d[\"overview\"]\n",
    "    det[\"originalLanguage\"] = d[\"originalLanguage\"]\n",
    "    det[\"genre\"] = d['genres']\n",
    "    det[\"country\"] = d['countries'][0]\n",
    "    det[\"streaming_info\"] = d[\"streamingInfo\"]\n",
    "    det[\"cast\"] = d[\"cast\"]\n",
    "    \n",
    "    return dict(det, indent=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "14ec5c7c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'title': '#AnneFrank. Parallel Stories',\n",
       " 'overview': \"One single Anne Frank moves us more than the countless others who suffered just as she did but whose faces have remained in the shadows-Primo Levi. The Oscar®-winning Helen Mirren will introduce audiences to Anne Frank's story through the words in her diary. The set will be her room in the secret refuge in Amsterdam, reconstructed in every detail by set designers from the Piccolo Theatre in Milan. Anne Frank this year would have been 90 years old. Anne's story is intertwined with that of five Holocaust survivors, teenage girls just like her, with the same ideals, the same desire to live: Arianna Szörenyi, Sarah Lichtsztejn-Montard, Helga Weiss and sisters Andra and Tatiana Bucci. Their testimonies alternate with those of their children and grandchildren.\",\n",
       " 'originalLanguage': 'en',\n",
       " 'genre': [18, 36],\n",
       " 'country': 'IT',\n",
       " 'streaming_info': {'netflix': {'us': {'link': 'https://www.netflix.com/title/81264660/',\n",
       "    'added': 1600283847,\n",
       "    'leaving': 0}}},\n",
       " 'cast': ['Helen Mirren', 'Anne Frank', 'Martina Gatti', 'Arianna Szorenyi'],\n",
       " 'indent': 4}"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "file = essentials()\n",
    "file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f83b6df7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
