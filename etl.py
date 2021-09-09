import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """Process song file.
    
    Args:
        cur: cusor of psycopg2.
        filepath: song file path (json).
    """
    # open song file
    

    # insert song record
    
    
    # insert artist record
    


def process_log_file(cur, filepath):
    """Process log file.
    
    Args:
        curL cusor of psycopg2.
        filepath: log file path (json).
    """
    # open log file

    # filter by NextSong action
    

    # convert timestamp column to datetime
    
    
    # insert time data records
    

    # load user table
    

    # insert user records
    

    # insert songplay records
    


def process_data(cur, conn, filepath, func):
    """Process data.
    
    Args:
        cur: cursor of psycopg2.
        conn: connection of postgresql.
        filepath: directory path of data.
        func: function of processing.
    """
    # get all files matching extension from directory
    

    # get total number of files found
    

    # iterate over files and process
    


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()