#!/bin/bash
sleep 5
flask db upgrade
flask run --host 0.0.0.0 -p 5000