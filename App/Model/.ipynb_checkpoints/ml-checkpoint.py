{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a8b87efc",
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
   "id": "38f7492c",
   "metadata": {},
   "outputs": [],
   "source": [
    "from API import detailed_results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "72b633f9",
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
   "execution_count": 30,
   "id": "2af46ca0",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "('title', 'overview', 'originalLanguage')",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "Cell \u001b[0;32mIn [30], line 5\u001b[0m\n\u001b[1;32m      2\u001b[0m     full \u001b[38;5;241m=\u001b[39m d[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtitle\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moverview\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moriginalLanguage\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n\u001b[1;32m      3\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m full\n\u001b[0;32m----> 5\u001b[0m \u001b[43messentials\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "Cell \u001b[0;32mIn [30], line 2\u001b[0m, in \u001b[0;36messentials\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21messentials\u001b[39m():\n\u001b[0;32m----> 2\u001b[0m     full \u001b[38;5;241m=\u001b[39m \u001b[43md\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mtitle\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43moverview\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43moriginalLanguage\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m]\u001b[49m\n\u001b[1;32m      3\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m full\n",
      "\u001b[0;31mKeyError\u001b[0m: ('title', 'overview', 'originalLanguage')"
     ]
    }
   ],
   "source": [
    "def essentials():\n",
    "    title = d[\"title\"]\n",
    "    overview = d[\"overview\"]\n",
    "    lang = d[]\"originalLanguage\"]\n",
    "    \n",
    "    return full\n",
    "\n",
    "essentials()"
   ]
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
