# Simple ELK log analyzer

This is simple log analyzer based on the ELK stack. Just put your log file here, set-up the GROK patterns and run docker-compose.

## How to use this

1. Copy your log file into `data` folder as `access.log` (you can use different name, but you must correctly set it in the `logstash_cache_log_pipeline.conf` file)
2. Correctly set the GROK pattern in the `logstash_cache_log_pipeline.conf` file in the filters section. Good way is to take few messages from your log and try it in [Heroku Debugger](https://grokdebug.herokuapp.com). If you need to see the messages produced by Logstash, uncomment output to stdout. 
3. Run `docker-compose up -d` to start up the machinery
4. Navigate yourself to Kibana running here: [http://localhost:5601]()
5. In Kibana add the index pattern: 
    - Go to _Management_
    - Click _Index Patterns_
    - Fill in `logstash-*`
    - Select `@timestamp` as _Time Filter field_
    - Click _Create Index Pattern_
6. Go to _Discover_, select _Time Range_ appropriate to your data and watch how messages from your log file are being indexed.


