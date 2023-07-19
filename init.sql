DO $$ BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'similarity_search_db') THEN
    CREATE DATABASE mydatabase;
  END IF;
END $$;